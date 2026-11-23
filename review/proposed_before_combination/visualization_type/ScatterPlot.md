---
layout: default
title: Scatter Plot
permalink: scatterplot.html
tags: [Correlation, Distribution]
description: "Guidance for accessible, statistically responsible scatter plots with reproducible ACS examples."
---

# Scatter Plot

Also known as: scatterplot, scatter graph, scatter chart, scattergram, or scatter diagram. See also: [Bubble Chart](bubblechart.html).

## Applying this guidance

Apply the [Census Bureau Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), revised September 29, 2026, within their stated scope. The chart-selection advice and implementation checks on this page explain practical design choices; they do not create additional agency mandates. Treat **Essential** items as the core design conditions for this chart, and confirm formal applicability through the program's review process.

Coordinate this page with [Titles and Subtitles](title.html), [Legends](legend.html), [Sources](source.html), and [Visualizing Uncertainty](uncertainty.html). Keep detailed component guidance in those shared pages rather than duplicating it here.

## 1. Purpose and Overview

A scatter plot places one observation at each pair of numerical coordinates (x, y), revealing patterns, clusters, outliers, and possible associations between **two quantitative variables**. A bubble chart adds a third quantitative variable through proportional circle **area**. Scatter plots display association, not causation; no fitted line is required.

## 2. When to Use

### Essential

- Specify the **unit of observation**, geography, year, x and y measures, and units in the title, axis labels, or caption.
- Use one consistent coordinate system and disclose missing, excluded, suppressed, or incomparable observations.
- Ensure markers can be distinguished and annotations do not obscure plotted values; supply a data table.
- Provide a clear source and explain derived variables and denominators.

### Avoid

- Do not infer causation or statistical significance from a visible trend or correlation alone.
- Do not connect scatter points as if they form an ordered time series.
- Do not use jitter without disclosing that positions were altered. Do not rely solely on color or hover to distinguish categories.

## 3. When to Use an Alternative

### Recommended

Use a **Bubble Chart** when the third quantity materially improves interpretation and can be encoded accurately by marker area. Use a **Line Graph** for changes over time; a **Small Multiples** display when group comparisons crowd a single view; and a data table when precise values matter most.

### Not Recommended

Avoid a single static scatter plot when severe overplotting hides most observations, the sample is too small for a meaningful relationship claim, or variables are categorical rather than quantitative. Consider transparency, faceting, binned counts, or tabular alternatives when appropriate.

## 4. Choosing Between Alternatives

| Question | Visualization |
|---|---|
| How do two numeric measures vary together? | Scatter plot |
| Does population size change the interpretation? | Bubble chart, with area-proportional markers |
| How do measurements evolve over ordered time? | Line graph |
| Are subgroup comparisons obscured? | Small multiples or separate charts |

## 5. Data Requirements and Statistical Considerations

- One observation must have one valid x–y pair. Record geography, collection period, variable labels, and source table IDs.
- Do not confuse a **poverty-status universe** with total population or number of households. For the ACS example below, percentage = `100 × B17001_002E / B17001_001E`.
- ACS estimates are subject to sampling error. `B19013_001M` and `B17001_002M` represent **published 90% margins of error for their respective estimates**, not a margin of error for the derived poverty percentage. Calculate ratio uncertainty using an appropriate Census-approved method if it is to be displayed or tested.
- Avoid misleading regressions: geographic aggregates do not establish individual-level relationships. If fitting a line, disclose its method, population, sample size, and statistical limitations.
- Reject negative ACS sentinel codes, zero denominators, missing fields, and non-comparable units before drawing the chart.

## 6. Visualization-Specific Considerations and Accessibility

- Use simple, equally sized point markers when no third numeric quantity is encoded. Circular points avoid misleading unequal marker dimensions.
- Label axes and their units. Selectively label points without concealing nearby markers; an accompanying table provides all observations.
- Choose adequate contrast. Marker edges, text labels, or shapes should communicate distinctions **without reliance on color alone**.
- Provide descriptive alternative text and a properly structured HTML table with column headings. Test keyboard navigation and screen-reader behavior of the **published GitHub page**, not just the source image.
- If jitter, filtering, transformation, or regression is used, explain it adjacent to the graph.

### Categories and markers

