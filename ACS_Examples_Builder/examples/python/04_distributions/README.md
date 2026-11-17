# GB-DATA-001 — Boxplot and Histogram (Python)

This repository-ready example package supports four input options for county-level ACS median-income **estimates**: `api`, `csv`, `excel`, `dataframe`. Local modes do not call the API and do not require API keys. It works for external analysts with their own datasets and authorized output locations.

## Files

- `examples/python/boxplot.py` and `examples/python/histogram.py`: standalone command-line scripts or importable `run()` functions.
- `examples/python/common/county_income.py`: shared input/validation module, installed alongside the scripts in this package.
- `notebooks/boxplot_flexible_input.ipynb` and `notebooks/histogram_flexible_input.ipynb`: self-contained Colab/Jupyter notebooks (no shared module file required).
- `DATA_SCHEMA.md`: supported input columns and interpretation requirements.

## Install

```bash
python -m pip install pandas numpy matplotlib requests openpyxl
```

## Run on YOUR local CSV (no API key)

```bash
python examples/python/boxplot.py --source csv --input-file ./county_income.csv --states Florida Georgia --output-dir ./results/boxplot
python examples/python/histogram.py --source csv --input-file ./county_income.csv --states Florida Georgia --bin-width 10000 --output-dir ./results/histogram
```

For Excel, change `--source csv` to `--source excel` and use an `.xlsx` file. The scripts always save results in the analyst-specified output folder.

## Run with a Pandas DataFrame

```python
import sys
sys.path.insert(0, 'examples/python')  # only needed when running from repository root
import pandas as pd
from boxplot import run as boxplot
from histogram import run as histogram

df = pd.read_csv('county_income.csv', dtype={'GEOID': str})
boxplot(source='dataframe', dataframe=df, states=['Florida','Georgia'], year=2024, output_dir='./results/boxplot')
histogram(source='dataframe', dataframe=df, states=['Florida','Georgia'], year=2024, bin_width=10000, output_dir='./results/histogram')
```

## Optional Census API mode

Use `--source api` to fetch published 2024 ACS 5-year county B19013 estimates and MOEs. Set your own `CENSUS_API_KEY` in your environment if required; the code never saves it in an output. The API may require an active key. API mode is optional and cannot be used offline.

## Visual and statistical interpretation

- **Boxplot** displays Q1/median/Q3 of **county estimates**, with Tukey 1.5×IQR whiskers and marked outlier counties.
- **Histogram** displays the number of counties in fixed shared income bins. Bins are shared between selected states and bin counts must reconcile to the valid county count.
- Neither chart estimates the distribution of incomes *among households*. County estimates have sampling uncertainty, but quartiles, whiskers, and bins are not confidence bounds.
- Missing, negative, and sentinel income estimates are excluded and counted; the full input and published county estimate MOEs remain in exported tables.
- Local datasets must be an ACS-equivalent statistical universe and contain a documented `year`. The scripts do not verify local data provenance.
- Outputs include CSV, PNG, SVG, accessible-table HTML draft, alt-text draft, and an execution manifest. Manual review is required for Section 508 compliance.

## Offline test

```bash
python internal/run_offline_tests.py
```

The tests use *synthetic, ACS-shaped records*, not official Census data. Live data validation and manual accessibility checks remain outstanding.
