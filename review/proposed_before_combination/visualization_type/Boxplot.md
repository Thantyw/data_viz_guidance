---
layout: default
title: Boxplot
permalink: boxplot.html
tags: [Distribution, Comparison]
description: "Guidance for accessible boxplots that compare distributions, including reproducible ACS county-income examples."
---

# Boxplot

Also known as: **box-and-whisker plot**.

## Applying this guidance

Apply the [Census Bureau Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), revised September 29, 2026, within their stated scope. The chart-selection advice and implementation checks on this page explain practical design choices; they do not create additional agency mandates. Treat **Essential** items as the core design conditions for this chart, and confirm formal applicability through the program's review process.

Coordinate this page with [Titles and Subtitles](title.html), [Legends](legend.html), [Sources](source.html), and [Visualizing Uncertainty](uncertainty.html). Keep detailed component guidance in those shared pages rather than duplicating it here.

## 1. Purpose and Overview
A boxplot summarizes a numeric distribution using the first quartile (Q1), median, third quartile (Q3), whiskers, and optionally outlying observations. It supports comparisons of center, spread, skewness, and potential outliers **among groups**. It does not show the full distribution or a density estimate.

## 2. When to Use
### Essential
- Identify the **unit of observation** (for example, counties, *not* households).
- Define Q1, median, Q3, whiskers, and treatment of points beyond the whiskers in the chart note.
- Provide group counts and units, including whether plotted statistics are survey estimates.
- Use common numeric scales when comparing grouped boxplots.

### Avoid
- Do not silently omit outliers, or imply that whisker endpoints always represent minima and maxima.
- Do not describe the distribution of **county median household-income estimates** as the distribution of income across households.
- Do not interpret differences between survey-based boxplots as statistically significant without an appropriate uncertainty method.

## 3. When to Use an Alternative
### Recommended
- Use a histogram or density plot when the full shape or multiple modes matter.
- Use a dot plot for very small groups or when individual observations must be visible.

### Not Recommended
- Avoid boxplots for groups with too few valid observations to interpret quartiles reliably.
- Avoid boxplots when a simple comparison of individual point estimates is the actual analytical question.

## 4. Choosing Between Alternatives
| Question | Preferred display | Reason |
|---|---|---|
| Compare group medians and spreads | Boxplot | Compact summary across groups |
| Identify distribution peaks | Histogram or density plot | Boxplots conceal modes |
| See each observation | Dot/strip plot | Preserves individual values |
| Compare changing values over time | Line graph | Reveals time ordering |

## 5. Data Requirements and Statistical Considerations
- Inputs: one valid quantitative value per observation and one grouping variable.
- Standard demonstration: **2020–2024 ACS 5-Year Detailed Table B19013**, county-level `B19013_001E` median household income and published 90% MOE `B19013_001M`; dollar values are in 2024 inflation-adjusted dollars.
- All valid counties count equally in this **distribution of county estimates**; it is neither household-weighted nor a distribution of individual incomes.
- Exclude invalid or missing estimates explicitly and report the number excluded; preserve corresponding MOEs in the downloadable data table. MOEs of individual county estimates are **not** confidence intervals for calculated boxplot quartiles.
- Quartile conventions can differ between tools. The reproducible example specifies linear-interpolation quartiles (NumPy percentile/R quantile type 7) and the **1.5 × IQR** whisker rule: whiskers end at the most extreme observed values within Q1 − 1.5×IQR and Q3 + 1.5×IQR. Observations beyond them appear as separate points.
- A boxplot's points beyond the whiskers are flags, not evidence of erroneous data; do not remove them automatically.

## 6. Visualization-Specific Considerations and Accessibility
- Label each group and axis; explain outlier points and the whisker rule immediately below the figure.
- Use a shared income axis; do not encode group differences using color alone. Preserve labels in grayscale.
- Provide meaningful alternative text describing groups and structure, plus a keyboard-accessible HTML data table with the county values and summary statistics.
- Review text contrast, resizing at 200%, and screen-reader interpretation of the published page. Generated assets **do not automatically establish Section 508 compliance**.

### Choosing a whisker convention

