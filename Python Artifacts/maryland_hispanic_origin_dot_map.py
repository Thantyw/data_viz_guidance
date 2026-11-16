"""
Maryland Hispanic-Origin Dot Distribution Map
==============================================

This example recreates the general approach shown in the supplied reference:
a multivariate dot-density map in which each color represents a population
group and each dot represents an approximately fixed number of people.

Geography:
    Maryland census tracts

Demographic source:
    2024 American Community Survey (ACS) 5-Year Estimates, Table B03001

Groups shown:
    Mexican, Puerto Rican, Cuban, Dominican, Guatemalan, Honduran,
    Nicaraguan, Salvadoran, Colombian, and Venezuelan

Important:
    Dot locations are randomly sampled inside census tract polygons. They
    are not actual household or individual locations. Tract-level estimates
    are distributed across each tract only to illustrate spatial patterns.

Run:
    python maryland_hispanic_origin_dot_map.py
"""

from pathlib import Path
from getpass import getpass
import zipfile

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from shapely.geometry import Point
import matplotlib.patheffects as path_effects
from matplotlib.lines import Line2D


# =============================================================================
# 1. CONFIGURATION: SETTINGS THAT DEVELOPERS CAN CUSTOMIZE
# =============================================================================

STATE_FIPS = "24"  # Maryland's two-digit Census state code.
ACS_YEAR = 2024    # Latest 5-year ACS vintage used in this example.

# One dot represents approximately this many people in every group.
# Increase this value if the map is too crowded; decrease it if too sparse.
DOT_VALUE = 100

# Fixed seed makes random dot placement repeatable between runs.
RANDOM_SEED = 42

# ACS B03001 estimate variables for the selected Hispanic-origin groups.
# The variable labels are confirmed in the Census API's B03001 group metadata.
GROUPS = {
    "Mexican": "B03001_004E",
    "Puerto Rican": "B03001_005E",
    "Cuban": "B03001_006E",
    "Dominican": "B03001_007E",
    "Guatemalan": "B03001_010E",
    "Honduran": "B03001_011E",
    "Nicaraguan": "B03001_012E",
    "Salvadoran": "B03001_014E",
    "Colombian": "B03001_020E",
    "Venezuelan": "B03001_025E",
}

# Distinct categorical colors selected for contrast. Because ten categories
# exceed the size of a compact color-blind-safe palette, the legend also uses
# explicit text labels. Check the final map at its intended display size.
GROUP_COLORS = {
    "Mexican": "#4477AA",
    "Puerto Rican": "#EE6677",
    "Cuban": "#228833",
    "Dominican": "#CCBB44",
    "Guatemalan": "#66CCEE",
    "Honduran": "#AA3377",
    "Nicaraguan": "#BBBBBB",
    "Salvadoran": "#332288",
    "Colombian": "#44AA99",
    "Venezuelan": "#DDCC77",
}

# Use an appropriate projected coordinate system for Maryland.
# EPSG:26918 is NAD83 / UTM zone 18N and uses meters.
MAP_CRS = "EPSG:26918"

DATA_DIR = Path("census_data")
OUTPUT_DIR = Path("dot_distribution_output")
DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

ACS_API_URL = f"https://api.census.gov/data/{ACS_YEAR}/acs/acs5"
TRACT_ZIP_URL = (
    "https://www2.census.gov/geo/tiger/TIGER2024/TRACT/"
    f"tl_2024_{STATE_FIPS}_tract.zip"
)


# =============================================================================
# 2. CENSUS API KEY: PROMPT THE USER, BUT ALLOW AN EMPTY RESPONSE
# =============================================================================

def get_api_key():
    """
    Prompt for an optional Census API key.

    A key is not required for every Census API request. This example makes
    one request, which can generally be made without a key. Entering a key
    is supported for users who prefer to use one or who may adapt the code
    to make more requests.

    Request a free key:
        https://api.census.gov/data/key_signup.html
    """
    print("Census API key (optional for this single request).")
    print("Request a free key at https://api.census.gov/data/key_signup.html")
    return getpass("Enter API key, or press Enter to continue without one: ").strip()


