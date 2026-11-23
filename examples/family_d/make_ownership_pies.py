#!/usr/bin/env python3
"""Draw small pies for the sex of owners of all U.S. businesses in 2021.

Source: U.S. Census Bureau
Dataset: 2021 Nonemployer Statistics by Demographics Series (NES-D): Company Summary
Table: AB2100NESD01
API: https://api.census.gov/data/2021/absnesd
Count: FIRMALL, employer and nonemployer firms
Industry: NAICS2017 code 00 (total for all sectors)
Sex: 001 total, 002 female, 003 male, 004 equally male/female, 098 unclassifiable
The unclassifiable row is published with ethnicity 098, race 98, and veteran status 098.
The other sex rows use ethnicity 001, race 00, and veteran status 001.

Set a Census Data API key only in the environment. Do not paste it into this file:

    export CENSUS_API_KEY=your_key_here
    python3 examples/family_d/make_ownership_pies.py

If CENSUS_API_KEY is not set, the program still tries the API once. If that
does not return the table, it uses absnesd_2021_firms_by_sex.csv.
"""

from __future__ import annotations

import csv
import json
import math
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "absnesd_2021_firms_by_sex.csv"
OUT_PATH = HERE.parents[1] / "assets" / "family-d" / "ownership-by-sex-2021.png"
API_URL = "https://api.census.gov/data/2021/absnesd"

# Published relative standard error is a percent. Census uses 1.645 to turn
# that percent into an approximate 90 percent margin of error.
MOE_FACTOR = 1.645

SEX_ORDER = ("001", "002", "004", "003", "098")
PIE_SEX = ("002", "004", "003", "098")
SEX_LABELS = {
    "001": "Total",
    "002": "Female",
    "004": "Equally male/female",
    "003": "Male",
    "098": "Unclassifiable",
}
# Fills are dark enough to stand apart from a white page, and from each other
# for common kinds of color blindness. Black outlines separate the slices.
COLORS = {
    "002": "#D55E00",
    "004": "#009E73",
    "003": "#0072B2",
    "098": "#AA4499",
}
ABBREV = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
    "District of Columbia": "DC", "Florida": "FL", "Georgia": "GA", "Hawaii": "HI",
    "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA",
    "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME",
    "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN",
    "Mississippi": "MS", "Missouri": "MO", "Montana": "MT", "Nebraska": "NE",
    "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM",
    "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
    "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI",
    "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX",
    "United States": "US", "Utah": "UT", "Vermont": "VT", "Virginia": "VA",
    "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY",
}


def read_saved_rows(path: Path):
    """Read the saved table, skipping the source notes at the top."""
    lines = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            lines.append(line)
    return list(csv.DictReader(lines))


def _keep_api_row(row):
    sex = row.get("SEX", "")
    eth = row.get("ETH_GROUP", "")
    race = row.get("RACE_GROUP", "")
    vet = row.get("VET_GROUP", "")
    if row.get("NAICS2017") not in (None, "", "00") and "NAICS2017" in row:
        if row["NAICS2017"] != "00":
            return False
    if sex in {"001", "002", "003", "004"}:
        return eth in ("", "001") and race in ("", "00") and vet in ("", "001")
    if sex == "098":
        return eth in ("", "098") and race in ("", "98") and vet in ("", "098")
    return False


def _rows_from_api_table(table):
    header, *body = table
    records = []
    for values in body:
        item = dict(zip(header, values))
        if not _keep_api_row(item):
            continue
        flag = (item.get("FIRMALL_F") or "").strip()
        if flag in {"null", "None"}:
            flag = ""
        firms = "" if flag == "S" else str(item.get("FIRMALL", "")).strip()
        if firms in {"null", "None"}:
            firms = ""
        rse = "" if flag == "S" else str(item.get("FIRMALL_S", "")).strip()
        if rse in {"null", "None"}:
            rse = ""
        sex = item["SEX"]
        records.append(
            {
                "geo_id": item.get("GEO_ID", ""),
                "geo_label": item.get("NAME") or item.get("geo_label") or "",
                "sex": sex,
                "sex_label": item.get("SEX_LABEL") or SEX_LABELS.get(sex, sex),
                "firms": firms,
                "firm_flag": flag,
                "relative_standard_error": rse,
            }
        )
    return records


def _api_request(params, api_key):
    """Call the Census Data API. The key is not printed or saved."""
    query = dict(params)
    if api_key:
        query["key"] = api_key
    url = API_URL + "?" + urllib.parse.urlencode(query)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "data-viz-guidance family-d example"},
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        raise SystemExit(
            f"The Census Data API returned status {error.code}. "
            "Check that CENSUS_API_KEY is valid."
        )
    except urllib.error.URLError:
        raise SystemExit("The Census Data API could not be reached.")
    if raw.lstrip().startswith("<"):
        return None
    try:
        table = json.loads(raw)
    except json.JSONDecodeError:
        return None
    if not isinstance(table, list) or len(table) < 2:
        return None
    return table


