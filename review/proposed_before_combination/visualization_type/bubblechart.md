---
layout: default
title: Bubble Chart
permalink: bubblechart.html
tags: [Distribution, Correlation]
description: "Guidance for accurate and accessible bubble charts using reproducible Census data examples."
---

# Bubble Chart

Also known as: **bubble graph**, **bubble plot**. Related: [Scatter Plot](scatterplot.html), proportional-symbol maps.

## Applying this guidance

Apply the [Census Bureau Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), revised September 29, 2026, within their stated scope. The chart-selection advice and implementation checks on this page explain practical design choices; they do not create additional agency mandates. Treat **Essential** items as the core design conditions for this chart, and confirm formal applicability through the program's review process.

Coordinate this page with [Titles and Subtitles](title.html), [Legends](legend.html), [Sources](source.html), and [Visualizing Uncertainty](uncertainty.html). Keep detailed component guidance in those shared pages rather than duplicating it here.

## 1. Purpose and Overview

A bubble chart extends a scatter plot by representing a **third quantitative variable using circle area**. Two numerical measures determine each bubble's x- and y-position, while a nonnegative magnitude determines its size. Each mark should represent a clearly defined observation such as a state or occupation. A pattern in a bubble chart is not, by itself, evidence of causation or statistical significance.

## 2. When to Use

### Essential
- Identify all **three variables**, their units, the observation unit, geography, and time period.
- Make **circle area**, not radius or diameter, proportional to the size variable, with a labeled size key.
- Make small bubbles visible; consider plotting smaller marks above larger ones and using partial transparency.
- Identify important observations with text or an accessible accompanying table. If additional categories use color, also provide noncolor distinctions and a category key.

### Avoid
- Do not imply a causal relationship from the displayed association.
- Do not use bubble size for signed quantities without an explicit, defensible size transformation.
- Avoid an unlabeled or inconsistently scaled size variable, excessive overlap, or charts requiring hover to determine basic values.

## 3. When to Use an Alternative

### Recommended
- Use a **scatter plot** if only x and y measures matter or size is difficult to read.
- Use separate panels or **small multiples** when overlap conceals observations or subgroups need independent comparisons.
- Use a ranked table or bar chart for precise comparisons, and an accessible table for exact three-variable values.

### Not Recommended
- Avoid bubble charts when observations are too numerous, bubbles obscure each other, or the third measure is not analytically relevant.

## 4. Choosing Between Alternatives

| Communication goal | Preferred chart | Reason |
|---|---|---|
| Two quantitative measures | Scatter plot | Two-axis encoding is easier to read precisely |
| Three quantitative measures | Bubble chart | Adds area as a third encoding, with reduced precision |
| Compare many groups with heavy overlap | Faceted scatter plots or small multiples | Reduces occlusion and preserves comparisons |
| Exact values or ranked categories | Accessible table or bar chart | Area is not well suited to precise numerical judgments |

## 5. Data Requirements and Statistical Considerations

- **Consistent observation unit:** Each bubble represents one state, county, occupation, or other explicitly defined unit. Do not mix levels without a methodological justification.
- **Measure compatibility:** Verify the release year, geography, population universe, inflation basis, and denominators. Do not treat a poverty-status universe as identical to total population.
- **Size encoding:** The visual *area* of the circle must be proportional to the underlying nonnegative numeric size variable. Provide a quantitative size legend.
- **Missing and suppressed values:** Filter or flag Census sentinel codes and failed queries; never treat them as zeros.
- **Uncertainty:** ACS published margins of error apply to specific estimates. A derived rate requires its own appropriate uncertainty calculation; do not assign the numerator's MOE to the derived rate. See [Visualizing Uncertainty](uncertainty.html).
- **Interpretation:** Cross-sectional differences are descriptive; do not infer individual behavior from state-level relationships (ecological fallacy).

## 6. Visualization-Specific Considerations and Accessibility

- Combine dark bubble outlines, sufficiently contrasting fills, and text labels; do not rely solely on color, bubble area, or tooltips.
- Limit overlap, use transparent fills carefully, and check labels for clipping at ordinary zoom and at increased text size.
- Provide concise image alternative text that explains the encodings and central purpose; accompany the figure with a **properly headed HTML data table** for precise values and margins of error.
- If interactive, ensure all data and controls work by keyboard and expose usable names, values, and focus indicators to assistive technology.
- Check the rendered page for contrast, logical reading order, zoom/reflow, and screen-reader usability. Generated files alone do **not** certify Section 508 compliance.

### Categories and marker geometry

Use circles with equal width and height and a quantitative area key. If color or shape distinguishes categories, provide a category legend unless direct labels identify every category clearly. Keep selected point labels readable and plot smaller marks above larger ones where possible. The chart has three quantitative encodings: horizontal position, vertical position, and area. Category encodings should remain secondary and should not be confused with additional numerical axes.

### Design comparison