# =============================================================================
# 3. RETRIEVE ACS HISPANIC-ORIGIN ESTIMATES BY CENSUS TRACT
# =============================================================================

def download_acs_data(api_key=""):
    """
    Request the four selected population estimates for every Maryland tract.

    ACS 5-year data are used because they provide tract-level estimates.
    B03001 is 'Hispanic or Latino Origin by Specific Origin'. Each selected
    variable ends in E, meaning estimate. The corresponding M variables are
    margins of error and are also requested so uncertainty can be retained
    in the downloaded table for review.
    """
    estimate_variables = list(GROUPS.values())
    moe_variables = [variable.replace("E", "M") for variable in estimate_variables]
    get_variables = ["NAME"] + estimate_variables + moe_variables

    params = {
        "get": ",".join(get_variables),
        "for": "tract:*",
        "in": f"state:{STATE_FIPS}",
    }

    # Only include the key parameter if the user entered a value.
    if api_key:
        params["key"] = api_key

    print(f"\nRequesting {ACS_YEAR} ACS 5-year tract estimates for Maryland...")
    response = requests.get(ACS_API_URL, params=params, timeout=120)
    response.raise_for_status()

    rows = response.json()
    if len(rows) < 2:
        raise ValueError("The Census API returned no tract records.")

    data = pd.DataFrame(rows[1:], columns=rows[0])

    # Keep FIPS identifiers as text to preserve leading zeros.
    data["state"] = data["state"].astype(str).str.zfill(2)
    data["county"] = data["county"].astype(str).str.zfill(3)
    data["tract"] = data["tract"].astype(str).str.zfill(6)
    data["GEOID"] = data["state"] + data["county"] + data["tract"]

    # Convert estimate and margin-of-error fields to numeric values.
    for column in estimate_variables + moe_variables:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    # ACS can use special annotation values for some estimates. Converting
    # nonnumeric values to NaN prevents them from being treated as counts.
    data[estimate_variables] = data[estimate_variables].fillna(0).clip(lower=0)

    print(f"Retrieved {len(data):,} Maryland census tracts.")
    return data


# =============================================================================
# 4. DOWNLOAD AND PREPARE 2024 TIGER/LINE CENSUS TRACT BOUNDARIES
# =============================================================================

def download_tract_boundaries():
    """
    Download Maryland's 2024 TIGER/Line census tract shapefile.

    TIGER/Line contains geographic boundaries and identifiers, not the ACS
    demographic estimates. The two sources are joined using the tract GEOID.
    """
    zip_path = DATA_DIR / f"tl_2024_{STATE_FIPS}_tract.zip"
    extract_dir = DATA_DIR / f"tl_2024_{STATE_FIPS}_tract"
    shapefile = extract_dir / f"tl_2024_{STATE_FIPS}_tract.shp"

    if not shapefile.exists():
        if not zip_path.exists():
            print("\nDownloading 2024 Maryland tract boundaries...")
            response = requests.get(TRACT_ZIP_URL, timeout=300)
            response.raise_for_status()
            zip_path.write_bytes(response.content)

        extract_dir.mkdir(exist_ok=True)
        with zipfile.ZipFile(zip_path, "r") as archive:
            archive.extractall(extract_dir)

    if not shapefile.exists():
        raise FileNotFoundError(f"Expected shapefile not found: {shapefile}")

    tracts = gpd.read_file(shapefile)

    # Standard TIGER/Line tract files use GEOID as the state+county+tract ID.
    tracts["GEOID"] = tracts["GEOID"].astype(str).str.zfill(11)
    tracts["COUNTYFP"] = tracts["COUNTYFP"].astype(str).str.zfill(3)

    # Keep only the fields needed for mapping and county outlines.
    tracts = tracts[["GEOID", "COUNTYFP", "NAME", "geometry"]].copy()
    return tracts