A minimum-to-maximum boxplot and a 1.5 × IQR boxplot are different valid summaries. Name the convention for every example. The box spans Q1 to Q3 and the median is drawn at its actual value; the median need not be geometrically centered inside the box. Draw whiskers along the value axis in either a horizontal or vertical layout. For the original minimum-to-maximum convention, label the extremes; for the reproducible IQR convention, distinguish whiskers from separately plotted outliers.

Compare groups with equivalent measures, universes, units, and reference periods. A bar chart can compare a few named values, but it does not replace a boxplot's distribution summary merely because the numerical differences are large.

### Design comparison

Use these comparisons to connect each design choice with its effect on interpretation.

| Problematic approach | Why it matters | Preferred approach |
|---|---|---|
| Whiskers are unlabeled or described as a confidence interval | Readers cannot distinguish range, IQR-based limits, and sampling uncertainty | Name the quartile method and whisker rule in the figure note |
| Extreme county estimates are automatically deleted | The distribution is altered without a substantive reason | Display outlying points; investigate them and document any justified exclusions |
| Median of county medians is called state median household income | A summary across counties is confused with the source's household-level state statistic | Label the county-level summary explicitly; retrieve the state statistic separately if needed |

### Checking the published example

Test the chart at its intended display size and with enlarged text. Follow the reading sequence from title to explanation, figure, table, and source. Check that labels and meaningful marks remain distinguishable without color and that any controls can be operated by keyboard with visible focus. Read the explanation and table with a screen reader to confirm that they convey the same measures, units, missing-data conditions, and important relationships as the chart.

