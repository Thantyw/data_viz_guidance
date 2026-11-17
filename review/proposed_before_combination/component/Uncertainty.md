---
layout: default
title: Visualizing Uncertainty
permalink: uncertainty.html
description: "Displaying uncertainty in Census estimates with definitions, examples, and reproducible code."
---

# Visualizing Uncertainty

## Applying this guidance

Use the [consolidated Census Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), revised September 29, 2026, within their stated scope. Separate formal requirements from the practical design recommendations and implementation choices described here. Coordinate this guidance with [Titles and Subtitles](title.html), [Legends](legend.html), and [Sources](source.html).

## 1. Purpose and Overview

Uncertainty communicates how precisely a reported value is known. Census estimates may be affected by sampling error, nonsampling error, or modeling assumptions. When uncertainty could change how readers interpret a difference, ranking, or trend, explain it alongside the estimate.

| Measure | Meaning | Interpretation caution |
|---|---|---|
| Standard error (SE) | Estimated sampling variability of a statistic across repeated samples | Not a direct measure of all possible errors |
| Margin of error (MOE) | Published interval half-width at a specified confidence level | Always identify the confidence level |
| Confidence interval (CI) | Interval constructed by a stated statistical procedure | Do not call it the range containing a fixed percentage of observed people |
| Standard deviation (SD) | Spread of observed values around their mean | Describes data variability, not automatically the SE of an estimate |
| Survey coefficient of variation (CV) | SE divided by a positive estimate, often multiplied by 100 | Measures relative sampling error; undefined at zero and unstable near zero |
| Descriptive coefficient of variation | SD divided by the mean, under suitable conditions | Describes relative spread of observations; not the same quantity as survey CV |

The ACS publishes MOEs at the **90% confidence level**. For survey CV interpretation, see [Understanding Error and Determining Statistical Significance](https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch07.pdf). Other Census programs may use different methods; use the source's own documentation.

## 2. When to Use

Apply uncertainty guidance whenever an estimate's precision could influence comparisons, rankings, change over time, or decisions.

### Essential

- Use trustworthy data and retain each estimate's corresponding uncertainty measure, source, year, and geography.
- Identify whether marks represent MOE, SE, confidence intervals, or another quantity; state the confidence level where relevant.
- Communicate applicable sampling, nonsampling, or model limitations; an ACS MOE does not summarize every source of error.
- Explain uncertainty in language suitable for the intended audience, including a meaningful text alternative.
- If significant differences are annotated, use a consistent convention for **all comparisons being tested**, and document the test.

### Avoid

- Treating a visible difference or nonoverlapping-looking points as proof of statistical significance.
- Hiding uncertainty when it may materially affect interpretation, or using color alone to distinguish significance.

### Additional Recommendations

**Recommended:** Show intervals for rankings whose order could change within the uncertainty; provide exact values in an accessible data table and clarify highly uncertain estimates.

**Not Recommended:** Highly technical uncertainty encodings without explanation for the intended audience.

## 3. When to Use an Alternative

Use **dot-and-whisker intervals** when comparing several estimates; consider **confidence bands** for a valid fitted or time-series estimate with properly calculated uncertainty. Use **text and a table** when a graphical interval would become cluttered. If you need the distribution of individual observations, use a histogram or boxplot, but do not mistake observed-data spread for uncertainty about an estimate.

## 4. Choosing Between Alternatives

| Reader's task | Representation | Key caution |
|---|---|---|
| Compare estimates and precision | Point with labeled interval | Do not infer significance solely from interval overlap |
| Review a trend and uncertainty | Line with documented confidence band | Explain temporal comparability and band calculation |
| Check exact values or use assistive technology | Structured table and explanatory text | Define estimate, MOE, CI and units in headers/caption |
| Identify supported differences | Symbols and direct annotations | Base labels on a valid documented test; do not rely on color |
| Understand the distribution of observations | Histogram, boxplot, or density plot | Describes a different concept from a confidence interval |

