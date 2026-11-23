"""Micromap_Example.ipynb

# Commented out IPython magic to ensure Python compatibility.
# %pip install pandas requests plotly

# ================================================================
# CENSUS LINKED MICROMAP: INCOME AND POVERTY
# Color-blind-conscious grouped visualization
# ================================================================
# Google Colab setup:
#   %pip install pandas requests plotly
#
# Output:
#   - Three sections: High Poverty, Mid Poverty, Low Poverty
#   - One full U.S. map per section
#   - Unique state colors within each section
#   - Matching colors for state maps and statistical bars
#   - Inline interactive Plotly output
#   - CSV dataset and JSON metadata exports
# ================================================================

import json
import os
import time
from pathlib import Path
from getpass import getpass

import pandas as pd
import requests
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from IPython.display import display


# ================================================================
# BEGINNER GUIDE
# ================================================================
# In Google Colab:
# 1. Run: %pip install pandas requests plotly
# 2. Run the notebook cells from top to bottom.
# 3. Enter a Census API key when prompted (the entry is hidden).
# 4. Enter an ACS 1-year release year, such as 2012 or 2024.
# 5. The notebook downloads the data, saves a CSV and metadata JSON,
#    and displays the interactive linked micromap.
# Never publish your API key in a notebook or GitHub repository.
# ================================================================

# ================================================================
# 1. SETTINGS
# ================================================================

DEFAULT_YEAR = 2024
LATEST_CONFIGURED_YEAR = 2024

OUTPUT_DIR = Path("/content")
SAVE_HTML_COPY = False

TIMEOUT_SECONDS = 30
MAX_RETRIES = 3

GEOJSON_URL = (
    "https://raw.githubusercontent.com/"
    "PublicaMundi/MappingAPI/master/data/geojson/us-states.json"
)

INCOME_EST = "B19013_001E"
INCOME_MOE = "B19013_001M"

POVERTY_RATE = "S1701_C03_001E"
POVERTY_MOE = "S1701_C03_001M"

POVERTY_COUNT = "B17001_002E"
POVERTY_UNIVERSE = "B17001_001E"


# ================================================================
# 2. ACCESSIBLE COLOR PALETTE
# ================================================================

# A qualitative palette inspired by Okabe-Ito and other
# color-vision-conscious palettes. Each state's color is reused
# for its map highlight, income bar, and poverty bar.
#
# With many states, no palette can guarantee that every color
# will be distinguishable for every type of color-vision deficiency.
# State abbreviations, labels, and hover text provide redundancy.

STATE_PALETTE = [
    "#0072B2",  # Blue
    "#D55E00",  # Vermilion
    "#009E73",  # Bluish green
    "#CC79A7",  # Reddish purple
    "#E69F00",  # Orange
    "#56B4E9",  # Sky blue
    "#882255",  # Dark wine
    "#44AA99",  # Teal
    "#332288",  # Indigo
    "#AA4499",  # Purple
    "#117733",  # Green
    "#999933",  # Olive
    "#88CCEE",  # Light blue
    "#661100",  # Dark brown-red
    "#6699CC",  # Steel blue
    "#AA4466",  # Muted rose
    "#4D4D4D",  # Dark gray
    "#EE7733",  # Orange-red
]

NEUTRAL_STATE_COLOR = "#E0E0E0"
STATE_BORDER_COLOR = "#FFFFFF"
CHART_TEXT_COLOR = "#222222"

GROUPS = ["High Poverty", "Mid Poverty", "Low Poverty"]


# ================================================================
# 3. STATE FIPS LOOKUP
# ================================================================

FIPS_TO_ABBR = {
    "01": "AL", "02": "AK", "04": "AZ", "05": "AR",
    "06": "CA", "08": "CO", "09": "CT", "10": "DE",
    "11": "DC", "12": "FL", "13": "GA", "15": "HI",
    "16": "ID", "17": "IL", "18": "IN", "19": "IA",
    "20": "KS", "21": "KY", "22": "LA", "23": "ME",
    "24": "MD", "25": "MA", "26": "MI", "27": "MN",
    "28": "MS", "29": "MO", "30": "MT", "31": "NE",
    "32": "NV", "33": "NH", "34": "NJ", "35": "NM",
    "36": "NY", "37": "NC", "38": "ND", "39": "OH",
    "40": "OK", "41": "OR", "42": "PA", "44": "RI",
    "45": "SC", "46": "SD", "47": "TN", "48": "TX",
    "49": "UT", "50": "VT", "51": "VA", "53": "WA",
    "54": "WV", "55": "WI", "56": "WY",
}


# ================================================================
# 4. API HELPERS
# ================================================================
# These functions handle communication with the Census API.
# Beginner notes:
# - An API lets this notebook request data from another service.
# - Census returns the requested data in JSON format.
# - A Census API key is required for ACS data requests. Keep it private.
# - Temporary server/network problems are retried automatically.


def request_json(url, params=None):
    """Request JSON data and explain common API errors clearly."""
    last_error = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(
                url,
                params=params,
                timeout=TIMEOUT_SECONDS,
                headers={
                    "User-Agent": "Census-Linked-Micromap/1.0",
                    "Accept": "application/json",
                },
            )

            # Retry temporary server/rate-limit errors.
            if response.status_code in (429, 500, 502, 503, 504):
                last_error = (
                    f"HTTP {response.status_code}: {response.text[:500]}"
                )
                if attempt < MAX_RETRIES:
                    wait_seconds = 2 ** (attempt - 1)
                    print(f"Temporary API error. Retrying in {wait_seconds} seconds...")
                    time.sleep(wait_seconds)
                    continue
                break

            # Permanent HTTP errors need to be shown, not silently retried.
            if not response.ok:
                raise RuntimeError(
                    f"The Census API returned HTTP {response.status_code}.\n"
                    f"Endpoint: {url}\nResponse: {response.text[:1000]}"
                )

            # Check for an empty response before trying to decode JSON.
            if not response.text.strip():
                raise RuntimeError(
                    f"The API returned an empty response. Endpoint: {url}"
                )

            try:
                return response.json()
            except ValueError as exc:
                raise RuntimeError(
                    "The API response was not valid JSON. A proxy, firewall, "
                    "or network service may have returned an HTML page instead.\n"
                    f"Endpoint: {url}\n"
                    f"HTTP status: {response.status_code}\n"
                    f"Content-Type: {response.headers.get('Content-Type', 'unknown')}\n"
                    f"Response preview: {response.text[:1000]!r}"
                ) from exc

        except requests.exceptions.Timeout as exc:
            last_error = f"Request timed out: {exc}"
        except requests.exceptions.ConnectionError as exc:
            last_error = f"Connection error: {exc}"
        except requests.exceptions.RequestException as exc:
            last_error = f"Request error: {exc}"

        if attempt < MAX_RETRIES:
            wait_seconds = 2 ** (attempt - 1)
            print(f"Request failed. Retrying in {wait_seconds} seconds...")
            time.sleep(wait_seconds)

    raise RuntimeError(
        f"Request failed after {MAX_RETRIES} attempts.\nLast error: {last_error}"
    )


def get_api_key():
    """Get the Census API key without displaying it on screen."""
    # First check whether a key was configured as an environment variable.
    key = os.getenv("CENSUS_API_KEY", "").strip()
    if key:
        print("Using the Census API key from the environment.")
        return key

    print(
        "A Census API key is required for ACS data requests.\n"
        "Request a free key at:\n"
        "https://api.census.gov/data/key_signup.html"
    )
    try:
        key = getpass("Enter your Census API key (input is hidden): ").strip()
    except (EOFError, KeyboardInterrupt):
        raise SystemExit("API key entry was cancelled.")

    if not key:
        raise ValueError(
            "No Census API key was entered. A key is required to retrieve ACS data."
        )
    return key


def get_year():
    """Ask which ACS 1-year release year should be analyzed."""
    raw = input(f"ACS 1-year release year [{DEFAULT_YEAR}]: ").strip()
    try:
        year = int(raw) if raw else DEFAULT_YEAR
    except ValueError as exc:
        raise ValueError("Enter a four-digit year, such as 2012 or 2024.") from exc

    if not 2005 <= year <= LATEST_CONFIGURED_YEAR:
        raise ValueError(
            f"Enter a year between 2005 and {LATEST_CONFIGURED_YEAR}. "
            "Update LATEST_CONFIGURED_YEAR in the Settings section to support newer releases."
        )
    return year


def get_variables(endpoint):
    """Download the list of variables available for an ACS endpoint."""
    result = request_json(f"{endpoint}/variables.json")
    if not isinstance(result, dict) or "variables" not in result:
        raise RuntimeError(f"Could not retrieve Census variable metadata: {endpoint}")
    return result["variables"]


def fetch_table(endpoint, variables, api_key=None):
    """Request selected Census variables for every state and DC."""
    if not api_key:
        raise ValueError("A Census API key is required before requesting ACS data.")

    # 'get' names the columns we want; 'for' requests state-level records.
    params = {
        "get": ",".join(variables),
        "for": "state:*",
        "key": api_key,
    }
    result = request_json(endpoint, params)

    # Census returns a list: the first row has column names; later rows are data.
    if not isinstance(result, list) or len(result) < 2:
        raise RuntimeError(f"Unexpected Census API response: {result!r}")

    df = pd.DataFrame(result[1:], columns=result[0])
    if "state" not in df.columns:
        raise RuntimeError("The Census response did not include a state FIPS column.")

    # FIPS codes are identifiers, not quantities. Preserve leading zeros (e.g. 01).
    df["state"] = df["state"].astype(str).str.zfill(2)
    if df["state"].duplicated().any():
        raise RuntimeError("Duplicate state FIPS codes were returned by the Census API.")
    return df


# ================================================================
# 5. RETRIEVE CENSUS DATA
# ================================================================

def load_data(year, api_key=None):
    """Load income and poverty estimates, joining on state FIPS."""
    endpoint = f"https://api.census.gov/data/{year}/acs/acs1"
    detailed_meta = get_variables(endpoint)

    if INCOME_EST not in detailed_meta:
        raise RuntimeError(
            f"Median household income variable {INCOME_EST} "
            f"is unavailable for ACS {year}."
        )

    income_vars = ["NAME", INCOME_EST]
    income_moe_available = INCOME_MOE in detailed_meta

    if income_moe_available:
        income_vars.append(INCOME_MOE)

    print(f"\nRetrieving median household income for {year}...")

    income = fetch_table(
        endpoint, income_vars, api_key
    ).rename(
        columns={
            INCOME_EST: "median_income",
            INCOME_MOE: "income_moe",
        }
    )

    if "income_moe" not in income.columns:
        income["income_moe"] = pd.NA

    # Try to use the published ACS subject-table poverty rate.
    subject_endpoint = f"{endpoint}/subject"

    try:
        subject_meta = get_variables(subject_endpoint)
    except (requests.exceptions.RequestException, RuntimeError, ValueError):
        # If this older ACS release has no subject metadata, use the fallback
        # poverty calculation below. Other parts of the workflow still validate data.
        subject_meta = {}

    if POVERTY_RATE in subject_meta:
        poverty_vars = ["NAME", POVERTY_RATE]
        poverty_moe_available = POVERTY_MOE in subject_meta

        if poverty_moe_available:
            poverty_vars.append(POVERTY_MOE)

        print("Retrieving published ACS poverty-rate estimates...")

        poverty = fetch_table(
            subject_endpoint, poverty_vars, api_key
        ).rename(
            columns={
                POVERTY_RATE: "poverty_rate",
                POVERTY_MOE: "poverty_moe",
            }
        )

        if "poverty_moe" not in poverty.columns:
            poverty["poverty_moe"] = pd.NA

        poverty_method = (
            f"Published subject-table variable {POVERTY_RATE}"
        )

    else:
        # Fallback for years without the expected S1701 variable.
        required = [POVERTY_COUNT, POVERTY_UNIVERSE]
        missing = [
            variable for variable in required
            if variable not in detailed_meta
        ]

        if missing:
            raise RuntimeError(
                f"Poverty variables unavailable: {missing}"
            )

        print(
            "Published poverty-rate variable unavailable; "
            "calculating a rate from B17001 counts."
        )

        poverty = fetch_table(
            endpoint, ["NAME"] + required, api_key
        )

        for col in required:
            poverty[col] = pd.to_numeric(
                poverty[col], errors="coerce"
            )

        denominator = poverty[POVERTY_UNIVERSE].replace(
            0, float("nan")
        )

        poverty["poverty_rate"] = (
            100 * poverty[POVERTY_COUNT] / denominator
        )

        # Do not fabricate an MOE for the derived rate.
        poverty["poverty_moe"] = pd.NA

        poverty_method = (
            f"Derived from {POVERTY_COUNT} / "
            f"{POVERTY_UNIVERSE} * 100; MOE not calculated"
        )

    # Join using state FIPS rather than names. A merge combines records
    # when the key value (here, the state code) matches in both tables.
    data = income.merge(
        poverty[["state", "poverty_rate", "poverty_moe"]],
        on="state",
        how="outer",
        validate="one_to_one",
        indicator=True,
    )

    unmatched = data[data["_merge"] != "both"]

    if not unmatched.empty:
        print(
            "Warning: unmatched state FIPS codes:",
            unmatched["state"].tolist(),
        )

    data = data.drop(columns="_merge")
    data["state_abbr"] = data["state"].map(FIPS_TO_ABBR)

    for column in [
        "median_income",
        "income_moe",
        "poverty_rate",
        "poverty_moe",
    ]:
        data[column] = pd.to_numeric(
            data[column], errors="coerce"
        )
        data.loc[data[column] < 0, column] = pd.NA

    data = data[data["state_abbr"].notna()].copy()

    data = data.dropna(
        subset=["median_income", "poverty_rate"]
    ).copy()

    if data.empty:
        raise RuntimeError("No complete state records were returned.")

    data["median_income"] = data["median_income"].round(0)
    data["income_moe"] = data["income_moe"].round(0)
    data["poverty_rate"] = data["poverty_rate"].round(2)
    data["poverty_moe"] = data["poverty_moe"].round(2)

    data = data.sort_values(
        "poverty_rate", ascending=False
    ).reset_index(drop=True)

    # Divide states into roughly equal thirds by poverty-rate rank.
    # These are relative groups for this dataset, not official Census labels.
    # These are analytical groups, not official Census classifications.
    rank = data["poverty_rate"].rank(
        method="first", ascending=False
    )
    n = len(data)

    data["poverty_group"] = rank.apply(
        lambda r: (
            "High Poverty" if r <= n / 3
            else "Mid Poverty" if r <= 2 * n / 3
            else "Low Poverty"
        )
    )

    metadata = {
        "source": "U.S. Census Bureau, ACS 1-Year Estimates",
        "release_year": year,
        "geography": "State-level geographies returned by ACS",
        "income_variable": INCOME_EST,
        "income_moe_variable": (
            INCOME_MOE if income_moe_available else None
        ),
        "poverty_method": poverty_method,
        "grouping": "Roughly equal thirds ranked by poverty rate",
        "ordering": "Descending poverty rate within each group",
        "caveats": [
            "ACS estimates have sampling error.",
            "Missing margins of error are not fabricated.",
            "No MOE is calculated for the fallback derived poverty rate.",
            "Income comparisons across years require inflation adjustment.",
            "High, Mid, and Low Poverty are relative groups, not official labels.",
            "Color is supplemented by labels and hover information.",
        ],
    }

    print(f"Records available: {len(data)} (expected 51 including DC)")
    return data, metadata


# ================================================================
# 6. LOAD U.S. MAP GEOGRAPHY
# ================================================================

def load_state_geojson():
    """Load state boundaries for Plotly's U.S. choropleth maps."""
    # GeoJSON is a common format for storing geographic shapes and boundaries.
    print("Loading U.S. state boundaries...")
    geojson = request_json(GEOJSON_URL)

    if not isinstance(geojson, dict) or "features" not in geojson:
        raise RuntimeError("The GeoJSON source returned no features.")

    return geojson


