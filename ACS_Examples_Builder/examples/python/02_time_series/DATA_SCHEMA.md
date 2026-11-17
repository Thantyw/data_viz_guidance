# Local input contract for time-series examples

One row per geography and ACS release year, with `year` (integer), `NAME` (full state name), and `state` (two-digit state FIPS). For CSV/Excel, field names match Census API variable codes. Users supply their own authorized dataset and are responsible for confirming release, geography, units, source, and comparability.

| Example | Required measure columns | Interpretation |
|---|---|---|
| Line Graph | `B19013_001E`, `B19013_001M` | Annual state median household income estimate and published 90% MOE (release-year dollars); script adjusts supported years to 2024 dollars |
| Area Chart | `B17001_001E`, `B17001_002E`, `B17001_002M` | Poverty-status universe; count below poverty; published count MOE |
| Small Multiples | `B17001_001E`, `B17001_002E`, `B17001_001M`, `B17001_002M` | Counts, published count MOEs, derived poverty percentage |
| Stacked Area | `B01001_001E`, `B01001_002E`, `B01001_026E`, `B01001_002M`, `B01001_026M` | Total, male, female populations; published sex-specific count MOEs |

To use one file for all four, include the union of all columns. Chart routines require complete requested state/year combinations. Invalid count denominators, duplicate geography-year observations, missing/suppressed values, and negative MOEs must not be silently treated as valid. Local data might be transformed data from another source; in that case the displayed labels and provenance must be customized before publication.

The `dataframe` mode expects the same columns and does not use any network connection. The `api` mode uses a chart-specific Census request and validates the returned columns. The DataFrame path is a Python integration API; CLI supports CSV/Excel/API.
