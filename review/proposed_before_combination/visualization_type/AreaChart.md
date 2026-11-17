---
layout: default
title: Area Chart
permalink: areachart.html
tags: [Distribution]
description: "Guidance for accessible, statistically accurate, non-stacked area charts with reproducible Census data examples."
---

# Area Chart

## Applying this guidance

Apply the [Census Bureau Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), revised September 29, 2026, within their stated scope. The chart-selection advice and implementation checks on this page explain practical design choices; they do not create additional agency mandates. Treat **Essential** items as the core design conditions for this chart, and confirm formal applicability through the program's review process.

Coordinate this page with [Titles and Subtitles](title.html), [Legends](legend.html), [Sources](source.html), and [Visualizing Uncertainty](uncertainty.html). Keep detailed component guidance in those shared pages rather than duplicating it here.

## 1. Purpose and Overview

An **area chart** connects observations in their natural order and shades the region between the line and a meaningful baseline, ordinarily zero. Shading emphasizes **quantity or magnitude** as well as change. This page concerns **non-stacked area charts**. For cumulative parts of a whole, consult [Stacked Area Chart](stackedareachart.html) instead.

Do not interpret the filled area as an additional measure beyond the plotted values, or assume that overlapping shaded series should be summed.

## 2. When to Use

### Essential
- Use an ordered x-axis (such as time), a numerical quantity, and a **zero-based y-axis**.
- Label units, geographic coverage, population universe, and the reporting period.
- Make the boundary line legible and distinguish series without relying on color alone.
- Identify data gaps, revisions, and substantive comparability limitations.

### Avoid
- Do not fill under variables whose zero is arbitrary or misleading.
- Do not connect missing observations as though they were measured.
- Do not use overlapping filled regions when occlusion obscures the data.

## 3. When to Use an Alternative

### Recommended
- Use a **line graph** when trends and exact changes are more important than magnitude.
- Use **small multiples** to compare multiple quantities without overlapping fills.
- Use a **bar chart** for unordered categories or a few discrete comparisons.

### Not Recommended
- Avoid an area chart when small differences, rapid fluctuations, or dense overlapping series require precise readings.
- Do not substitute a non-stacked area chart for a stacked area chart when the message requires additive composition.

## 4. Choosing Between Alternatives

| Need | More suitable form | Why |
|---|---|---|
| Emphasize a quantity changing over ordered periods | Non-stacked area chart | Zero-based fill reinforces magnitude |
| Compare trends precisely | Line graph | Avoids area/overlap distortion |
| Compare several states without occlusion | Small-multiple areas or lines | Preserves legibility and common scales |
| Show components summing to a total | Stacked area chart, after verifying exclusivity | Conveys additive composition |
| Compare unrelated categories | Bar chart | Does not imply continuity |

## 5. Data Requirements and Statistical Considerations

- **Baseline and scale:** Start at zero; use the same y-axis scale in comparative panels unless clearly documented otherwise.
- **Ordered observations:** Sort periods chronologically. Retain missing periods as explicit gaps, never as invented values.
- **Comparability:** Review changes to survey questions, universes, geography, estimation methods, and reference periods. ACS annual estimates are not longitudinal observations of identical respondents.
- **Uncertainty:** ACS estimates have margins of error (MOEs). Do not conclude that changes are statistically significant merely because values differ. Consult [Visualizing Uncertainty](uncertainty.html).
- **Totals versus rates:** Larger states may show larger counts without higher *rates*. Explain the denominator, and consider a separate rate chart for comparisons of prevalence.
- **Avoid stacking:** Distinct panels are not additive. Only stack mutually exclusive components that form an appropriate partition.

## 6. Visualization-Specific Considerations and Accessibility