# ================================================================
# 7. BUILD GROUPED LINKED MICROMAP
# ================================================================

def make_grouped_micromap(data, metadata):
    """Render one U.S. map per poverty group with matching state bars."""
    # Each row contains a map, an income bar chart, and a poverty-rate bar chart.
    # State ordering is kept consistent so the panels can be compared.
    year = metadata["release_year"]
    geojson = load_state_geojson()

    fig = make_subplots(
        rows=3,
        cols=3,
        specs=[
            [{"type": "geo"}, {"type": "xy"}, {"type": "xy"}],
            [{"type": "geo"}, {"type": "xy"}, {"type": "xy"}],
            [{"type": "geo"}, {"type": "xy"}, {"type": "xy"}],
        ],
        column_widths=[0.34, 0.36, 0.30],
        horizontal_spacing=0.055,
        vertical_spacing=0.12,
        subplot_titles=[
            "HIGH POVERTY — State Map",
            "Median Household Income",
            "Poverty Rate",
            "MID POVERTY — State Map",
            "Median Household Income",
            "Poverty Rate",
            "LOW POVERTY — State Map",
            "Median Household Income",
            "Poverty Rate",
        ],
    )

    # Create three panels. Each group has its own map and state colors.
    for row_num, group_name in enumerate(GROUPS, start=1):
        subset = data[
            data["poverty_group"] == group_name
        ].sort_values(
            "poverty_rate", ascending=False
        ).reset_index(drop=True)

        members = subset["state_abbr"].tolist()

        # Assign a different color to each state within this group.
        state_colors = {
            abbr: STATE_PALETTE[i % len(STATE_PALETTE)]
            for i, abbr in enumerate(members)
        }

        # Base map: all states in neutral gray.
        fig.add_trace(
            go.Choropleth(
                geojson=geojson,
                locations=list(FIPS_TO_ABBR.values()),
                featureidkey="properties.postal",
                z=[0] * len(FIPS_TO_ABBR),
                locationmode="USA-states",
                colorscale=[
                    [0, NEUTRAL_STATE_COLOR],
                    [1, NEUTRAL_STATE_COLOR],
                ],
                showscale=False,
                marker_line_color=STATE_BORDER_COLOR,
                marker_line_width=0.65,
                hoverinfo="skip",
                showlegend=False,
                name="States outside group",
            ),
            row=row_num,
            col=1,
        )

        # Highlight the states in the current poverty group.
        # Each state receives its own distinct color.
        for _, record in subset.iterrows():
            abbr = record["state_abbr"]
            color = state_colors[abbr]

            income_moe_text = (
                "Unavailable"
                if pd.isna(record["income_moe"])
                else f"${float(record['income_moe']):,.0f}"
            )

            poverty_moe_text = (
                "Unavailable"
                if pd.isna(record["poverty_moe"])
                else (
                    f"{float(record['poverty_moe']):.2f} "
                    "percentage points"
                )
            )

            hover = (
                f"<b>{record['NAME']}</b><br>"
                f"Group: {group_name}<br>"
                f"Median household income: "
                f"${float(record['median_income']):,.0f}<br>"
                f"Income MOE: {income_moe_text}<br>"
                f"Poverty rate: "
                f"{float(record['poverty_rate']):.2f}%<br>"
                f"Poverty MOE: {poverty_moe_text}"
            )

            # Highlight the state on the group's single U.S. map.
            fig.add_trace(
                go.Choropleth(
                    locations=[abbr],
                    locationmode="USA-states",
                    z=[1],
                    colorscale=[
                        [0, color],
                        [1, color],
                    ],
                    showscale=False,
                    marker_line_color=STATE_BORDER_COLOR,
                    marker_line_width=1.0,
                    text=[record["NAME"]],
                    customdata=[[
                        record["median_income"],
                        record["poverty_rate"],
                    ]],
                    hovertemplate=(
                        "<b>%{text}</b><br>"
                        f"Group: {group_name}<br>"
                        "Median household income: "
                        "$%{customdata[0]:,.0f}<br>"
                        "Poverty rate: %{customdata[1]:.2f}%"
                        "<extra></extra>"
                    ),
                    showlegend=False,
                    name=f"{abbr} — {record['NAME']}",
                ),
                row=row_num,
                col=1,
            )

        # Aligned statistical panels.
        for _, record in subset.iterrows():
            abbr = record["state_abbr"]
            color = state_colors[abbr]

            income = float(record["median_income"])
            poverty = float(record["poverty_rate"])

            income_moe = (
                0 if pd.isna(record["income_moe"])
                else max(0, float(record["income_moe"]))
            )

            poverty_moe = (
                0 if pd.isna(record["poverty_moe"])
                else max(0, float(record["poverty_moe"]))
            )

            # Median household income.
            fig.add_trace(
                go.Bar(
                    x=[income],
                    y=[abbr],
                    orientation="h",
                    marker_color=color,
                    error_x={
                        "type": "data",
                        "array": [income_moe],
                        "visible": not pd.isna(record["income_moe"]),
                    },
                    customdata=[[
                        record["NAME"],
                        poverty,
                        (
                            "Unavailable"
                            if pd.isna(record["income_moe"])
                            else f"${float(record['income_moe']):,.0f}"
                        ),
                    ]],
                    hovertemplate=(
                        "<b>%{customdata[0]}</b><br>"
                        "Median household income: $%{x:,.0f}<br>"
                        "Poverty rate: %{customdata[1]:.2f}%<br>"
                        "Income MOE: %{customdata[2]}"
                        "<extra></extra>"
                    ),
                    showlegend=False,
                ),
                row=row_num,
                col=2,
            )

            # Poverty rate.
            fig.add_trace(
                go.Bar(
                    x=[poverty],
                    y=[abbr],
                    orientation="h",
                    marker_color=color,
                    error_x={
                        "type": "data",
                        "array": [poverty_moe],
                        "visible": not pd.isna(record["poverty_moe"]),
                    },
                    customdata=[[
                        record["NAME"],
                        income,
                        (
                            "Unavailable"
                            if pd.isna(record["poverty_moe"])
                            else f"{float(record['poverty_moe']):.2f} pp"
                        ),
                    ]],
                    hovertemplate=(
                        "<b>%{customdata[0]}</b><br>"
                        "Poverty rate: %{x:.2f}%<br>"
                        "Median household income: "
                        "$%{customdata[1]:,.0f}<br>"
                        "Poverty MOE: %{customdata[2]}"
                        "<extra></extra>"
                    ),
                    showlegend=False,
                ),
                row=row_num,
                col=3,
            )

        # Keep state order aligned across both statistical panels.
        for col in (2, 3):
            fig.update_yaxes(
                categoryorder="array",
                categoryarray=members,
                autorange="reversed",
                tickfont={"size": 9, "color": CHART_TEXT_COLOR},
                row=row_num,
                col=col,
            )

        fig.update_geos(
            scope="usa",
            showlakes=True,
            lakecolor="white",
            bgcolor="rgba(0,0,0,0)",
            row=row_num,
            col=1,
        )

        fig.update_xaxes(
            title_text="Median household income ($)",
            tickprefix="$",
            separatethousands=True,
            row=row_num,
            col=2,
        )

        fig.update_xaxes(
            title_text="Poverty rate (%)",
            ticksuffix="%",
            row=row_num,
            col=3,
        )

    # Source note and accessibility note.
    source_note = (
        f"Source: U.S. Census Bureau, ACS 1-Year Estimates ({year}). "
        "Groups contain roughly one-third of available records, ranked by "
        "poverty rate. State colors link the map and bars. "
        "States outside each group are gray. State labels and hover details "
        "supplement color. Error bars appear only when MOEs are available. "
        "Income is not inflation-adjusted across years."
    )

    fig.update_layout(
        title={
            "text": (
                f"Linked Micromap: U.S. Income and Poverty ({year})"
                "<br><sup>Three poverty groups; distinct state colors are "
                "reused across each group's map and statistics.</sup>"
            ),
            "x": 0.5,
            "xanchor": "center",
        },
        height=1450,
        width=1500,
        template="plotly_white",
        margin={"l": 65, "r": 40, "t": 125, "b": 115},
        font={"family": "Arial, sans-serif", "color": CHART_TEXT_COLOR},
        showlegend=False,
        barmode="overlay",
        annotations=list(fig.layout.annotations) + [
            {
                "text": source_note,
                "xref": "paper",
                "yref": "paper",
                "x": 0,
                "y": -0.06,
                "showarrow": False,
                "align": "left",
                "font": {"size": 10, "color": "#444444"},
            }
        ],
    )

    # Render the interactive visualization directly in Colab/Jupyter.
    display(fig)

    if SAVE_HTML_COPY:
        html_path = (
            OUTPUT_DIR
            / f"census_income_poverty_micromap_{year}.html"
        )
        fig.write_html(html_path, include_plotlyjs=True)
        print(f"HTML copy saved to: {html_path.resolve()}")