If categories or multiple point series require a key, include a clear legend unless direct labels already identify them unambiguously. Keep the title's observation unit explicit. Use simple markers, position selective labels so they do not overlap, and use leader lines where needed. Two quantitative coordinates define the scatter plot; additional categories must not obscure that relationship. If a third quantitative value changes marker area, follow the Bubble Chart guidance.

### Design comparison

Use these comparisons to connect each design choice with its effect on interpretation.

| Problematic approach | Why it matters | Preferred approach |
|---|---|---|
| Point sizes vary without a named third measure | Readers may infer a quantity that is not encoded | Use equal marker areas for the two-variable scatter plot |
| Poverty count is divided by total population | The denominator differs from the published poverty-status universe | Use B17001_001E for the derived percentage and document the formula |
| A fitted line is described as a causal or nationally representative result | Selected aggregate observations cannot support that conclusion by themselves | Describe the selected-state association and disclose any fitted-line method and limitations |

### Checking the published example

Test the chart at its intended display size and with enlarged text. Follow the reading sequence from title to explanation, figure, table, and source. Check that labels and meaningful marks remain distinguishable without color and that any controls can be operated by keyboard with visible focus. Read the explanation and table with a screen reader to confirm that they convey the same measures, units, missing-data conditions, and important relationships as the chart.

