---
layout: default
title: Histogram
permalink: histogram.html
tags: [Distribution, Comparison]
description: "Accessible histogram guidance and reproducible ACS county-estimate examples."
---

# Histogram

## Applying this guidance

Apply the [Census Bureau Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), revised September 29, 2026, within their stated scope. The chart-selection advice and implementation checks on this page explain practical design choices; they do not create additional agency mandates. Treat **Essential** items as the core design conditions for this chart, and confirm formal applicability through the program's review process.

Coordinate this page with [Titles and Subtitles](title.html), [Legends](legend.html), [Sources](source.html), and [Visualizing Uncertainty](uncertainty.html). Keep detailed component guidance in those shared pages rather than duplicating it here.

## 1. Purpose and Overview
A **histogram** summarizes a distribution of quantitative observations by grouping values into adjacent numeric intervals (bins). Bar height represents the count, proportion, or density of observations in each bin. Histograms reveal shape, concentration, asymmetry, gaps, and possible multiple modes. Unlike a categorical bar chart, a histogram uses ordered numeric intervals.

## 2. When to Use
### Essential
- Identify the **unit of observation**, variable, measurement units, and the meaning of bar height.
- State the bin width or binning rule, and use non-overlapping intervals that cover every valid observation.
- Use a zero baseline for count, proportion, or density heights; identify which scale is used.
- Label exclusions and distinguish estimated Census statistics from observed microdata.

### Avoid
- Do not present the distribution of *county estimates* as the distribution of *individual households*.
- Do not vary bin widths without using an appropriate density scale and explaining why.
- Do not describe changes in a histogram's apparent peaks as substantive without checking the effect of bin selection.

## 3. When to Use an Alternative
### Recommended
Use a boxplot for compact comparisons of quartiles and outliers, a dot plot for small samples, or a density plot when smoothing assumptions are appropriate and disclosed.

### Not Recommended
Avoid a histogram for unrelated categories or to show a small number of named individual observations. Use a line graph for changes over time.

## 4. Choosing Between Alternatives
| Reader's question | Display | Reason |
|---|---|---|
| Where are estimates concentrated? | Histogram | Shows frequency across numeric ranges |
| What are each state's median and quartiles? | Boxplot | Summarizes distribution compactly |
| Which county has a particular value? | Dot plot or table | Identifies observations |
| How does the distribution change over years? | Faceted histograms with fixed bins | Supports comparable distributions, with proper year and dollar adjustments |

## 5. Data Requirements and Statistical Considerations
- The **reproducible example** uses **2020–2024 ACS 5-Year Detailed Tables, B19013**. Each observation is a county's estimated *median household income*, `B19013_001E`, in 2024 inflation-adjusted dollars. The published 90% margin of error for that county estimate is `B19013_001M`.
- The chart shows a distribution **across counties**, with one county contributing one observation. It does **not** describe how income is distributed among households or individuals; counties are not weighted by population.
- Exclude invalid and missing estimates, report exclusions, and retain source MOEs in the accompanying table. A histogram of point estimates is **not** a direct visualization of the sampling-error distribution.
- Use **equal-width, shared bins** and a consistent x-axis when comparing panels. In the example, the analyst can change the default $10,000 bin width and inspect the results.
- Report count of valid counties per state and verify that bin frequencies reconcile to that number. Interpret shape carefully for small samples, heaped values, and estimates with large MOEs.

## 6. Visualization-Specific Considerations and Accessibility
- Label axes with the underlying unit and count definition; title each panel with its state and number of counties.
- Use clear bar boundaries and sufficient contrast, avoiding color-only meaning. Do not use decorative gaps to imply categorical separation.
- Supply descriptive alternative text and an accessible HTML table of bin ranges, frequencies, and source county values. Confirm the page is understandable under zoom, keyboard navigation, and screen-reader reading order.
- A generated HTML table and draft alt text **do not establish Section 508 compliance** without manual testing.

### Bar arrangement and color

Keep numeric ranges on the horizontal axis and count, proportion, or density on the vertical axis. Use an upright, zero-based magnitude scale. Adjacent numeric bins should touch; thin outlines can separate bars, but decorative gaps should not suggest unrelated categories. Use one fill color for a single distribution, with at most one additional highlight color when that highlight has an explained analytical purpose. If separate groups require different encodings, label them explicitly or use separate panels.

