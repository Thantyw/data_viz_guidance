# GB-DATA-001 — Flexible Data Input Pilot

This package upgrades **Bubble Chart** and **Scatter Plot** so external analysts can use a saved CSV, Excel workbook or in-memory data frame. The Census API is **optional** and must be explicitly selected. Local inputs need no API key and no internet connection once software dependencies are installed.

## Quick start — Python

Install: `python -m pip install pandas matplotlib requests openpyxl`

From an analyst-owned CSV with the documented schema:

```bash
python bubble_chart.py --source csv --input ./my_acs_data.csv --out ./my_bubble_outputs
python scatter_chart.py --source csv --input ./my_acs_data.csv --out ./my_scatter_outputs
```

From an Excel workbook:

```bash
python bubble_chart.py --source excel --input ./my_data.xlsx --sheet 0 --out ./outputs
```

Use only Florida and Georgia from a file:

```bash
python scatter_chart.py --source csv --input ./my_acs_data.csv --states Florida,Georgia --out ./outputs
```

From a Python DataFrame:

```python
from bubble_chart import run
result = run(source='dataframe', dataframe=my_dataframe, output_dir='./outputs')
```

To fetch public Census data directly (network and own API key required):

```bash
export CENSUS_API_KEY='your-key'  # use your environment's secret manager instead when available
python bubble_chart.py --source api --states Florida,Georgia --out ./outputs
```

Never save a key in a notebook cell or Git repository. Analysts can inspect the chart and CSV in `--out`; the HTML table and alternative text are **draft accessibility aids** and require review. The data examples use Census measures with 2024 reference-year definitions.

## Colab notebooks

Upload either `.ipynb` file. Change `SOURCE` to `csv`, `excel`, `dataframe`, or `api` in the configuration cell. For CSV/Excel input, upload the file to the Colab runtime or use an analyst-controlled mounted directory and update `INPUT_FILE`. For DataFrame mode, define `ANALYST_FRAME` in an earlier cell. For API mode, retrieve your own key from Colab Secrets and put it in `os.environ['CENSUS_API_KEY']` **without displaying it**. Notebook code is embedded: no private local `.py` file is needed.

## R

Install once: `install.packages(c('jsonlite', 'ggplot2', 'readxl'))`. Install `httr` additionally if using the API.

```r
Sys.setenv(BUBBLE_DATA_SOURCE='csv', BUBBLE_INPUT_FILE='./my_acs_data.csv',
           BUBBLE_OUTPUT_DIR='./my_bubble_outputs')
source('bubble_chart.R')
```

For Excel: set `BUBBLE_DATA_SOURCE='excel'` (or `SCATTER_DATA_SOURCE='excel'`) and `*_INPUT_FILE` to an `.xlsx` file. For a loaded R data frame:

```r
ANALYST_DATA <- read.csv('my_acs_data.csv')
Sys.setenv(SCATTER_DATA_SOURCE='dataframe', SCATTER_OUTPUT_DIR='./outputs')
source('scatter_chart.R')
```

API mode: set `*_DATA_SOURCE='api'`, provide your own `CENSUS_API_KEY`, and optionally set `*_STATES`. R was not executed in the current development environment; test R execution and Python/R parity before relying on it for publication.

## Validation and limitations

Read [DATA_INPUT_SCHEMA.md](DATA_INPUT_SCHEMA.md). Both chart pipelines enforce required fields, geography uniqueness, valid numeric counts and denominators, and poverty ratios in 0–100%. **A renamed dataset is not automatically statistically comparable.** The demonstration assumes 2024 ACS measures and units. Different release years, different geographic units, or non-ACS datasets require confirmation of source metadata, inflation basis, uncertainty methods, and code captions before publication. Both scripts currently reuse 2024 labels; a general-purpose cross-year mode is outside this pilot.

The following evidence was produced in an **offline test with synthetic input only**: [OFFLINE_TEST_RESULTS.csv](OFFLINE_TEST_RESULTS.csv). Live Census API execution, R/Python parity, and manual Section 508 testing were not completed.
