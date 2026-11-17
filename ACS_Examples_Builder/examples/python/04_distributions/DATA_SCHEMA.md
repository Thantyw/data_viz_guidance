# GB-DATA-001 — County income input specification

One record **per unique county per selected ACS five-year release**. The example accepts either the Census API variable names or a normalized analyst schema.

| Field | Required? | Meaning |
|---|---|---|
| `year` | Always | Release year, e.g. `2024`; must match the configured year |
| `NAME` | Always | Descriptive county name |
| `state_name` | Always | Full state name, e.g. `Florida` |
| `GEOID` | For tidy input | Five-digit state+county FIPS identifier; preserve leading zeroes |
| `median_income` | For tidy input | County median household-income *estimate*, USD, strictly positive |
| `moe_90` | For tidy input | Published 90% MOE of county estimate; nonnegative or flagged invalid |
| `state`, `county` | For ACS-shaped input | Two/three-digit FIPS codes |
| `B19013_001E`, `B19013_001M` | For ACS-shaped input | Census estimate and 90% MOE |

**Shapes:**
- **Tidy**: `year,NAME,state_name,GEOID,median_income,moe_90`
- **ACS**: `year,NAME,state_name,state,county,B19013_001E,B19013_001M`

Local CSV must be UTF-8 encoded. Excel uses `.xlsx` and the first worksheet by default. Keep a single release year per run. Do not provide aggregate state median income as though it were a county observation; these distributions count counties equally, not households. MOEs may be missing/invalid but are flagged; they are not confidence limits for the boxplot summary or histogram bin counts. For distributional analyses of *household income*, use appropriately authorized microdata and a different analytical workflow.

Supported Python input sources:

`run(source='api'|'csv'|'excel'|'dataframe', states=[...], year=2024, input_file=..., dataframe=..., output_dir=...)`

The Census API is an optional acquisition method, never a precondition for visualization using local data.