The original guidance specifies at least three intervals. Use three or more meaningful bins when the observations support them; if so few distinct values exist that this would create artificial structure, consider a dot plot or table and document the chart-choice rationale.

### Design comparison

Use these comparisons to connect each design choice with its effect on interpretation.

| Problematic approach | Why it matters | Preferred approach |
|---|---|---|
| Title says household income distribution but each row is a county median | Readers infer a distribution of household observations | Title the chart as a distribution of county median household-income estimates |
| Panels choose separate automatic bin edges | Similar bars represent different numerical ranges | Calculate and reuse one set of bin edges for all comparison panels |
| A value on a bin boundary is counted twice or omitted | Frequencies no longer reconcile to included observations | Specify left-closed/right-open intervals, with the final upper edge included |

### Checking the published example

Test the chart at its intended display size and with enlarged text. Follow the reading sequence from title to explanation, figure, table, and source. Check that labels and meaningful marks remain distinguishable without color and that any controls can be operated by keyboard with visible focus. Read the explanation and table with a screen reader to confirm that they convey the same measures, units, missing-data conditions, and important relationships as the chart.

Use [automated and manual accessibility testing](https://www.section508.gov/test/testing-overview/) together. A downloadable CSV supplies values but does not replace the chart's explanatory narrative; see [USWDS visualization guidance](https://designsystem.digital.gov/components/data-visualizations/). Record the page/version, tool or assistive technology, result, and corrective action. Apply the sponsor's agreed accessibility baseline rather than treating a palette simulation as a conformance test.

## 7. Census Data Examples

### Original archive example: percentage aged 65 and older by county

![Historical histogram of counties grouped by the percentage of residents aged 65 and older. The horizontal axis is percentage of seniors in a county and the vertical axis is number of counties.](assets/originals/histogram_original.jpg)

The original illustration is titled *Item 1: Percentage of Population Aged 65 and Older*. Each observation is a county, not a person. The distribution has a central concentration and a longer right tail; the figure uses a single fill and a zero-based frequency axis. Its embedded source URL refers to the 2014 Population Estimates Program. It is a historical design example, separate from the ACS income demonstration below.

**Reading lesson:** distinguish the percentage measured within each county from the number of counties in each bin. The raster illustration does not supply an exact bin-count table; retrieve the original data and confirm the bin definitions before making numerical claims or reproducing the figure. Its presence here is not a claim that the historical graphic satisfies current accessibility requirements.

**Reproducible ACS demonstration — county median household-income estimates in selected states (2020–2024 ACS 5-Year).** Each panel displays how many counties fall in each income-estimate range. All states use the same bin boundaries. This chart does not represent the income distribution of residents.

<!-- Add only the actual image created from a verified live Census API run. -->
<!-- Verified-output image target: ![Histogram panels showing counts of counties within shared county median-income estimate ranges for selected states. Exact counts and ranges are provided in the linked data table.](assets/examples/histogram_acs.png) -->

Expected table asset: `assets/examples/histogram_data_table.html`, containing exact bin counts and county-estimate values. The published 90% county-level margins of error appear in the table; they are not histogram error bars.

## 8. Developer Implementation

The following contract defines the intended behavior of the linked examples. Confirm the files, commands, dependencies, and generated results against the repository before publication.

### 8.1 Data Preparation

**Inputs:** 2020–2024 ACS 5-Year B19013 county estimates and published MOEs, state/county identifiers, annotations, and an analyst-selected common bin width.

Keep one valid county estimate per geographic identifier. Identify the full 2020–2024 reference period and 2024 dollar basis. Count valid and excluded counties by state. Define shared bin edges covering every included value and record interval closure; use left-closed/right-open bins with the last upper endpoint included.

### 8.2 Python

[Python script](examples/python/histogram.py) or [notebook](notebooks/histogram_colab.ipynb). The documented parameters are `--states`, `--year`, `--bin-width`, and `--output-dir`.

### 8.3 R

[R script](examples/R/histogram.R), using `HISTOGRAM_STATES`, `HISTOGRAM_ACS_YEAR`, `HISTOGRAM_BIN_WIDTH`, and `HISTOGRAM_OUTPUT_DIR`. Set interval closure explicitly to match Python rather than relying on each language's defaults.

### 8.4 Reproducibility and Adaptation

A personal Census API key is required for data queries under the [current Census API guidance](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html). Read `CENSUS_API_KEY` from the analyst's environment. Do not include keys in source control, saved notebooks, request logs, error messages, or execution manifests; redact the `key` query parameter wherever a request URL is recorded. No shared developer credential or private file path should be required.

For each run, save the validated data, chart PNG/SVG, a semantic HTML table, descriptive-text draft, and a nonsecret manifest in the selected output folder. Include source table/variables, full reference period, geography, units, transformations, exclusions, dependency versions, and retrieval time. Pin or record versions actually tested. For identical inputs, R and Python should reproduce the same analytical values within an explicitly documented tolerance; visual styling need not be pixel-identical.

When changing years or geographies, recheck product coverage, definitions, annotations, and comparability. A successful run does not establish statistical significance or accessibility conformance.

### 8.5 Output Verification

| Check | Expected evidence |
|---|---|
| Frequencies | For each state, sum of bin counts equals the number of included counties; excluded records are counted separately |
| Boundaries | Minimum, maximum, and every exact boundary value belong to one bin only; Python and R return the same bin counts |
| Density mode | If density is used, sum of bar height × bin width equals one within the stated tolerance; do not label density as county count |

**Source-statement pattern for this example:** U.S. Census Bureau, American Community Survey, 2020–2024 ACS 5-Year Estimates, Detailed Table B19013. One observation per county median household-income estimate; values in 2024 inflation-adjusted dollars; counties equally weighted. Add the specific source or reproducible request link and actual retrieval date; omit the API key. Identify derived calculations separately from published estimates.

## 9. Common Errors and Misinterpretations
| Problem | Correction |
|---|---|
| Calling county estimates a histogram of household incomes | Name counties as the observation unit |
| Different bin boundaries in state comparisons | Use shared numerical bin edges |
| Omitted or invalid counties disappear silently | Show exclusion counts in the data table |
| Treating point-estimate histograms as precise | Preserve county MOEs and explain survey uncertainty |
| Reading a binning artifact as a real population cluster | Check alternative bin widths and avoid unsupported inference |

## 10. Publication Quality Checklist
- [ ] Data source, release, geography, observation unit, and variable units are identified.
- [ ] Bin widths, edges, and frequency denominators are disclosed and mathematically verified.
- [ ] The actual ACS figure, bin-count table, and county-data table are available at working relative links.
- [ ] County estimates are not confused with household microdata; MOEs and exclusions are documented.
- [ ] The Python and R code run independently with user-controlled settings and no private files.
- [ ] Original Census examples are reconciled and verified before final publication.
- [ ] Section 508 checks are performed on the rendered GitHub Pages site.

## Related Pages and References
Related: [Boxplot](boxplot.html), [Line Graph](linegraph.html), [Visualizing Uncertainty](uncertainty.html).

Sources: [ACS 5-Year API](https://api.census.gov/data/2024/acs/acs5); [B19013 estimate definition](https://api.census.gov/data/2024/acs/acs5/variables/B19013_001E.html); [B19013 on data.census.gov](https://data.census.gov/table?q=B19013&tid=ACSDT5Y2024.B19013).

### Standards and Review References

Adapted in part from the *U.S. Data Design Standards* archive, `_visualizations/histogram.md`. The source archive is an earlier site implementation; its layout, front matter, and examples require reconciliation with the current Census repository.

Use the [September 29, 2026 consolidated Census Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), especially E1-6 (replication documentation), E2-2.3 (visualization requirements), and E3-2.4 (visualization review). Retain review findings and corrections separately from the design checklist.

- [Census API query requirements](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html).
- [Section 508 testing methods](https://www.section508.gov/test/testing-overview/).
- [USWDS data visualization guidance](https://designsystem.digital.gov/components/data-visualizations/).
