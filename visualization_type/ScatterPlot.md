---
layout: default
title: Scatter Plot
permalink: scatterplot.html
tags: [Correlation, Distribution]
description: "Guidance for accessible, statistically responsible scatter plots with reproducible ACS examples."
---

# Scatter Plot

Also known as: scatterplot, scatter graph, scatter chart, scattergram, or scatter diagram. See also: [Bubble Chart]({{ '/bubblechart.html' | relative_url }}).

## Applying this guidance

Apply the [Census Bureau Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), revised September 29, 2026, within their stated scope. The chart-selection advice and implementation checks on this page explain practical design choices; they do not create additional agency mandates. Treat **Essential** items as the core design conditions for this chart, and confirm formal applicability through the program's review process.

Coordinate this page with [Titles and Subtitles]({{ '/title.html' | relative_url }}), [Legends]({{ '/legend.html' | relative_url }}), [Sources]({{ '/source.html' | relative_url }}), and [Visualizing Uncertainty]({{ '/uncertainty.html' | relative_url }}). Keep detailed component guidance in those shared pages rather than duplicating it here.

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

## 7. Original Examples and Additional ACS Demonstration

### 7.1 Original examples and their teaching purpose

The following examples are retained from the Census guidance. Their datasets, periods, universes and design lessons remain distinct. Some illustrate limitations or less-preferred choices; inclusion does not certify every design or its accessibility.

***Example 1:*** Percent Labor Force Covered by Public Pensions vs Percent of Former Wages Replaced by Pensions in Select Asian Countries.

![Public-pension coverage versus wage replacement for selected Asian countries, with labeled observations.]({{ '/visualization_type/assets/ScatterPlot1.png' | relative_url }})

In Example 1 we notice the following consistencies with our standards:
* The variables and units of analysis are explained in the title of the graph.
* Labels are being used for specific observations and the labels do not overlap point markers.
* Circles are being used as point markers, which are proportional in height and width.
* There is not an excessive number of observations.

***Example 2:*** Median Estimated Earnings by Sex and Occupation

![Occupation earnings dashboard with an equal-marker scatter plot and monetary axes.]({{ '/visualization_type/assets/ScatterPlot2.png' | relative_url }})

This plot is a good example of the following:
* The units of analysis on this dashboard scatter plot are clearly identified as dollars using the dollar signs in front of the axis labels.
* The symbol used for each data point is a circle.

***Example 3:*** Uninsured Rate in 2013 and Change from 2013 to 2014 for Occupations

![Uninsured rate in 2013 versus its change to 2014 by occupation, with annotations, leader lines and a significance key.]({{ '/visualization_type/assets/ScatterPlot3.png' | relative_url }})

This plot is a good example of the following:
*	The data is represented using circles that are shaded in two different colors.  
*	The colors are defined in a legend on the graph.
*	Units of analysis are clearly defined in the axis labels. 
*	All labels do not interfere with the data points on the graph using leader lines to connect the label to each data point being identified.

### 7.2 Additional ACS demonstration

**2024 ACS income and poverty by state.** B19013 and B17001: use the same x/y definitions as the bubble example with equal marker areas.

**What this adds:** Demonstrates how a two-variable display differs from the three-variable bubble display without changing x/y meaning.

**Run evidence:** The supplied November 10, 2026 run generated this example. Saved-data arithmetic and chart layout were reviewed for this package; published-page accessibility testing remains outstanding.

![Four equal-sized labeled points compare state median household income with the percentage below poverty threshold in 2024. Virginia has the highest income and lowest poverty point estimate among the four selected states. Equal marker areas carry no population encoding.]({{ '/assets/examples/scatter_plot/scatter_plot.png' | relative_url }})

**Source and interpretation:** U.S. Census Bureau, 2024 ACS 1-Year Estimates, Detailed Tables B19013 and B17001. Poverty percentage = 100 × below-poverty count / poverty-status universe; income is in 2024 dollars. The supplied run completed November 10, 2026 (UTC).

