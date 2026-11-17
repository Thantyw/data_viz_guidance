# Flexible-input Python demonstrations: four time-series visualizations

These examples support **GB-DATA-001** and **GB-REP-001**. They are designed for analysts who clone or fork a public GitHub repository, use their own files, and choose their own output folders. No private files, developer paths, or credentials are included.

## Install

Python 3.10+ is recommended. From this package directory:

```bash
python -m pip install -r requirements.txt
```

## Input modes

- `csv` — uses a local CSV with `year`, `NAME`, `state`, and required ACS-named measure columns. **No Census API call or key.**
- `excel` — same structure in the first worksheet of an XLSX file. **No Census API call or key.**
- `dataframe` — in-memory `pandas.DataFrame`, through documented Python functions, with the same field schema. **No Census API call or key.**
- `api` — retrieves public ACS 1-Year data. Any credentials are analyst-controlled (`CENSUS_API_KEY`); do not save the key in code, notebooks, screenshots, or outputs. A key may be required for successful service access.

The default command-line mode remains `api` for continuity with the original demonstrations. Select `csv` or `excel` for offline use. The Colab notebooks default to `csv` so users are not inadvertently required to authenticate.

## Commands

Run from `examples/python` (or use an absolute path to the script):

```bash
python line_graph.py --source csv --input-file ./my_acs.csv --states Florida,Georgia --years 2021,2022,2023,2024 --out ./out_line
python area_chart.py --source excel --input-file ./my_acs.xlsx --states Florida,Georgia --years 2021,2022,2023,2024 --out ./out_area
python small_multiples.py --source csv --input-file ./my_acs.csv --states Florida,Georgia --years 2021,2022,2023,2024 --output-dir ./out_small
python stacked_area.py --source csv --input-file ./my_acs.csv --states Florida,Georgia --years 2021,2022,2023,2024 --out ./out_stacked
```

For API mode, omit `--input-file` and use `--source api`, with `CENSUS_API_KEY` in your environment if required.

## In-memory example

```python
import pandas as pd
from line_graph import make_data
frame = pd.read_csv('my_acs.csv')
result, source_urls = make_data([2021, 2022, 2023, 2024], ['Florida', 'Georgia'],
                                source='dataframe', dataframe=frame)
```

`area_chart.main(args=['--source','dataframe','--states','Florida,Georgia', '--years','2021,2022', '--out','./out'], dataframe=frame)` is also supported; `small_multiples.run(source='dataframe', dataframe=frame, ...)` and `stacked_area.main(source='dataframe', dataframe=frame)` likewise accept in-memory data. For Stacked Area `STACKED_STATES`, `STACKED_YEARS`, and `STACKED_OUTPUT_DIR` can be set in the environment or as command-line flags for file modes.

## Important limitations

- **Local inputs are not guaranteed to be ACS data.** Chart titles, source text, interpretation, currency-year claims, and manifest provenance must be verified before reusing the example with different datasets.
- The Line Graph uses **specific 2021–2024 ACS income and R-CPI-U-RS adjustments**. This example does not accept arbitrary year/data definitions or silently change its inflation factors.
- Area and Small Multiples derive poverty measures using `B17001`; the published count MOEs do **not** become MOEs for calculated poverty percentages.
- Stacked Area checks `B01001_002E` (male) + `B01001_026E` (female) = `B01001_001E` (total) at each state/year. Never stack overlapping categories as though additive.
- These programs generate data tables and draft alternative text, but **do not certify Section 508/WCAG compliance**. Verify chart readability, color/noncolor differentiation, images/links, alt text, and HTML in the deployed site.
- The offline tests use **synthetic data only** and prove no live API or R parity.
- `2020` standard ACS 1-Year is not treated as part of the supported time series.

See `DATA_SCHEMA.md` for required columns and `internal/PYTHON_OFFLINE_TEST_RESULTS.csv` for local verification evidence (internal only).