Use [automated and manual accessibility testing](https://www.section508.gov/test/testing-overview/) together. A downloadable CSV supplies values but does not replace the chart's explanatory narrative; see [USWDS visualization guidance](https://designsystem.digital.gov/components/data-visualizations/). Record the page/version, tool or assistive technology, result, and corrective action. Apply the sponsor's agreed accessibility baseline rather than treating a palette simulation as a conformance test.

## 7. Census Data Examples

**2024 ACS 1-Year Detailed Tables: state median household income versus poverty percentage.** Each point represents one state. The horizontal axis displays `B19013_001E` (median household income in 2024 inflation-adjusted dollars); the vertical axis is `100 × B17001_002E / B17001_001E` (percentage below poverty threshold among people whose poverty status is determined). The example uses the same axes as the related Bubble Chart but intentionally does **not** encode population through marker size.

<!-- Verified-output image target: ![Scatter plot comparing 2024 median household income and percentage below the poverty threshold for selected states; each point uses an equal-sized marker. Exact values are available in the linked data table.](assets/examples/scatter_plot.png) -->

- Expected table asset: `assets/examples/scatter_plot_table.html`. Publish the verified chart and table together.
- [2024 Census ACS API metadata: B17001](https://api.census.gov/data/2024/acs/acs1/groups/B17001.html) and [B19013](https://api.census.gov/data/2024/acs/acs1/groups/B19013.html).

### Additional published examples

These retained examples show distinct labeling and interpretation choices. The corresponding image assets must be present in the repository.

**Example A — Public pension coverage versus wage replacement, selected Asian countries.** The original figure shows how selected labels can identify important observations without covering the coordinates. **Reading lesson:** inspect the axes and any fitted line separately; a regression line alone does not establish causation.

![Scatter plot of public pension coverage versus wage replacement, with selected observations labeled.](assets/ScatterPlot1.png)

**Example B — Median estimated earnings by sex and occupation.** Monetary axes and equally sized point markers help comparisons. **Reading lesson:** verify the occupation and sex groups before inferring what any apparent difference represents.

![Scatter plot of estimated earnings across sex and occupation categories.](assets/ScatterPlot2.png)

**Example C — Uninsured rate in 2013 versus change from 2013 to 2014, by occupation.** Leader lines connect labels to observations. **Reading lesson:** distinguish a starting rate from its subsequent change, and do not infer that the start rate caused the change.

![Scatter plot of uninsured rates and year-over-year change by occupation, with annotation leader lines.](assets/ScatterPlot3.png)

## 8. Developer Implementation

The following contract defines the intended behavior of the linked examples. Confirm the files, commands, dependencies, and generated results against the repository before publication.

### 8.1 Data Preparation

**Inputs:** 2024 ACS 1-Year B19013 and B17001 records joined by state identifier, with income estimate/MOE, poverty count/MOE, poverty-status universe, and annotations.

Require one x–y pair per included state. Derive poverty percentage as 100 × B17001_002E / B17001_001E only for a valid positive universe. Check the count is between zero and its universe, join cardinality is one-to-one, and both measures use the same release and geography. Document excluded states and retain published MOEs.

### 8.2 Python

[Python script](examples/python/scatter_plot.py) or [notebook](examples/notebooks/scatter_plot_colab.ipynb). Use `SCATTER_STATES` or `--states`, and `SCATTER_OUTPUT_DIR` or `--out` as documented in the [run guide](examples/scatter_plot_README.md).

### 8.3 R

[R script](examples/R/scatter_plot.R) with the same state selection, percentage definition, source release, and output configuration.

### 8.4 Reproducibility and Adaptation

A personal Census API key is required for data queries under the [current Census API guidance](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html). Read `CENSUS_API_KEY` from the analyst's environment. Do not include keys in source control, saved notebooks, request logs, error messages, or execution manifests; redact the `key` query parameter wherever a request URL is recorded. No shared developer credential or private file path should be required.

For each run, save the validated data, chart PNG/SVG, a semantic HTML table, descriptive-text draft, and a nonsecret manifest in the selected output folder. Include source table/variables, full reference period, geography, units, transformations, exclusions, dependency versions, and retrieval time. Pin or record versions actually tested. For identical inputs, R and Python should reproduce the same analytical values within an explicitly documented tolerance; visual styling need not be pixel-identical.

When changing years or geographies, recheck product coverage, definitions, annotations, and comparability. A successful run does not establish statistical significance or accessibility conformance.

### 8.5 Output Verification

| Check | Expected evidence |
|---|---|
| Point count | Number of plotted points equals the number of valid, unique joined states; each state has one recorded x–y pair |
| Coordinates | X equals the income estimate and Y equals the documented poverty percentage; marker area is constant |
| Uncertainty | Published poverty-count MOE remains labeled as a count MOE; no uncalculated percentage MOE or fitted-model inference is reported |

**Source-statement pattern for this example:** U.S. Census Bureau, American Community Survey, 2024 ACS 1-Year Estimates, Detailed Tables B19013 and B17001, selected states. Poverty percentages calculated from B17001 estimates; income is in 2024 inflation-adjusted dollars. Add the specific source or reproducible request link and actual retrieval date; omit the API key. Identify derived calculations separately from published estimates.

## 9. Common Errors and Misinterpretations

| Error | Correction |
|---|---|
| Treating association as causation | State the graph is descriptive; avoid causal claims |
| Using total population to calculate poverty percentage | Divide by the B17001 poverty-status universe |
| Claiming numerator MOE is the derived percentage MOE | Use a suitable ratio-MOE method or omit a percentage MOE |
| Overlapping every point label | Label selectively and provide an accompanying table |
| Displaying suppressed ACS values as actual numbers | Filter and document invalid or suppressed observations |
| Using bubble-size encoding unintentionally | Keep point areas equal for a two-variable scatter plot |

## 10. Publication Quality Checklist

- [ ] Variables, units, observation geography, and denominator are documented.
- [ ] Source values and estimates validated; missing or suppressed observations handled.
- [ ] Scatter markers are legible; overlaps and label collisions evaluated.
- [ ] Each image is an **actual**, verified chart and its relative path resolves from the published page.
- [ ] Descriptive text alternative, accompanying table, and source/caption are present.
- [ ] PNG/SVG, CSV, and HTML outputs correspond to the same API retrieval.
- [ ] Python and R run with the reader's own credentials and output directory.
- [ ] Published HTML is manually assessed for keyboard access, screen-reader navigation, and legibility.

**Related pages:** [Bubble Chart](bubblechart.html), [Line Graph](linegraph.html), and [Visualizing Uncertainty](uncertainty.html).

### Standards and Review References

Adapted in part from the *U.S. Data Design Standards* archive, `_visualizations/scatter-plot.md`. The source archive is an earlier site implementation; its layout, front matter, and examples require reconciliation with the current Census repository.

Use the [September 29, 2026 consolidated Census Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), especially E1-6 (replication documentation), E2-2.3 (visualization requirements), and E3-2.4 (visualization review). Retain review findings and corrections separately from the design checklist.

- [Census API query requirements](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html).
- [Section 508 testing methods](https://www.section508.gov/test/testing-overview/).
- [USWDS data visualization guidance](https://designsystem.digital.gov/components/data-visualizations/).