Use these comparisons to connect each design choice with its effect on interpretation.

| Problematic approach | Why it matters | Preferred approach |
|---|---|---|
| Circle radius is proportional to population | Circle area grows with the square of the intended quantity | Make area proportional: radius = k × square root of the nonnegative size value |
| A size key shows only small/medium/large | Readers cannot recover the quantitative meaning | Label reference circles with values in the same units and scaling as the plotted bubbles |
| Large bubbles hide small bubbles and their labels | Some observations disappear visually | Use drawing order, restrained sizes, clear edges, and an exact-value table; switch to facets if needed |

### Checking the published example

Test the chart at its intended display size and with enlarged text. Follow the reading sequence from title to explanation, figure, table, and source. Check that labels and meaningful marks remain distinguishable without color and that any controls can be operated by keyboard with visible focus. Read the explanation and table with a screen reader to confirm that they convey the same measures, units, missing-data conditions, and important relationships as the chart.

Use [automated and manual accessibility testing](https://www.section508.gov/test/testing-overview/) together. A downloadable CSV supplies values but does not replace the chart's explanatory narrative; see [USWDS visualization guidance](https://designsystem.digital.gov/components/data-visualizations/). Record the page/version, tool or assistive technology, result, and corrective action. Apply the sponsor's agreed accessibility baseline rather than treating a palette simulation as a conformance test.

## 7. Census Data Examples

**Selected U.S. states, 2024 ACS 1-Year Detailed Tables**:

| Visual encoding | ACS variable | Meaning |
|---|---|---|
| X | `B19013_001E` | Median household income (2024 inflation-adjusted dollars) |
| Y | `100 × B17001_002E / B17001_001E` | People below the poverty threshold as a percentage of the population for whom poverty status is determined |
| Bubble **area** | `B01003_001E` | Total population (not the poverty-status universe) |
| Supporting uncertainty | `B19013_001M`, `B17001_002M` | Published 90% MOEs for income and the poverty-count estimate respectively; **not** an MOE for the derived percentage |

The worked example uses the public API dataset `https://api.census.gov/data/2024/acs/acs1` for a bubble chart and accompanying exact-value table. The example demonstrates three-variable encoding, not a causal or statistically significant association. A methodology appropriate to the derived rate would be required for significance testing.

### Example 1 — Geographic mobility and commuting-zone income (published illustration)

![Bubble chart showing commuting-zone income and mobility for young adults from low-income families. Several observations overlap; transparency and selective labels help distinguish the displayed groups.](assets/bubblechart1.png)

**What it teaches:** Each mark represents an observation in a three-variable comparison. Transparency and selected labels improve interpretation, but overlapping bubbles can still conceal individual observations. Readers should consult the original figure for its exact definitions, units, population universe, and source notes; these have not been independently revalidated here.

**Design decision:** Keep an accessible exact-value data alternative and consider a scatter plot or faceted presentation if overlap makes the third quantity hard to interpret.

### Example 2 — Median earnings and educational attainment by occupation (published Census illustration)

![Occupation bubble chart relating median earnings and percentage with a bachelor's degree or higher; circle size represents a third quantity identified by the original figure's size key.](assets/bubblechart2.png)

**What it teaches:** Axis units and a numerical size key make three-variable encoding interpretable. Selective occupation labels can aid orientation, but labels, size keys, and bubbles must not overlap or be clipped.

Source: [Teachers Are Among Most Educated, Yet Their Pay Lags](https://www.census.gov/library/visualizations/interactive/teachers-pay.html).

### Example 3 — Reproducible ACS state-level bubble chart

**2024 ACS 1-Year:** x = median household income; y = poverty percentage among people whose poverty status is determined; **circle area** = total state population. The chart does not claim causation or statistical significance. Total population is not the same as the poverty-status universe.

<!-- Verified-output image target: ![State-level scatter plot of 2024 median household income and poverty percentage, with circle areas proportional to total population. The exact state values are provided in a separate table.](assets/examples/bubble_chart.png) -->

Expected output assets: `assets/examples/bubble_chart_table.html` and `assets/examples/bubble_chart_data.csv`. Publish verified values together with the chart; implementation links are listed below.

**How to read it:** Compare each state's horizontal income position and vertical poverty percentage first. Then use the labeled bubble-area key to interpret population size. All three variables are descriptive state-level quantities; exact values and published MOEs belong in the accessible table.

## 8. Developer Implementation

The following contract defines the intended behavior of the linked examples. Confirm the files, commands, dependencies, and generated results against the repository before publication.

### 8.1 Data Preparation

**Inputs:** Matched 2024 ACS 1-Year state records for B19013 (income), B17001 (poverty universe/count), and B01003 (total population), with applicable published MOEs and annotations.

Validate a one-to-one state join across all three tables. Derive poverty percentage from B17001_002E/B17001_001E, and use B01003_001E only for bubble area. Require finite valid coordinates and nonnegative size values. Explicitly handle zero-size observations so their absence is not mistaken for missing data.

### 8.2 Python

[Python script](examples/python/bubble_chart.py) or [notebook](examples/notebooks/bubble_chart_colab.ipynb); dependencies: `requests`, `pandas`, and `matplotlib`. The draft command is `python examples/python/bubble_chart.py --states Florida,Georgia,Texas,Virginia --out ./bubble_outputs`.

### 8.3 R

[R script](examples/R/bubble_chart.R); dependencies: `httr`, `jsonlite`, and `ggplot2`. Use `BUBBLE_STATES` and `BUBBLE_OUTPUT_DIR` as documented in the [run guide](examples/bubble_chart_README.md).

### 8.4 Reproducibility and Adaptation

A personal Census API key is required for data queries under the [current Census API guidance](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html). Read `CENSUS_API_KEY` from the analyst's environment. Do not include keys in source control, saved notebooks, request logs, error messages, or execution manifests; redact the `key` query parameter wherever a request URL is recorded. No shared developer credential or private file path should be required.

For each run, save the validated data, chart PNG/SVG, a semantic HTML table, descriptive-text draft, and a nonsecret manifest in the selected output folder. Include source table/variables, full reference period, geography, units, transformations, exclusions, dependency versions, and retrieval time. Pin or record versions actually tested. For identical inputs, R and Python should reproduce the same analytical values within an explicitly documented tolerance; visual styling need not be pixel-identical.

When changing years or geographies, recheck product coverage, definitions, annotations, and comparability. A successful run does not establish statistical significance or accessibility conformance.

### 8.5 Output Verification

| Check | Expected evidence |
|---|---|
| Area scaling | For positive sizes, area ratios equal quantity ratios. A fourfold quantity has fourfold area and twice the radius; the size key uses the same mapping |
| Cross-chart agreement | For the same state selection, bubble x–y coordinates match the related scatter plot; only the third-variable area encoding differs |
| Coverage and access | Included and excluded state counts reconcile; overlapping observations remain recoverable in the table, and no size or color is the sole source of an exact value |

**Source-statement pattern for this example:** U.S. Census Bureau, American Community Survey, 2024 ACS 1-Year Estimates, Detailed Tables B19013, B17001, and B01003, selected states. Poverty percentage is derived; bubble area represents total population. Add the specific source or reproducible request link and actual retrieval date; omit the API key. Identify derived calculations separately from published estimates.

## 9. Common Errors and Misinterpretations

| Error | Correction |
|---|---|
| Scaling bubble **radius** linearly with population | Scale **area** linearly with population |
| Treating state-level association as causation | Describe association only; avoid ecological inference |
| Reporting numerator MOE as poverty-rate MOE | Preserve the published MOE and calculate the rate's uncertainty using an appropriate method if needed |
| Interpreting total population as poverty-universe count | Label these denominators separately |
| Depending exclusively on hover or color | Include labels and an accessible underlying data table |
| Enlarging bubbles until smaller ones disappear | Reduce size, use transparency, adjust ordering, or choose small multiples |

## 10. Publication Quality Checklist

- [ ] All three variables, units, year, geography, and observation units are documented.
- [ ] Bubble **area** proportionality and the quantitative size legend are verified.
- [ ] Denominators, invalid values, and MOEs have been checked against Census metadata.
- [ ] The static chart is understandable without hover or reliance on color alone.
- [ ] Alternative text and the exact-value HTML table are reviewed in context.
- [ ] Contrast, labels, keyboard behavior (where applicable), reflow, and screen-reader output are manually tested.
- [ ] A new analyst can execute the code with their own credentials and output directory.

## Related Pages and References

- [Scatter Plot](scatterplot.html) · [Small Multiples](smallmultiples.html) · [Visualizing Uncertainty](uncertainty.html)
- [ACS 2024 B19013 variable metadata](https://api.census.gov/data/2024/acs/acs1/groups/B19013.html)
- [ACS 2024 B17001 variable metadata](https://api.census.gov/data/2024/acs/acs1/groups/B17001.html)
- [ACS 2024 B01003 variable metadata](https://api.census.gov/data/2024/acs/acs1/groups/B01003.html)

### Standards and Review References

Adapted in part from the *U.S. Data Design Standards* archive, `_visualizations/bubble-chart.md`. The source archive is an earlier site implementation; its layout, front matter, and examples require reconciliation with the current Census repository.

Use the [September 29, 2026 consolidated Census Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), especially E1-6 (replication documentation), E2-2.3 (visualization requirements), and E3-2.4 (visualization review). Retain review findings and corrections separately from the design checklist.

- [Census API query requirements](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html).
- [Section 508 testing methods](https://www.section508.gov/test/testing-overview/).
- [USWDS data visualization guidance](https://designsystem.digital.gov/components/data-visualizations/).