# =============================================================================
# 5. JOIN THE ACS DATA TO THE TRACT POLYGONS
# =============================================================================

def prepare_map_data(acs_data, tract_boundaries):
    """
    Join demographic estimates to their matching census tract geometries.

    A one-to-one tract GEOID join avoids relying on tract names, which can
    be formatted differently across datasets.
    """
    print("\nJoining ACS estimates to tract boundaries...")
    map_data = tract_boundaries.merge(acs_data, on="GEOID", how="inner")

    map_data = map_data.loc[
        map_data.geometry.notna() & (~map_data.geometry.is_empty)
    ].copy()

    if map_data.empty:
        raise ValueError("The ACS-to-tract-boundary join returned no records.")

    map_data = map_data.to_crs(MAP_CRS)

    print(f"Matched {len(map_data):,} tracts.")
    return map_data


# =============================================================================
# 6. CREATE RANDOM DOT LOCATIONS WITHIN EACH CENSUS TRACT
# =============================================================================

def random_points_in_polygon(polygon, count, rng):
    """
    Randomly sample points inside a tract polygon.

    The function samples candidate coordinates from the polygon's bounding
    rectangle and keeps only points that fall inside the polygon. If a very
    narrow or complex polygon makes sampling difficult, representative points
    are used as a fallback. Fallback points can overlap and should be treated
    as a cartographic approximation.
    """
    if count <= 0:
        return []

    min_x, min_y, max_x, max_y = polygon.bounds
    points = []
    attempts = 0
    max_attempts = max(1000, count * 100)

    while len(points) < count and attempts < max_attempts:
        candidate = Point(
            rng.uniform(min_x, max_x),
            rng.uniform(min_y, max_y),
        )
        if polygon.contains(candidate):
            points.append(candidate)
        attempts += 1

    if len(points) < count:
        fallback = polygon.representative_point()
        points.extend([fallback] * (count - len(points)))

    return points


def make_dot_layers(map_data):
    """
    Build a separate point layer for each origin group.

    Stochastic rounding converts a tract estimate into a whole number of dots.
    For example, an expected value of 12.3 dots becomes 12 dots most of the
    time and 13 dots 30% of the time. This avoids always rounding every tract
    down and keeps the statewide dot total close to estimate / DOT_VALUE.

    Important: ACS estimates are tract-level totals. Randomly distributing
    dots throughout the tract does not reveal where people actually live.
    """
    rng = np.random.default_rng(RANDOM_SEED)
    dot_layers = {}

    for group_name, estimate_variable in GROUPS.items():
        print(f"Placing {group_name} dots...")
        group_x = []
        group_y = []

        for row in map_data.itertuples():
            estimate = getattr(row, estimate_variable)
            estimate = max(0, float(estimate)) if pd.notna(estimate) else 0

            expected_dots = estimate / DOT_VALUE
            whole_dots = int(np.floor(expected_dots))
            fractional_part = expected_dots - whole_dots
            number_of_dots = whole_dots + int(rng.random() < fractional_part)

            if number_of_dots == 0:
                continue

            points = random_points_in_polygon(row.geometry, number_of_dots, rng)
            group_x.extend(point.x for point in points)
            group_y.extend(point.y for point in points)

        dot_layers[group_name] = (
            np.asarray(group_x, dtype=float),
            np.asarray(group_y, dtype=float),
        )
        print(f"  {len(group_x):,} dots created.")

    return dot_layers


# =============================================================================
# 7. DRAW THE MULTIVARIATE DOT-DENSITY MAP
# =============================================================================