- Render a clear, visible boundary line; fill opacity should not obscure labels or nearby data.
- Use text labels, panel titles, and consistent axes rather than color alone; verify contrast on the actual published page.
- Supply concise alternative text summarizing the purpose and important relationships, plus an accessible table for exact values and MOEs.
- Ensure heading hierarchy, keyboard access (for interactive charts), zoom/reflow, and screen-reader reading order are checked in the rendered site.
- The existence of an SVG, alt-text draft, or HTML table does **not** by itself demonstrate Section 508 compliance.

### Design comparison

Use these comparisons to connect each design choice with its effect on interpretation.

| Problematic approach | Why it matters | Preferred approach |
|---|---|---|
| Fill begins at a truncated vertical baseline | Shaded magnitude is exaggerated | Use a zero baseline; choose a line graph if variation around a nonzero value is the question |
| Several transparent areas overlap | Hidden regions and shared fills can imply a total that does not exist | Use separate panels with common scales; explain that state counts are independent |
| A missing year is removed before plotting | The remaining polygon suggests continuous observed coverage | Retain the missing period and break the line and fill at that position |

### Checking the published example

Test the chart at its intended display size and with enlarged text. Follow the reading sequence from title to explanation, figure, table, and source. Check that labels and meaningful marks remain distinguishable without color and that any controls can be operated by keyboard with visible focus. Read the explanation and table with a screen reader to confirm that they convey the same measures, units, missing-data conditions, and important relationships as the chart.

