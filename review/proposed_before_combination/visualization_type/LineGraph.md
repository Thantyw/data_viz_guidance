---
layout: default
title: Line Graph
permalink: linegraph.html
tags: [Comparison, Trends]
description: "Guidance for statistically sound, accessible, reproducible Census line graphs and time-series comparisons."
---

# Line Graph

**Also known as:** line chart, line plot, line diagram. A **spaghetti plot** is a special case containing many overlapping lines; it is not a synonym for every line graph.

## Applying this guidance

Apply the [Census Bureau Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), revised September 29, 2026, within their stated scope. The chart-selection advice and implementation checks on this page explain practical design choices; they do not create additional agency mandates. Treat **Essential** items as the core design conditions for this chart, and confirm formal applicability through the program's review process.

Coordinate this page with [Titles and Subtitles](title.html), [Legends](legend.html), [Sources](source.html), and [Visualizing Uncertainty](uncertainty.html). Keep detailed component guidance in those shared pages rather than duplicating it here.

## 1. Purpose and Overview

A line graph connects ordered observations to show change, continuity, or patterns across a meaningful sequence—most often time. It is useful for identifying upward or downward trends, turning points, gaps, and differences between a small number of comparable series. Connecting points implies meaningful order and suggests values between the displayed observations; do not use it for unrelated categories.

Line graphs emphasize the **direction and rate of change**, but precise magnitudes, units, and uncertainty still matter. A line represents observations or estimates—not proof that a trend is statistically significant.

## 2. When to Use

Use a line graph when observations have a meaningful order, a comparable measure is available at successive periods, and changes across periods are central to the analytical question.

### Essential

- Label the time/reference axis, outcome measure, units, geographic universe, and data source.
- Make each series identifiable through direct labels or a legend supported by noncolor cues; do not rely on hover alone.
- Plot periods at their actual positions when spacing is irregular. Explain substantive breaks in collection, definitions, or methodology.
- Represent missing or unavailable observations with a visible gap or documented discontinuity; never silently connect missing periods.
- Keep series legible and explain limitations affecting interpretation, including survey uncertainty where applicable.

### Avoid

- Connecting unordered categories or incompatible measures as though they form a continuous trend.
- Treating the number of lines as a universal accessibility threshold. Reduce clutter based on legibility and user tasks, not solely on a six-series rule.
- Presenting an interactive highlight as the sole means of identifying a series; keyboard and noninteractive alternatives are essential.
- Describing a visual increase/decrease as statistically meaningful without an appropriate test.

## 3. When to Use an Alternative

Consider another chart if the main question is a single-period comparison, exact values, part-to-whole composition, or dozens of crowded series. If observations occur only at disconnected or unordered categories, a dot or bar chart may communicate them more faithfully. When changes between periods are not directly comparable, avoid joining estimates into a misleading trend.

**Recommended:** Use a simple line graph for a few comparable time series; consider small multiples when the series crowd each other.

**Not recommended:** A dense, color-dependent spaghetti plot for a static public report without readable labels or a usable alternative.

## 4. Choosing Between Alternatives

| Analytical goal | Alternative visualization | Why it may be preferable |
|---|---|---|
| Compare many separate time series | Small multiples | Repeated panels reduce overlap; scales must be consistently described |
| Compare values at one period | Dot plot or bar chart | Emphasizes magnitudes without implying a temporal path |
| Show part-to-whole composition over time | Stacked area chart | Shows composition when categories form a valid exclusive partition; not appropriate for overlapping categories |
| Check exact values or assistive-technology access | Accessible data table | Supports precise lookup and interpretation of missing values |
| Show one estimate with uncertainty for each time point | Line with error bars or a documented interval band | Communicates precision, provided the intervals are calculated and labeled appropriately |

## 5. Data Requirements and Statistical Considerations

Record **Census program, table and variable IDs, vintage, geography, universe, units, price year (when relevant), reference period, retrieval date, and data quality flags**. Validate that each observation is unique for its geography/period/measure and that periods sort chronologically.