def create_map(map_data, dot_layers):
    """
    Draw the Maryland map with one color per Hispanic-origin group.

    The county outlines provide geographic context without competing with
    the dots. Equal aspect ratio and a projected CRS prevent map distortion.
    """
    fig, ax = plt.subplots(figsize=(14, 15), facecolor="white")
    ax.set_facecolor("#EAF3F8")  # Pale blue background for surrounding water.

    # County outlines are created by dissolving tracts that share a county FIPS.
    county_boundaries = map_data.dissolve(by="COUNTYFP")
    county_boundaries.boundary.plot(
        ax=ax,
        color="#4B5563",
        linewidth=0.9,
        zorder=2,
    )

    # County names help readers orient themselves. Representative points are
    # guaranteed to fall inside each county polygon, unlike a simple centroid
    # that could fall outside an irregular county shape.
    county_names = {
        "001": "Allegany", "003": "Anne Arundel", "005": "Baltimore County",
        "009": "Calvert", "011": "Caroline", "013": "Carroll",
        "015": "Cecil", "017": "Charles", "019": "Dorchester",
        "021": "Frederick", "023": "Garrett", "025": "Harford",
        "027": "Howard", "029": "Kent", "031": "Montgomery",
        "033": "Prince George's", "035": "Queen Anne's", "037": "St. Mary's",
        "039": "Somerset", "041": "Talbot", "043": "Washington",
        "045": "Wicomico", "047": "Worcester", "510": "Baltimore City",
    }

    for county_fips, county_row in county_boundaries.iterrows():
        label = county_names.get(str(county_fips).zfill(3))
        if label:
            label_point = county_row.geometry.representative_point()
            ax.annotate(
                label,
                xy=(label_point.x, label_point.y),
                ha="center",
                va="center",
                fontsize=7.0,
                fontweight="bold",
                color="#17212B",
                zorder=8,
                bbox={
                    "boxstyle": "round,pad=0.22",
                    "facecolor": "white",
                    "edgecolor": "#687482",
                    "linewidth": 0.45,
                    "alpha": 0.94,
                },
                path_effects=[
                    path_effects.withStroke(linewidth=2.2, foreground="white")
                ],
            )

    # Draw larger dot groups first and smaller groups later so all categories
    # remain visible when points overlap. All dots use the same size.
    for group_name, (x_values, y_values) in dot_layers.items():
        ax.scatter(
            x_values,
            y_values,
            s=4.0,
            marker="o",
            color=GROUP_COLORS[group_name],
            alpha=1.0,
            linewidths=0,
            edgecolors="none",
            antialiaseds=True,
            rasterized=False,
            label=group_name,
            zorder=3,
        )

    ax.set_title(
        "U.S. CENSUS BUREAU | MARYLAND HISPANIC-ORIGIN POPULATION",
        fontsize=17,
        fontweight="bold",
        loc="left",
        pad=24,
    )
    ax.text(
        0,
        1.018,
        f"OFFICIAL SOURCE: {ACS_YEAR} AMERICAN COMMUNITY SURVEY (ACS) 5-YEAR ESTIMATES",
        transform=ax.transAxes,
        fontsize=10.5,
        fontweight="bold",
        color="#17212B",
        ha="left",
    )
    ax.text(
        0,
        1.002,
        f"GEOGRAPHY: MARYLAND CENSUS TRACTS • EACH DOT ≈ "
        f"{DOT_VALUE:,} PEOPLE IN THE SELECTED ORIGIN GROUP",
        transform=ax.transAxes,
        fontsize=9.5,
        color="#404040",
        ha="left",
    )

    # The legend identifies each subgroup and the value represented by a dot.
    # Build custom legend handles so legend dots stay large and easy to see,
    # regardless of the marker size needed for the map itself.
    legend_handles = [
        Line2D(
            [0], [0],
            marker="o",
            linestyle="None",
            markerfacecolor=GROUP_COLORS[group_name],
            markeredgecolor="#263238",
            markeredgewidth=0.35,
            markersize=9.5,
            label=group_name,
        )
        for group_name in GROUPS
    ]
    legend = ax.legend(
        handles=legend_handles,
        title=f"ACS estimated population\\nEach dot ≈ {DOT_VALUE:,} people",
        loc="lower left",
        ncol=2,
        columnspacing=1.1,
        handletextpad=0.5,
        borderpad=0.9,
        labelspacing=0.65,
        frameon=True,
        framealpha=0.99,
        facecolor="white",
        edgecolor="#4B5563",
        fontsize=9.5,
        title_fontsize=10,
    )
    legend.set_zorder(10)

    ax.set_aspect("equal")
    ax.axis("off")

    # Prominent source attribution identifies this as Census-derived data.
    fig.text(
        0.07, 0.055,
        f"DATA SOURCE: U.S. CENSUS BUREAU | {ACS_YEAR} AMERICAN COMMUNITY SURVEY (ACS) 5-YEAR ESTIMATES",
        fontsize=9.2, fontweight="bold", color="#17212B", ha="left",
    )
    fig.text(
        0.07, 0.033,
        "TABLE B03001: HISPANIC OR LATINO ORIGIN BY SPECIFIC ORIGIN | GEOGRAPHY: CENSUS TRACTS | BOUNDARIES: 2024 TIGER/LINE",
        fontsize=8.0, color="#333333", ha="left",
    )
    fig.text(
        0.07, 0.012,
        "Dots are randomly distributed within tract boundaries and do not show actual residences. ACS values are estimates with sampling error.",
        fontsize=7.6, color="#333333", ha="left",
    )

    plt.tight_layout(rect=[0.03, 0.11, 0.98, 0.94])

    output_path = OUTPUT_DIR / "maryland_hispanic_origin_dot_distribution.png"
    pdf_path = OUTPUT_DIR / "maryland_hispanic_origin_dot_distribution.pdf"

    # 600 DPI creates a sharper raster image for print and detailed viewing.
    fig.savefig(
        output_path,
        dpi=600,
        bbox_inches="tight",
        facecolor="white",
    )

    # PDF preserves text and symbols as vector elements for clean zooming.
    fig.savefig(
        pdf_path,
        bbox_inches="tight",
        facecolor="white",
    )

    plt.show()
    plt.close(fig)

    print(f"\nHigh-resolution PNG saved to: {output_path.resolve()}")
    print(f"Vector PDF saved to: {pdf_path.resolve()}")