Use [automated and manual accessibility testing](https://www.section508.gov/test/testing-overview/) together. A downloadable CSV supplies values but does not replace the chart's explanatory narrative; see [USWDS visualization guidance](https://designsystem.digital.gov/components/data-visualizations/). Record the page/version, tool or assistive technology, result, and corrective action. Apply the sponsor's agreed accessibility baseline rather than treating a palette simulation as a conformance test.

## 7. Census Data Examples

**Non-stacked area charts: persons below the poverty threshold, selected states, 2021–2024.** This example uses the **ACS 1-Year Detailed Tables**, table **B17001: Poverty Status in the Past 12 Months by Sex by Age**.

| Field | Meaning |
|---|---|
| `B17001_001E` | Universe for whom poverty status is determined |
| `B17001_002E` | Estimated number of people below the poverty threshold |
| `B17001_002M` | Published 90% margin of error for that estimate |

The API data-query pattern is `https://api.census.gov/data/2024/acs/acs1?get=NAME,B17001_001E,B17001_002E,B17001_002M&for=state:*`. The implementation must append the analyst's API key at runtime and redact it from recorded URLs.

The example specifies **separate, equal-scale zero-based area charts for each selected state**, not a stacked area chart. A shared tabular alternative provides exact estimates and MOEs. The [standard 2020 ACS 1-Year data product was not released](https://www.census.gov/data/developers/data-sets/acs-1year/2020.html); the example intentionally uses 2021–2024. Comparability and year-to-year significance still require assessment before making claims about trends.

## 8. Developer Implementation

The following contract defines the intended behavior of the linked examples. Confirm the files, commands, dependencies, and generated results against the repository before publication.

### 8.1 Data Preparation

**Inputs:** Annual ACS 1-Year B17001 state records for 2021–2024: geography, year, poverty-status universe, poverty-count estimate, published count MOE, and annotations.

Use B17001_001E as the poverty-status universe and B17001_002E as the count below the poverty threshold. Retain B17001_002M as its published 90% count MOE. Check requested state/year coverage, unique records, finite nonnegative counts, and count not exceeding the universe. Report exclusions; preserve missing periods as gaps.

### 8.2 Python

[Python script](examples/python/area_chart.py) or [notebook](examples/python/area_chart_colab.ipynb); dependencies: `requests`, `pandas`, and `matplotlib`. The draft command is `python examples/python/area_chart.py --states Florida,Georgia,Virginia --out ./area_outputs`.

### 8.3 R

[R script](examples/R/area_chart.R). Use the geography, year, and output settings documented in the [run guide](examples/area_chart_README.md).

### 8.4 Reproducibility and Adaptation

A personal Census API key is required for data queries under the [current Census API guidance](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html). Read `CENSUS_API_KEY` from the analyst's environment. Do not include keys in source control, saved notebooks, request logs, error messages, or execution manifests; redact the `key` query parameter wherever a request URL is recorded. No shared developer credential or private file path should be required.

For each run, save the validated data, chart PNG/SVG, a semantic HTML table, descriptive-text draft, and a nonsecret manifest in the selected output folder. Include source table/variables, full reference period, geography, units, transformations, exclusions, dependency versions, and retrieval time. Pin or record versions actually tested. For identical inputs, R and Python should reproduce the same analytical values within an explicitly documented tolerance; visual styling need not be pixel-identical.

When changing years or geographies, recheck product coverage, definitions, annotations, and comparability. A successful run does not establish statistical significance or accessibility conformance.

### 8.5 Output Verification

| Check | Expected evidence |
|---|---|
| Coverage | Every requested state/year has a value or an explicit missing-data record; no straight segment or fill bridges a missing observation |
| Chart and table | Plotted counts equal the exported estimates; each panel has a zero baseline and the same stated count scale |
| Interpretation | Labels identify people below the poverty threshold, not poverty rates; count MOEs are not relabeled as percentage MOEs |

**Source-statement pattern for this example:** U.S. Census Bureau, American Community Survey, 2021–2024 ACS 1-Year Estimates, Detailed Table B17001, selected states. Measure: people below the poverty threshold among the population for whom poverty status is determined. Add the specific source or reproducible request link and actual retrieval date; omit the API key. Identify derived calculations separately from published estimates.

## 9. Common Errors and Misinterpretations

| Error | Correction |
|---|---|
| Displaying an area chart with a truncated vertical axis | Begin at zero or select another chart form |
| Treating multiple non-stacked areas as additive | Explain that panels are independent; stack only legitimate components |
| Using transparent overlapping fills for many series | Use separate panels or lines |
| Comparing state counts as though they were poverty rates | Label counts and provide rates when discussing prevalence |
| Treating an estimate change as statistically significant | Evaluate uncertainty and appropriate significance methods |
| Silently filling missing years | Leave visible gaps and explain why observations are missing |

## 10. Publication Quality Checklist

- [ ] Zero baseline and correct units are visible.
- [ ] Period, source, population universe, and series are clear.
- [ ] Missing values, comparability limitations, and uncertainty are disclosed.
- [ ] Multiple area charts are not mislabeled as stacked or additive.
- [ ] Python and R independently execute with user-configurable settings and output paths.
- [ ] Plotted numbers match the saved source table and MOEs.
- [ ] Alt text and an accessible data table are provided; manual accessibility checks have been performed on the published rendering.

## Related Pages and References

The following illustrations from the original guidance remain as contextual examples, separate from the reproducible ACS demonstration:

<!-- Upstream illustration retained for maintainer review: assets/areaplot1.jpeg, world population by age group, https://www.census.gov/library/stories/2023/11/world-population-estimated-eight-billion.html. Confirm whether it is stacked before displaying on this non-stacked area page or relocating it. -->

**Real median household and family income.**

![Area-chart illustration comparing real median household and family income; read the source for exact values.](assets/areaplot2.png)

Source: [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/series/MEHOINUSA672N). A comparison of these variables should not imply the filled areas are additive.

Related guidance: [Line Graph](linegraph.html), [Small Multiples](smallmultiples.html), [Visualizing Uncertainty](uncertainty.html), and [Stacked Area Chart](stackedareachart.html).

### Standards and Review References

Use the [September 29, 2026 consolidated Census Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), especially E1-6 (replication documentation), E2-2.3 (visualization requirements), and E3-2.4 (visualization review). Retain review findings and corrections separately from the design checklist.

- [Census API query requirements](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html).
- [Section 508 testing methods](https://www.section508.gov/test/testing-overview/).
- [USWDS data visualization guidance](https://designsystem.digital.gov/components/data-visualizations/).
