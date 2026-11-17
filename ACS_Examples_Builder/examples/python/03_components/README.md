# Flexible-input Python component examples

Three independently reusable Python examples for the public Census Bureau visualization guidance: **Visualizing Uncertainty**, **Nested or Non-Mutually Exclusive Categories**, and **Population Pyramid**.

These examples follow GB-DATA-001 and GB-REP-001. **The Census API is optional.** Analysts can select their own CSV/Excel input file, in-memory Pandas DataFrame, output location, and geographies without needing access to the original author's files. No private project process or approval is required.

## Installation

Python 3.10+:

```bash
python -m pip install -r requirements.txt
```

Run from `examples/python`, or place the `common` folder alongside the scripts when copying files into another directory.

## Command-line examples (no API access)

```bash
python uncertainty.py --source csv --input-file ./my_acs_extract.csv --states Florida,Georgia --out ./outputs_uncertainty
python nested_categories.py --source excel --input-file ./my_acs_extract.xlsx --states Florida,Georgia --out ./outputs_nested
python population_pyramid.py --source csv --input-file ./my_b01001.csv --states Florida,Georgia --mode percent --out ./outputs_pyramid
```

For API demonstrations, use `--source api` and omit `--input-file`. Supply `CENSUS_API_KEY` via your environment if required for the Census service; never include an API key in published code.

## Pandas DataFrame example

```python
import pandas as pd
from uncertainty import run
frame = pd.read_csv('./my_acs_extract.csv')
result = run(source='dataframe', dataframe=frame, states=['Florida'], output_dir='./outputs')
```

The equivalent function `run(...)` is available in `nested_categories.py` and `population_pyramid.py` (with optional `mode='count'|'percent'`).

## Colab notebooks

The three notebooks in `notebooks/` contain their own copies of the Python scripts and reusable utilities. Run setup and choose the input location before running the final cell. You **do not** need access to the original developer's files.

For field definitions, expected tables, and statistical limitations, read `DATA_SCHEMA.md`.

## Safety and interpretation

- **Uncertainty:** B19013 MOEs produce 90% intervals; never use overlap alone to assert statistical significance.
- **Nested Categories:** B03002 origin groups form a partition; DP03 private/public insurance groups may overlap and must not be stacked as if mutually exclusive. If using non-Census files, map and validate definitions before reusing the code.
- **Population Pyramid:** B01001 age/sex groups must reconcile to total population; percentages of both sexes together equal 100%.
- **Section 508:** Draft alt text and HTML tables are supporting artifacts; manual deployed-page review is needed.

The offline tests use simulated ACS-shaped values; they do **not** establish live API validity, statistical representativeness, Python/R parity, or full Section 508 compliance.