- **Comparability:** Compare like-for-like estimates. Verify revisions to definitions, survey methodology, geography, sampling frames, and reference periods. Do not imply a continuous ACS 1-year series across **2020**, when the standard ACS 1-year release was not available.
- **Money measures:** Median household income is reported in each ACS release's inflation-adjusted dollars. A nominal line across releases is **not** an inflation-adjusted trend without a documented common-dollar conversion.
- **Uncertainty:** Retain paired ACS margins of error when interpreting differences. Do not determine statistical significance solely from whether intervals overlap; use applicable source-specific testing guidance.
- **Missing/flagged values:** Check API special values and suppressed estimates before numeric conversion. Never replace missing data with zero or interpolate without a prominent methodological disclosure.
- **Multiple series:** Verify identical measures, denominators, and units before comparing or placing series on one axis. Avoid dual axes when they create misleading apparent correspondence.

## 6. Visualization-Specific Considerations and Accessibility

- Use a chronological x-axis with honest spacing. Put a visible gap at omitted observations rather than bridging across them.
- Choose a y-axis range that reveals meaningful variation **without exaggerating** small differences. A zero baseline is not universally required for lines; disclose meaningful truncation where interpretation could change.
- Prefer end-of-line direct labels for a small number of series and a clear legend for larger sets. Use distinguishable dash patterns, markers, or labels as redundant noncolor cues.
- Avoid crowding. For many comparable series, offer filtering/highlighting **with keyboard operation**, or a static small-multiples alternative.
- Use gridlines sparingly and specify axis units. Do not annotate every point if labels obscure the data.
- Supply concise alt text describing the main observed pattern and meaningful gaps, plus a **semantic HTML data table** with period, estimate, geography/series, and uncertainty as applicable. Review reading order, accessible names, contrast, resize, and keyboard interaction in the **rendered GitHub Pages page**.

See relevant repository guidance for axes, color, typography, sources, **Visualizing Uncertainty**, and **Small Multiples**; verify links before publication.

### Legends and reference lines

For a single plainly identified series, omit a redundant legend. For several series, use direct labels or a legend that clearly maps each line to its meaning. Use horizontal reference lines only when they help readers compare values or interpret a meaningful threshold; keep them visually subordinate to the data.

### Design comparison

Use these comparisons to connect each design choice with its effect on interpretation.

| Problematic approach | Why it matters | Preferred approach |
|---|---|---|
| Omitted years are squeezed out of the horizontal axis | The apparent rate of change is distorted | Use actual year coordinates and leave a visible break for missing observations |
| Income estimates from different release years are joined without a common price basis | Inflation and income change are mixed | Convert estimates and MOEs to a documented common dollar year before comparison |
| Series can be identified only by color or hover | Some readers cannot follow the lines | Combine direct labels, distinguishable line styles or markers, and a matching table |

### Checking the published example

Test the chart at its intended display size and with enlarged text. Follow the reading sequence from title to explanation, figure, table, and source. Check that labels and meaningful marks remain distinguishable without color and that any controls can be operated by keyboard with visible focus. Read the explanation and table with a screen reader to confirm that they convey the same measures, units, missing-data conditions, and important relationships as the chart.

