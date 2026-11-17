# GB-DATA-001 common input contract

The **API, CSV, Excel and Python DataFrame** modes use the same chart-specific `prepare()` checks.

Two supported input layouts:

1. **Census ACS raw columns**: `NAME`, `B19013_001E`, `B19013_001M`, `B17001_001E`, `B17001_002E`, `B17001_002M`, `B01003_001E`. `state` geographic code may also be present; not mandatory for file mode.
2. **Normalized analytical columns**: `state`, `median_household_income_usd`, `income_moe_90_usd`, `poverty_universe`, `below_poverty_count`, `below_poverty_count_moe_90`, `total_population`. This layout is convenient for saved datasets and Pandas DataFrames.

Input values represent **2024 ACS 1-Year Detailed Tables** measures or a dataset with **equivalent documented definitions, reference year and units**. The demonstration assumes income amounts are in 2024 dollars. Merely renaming arbitrary fields does not establish comparability or statistical validity. The poverty universe is the population for whom poverty status is determined, not total population. Published count MOEs do not equal the derived poverty-percentage MOE.

File mode supports `.csv` and `.xlsx` (`--sheet` selects an Excel sheet). API mode is explicitly selected via `--source api`. Neither file nor DataFrame mode accesses the network or asks for an API key. API mode requires a valid API key according to the service's current requirements; supply `CENSUS_API_KEY` as an environment variable. For file/dataframe input provide any state names in the data; configure `--states` to filter a subset, or omit it to include all rows. Duplicates, missing fields, invalid numerics, negative sentinel values, zero denominators and numerator > denominator fail validation.

Outputs are always created under `--out`; the notebook can use `./outputs` or another authorized directory. Avoid committing credentials or private input data to public GitHub. Manual Section 508 checks are still required. Generated HTML tables and alt-text drafts are **supporting assets, not compliance certification**.