The companion bubble chart has the same x/y values; this chart uses equal marker areas. Published income and poverty-count MOEs are retained in the data table, but no derived percentage MOE is calculated. A pattern across four selected states does not establish causation or a statistically significant relationship.

**Selected values** (rounded for display; CSV retains exported precision):

| State | Income estimate ($) | Below poverty (%) |
|---|---|---|
| Florida | 77,735 | 12.05 |
| Georgia | 79,991 | 12.59 |
| Texas | 79,721 | 13.41 |
| Virginia | 92,090 | 9.75 |

[Read the data tables]({{ '/assets/examples/scatter_plot/reviewed_data_table.html' | relative_url }}) · [Download scatter_plot_data.csv]({{ '/assets/examples/scatter_plot/scatter_plot_data.csv' | relative_url }})

Implementation: [Python source]({{ '/ACS_Examples_Builder/examples/python/01_bubble_scatter/scatter_plot.py' | relative_url }}). The original illustrations above and the ACS output have separate asset paths and source statements.

### 7.3 How the examples work together

Use the original illustrations to discuss design choices and their source-specific limitations. Use the ACS addition to demonstrate a documented data-to-chart workflow. Do not combine values across examples, imply that they use one dataset, or relabel a historical image as a new ACS output.

## 8. Developer Implementation

The following contract defines the intended behavior of the linked examples. Confirm the files, commands, dependencies, and generated results against the repository before publication.

### 8.1 Data Preparation

**Inputs:** 2024 ACS 1-Year B19013 and B17001 records joined by state identifier, with income estimate/MOE, poverty count/MOE, poverty-status universe, and annotations.

Require one x–y pair per included state. Derive poverty percentage as 100 × B17001_002E / B17001_001E only for a valid positive universe. Check the count is between zero and its universe, join cardinality is one-to-one, and both measures use the same release and geography. Document excluded states and retain published MOEs.

### 8.2 Python

Use the [supplied Python implementation]({{ '/ACS_Examples_Builder/examples/python/01_bubble_scatter/scatter_plot.py' | relative_url }}) and the [ACS example runner]({{ '/ACS_Examples_Builder/build_acs_examples.py' | relative_url }}). The runner maps this page to job `scatter_plot`. Its dependencies are listed in [requirements.txt]({{ '/ACS_Examples_Builder/requirements.txt' | relative_url }}). Confirm supported input options in the implementation and its accompanying README.

The [executed notebook]({{ '/review/evidence/RUN_ALL_ACS_EXAMPLES_v03_executed.ipynb' | relative_url }}) contains saved outputs from the supplied ACS run. The [run status CSV]({{ '/review/evidence/ACS_Actual_Results/execution_status.csv' | relative_url }}) records generated results. The notebook produces the ACS additions; it does not recreate the historical Census illustrations.

### 8.3 R

The analytical definitions and output checks on this page also specify the requirements for an R counterpart. A verified R implementation is not bundled in this combined package. Retain R execution and Python/R agreement as outstanding validation tasks; do not describe them as completed.

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

**Related pages:** [Bubble Chart]({{ '/bubblechart.html' | relative_url }}), [Line Graph]({{ '/linegraph.html' | relative_url }}), and [Visualizing Uncertainty]({{ '/uncertainty.html' | relative_url }}).

### Standards and Review References

The original Census page and its example assets are preserved in this package; see the review record for the exact baseline and changes.

Use the [September 29, 2026 consolidated Census Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), especially E1-6 (replication documentation), E2-2.3 (visualization requirements), and E3-2.4 (visualization review). Retain review findings and corrections separately from the design checklist.

- [Census API query requirements](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html).
- [Section 508 testing methods](https://www.section508.gov/test/testing-overview/).
- [USWDS data visualization guidance](https://designsystem.digital.gov/components/data-visualizations/).