# =============================================================================
# 8. OPTIONAL DATA CHECK: REVIEW ESTIMATES AND MARGINS OF ERROR
# =============================================================================

def print_data_summary(map_data):
    """
    Summarize the statewide estimates and their ACS margins of error.

    The margin of error is not drawn as a dot. It is retained for developers
    to inspect because ACS estimates are survey estimates, not exact counts.
    """
    print("\nStatewide subgroup estimates and margins of error:")
    for group_name, estimate_variable in GROUPS.items():
        moe_variable = estimate_variable.replace("E", "M")
        total_estimate = map_data[estimate_variable].sum(skipna=True)
        total_moe = map_data[moe_variable].sum(skipna=True)
        print(
            f"- {group_name}: estimate sum={total_estimate:,.0f}; "
            f"sum of tract MOEs (not a combined statewide MOE)={total_moe:,.0f}"
        )

    print(
        "\nNote: Adding tract-level margins of error does not produce a valid "
        "statewide margin of error. Use the appropriate Census aggregation "
        "or variance methodology for statewide uncertainty estimates."
    )


# =============================================================================
# 9. RUN THE COMPLETE WORKFLOW
# =============================================================================

def main():
    """Run the data download, join, dot placement, and mapping steps."""
    print("=" * 72)
    print("MARYLAND HISPANIC-ORIGIN DOT DISTRIBUTION MAP")
    print("=" * 72)

    api_key = get_api_key()
    acs_data = download_acs_data(api_key)
    tract_boundaries = download_tract_boundaries()
    map_data = prepare_map_data(acs_data, tract_boundaries)

    print_data_summary(map_data)

    dot_layers = make_dot_layers(map_data)
    create_map(map_data, dot_layers)

    print("\nFinished. Review the map and its methodological limitations before use.")


if __name__ == "__main__":
    main()