def fetch_live_rows(api_key):
    """Download the sex rows for the United States and the states."""
    common = {
        "get": "NAME,SEX,FIRMALL,FIRMALL_F,FIRMALL_S,NAICS2017,ETH_GROUP,RACE_GROUP,VET_GROUP",
        "NAICS2017": "00",
    }
    calls = (
        {**common, "ETH_GROUP": "001", "RACE_GROUP": "00", "VET_GROUP": "001"},
        {**common, "SEX": "098", "ETH_GROUP": "098", "RACE_GROUP": "98", "VET_GROUP": "098"},
    )
    collected = []
    for predicates in calls:
        for geography in ("us:1", "state:*"):
            table = _api_request({**predicates, "for": geography}, api_key)
            if table is None:
                return None
            collected.extend(_rows_from_api_table(table))
    if not collected:
        return None
    return collected


def load_rows():
    """Use the live API when it answers, and the saved CSV otherwise."""
    api_key = os.environ.get("CENSUS_API_KEY", "").strip()
    if api_key:
        print("Reading live 2021 NES-D estimates from the Census Data API.")
        rows = fetch_live_rows(api_key)
        if rows is None:
            raise SystemExit(
                "The Census Data API did not return the firm table. "
                "Check that CENSUS_API_KEY is valid."
            )
        return rows
    print("No CENSUS_API_KEY set. Trying the Census Data API once.")
    rows = fetch_live_rows(None)
    if rows:
        print("Using live 2021 NES-D estimates from the Census Data API.")
        return rows
    print("The Census Data API did not return the table. Using the saved CSV.")
    return read_saved_rows(CSV_PATH)


def _number(text):
    text = (text or "").strip()
    if not text:
        return None
    return float(text)


def group_geographies(rows):
    """Group rows into United States first, then states A to Z."""
    grouped = {}
    for row in rows:
        label = row["geo_label"]
        grouped.setdefault(label, {})[row["sex"]] = row
    names = sorted(name for name in grouped if name != "United States")
    if "United States" in grouped:
        names.insert(0, "United States")
    places = []
    for name in names:
        sexes = grouped[name]
        total_row = sexes.get("001", {})
        total = _number(total_row.get("firms", ""))
        published = []
        for code in PIE_SEX:
            item = sexes.get(code, {})
            suppressed = (item.get("firm_flag") or "").strip() == "S" or not (item.get("firms") or "").strip()
            firms = None if suppressed else int(float(item["firms"]))
            rse = None if suppressed else _number(item.get("relative_standard_error"))
            published.append(
                {
                    "code": code,
                    "label": SEX_LABELS[code],
                    "firms": firms,
                    "suppressed": suppressed or firms is None,
                    "rse": rse,
                }
            )
        shown = [item for item in published if not item["suppressed"]]
        shown_total = sum(item["firms"] for item in shown)
        places.append(
            {
                "label": name,
                "abbrev": ABBREV.get(name, name),
                "total": None if total is None else int(total),
                "groups": published,
                "shown_total": shown_total,
            }
        )
    return places


def margin_of_error(firms, rse):
    """Approximate 90 percent margin of error from the published RSE."""
    if firms is None or rse is None:
        return None
    return int(round(firms * (rse / 100.0) * MOE_FACTOR))


# Row, column on a tile grid that follows the shape of the United States.
# This is the usual small-multiple state map: Alaska and Hawaii sit at the
# lower left and upper left, and the East Coast is on the right.
TILE = {
    "AK": (0, 0), "ME": (0, 10),
    "WI": (1, 5), "VT": (1, 9), "NH": (1, 10),
    "WA": (2, 0), "ID": (2, 1), "MT": (2, 2), "ND": (2, 3), "MN": (2, 4),
    "IL": (2, 5), "MI": (2, 6), "NY": (2, 8), "MA": (2, 9),
    "OR": (3, 0), "NV": (3, 1), "WY": (3, 2), "SD": (3, 3), "IA": (3, 4),
    "IN": (3, 5), "OH": (3, 6), "PA": (3, 7), "NJ": (3, 8), "CT": (3, 9),
    "RI": (3, 10),
    "CA": (4, 0), "UT": (4, 1), "CO": (4, 2), "NE": (4, 3), "MO": (4, 4),
    "KY": (4, 5), "WV": (4, 6), "VA": (4, 7), "MD": (4, 8), "DE": (4, 9),
    "AZ": (5, 1), "NM": (5, 2), "KS": (5, 3), "AR": (5, 4), "TN": (5, 5),
    "NC": (5, 6), "SC": (5, 7), "DC": (5, 8),
    "OK": (6, 3), "LA": (6, 4), "MS": (6, 5), "AL": (6, 6), "GA": (6, 7),
    "HI": (7, 0), "TX": (7, 3), "FL": (7, 8),
}


