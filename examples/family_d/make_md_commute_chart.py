#!/usr/bin/env python3
"""Draw a part-to-whole chart of how Maryland workers got to work.

The numbers are published Census estimates for the 2020-2024 American
Community Survey 5-year estimates, table B08301, Maryland (FIPS 24),
workers 16 years and over.
Published table: https://data.census.gov/table/ACSDT5Y2024.B08301?g=040XX00US24
API: https://api.census.gov/data/2024/acs/acs5

To download the live estimates, set a Census Data API key in the environment.
Do not paste the key into this file:

    export CENSUS_API_KEY=your_key_here
    python3 examples/family_d/make_md_commute_chart.py

If CENSUS_API_KEY is not set, the program uses the saved estimates in
md_b08301_means_of_transportation.csv. Those saved numbers were copied from
the published 2024 ACS 5-year table on 2026-11-08.
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

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "md_b08301_means_of_transportation.csv"
OUT_PATH = HERE.parents[1] / "assets" / "family-d" / "md-means-of-transportation.png"
API_URL = "https://api.census.gov/data/2024/acs/acs5"
STATE_FIPS = "24"

# variable, label, chart group. The total is not given a group.
PUBLISHED_LINES = (
    ("B08301_001", "Total", ""),
    ("B08301_002", "Car, truck, or van", "car"),
    ("B08301_021", "Worked from home", "home"),
    ("B08301_010", "Public transportation", "transit"),
    ("B08301_019", "Walked", "other"),
    ("B08301_016", "Taxi or ride-hailing services", "other"),
    ("B08301_020", "Other means", "other"),
    ("B08301_018", "Bicycle", "other"),
    ("B08301_017", "Motorcycle", "other"),
)

# These colors stay distinct for common kinds of color blindness.
# Each fill has at least a 3 to 1 contrast with the white page, and the
# black outline has at least a 3 to 1 contrast with each fill.
COLORS = {
    "car": "#0072B2",
    "home": "#D55E00",
    "transit": "#009E73",
    "other": "#AA4499",
}

GROUP_LABELS = {
    "car": "Car, truck, or van",
    "home": "Worked from home",
    "transit": "Public transportation",
    "other": "Walking, taxi or ride-hailing, bicycle, motorcycle, or other means",
}

# Same words as GROUP_LABELS, with a line break so the legend fits.
LEGEND_LABELS = {
    "car": "Car, truck, or van",
    "home": "Worked from home",
    "transit": "Public transportation",
    "other": "Walking, taxi or ride-hailing,\nbicycle, motorcycle, or other means",
}


def read_published_rows(path: Path):
    """Read the saved table, skipping the source notes at the top."""
    data_lines = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            data_lines.append(line)
    return list(csv.DictReader(data_lines))


def rows_from_api_payload(raw: str):
    """Turn a Census Data API JSON table into the same rows as the CSV."""
    try:
        table = json.loads(raw)
    except json.JSONDecodeError:
        raise SystemExit(
            "The Census Data API did not return a data table. "
            "Check that CENSUS_API_KEY is valid."
        )
    if (
        not isinstance(table, list)
        or len(table) < 2
        or not isinstance(table[0], list)
        or not isinstance(table[1], list)
    ):
        raise SystemExit(
            "The Census Data API returned an unexpected table. "
            "Check that CENSUS_API_KEY is valid."
        )

    by_name = dict(zip(table[0], table[1]))
    if by_name.get("state") != STATE_FIPS:
        raise SystemExit(
            "The Census Data API response did not include Maryland. "
            "Check that CENSUS_API_KEY is valid."
        )

    rows = []
    for code, label, group in PUBLISHED_LINES:
        estimate_name = f"{code}E"
        margin_name = f"{code}M"
        if estimate_name not in by_name or margin_name not in by_name:
            raise SystemExit(f"The Census Data API response is missing {code}.")
        try:
            estimate = str(int(by_name[estimate_name]))
            margin = str(int(by_name[margin_name]))
        except (TypeError, ValueError):
            raise SystemExit(
                f"The Census Data API returned a non-numeric value for {code}."
            )
        rows.append(
            {
                "variable": code,
                "label": label,
                "estimate": estimate,
                "margin_of_error": margin,
                "chart_group": group,
            }
        )
    return rows


def fetch_live_rows(api_key: str):
    """Download B08301 for Maryland. The key is not printed or saved."""
    fields = ["NAME"]
    for code, _label, _group in PUBLISHED_LINES:
        fields.extend((f"{code}E", f"{code}M"))
    params = urllib.parse.urlencode(
        {
            "get": ",".join(fields),
            "for": f"state:{STATE_FIPS}",
            "key": api_key,
        }
    )
    request = urllib.request.Request(
        f"{API_URL}?{params}",
        headers={"User-Agent": "data-viz-guidance family-d example"},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        raise SystemExit(
            f"The Census Data API returned status {error.code}. "
            "Check that CENSUS_API_KEY is valid."
        )
    except urllib.error.URLError:
        raise SystemExit(
            "The Census Data API could not be reached. "
            "Check your network connection."
        )
    return rows_from_api_payload(raw)


def load_rows():
    """Use the live API when a key is set, and the saved CSV otherwise."""
    api_key = os.environ.get("CENSUS_API_KEY", "").strip()
    if not api_key:
        print("No CENSUS_API_KEY set. Using the saved CSV.")
        return read_published_rows(CSV_PATH)
    print(
        "Using live 2020-2024 ACS 5-year estimates for Maryland "
        "from the Census Data API."
    )
    return fetch_live_rows(api_key)


def build_slices(rows):
    """Turn the published rows into the four slices drawn on the chart."""
    total = None
    total_margin = None
    grouped = {
        key: {"estimate": 0, "squared_margins": 0}
        for key in GROUP_LABELS
    }

    for row in rows:
        estimate = int(row["estimate"])
        margin = int(row["margin_of_error"])
        group = row["chart_group"].strip()
        if row["variable"] == "B08301_001":
            total = estimate
            total_margin = margin
            continue
        if group not in grouped:
            raise SystemExit(f"Unknown chart group '{group}' in {row['variable']}.")
        grouped[group]["estimate"] += estimate
        grouped[group]["squared_margins"] += margin ** 2

    if total is None or total_margin is None:
        raise SystemExit("The estimates are missing the published total, B08301_001.")

    slices = []
    for key, values in grouped.items():
        estimate = values["estimate"]
        # For one published row, this is that row's own margin of error.
        # For the combined slice, this is the Census formula for a sum:
        # the square root of the sum of the squared margins.
        margin = math.sqrt(values["squared_margins"])
        share = estimate / total
        # Census proportion margin of error. If the usual term under the
        # square root is negative, the Census approximation adds the terms.
        under_root = margin ** 2 - (share ** 2) * (total_margin ** 2)
        if under_root < 0:
            under_root = margin ** 2 + (share ** 2) * (total_margin ** 2)
        percent_margin = 100.0 * math.sqrt(under_root) / total
        slices.append(
            {
                "key": key,
                "label": GROUP_LABELS[key],
                "estimate": estimate,
                "margin": margin,
                "percent": 100.0 * share,
                "percent_margin": percent_margin,
                "color": COLORS[key],
            }
        )

    added = sum(item["estimate"] for item in slices)
    if added != total:
        raise SystemExit(
            f"The slices add to {added:,}, but the published total is {total:,}."
        )
    return total, total_margin, slices


def draw_chart(total, total_margin, slices, out_path: Path):
    """Save a pie chart with labels in a legend, not color alone."""
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(12.4, 7.0), dpi=120)
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#ffffff")

    wedges, _ = ax.pie(
        [item["estimate"] for item in slices],
        colors=[item["color"] for item in slices],
        startangle=90,
        counterclock=False,
        wedgeprops={"edgecolor": "#1b1b1b", "linewidth": 1.8},
    )

    legend_labels = [
        f"{LEGEND_LABELS[item['key']]}\n{item['percent']:.1f}% ± {item['percent_margin']:.2f}"
        for item in slices
    ]
    legend = ax.legend(
        wedges,
        legend_labels,
        loc="center left",
        bbox_to_anchor=(0.98, 0.52),
        frameon=False,
        fontsize=12,
        handlelength=1.4,
        handleheight=1.4,
        labelspacing=1.15,
        borderaxespad=0.2,
    )
    for text in legend.get_texts():
        text.set_color("#1b1b1b")

    ax.set_title(
        "How Maryland workers got to work, 2020–2024",
        loc="left",
        fontsize=18,
        color="#1b1b1b",
        fontweight="bold",
        pad=14,
    )

    fig.text(
        0.01,
        0.075,
        f"Share of {total:,} workers age 16 and over (±{total_margin:,.0f}). "
        "Percents are rounded to one decimal place.",
        fontsize=11,
        color="#1b1b1b",
        ha="left",
    )
    fig.text(
        0.01,
        0.03,
        "U.S. Census Bureau, 2020–2024 American Community Survey 5-Year Estimates, Table B08301.",
        fontsize=11,
        color="#1b1b1b",
        ha="left",
    )

    fig.subplots_adjust(left=0.02, right=0.52, top=0.86, bottom=0.16)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, facecolor="#ffffff", bbox_inches="tight", pad_inches=0.35)
    plt.close(fig)


def main():
    total, total_margin, slices = build_slices(load_rows())
    draw_chart(total, total_margin, slices, OUT_PATH)
    print(f"Published total: {total:,} workers (±{total_margin:,.0f})")
    for item in slices:
        print(
            f"{item['label']}: {item['estimate']:,} "
            f"(±{item['margin']:,.0f}), {item['percent']:.1f}% "
            f"(±{item['percent_margin']:.2f})"
        )
    print(f"Saved {OUT_PATH}")


if __name__ == "__main__":
    main()
