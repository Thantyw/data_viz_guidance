# GB-DATA-001 input specifications — component examples

These examples expect **ACS-compatible data structures**, even when the records come from local files or in-memory DataFrames. Do not claim unrelated or transformed data are Census estimates without verifying source, year, universe, units, and variable definitions.

All local datasets require `NAME` (geography name). A `year` integer column is recommended; if present, it is filtered against 2024. An optional `state` FIPS column can be retained. Local inputs may contain additional columns. **One record per selected geography** is required for these component demonstrations.

| Script | Required 2024 ACS columns | Interpretation and checks |
| --- | --- | --- |
| `uncertainty.py` | `B19013_001E`, `B19013_001M` | Median household income, published 90% MOE; interval = estimate ± MOE; not a significance test |
| `nested_categories.py` | `B03002_001E`–`B03002_009E`, `B03002_012E`, `DP03_0095E`–`DP03_0099E` | Total = Hispanic + non-Hispanic; non-Hispanic nested race groups sum to their parent. Civilian noninstitutionalized = insured + uninsured; private/public coverage may overlap and cannot be stacked as disjoint groups |
| `population_pyramid.py` | `B01001_001E`–`B01001_049E` (full detailed estimates) | Male + female = total; detailed age-bin sums reconcile; whole-population denominator used for percentages |

The population pyramid script requests the 49 estimate variables used by B01001 (some comprise separate totals and age bands). It plots 18 age bands, with 85+ open-ended; it **does not** derive sampling margins of error for the plotted age groups.

## Input methods

- **CSV:** local comma-delimited UTF-8 data with header columns.
- **Excel:** first worksheet of a local `.xlsx` workbook, same field names; requires `openpyxl`.
- **DataFrame:** `pandas.DataFrame` passed to `run(source='dataframe', dataframe=frame, ...)`.
- **API:** optional direct Census API retrieval. Key is obtained from analyst environment variable `CENSUS_API_KEY`, if configured. No key is stored in output manifests.

For **Nested Categories API mode**, the script separately requests B03002 Detailed Tables and DP03 Profile data, then joins on state names. For **local input modes**, an analyst must supply the merged columns shown above.

## Missing and suppressed values

Negative Census special values and missing data are rejected rather than treated as zero. A user must resolve missing geography/year rows before running. Avoid dropping records silently, especially when records represent distinct geographic or demographic groups.

## Chart output and accessibility

Each script creates PNG, SVG, CSV, HTML data table, draft alt-text, and JSON manifest in the selected folder. The files are **not an accessibility certification**. Check noncolor distinctions, screen-reader reading order, text alternatives, visual scaling, data-table labeling, and readability on the deployed website.