def _draw_pie(axis, place, title_size):
    # If any owner group is suppressed, do not draw a pie. Drawing the
    # remaining slices would renormalize them and misstate each group's
    # share of all firms. Do not invent a residual or suppressed count.
    if any(item["suppressed"] for item in place["groups"]):
        axis.set_axis_off()
        axis.text(
            0.5,
            0.5,
            "Chart not shown\n"
            "because an ownership\n"
            "category is suppressed.\n"
            "See the data table\n"
            "for published values.",
            ha="center",
            va="center",
            fontsize=7 if title_size <= 8 else 8,
            color="#1b1b1b",
            linespacing=1.15,
            transform=axis.transAxes,
        )
    else:
        sizes = [
            item["firms"]
            for item in place["groups"]
            if not item["suppressed"] and item["firms"]
        ]
        colors = [
            COLORS[item["code"]]
            for item in place["groups"]
            if not item["suppressed"] and item["firms"]
        ]
        if sizes:
            axis.pie(
                sizes,
                colors=colors,
                startangle=90,
                counterclock=False,
                wedgeprops={"edgecolor": "#1b1b1b", "linewidth": 0.6},
            )
    title = place["abbrev"] if place["abbrev"] != "US" else "United States"
    if place["total"] is not None:
        title = f"{title}\n{place['total']:,}"
    axis.set_title(title, fontsize=title_size, color="#1b1b1b", pad=1)


def draw_chart(places, out_path: Path):
    """Save state pies in a map-shaped tile grid, with the U.S. pie above."""
    plt.rcParams["font.family"] = "DejaVu Sans"
    by_abbrev = {place["abbrev"]: place for place in places}
    missing = [code for code in TILE if code not in by_abbrev]
    if missing:
        raise SystemExit(f"Missing a state for the map: {', '.join(missing)}")
    fig = plt.figure(figsize=(13.2, 11.6), dpi=110)
    fig.patch.set_facecolor("#ffffff")
    grid = fig.add_gridspec(
        9,
        11,
        left=0.02,
        right=0.98,
        top=0.86,
        bottom=0.07,
        wspace=0.08,
        hspace=0.55,
    )
    united = by_abbrev.get("US")
    if united:
        _draw_pie(fig.add_subplot(grid[0, 4:7]), united, 11)
    for abbrev, (row, col) in TILE.items():
        _draw_pie(fig.add_subplot(grid[row + 1, col]), by_abbrev[abbrev], 8)

    handles = [
        Patch(facecolor=COLORS[code], edgecolor="#1b1b1b", label=SEX_LABELS[code])
        for code in PIE_SEX
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.965),
        ncol=4,
        frameon=False,
        fontsize=11,
    )
    fig.text(
        0.03,
        0.975,
        "Ownership share of all businesses by sex, 2021",
        fontsize=16,
        fontweight="bold",
        color="#1b1b1b",
        ha="left",
        va="top",
    )
    fig.text(
        0.03,
        0.028,
        "States sit where they do on a map. Each pie uses the published owner groups. "
        "The number under the name is all firms. "
        "Groups are rounded separately from that total. "
        "In Maine, the female-owned count is suppressed.",
        fontsize=8,
        color="#1b1b1b",
        ha="left",
    )
    fig.text(
        0.03,
        0.012,
        "Source: U.S. Census Bureau. NES-D Company Summary, 2021, table AB2100NESD01.",
        fontsize=8,
        color="#1b1b1b",
        ha="left",
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, facecolor="#ffffff")
    plt.close(fig)


def format_count(value):
    if value is None:
        return "Suppressed"
    return f"{value:,}"


def main():
    places = group_geographies(load_rows())
    draw_chart(places, OUT_PATH)
    us = next(place for place in places if place["label"] == "United States")
    print(f"United States, all firms: {us['total']:,}")
    for item in us["groups"]:
        if item["suppressed"]:
            print(f"United States, {item['label']}: suppressed")
        else:
            print(f"United States, {item['label']}: {item['firms']:,}")
    print(f"Places: {len(places)}")
    print(f"Saved {OUT_PATH}")


if __name__ == "__main__":
    main()