Use [automated and manual accessibility testing](https://www.section508.gov/test/testing-overview/) together. A downloadable CSV supplies values but does not replace the chart's explanatory narrative; see [USWDS visualization guidance](https://designsystem.digital.gov/components/data-visualizations/). Record the page/version, tool or assistive technology, result, and corrective action. Apply the sponsor's agreed accessibility baseline rather than treating a palette simulation as a conformance test.

## 7. Census Data Examples
**Example 1 — Original Census boxplot:** *Range of Median Household Income at the County Level by Region: 2012*. **Reading lesson:** the whiskers represent minimum and maximum in the original, so do not interpret any values as 1.5 × IQR outliers. The county values are county **median estimates**, not household income observations. This illustrates that the whisker rule must be printed beside every boxplot.

![Original Census county median-income boxplot; whisker definitions must be read in the figure note.](assets/Boxandwhisker1.png)

**Example 2 — Reproducible ACS boxplot:** *Distribution of county median household-income estimates across selected states, 2020–2024 ACS 5-Year*. **Reading lesson:** the whiskers extend to the most extreme observations within 1.5 × IQR of each quartile; outlying county estimates appear as separate points. County estimates carry sampling uncertainty, which the data table reports separately.

<!-- Add the actual file from executing the Python/R script, after verifying its output. -->
<!-- Verified-output image target: ![County median household-income boxplots for selected states. One observation per county; center lines show medians; whiskers use the 1.5-times-IQR rule; isolated circles mark county outliers.](assets/examples/boxplot_acs.png) -->

The example visualizes county-level **estimates**, not household observations. The accompanying table should give exact estimates, published county-level MOEs, and summary statistics; its intended path is `assets/examples/boxplot_data_table.html`. Before publication, copy the **actual generated** chart and table into the relative paths shown above; do not use simulated output.

## 8. Developer Implementation

The following contract defines the intended behavior of the linked examples. Confirm the files, commands, dependencies, and generated results against the repository before publication.

### 8.1 Data Preparation

**Inputs:** 2020–2024 ACS 5-Year B19013 county median household-income estimates and published county MOEs, grouped by state, with geographic identifiers and annotations.

Give each valid county equal weight. Retain source MOEs separately from the computed distribution summaries. Use type-7 linear-interpolation quartiles in both languages and 1.5 × IQR whiskers ending at observed values inside the fences. Include valid and excluded county counts for each state.

### 8.2 Python

[Python script](examples/python/boxplot.py) or [notebook](examples/notebooks/boxplot_colab.ipynb), with documented `--states`, `--year`, and `--output-dir` options.

### 8.3 R

[R script](examples/R/boxplot.R), configured through `BOXPLOT_STATES`, `BOXPLOT_YEAR`, and `BOXPLOT_OUTPUT_DIR`. Compute type-7 summaries explicitly if the plotting function uses different hinges; pass the agreed summaries to the renderer.

### 8.4 Reproducibility and Adaptation

A personal Census API key is required for data queries under the [current Census API guidance](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html). Read `CENSUS_API_KEY` from the analyst's environment. Do not include keys in source control, saved notebooks, request logs, error messages, or execution manifests; redact the `key` query parameter wherever a request URL is recorded. No shared developer credential or private file path should be required.

For each run, save the validated data, chart PNG/SVG, a semantic HTML table, descriptive-text draft, and a nonsecret manifest in the selected output folder. Include source table/variables, full reference period, geography, units, transformations, exclusions, dependency versions, and retrieval time. Pin or record versions actually tested. For identical inputs, R and Python should reproduce the same analytical values within an explicitly documented tolerance; visual styling need not be pixel-identical.

When changing years or geographies, recheck product coverage, definitions, annotations, and comparability. A successful run does not establish statistical significance or accessibility conformance.

### 8.5 Output Verification

| Check | Expected evidence |
|---|---|
| Summary ordering | Lower whisker ≤ Q1 ≤ median ≤ Q3 ≤ upper whisker for each nonempty group |
| Whiskers and points | Whiskers are actual included values within the IQR fences, not the fences themselves; every point beyond the fences is accounted for |
| Language agreement | Q1, median, Q3, whiskers, and outlier membership match across Python/R within the stated precision; county MOEs are not quartile confidence intervals |

**Source-statement pattern for this example:** U.S. Census Bureau, American Community Survey, 2020–2024 ACS 5-Year Estimates, Detailed Table B19013. Boxplots summarize equally weighted county median household-income estimates in 2024 dollars; they do not show household income distributions. Add the specific source or reproducible request link and actual retrieval date; omit the API key. Identify derived calculations separately from published estimates.

## 9. Common Errors and Misinterpretations
| Error | Better practice |
|---|---|
| Calling every extreme point an error | Explain the outlier rule; investigate context before exclusion |
| Assuming whiskers are minimum/maximum | State the exact convention |
| Interpreting county income medians as household income data | Identify the county as the observation unit |
| Ignoring ACS sampling error | Retain county MOEs; do not treat a boxplot as an uncertainty interval |
| Changing scales across panels | Use a consistent axis for comparison |

## 10. Publication Quality Checklist
- [ ] Source, year, geographic universe, units, and observation level appear on the page.
- [ ] Quartile/whisker/outlier conventions are stated and match the code.
- [ ] Valid and excluded county counts are recorded; county MOEs remain available.
- [ ] The actual generated ACS image and HTML data table are included and match the source CSV.
- [ ] Code runs with an analyst's credentials, parameters, and output directory.
- [ ] Keyboard, text alternative, grayscale/noncolor, contrast, and screen-reader checks are documented.

## Related Pages and References
Related: [Histogram](histogram.html), [Scatter Plot](scatterplot.html), [Visualizing Uncertainty](uncertainty.html).

Sources: [Census Bureau ACS 5-Year dataset](https://www.census.gov/data/developers/data-sets/acs-5year.html); [ACS B19013 API variable](https://api.census.gov/data/2024/acs/acs5/variables/B19013_001E.html).

### Standards and Review References

Adapted in part from the *U.S. Data Design Standards* archive, `_visualizations/box-and-whisker.md`. The source archive is an earlier site implementation; its layout, front matter, and examples require reconciliation with the current Census repository.

Use the [September 29, 2026 consolidated Census Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), especially E1-6 (replication documentation), E2-2.3 (visualization requirements), and E3-2.4 (visualization review). Retain review findings and corrections separately from the design checklist.

- [Census API query requirements](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html).
- [Section 508 testing methods](https://www.section508.gov/test/testing-overview/).
- [USWDS data visualization guidance](https://designsystem.digital.gov/components/data-visualizations/).