**Existing Census illustrations:** [U.S. Exporting Firms by Demographics in 2021](https://www.census.gov/library/visualizations/2024/econ/exports-2021.html) (intervals); [Population Without Health Insurance Coverage by State: 2019 and 2021](https://www.census.gov/library/visualizations/interactive/population-without-health-insurance-coverage-2019-and-2021.html) (differences); [Married Couple Place of Birth and Current State of Residence: 1900–2018](https://www.census.gov/library/visualizations/interactive/married-couple-place-of-birth-and-current-state-of-residence-1900-2018.html) (uncertainty as text). Confirm linked content and accessibility. Additional illustrative approaches include confidence bands, distribution-based displays, and outcome plots; these require carefully labeled statistical interpretations.

## 5. Data Requirements and Statistical Considerations

For each chart, document program, survey product, vintage, table and variables, population universe, geography, units, reference period, missing/suppressed flags, and source retrieval details. Check that an estimate and its MOE correspond to the **same record and quantity**.

For the example below, use **2024 ACS 1-Year Detailed Table B19013**, `B19013_001E` (median household income) and `B19013_001M` (paired MOE), for selected states. Income units are **2024 inflation-adjusted dollars**. The interval `estimate ± MOE` is used as an illustrative 90% interval for valid published pairs. Inspect special values before calculation; never turn suppressed values into zero.

For differences between estimates, use applicable [ACS statistical testing guidance](https://www.census.gov/programs-surveys/acs/guidance/statistical-testing-tool.html). Confidence-interval overlap alone does not establish whether a difference is significant. For comparisons across years, check changes in variable definition, geography and price-year units; the standard 2020 ACS 1-year product was not released.

## 6. Visualization-Specific Considerations

Keep point estimates and interval endpoints on a common readable scale. Identify the interval level in the caption, preserve numerical units, and use consistent ordering. Prefer labels and marker shapes in addition to color. When intervals crowd the chart, consider a simpler layout plus a table.

### Accessibility

- Provide outcome-focused **alt text** that describes the observed pattern **and any uncertainty necessary to interpret it**; finalize it only after running the example.
- Publish a structured HTML table with row/column headers for estimate, MOE, lower/upper bounds, and units. A CSV is a useful supplement, not the sole accessible alternative.
- Check text and non-text contrast, label readability, reading order and resize/reflow. For interactive content also check keyboard operation and focus.
- Evaluate the **rendered GitHub Pages HTML**, including manual assistive-technology testing where applicable. An automated scan does not establish Section 508 conformance.

See the [508 Compliance](508.html) and [Color](color.html) pages.

### Design comparison

| Problematic approach | Why it matters | Preferred approach |
|---|---|---|
| Error bars labeled only as “error” | SD, SE, MOE and CI communicate different quantities | Name the measure, confidence level, units and calculation/source |
| Significance inferred by eye from overlapping intervals | The comparison may depend on covariance and a separate test | Apply the appropriate comparison method; state tested/not tested explicitly |
| Empirical spread described as uncertainty of an estimate | Variation among observations is confused with estimation precision | Identify the distribution's unit and statistical meaning |
| Estimates omitted solely because they do not differ significantly | A display decision is confused with an inferential conclusion | Report justified estimates with uncertainty; do not describe an unsupported difference as meaningful |

**Annotation consistency:** distinguish statistically significant, not statistically significant, and not tested. If testing several comparisons, identify the comparison family, applicable multiple-comparison treatment, and confidence level; apply the annotation convention consistently. A reliability threshold should be source- and use-specific rather than an invented universal CV cutoff.

## 7. Census Data Examples

**Question:** How do 90% ACS margins of error affect comparisons of median household income among selected states in 2024?

- **Source:** [2024 ACS 1-Year Detailed Tables API](https://api.census.gov/data/2024/acs/acs1.html), B19013; geographic level: state.
- **Variables:** `NAME`, `state`, `B19013_001E`, `B19013_001M`.
- **Expected visual:** labeled dot-and-whisker chart, plus accessible numerical table.
- **Interpretation:** describe the observed comparisons only after verifying downloaded values; do not claim significant differences without an appropriate test.
- **Reproducibility note:** Run the example against the documented data source before publishing output images; do not substitute invented estimates.

### Original example strategies and their limitations

The original guidance illustrates several different ways to communicate uncertainty. Preserve their distinct teaching purposes rather than treating a table, interval, significance marker, and distribution plot as interchangeable.

| Strategy | Original examples | What it helps communicate | Limitation to explain |
|---|---|---|---|
| Intervals and bands | [Exporting firms, 2021](https://www.census.gov/library/visualizations/2024/econ/exports-2021.html); [Population 65 years and older, 2016](https://www.census.gov/library/visualizations/interactive/population-65-years.html) | Point estimate and its stated precision | Identify the uncertainty quantity and confidence level; interval overlap is not a general significance test |
| Explicit significance annotations | [Uninsured population, 2019 and 2021](https://www.census.gov/library/visualizations/interactive/population-without-health-insurance-coverage-2019-and-2021.html); [Coupled households, 2017–2021](https://www.census.gov/library/visualizations/interactive/coupled-households-by-county-2017-2021.html) | Whether a specified tested difference meets the stated criterion | Does not by itself show interval width or justify other untested comparisons |
| Uncertainty as text | [Married couples, 1900–2018](https://www.census.gov/library/visualizations/interactive/married-couple-place-of-birth-and-current-state-of-residence-1900-2018.html) | Exact MOEs, SEs or bounds in notes, tables or accessible details | Essential uncertainty must not be available only by mouse hover or hidden in distant notes |
| Distribution-based displays | The original references [Error Bars Considered Harmful](https://vis.csail.mit.edu/classes/6.859/readings/pdfs/Corell-ErrorBarsConsideredHarmful.pdf) | Distribution shape when its statistical meaning is explicitly defined | A distribution of observed people/counties is different from a sampling, bootstrap or posterior distribution of an estimate |
| Hypothetical outcome plots | Additional method suggested by the original guidance | Variation across modeled or simulated outcomes | Requires a justified model, clear labeling, and an accessible nonanimated explanation |

<!-- Original illustration references retained for integration: assets/Uncertainty1.png and assets/Uncertainty2.png (intervals/bands), assets/Uncertainty3.png and assets/Uncertainty4.png (significance), assets/Uncertainty5.png (text), assets/Uncertainty6.png (distribution methods). Supply and inspect the actual assets before activating image links. -->

**High uncertainty:** if an estimate's interval crosses several classification boundaries or would materially change a rank, explain that instability and reconsider a categorical ranking or map. Do not convert an uncertain estimate into a falsely precise class. When uncertainty cannot be encoded directly, provide an explicit reliability note and the applicable linked uncertainty information.

## 8. Developer Implementation

### 8.1 Data Preparation

For the ACS demonstration, retrieve state-level `B19013_001E` and `B19013_001M` from the same 2024 ACS 1-Year record. Validate geographic identifiers, reference period, units, annotations and estimate/MOE pairing. Preserve invalid and suppressed records as documented exclusions rather than zeros. Calculate raw lower/upper bounds as estimate minus/plus the valid published MOE. Apply source guidance on logical limits when relevant, retain the raw calculation, and disclose any bound adjustment. Negative monetary values are not automatically invalid for every Census measure.

ACS published MOEs use a 90% confidence level; the corresponding normal-approximation factor is 1.645. Derive an SE as `MOE / 1.645` only for a compatible published 90% MOE. See [ACS variance methodology, Chapter 12](https://www2.census.gov/programs-surveys/acs/methodology/design_and_methodology/2024/acs_design_methodology_ch12_2024.pdf). Derived percentages, differences, or aggregates require their own appropriate uncertainty method; do not reuse or simply add source MOEs.

### 8.2 Python

The existing draft references [the Python implementation](examples/python/uncertainty.py). Verify its actual input modes and execution guide before publishing claims that API, CSV, Excel, or DataFrame inputs are supported. An implementation should validate the data contract above and generate a dot-and-whisker chart, exact-value table, descriptive-text draft, and nonsecret manifest in the analyst's selected folder.

### 8.3 R

The existing draft references [the R implementation](examples/R/uncertainty.R). Verify it independently using the same source records, interval definitions, handling of special values, and display order. Cross-language agreement concerns analytical values and stated tolerances; figures need not be pixel-identical.

### 8.4 Reproducibility and Adaptation

A personal Census API key is required for data queries under the [current API guidance](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html). Read `CENSUS_API_KEY` from the analyst's environment. Redact the key from logged URLs, errors, saved notebooks, and manifests; do not commit it. Save source variables, the full reference period, geography, transformations, exclusions, retrieval time, and tested dependency versions with the outputs.

Record the estimate, MOE, confidence level, raw bounds and any adjusted display bounds. Do not report a significance result unless the method was actually implemented and reviewed. Test the rendered figure, narrative and semantic table together; a generated table or automated scan alone does not establish accessibility conformance.

### 8.5 Output Verification

| Check | Expected evidence |
|---|---|
| Pairing | One valid estimate/MOE pair for each included geography, measure and reference period |
| Arithmetic | Raw lower = estimate − MOE; raw upper = estimate + MOE; source-defined MOE is nonnegative and special codes are excluded explicitly |
| Bounds | Any logical-bound adjustment follows the source method and is separately recorded; the underlying estimate is not changed |
| Labels | The chart and table identify 90% MOEs/intervals, units, source, geography and comparison limitations |
| Testing | Annotation records distinguish significant, not significant and not tested; no overlap-only test is used |

## 9. Common Errors and Misinterpretations

| Error | Consequence | Correction |
|---|---|---|
| Uncertainty measure or level unlabeled | False confidence in precision | State MOE/SE/CI and confidence level |
| Estimate paired with a different geography/year MOE | Invalid interval | Join/validate by the full record keys |
| Data-source special code treated as a number | Fabricated results | Detect and document flagged values |
| Interval overlap used as a significance test | Unsupported claim | Apply approved comparison method |
| SD or observed-value distribution treated as CI | Confuses distinct concepts | Identify what varies and how it was estimated |
| Significance shown only by color | Inaccessible interpretation | Use direct annotation and text |

## 10. Publication Quality Checklist

- [ ] Dataset, table, year, geography, units, variables and source provenance are recorded.
- [ ] Missing values, estimation assumptions, MOE pairing and comparisons are statistically reviewed.
- [ ] The published Python example executes independently and matches the source; cross-language checks should be performed when an R implementation is available.
- [ ] Figure has usable title, units, interval legend/caption and finalized descriptive alt text.
- [ ] Structured HTML data alternative and applicable Section 508 tests are documented.
- [ ] Existing links, component references and deployment paths are verified.

## Related Pages and References

- [Line Graph](linegraph.html), [Scatter Plot](scatterplot.html), [Small Multiples](smallmultiples.html) — verify relative links after cloning.
- [Census Bureau Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf)
- [ACS Statistical Testing Tool](https://www.census.gov/programs-surveys/acs/guidance/statistical-testing-tool.html)
- [Section508.gov](https://www.section508.gov/) and [WCAG 2.2](https://www.w3.org/TR/WCAG22/)

### Standards and Review References

Use the September 29, 2026 consolidated Census standards, especially E1-6, E2-2.3 and E3-2.4, within their stated scope. Record the implementation review, applicable statistical methods and actual rendered-site accessibility findings separately from this guidance checklist.