Use [automated and manual accessibility testing](https://www.section508.gov/test/testing-overview/) together. A downloadable CSV supplies values but does not replace the chart's explanatory narrative; see [USWDS visualization guidance](https://designsystem.digital.gov/components/data-visualizations/). Record the page/version, tool or assistive technology, result, and corrective action. Apply the sponsor's agreed accessibility baseline rather than treating a palette simulation as a conformance test.

## 7. Census Data Examples

- **Analytical question:** How did published annual ACS median household income estimates change across selected states during comparable release years?
- **Dataset and table:** ACS 1-Year Detailed Tables, **B19013** (median household income), estimate `B19013_001E`, margin of error `B19013_001M`.
- **Official source:** [ACS API documentation](https://api.census.gov/data.html); confirm the chosen release/variable definitions before execution.
- **Geographic level:** User-selected states with supported ACS 1-year coverage.
- **Reference period:** 2021–2024 annual ACS 1-year releases; validate comparability for the selected measure and geography.
- **Measure and units:** Median household income, **2024 dollars**, adjusted using Census-recommended R-CPI-U-RS factors for adjacent ACS releases. Document and verify the factor values and source links using [Census comparison guidance](https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data/2024.html).
- **Reason for selection:** An ordered annual series permits direct demonstration of labeling, uncertainty, gap handling, and temporal comparability.
- **Limitations:** ACS annual income reference periods can overlap; published margins of error do not alone establish significance of cross-year changes.

**Additional Census examples:**

1. **Poverty rate and people in poverty, 1959–2022** (`assets/LineGraph1.png`): separate units and an explained gap.

   ![Poverty rate and population in poverty over time. Original Census graphic; source information and data interpretation appear in the preceding description.](assets/LineGraph1.png)
2. **Children in poverty by Supplemental Poverty Measure components** (`assets/LineGraph2.png`): four labeled lines and supporting definitions.

   ![Children in poverty by Supplemental Poverty Measure component. Original Census graphic; source information and data interpretation appear in the preceding description.](assets/LineGraph2.png)
3. **Median monthly rent, 2017/2019/2021** (`assets/LineGraph3.png`): error bars with definitions and labels.

   ![Median monthly rent with interval indicators. Original Census graphic; source information and data interpretation appear in the preceding description.](assets/LineGraph3.png)
4. **Men's leave after the birth of a first child** (`assets/LineGraph4.png`): legend and useful gridlines.

   ![Types of leave after the birth of a first child. Original Census graphic; source information and data interpretation appear in the preceding description.](assets/LineGraph4.png)

These images illustrate useful design choices. Ensure image paths, descriptive alternative text, and attribution are correct when deploying the page.

## 8. Developer Implementation

The following contract defines the intended behavior of the linked examples. Confirm the files, commands, dependencies, and generated results against the repository before publication.

### 8.1 Data Preparation

**Inputs:** ACS 1-Year B19013 state estimates and published MOEs for 2021–2024, with release year, geography, source price year, and documented inflation-conversion factors.

Validate one record per state/year. Convert B19013_001E and valid B19013_001M to 2024 dollars with the same positive factor for each release year. Record the factor source, price-year direction, and formula. Do not label the series as 2024 dollars until the conversion is verified. Preserve missing observations and annotation codes.

### 8.2 Python

[Python notebook](examples/python/line_graph.ipynb) or [script](examples/python/line_graph.py); dependencies: `requests`, `pandas`, and `matplotlib`. Retain `LINEGRAPH_STATES`, `LINEGRAPH_YEARS`, and `LINEGRAPH_OUTPUT_DIR` as the documented configuration contract.

### 8.3 R

[R script](examples/R/line_graph.R); dependencies: `jsonlite` and `ggplot2`. Use the same configuration and factor table. Compare analytical values with Python rather than requiring pixel-identical images.

### 8.4 Reproducibility and Adaptation

A personal Census API key is required for data queries under the [current Census API guidance](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html). Read `CENSUS_API_KEY` from the analyst's environment. Do not include keys in source control, saved notebooks, request logs, error messages, or execution manifests; redact the `key` query parameter wherever a request URL is recorded. No shared developer credential or private file path should be required.

For each run, save the validated data, chart PNG/SVG, a semantic HTML table, descriptive-text draft, and a nonsecret manifest in the selected output folder. Include source table/variables, full reference period, geography, units, transformations, exclusions, dependency versions, and retrieval time. Pin or record versions actually tested. For identical inputs, R and Python should reproduce the same analytical values within an explicitly documented tolerance; visual styling need not be pixel-identical.

When changing years or geographies, recheck product coverage, definitions, annotations, and comparability. A successful run does not establish statistical significance or accessibility conformance.

### 8.5 Output Verification

| Check | Expected evidence |
|---|---|
| Price conversion | For each year, adjusted estimate = source estimate × factor and adjusted MOE = source MOE × the same factor; rounding occurs only for display |
| Time and gaps | Year coordinates preserve elapsed time, and missing estimates break the plotted path |
| Agreement | Both languages use the same source release, factor precision, units, and stated numerical tolerance; no significance claim is inferred from appearance |

**Source-statement pattern for this example:** U.S. Census Bureau, American Community Survey, 2021–2024 ACS 1-Year Estimates, Detailed Table B19013, selected states. Estimates and MOEs converted to 2024 dollars using the documented R-CPI-U-RS factors. Add the specific source or reproducible request link and actual retrieval date; omit the API key. Identify derived calculations separately from published estimates.

## 9. Common Errors and Misinterpretations

| Issue | Why it matters | Recommended correction |
|---|---|---|
| Connect unrelated categories | Creates a fictional trajectory | Use dots/bars or a genuinely ordered variable |
| Bridge missing periods without disclosure | Suggests unobserved continuity | Preserve a visible gap and note its cause |
| Ignore unequal time intervals | Distorts the apparent rate of change | Use actual chronological x coordinates |
| Compare ACS income releases in different price-year dollars | Creates a misleading trend | Convert to common-dollar units using documented factors |
| Suppress MOE or overclaim significance | Overstates differences | Document uncertainty and apply approved comparison methods |
| Differentiate lines only with color or hover | Excludes some readers | Use direct labels, patterns, keyboard support and a table |
| Clutter the plot with too many lines | Obscures comparison | Highlight/facet/filter without losing accessible alternatives |
| Treat source special codes as numeric values | Introduces fabricated points | Validate codes and display missing appropriately |

## 10. Publication Quality Checklist

- [ ] The analysis requires ordered comparisons, and alternative chart choices were evaluated.
- [ ] Source program, tables, variables, years, geography, universe, units and retrieval metadata are recorded.
- [ ] The chronological axis is correct; missing years and methodological breaks are explicitly handled.
- [ ] Inflation adjustment and uncertainty decisions are documented where applicable.
- [ ] The chart remains interpretable without color or mouse hover; alt text and semantic table are provided.
- [ ] Rendering is tested for contrast, reading order, screen reader/keyboard interaction as applicable, and zoom/reflow on the published page.
- [ ] Python and R execute independently in a clean environment and reproduce validated results (retain execution evidence).
- [ ] Original Census illustrations and links have verified permissions, paths, captions and alt text.
- [ ] All links, file paths, images, and commands work from a fresh public repository clone.

## Related Pages and References

- [Visualizing Uncertainty](uncertainty.html) — interpretation of estimates and margins of error.
- [Small Multiples](smallmultiples.html) — alternate arrangement when series overlap; verify repository permalink.
- [ACS statistical testing guidance](https://www.census.gov/programs-surveys/acs/guidance/statistical-testing-tool.html) — verify relevant methodology for selected estimates and periods.
- [Census Data API](https://api.census.gov/data.html) — API catalog and metadata.

### Standards and Review References

Adapted in part from the *U.S. Data Design Standards* archive, `_visualizations/line-graph.md`. The source archive is an earlier site implementation; its layout, front matter, and examples require reconciliation with the current Census repository.

Use the [September 29, 2026 consolidated Census Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), especially E1-6 (replication documentation), E2-2.3 (visualization requirements), and E3-2.4 (visualization review). Retain review findings and corrections separately from the design checklist.

- [Census API query requirements](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html).
- [Section 508 testing methods](https://www.section508.gov/test/testing-overview/).
- [USWDS data visualization guidance](https://designsystem.digital.gov/components/data-visualizations/).