# ================================================================
# 8. RUN PROJECT AND EXPORT DATA
# ================================================================

def main():
    """Run the workflow from API-key entry through chart creation."""
    print("Census Income and Poverty — Accessible Linked Micromap")
    print("=" * 58)

    try:
        # Step 1: Ask for the credentials and data year.
        api_key = get_api_key()
        year = get_year()

        # Step 2: Download, clean, and combine the Census estimates.
        data, metadata = load_data(year, api_key)

        # Step 3: Create the output folder and save the data files.
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        csv_path = OUTPUT_DIR / f"census_income_poverty_{year}.csv"
        json_path = OUTPUT_DIR / f"census_income_poverty_{year}_metadata.json"

        data.to_csv(csv_path, index=False)
        json_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

        print(f"\nCSV saved to: {csv_path.resolve()}")
        print(f"Metadata saved to: {json_path.resolve()}")
        print("\nRendering the grouped micromap...")

        # Step 4: Build and display the interactive Plotly visualization.
        make_grouped_micromap(data, metadata)
        print("\nFinished successfully.")

    except (requests.exceptions.RequestException, ValueError, RuntimeError,
            KeyError, pd.errors.MergeError) as exc:
        print(
            "\nThe analysis could not be completed.\n"
            "Review the message below, correct the issue, and run the cell again:\n"
            f"{exc}"
        )


# Run the workflow when this notebook cell or Python script is executed.
main()
