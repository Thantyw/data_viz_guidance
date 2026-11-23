---
layout: default
title: Stacked Area Chart
permalink: stackedareachart.html
tags: [Distribution]
description: "Guidance for accessible stacked area charts that show how mutually exclusive categories contribute to totals over time."
---

# Stacked Area Chart

## Applying this guidance

Apply the [Census Bureau Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), revised September 29, 2026, within their stated scope. The chart-selection advice and implementation checks on this page explain practical design choices; they do not create additional agency mandates. Treat **Essential** items as the core design conditions for this chart, and confirm formal applicability through the program's review process.

Coordinate this page with [Titles and Subtitles](title.html), [Legends](legend.html), [Sources](source.html), and [Visualizing Uncertainty](uncertainty.html). Keep detailed component guidance in those shared pages rather than duplicating it here.

## 1. Purpose and Overview

A **stacked area chart** shows how several **non-overlapping components** contribute to a total across a naturally ordered variable, usually time. Each series forms a band above the preceding series; the top boundary indicates the overall total. In a **100% stacked area chart**, each period is normalized to 100%, emphasizing composition rather than absolute magnitude.

Stacked areas are **not** the same as overlapping transparent area charts: the height of a stacked band represents its value, while overlapping areas share a baseline and can obscure one another. Do not interpret band boundaries as independent trends when they are cumulative sums.

## 2. When to Use

### Essential

- Use nonnegative, additive component values that represent a **mutually exclusive, collectively exhaustive partition** of the defined total. Document the population universe and units.
- Start the magnitude axis at **zero**. For 100% stacked areas, use the 0%–100% scale and disclose each period's denominator.
- Identify each category with labels or a legend, not color alone. Maintain a consistent layer order across periods.
- Verify that all categories sum to the published total for every period. Never stack overlapping categories as though they were distinct portions of a whole.
- Identify the time range, source, geography, release, and any statistical uncertainty relevant to the interpretation.

### Avoid

- Do not stack rates with incompatible denominators, overlapping category counts, negative quantities, or values that do not have a meaningful zero.
- Do not bridge missing time periods with a continuous area. Do not compare noncomparable time series without an explicit adjustment or qualification.
- Do not imply that every layer's independent trend can be read from its upper edge: only the bottom layer has a common zero baseline.

## 3. When to Use an Alternative

### Recommended

- Use a **line graph** when the main question is the trend in one or several individual series.
- Use **small multiples** when each component's trend must be compared on a common scale.
- Use an **unstacked area chart** to emphasize one series' magnitude; see the Area Chart guidance.
- Use a table when precise comparisons, small differences, or many categories make the stacked display difficult to interpret.

### Not Recommended

- Avoid stacked areas for numerous highly volatile layers or when individual category comparisons dominate the analytical question.
- Do not use 100% stacking when changes in total size are the main finding; normalization hides changes in magnitude.

## 4. Choosing Between Alternatives

| Analytical question | Preferred form | Reason |
|---|---|---|
| How does the total change, and what contributes to it? | Stacked area (counts) | Shows magnitude and composition together |
| How does the mix change independent of total size? | 100% stacked area | Standardizes each period to 100% |
| How does each subgroup change independently? | Line graph or small multiples | Avoids unequal and shifting baselines |
| What is the exact value of each component? | Accessible data table | Supports precise comparisons |

## 5. Data Requirements and Statistical Considerations

Data should contain one ordered period, a clearly defined total, and mutually exclusive components for each period. Validate nonnegative values, unique period–geography records, missing observations, common units, stable category definitions, and `sum(components) = total`. When converting to percentages, use the same total for all components in a period; check that shares sum to 100% subject to rounding.

**ACS considerations:** ACS estimates have sampling uncertainty. Preserve published margins of error, identify the ACS release type, and avoid treating stacked estimates as exact population counts. Margins of error cannot simply be added to produce a total MOE. Standard ACS 1-Year data are not available for 2020; do not silently connect 2019 to 2021. Review year-to-year comparability before interpreting changes. See [Census ACS 2020 guidance](https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data/2020.html).

## 6. Visualization-Specific Considerations and Accessibility

Use a stable, thoughtfully ordered category sequence; for a two-layer chart, keeping the larger or more stable category at the base often makes the shape easier to read. Avoid reordering layers by year. Use distinguishable fills, clear boundaries and direct category labels where possible. Color alone is insufficient; consider textures/hatching and a corresponding legend. A short figure description should report the overall trend and identify layer order. Provide a structured table containing exact values and the source's statistical uncertainty. Verify contrast, readability at 200% zoom, and the accessibility of the published HTML with appropriate tools and assistive technologies; a generated table or alt-text draft is not proof of Section 508 compliance.

### Design comparison

Use these comparisons to connect each design choice with its effect on interpretation.

| Problematic approach | Why it matters | Preferred approach |
|---|---|---|
| Categories overlap or omit part of the named total | The top boundary is not the claimed total | Use a verified partition, add an explicitly defined remainder where justified, or choose separate lines |
| A middle layer is read from its upper boundary | That boundary includes lower layers | Read band thickness; use small multiples when independent component trends are the main question |
| A 100% stack is described as population growth | Normalization conceals total magnitude | Label the percentage denominator and provide totals, or use a count-based stack |

### Checking the published example

Test the chart at its intended display size and with enlarged text. Follow the reading sequence from title to explanation, figure, table, and source. Check that labels and meaningful marks remain distinguishable without color and that any controls can be operated by keyboard with visible focus. Read the explanation and table with a screen reader to confirm that they convey the same measures, units, missing-data conditions, and important relationships as the chart.

Use [automated and manual accessibility testing](https://www.section508.gov/test/testing-overview/) together. A downloadable CSV supplies values but does not replace the chart's explanatory narrative; see [USWDS visualization guidance](https://designsystem.digital.gov/components/data-visualizations/). Record the page/version, tool or assistive technology, result, and corrective action. Apply the sponsor's agreed accessibility baseline rather than treating a palette simulation as a conformance test.

## 7. Census Data Examples

### Existing Census example: Married Couple Place of Birth and Current State of Residence, 1900–2018

![Existing Census stacked area example showing population categories over time; verify the figure, category labels, and its accompanying descriptive text before publication.](assets/StackedAreaChart1.png)

The original example illustrates compositional change over time. Examine the baseline, layer ordering, labels, source, and whether the represented categories truly form a partition before drawing conclusions. [Census interactive publication](https://www.census.gov/library/visualizations/interactive/married-couple-place-of-birth-and-current-state-of-residence-1900-2018.html).

### Reproducible ACS example: Population by sex in selected states, 2021–2024

ACS 1-Year **B01001 (Sex by Age)** provides the total estimate (`B01001_001E`), male estimate (`B01001_002E`), and female estimate (`B01001_026E`). In the table's classification, male and female estimates form an exhaustive, mutually exclusive partition, so their counts should sum to the total. The chart uses **counts**, not independent 100% shares; published 90% MOEs for male and female counts appear in its companion table. These variables follow the Census Bureau's published table metadata.

<!-- Verified-output target: assets/examples/stacked_area_florida.png. Activate the image and matching table only after a real-data run and review. -->

## 8. Developer Implementation

The following contract defines the intended behavior of the linked examples. Confirm the files, commands, dependencies, and generated results against the repository before publication.

### 8.1 Data Preparation

**Inputs:** ACS 1-Year B01001 state records for 2021–2024: total, male and female estimates, published MOEs, year, geography, and annotations.

Validate B01001_002E + B01001_026E = B01001_001E for each valid state/year. These are the source table's published sex categories. Keep layer order stable. Preserve missing periods and published MOEs. Do not add component MOEs to create a total MOE.

### 8.2 Python

[Python script](examples/python/stacked_area.py) or [notebook](examples/notebooks/stacked_area.ipynb). Configure states, supported years, and output location according to the [run guide](stacked_area_README.md).

### 8.3 R

[R script](examples/R/stacked_area.R), using the same states, years, category order, and count/share definitions as Python.

### 8.4 Reproducibility and Adaptation

A personal Census API key is required for data queries under the [current Census API guidance](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html). Read `CENSUS_API_KEY` from the analyst's environment. Do not include keys in source control, saved notebooks, request logs, error messages, or execution manifests; redact the `key` query parameter wherever a request URL is recorded. No shared developer credential or private file path should be required.

For each run, save the validated data, chart PNG/SVG, a semantic HTML table, descriptive-text draft, and a nonsecret manifest in the selected output folder. Include source table/variables, full reference period, geography, units, transformations, exclusions, dependency versions, and retrieval time. Pin or record versions actually tested. For identical inputs, R and Python should reproduce the same analytical values within an explicitly documented tolerance; visual styling need not be pixel-identical.

When changing years or geographies, recheck product coverage, definitions, annotations, and comparability. A successful run does not establish statistical significance or accessibility conformance.

### 8.5 Output Verification

| Check | Expected evidence |
|---|---|
| Count reconciliation | Each period's stack height equals the total; each band thickness equals its exported component estimate |
| Percentage mode | All shares use the same period/geography total and sum to 100% within a documented rounding tolerance |
| Continuity | Layer order is unchanged across periods; missing observations break the full stack rather than becoming zero-filled bands |

**Source-statement pattern for this example:** U.S. Census Bureau, American Community Survey, 2021–2024 ACS 1-Year Estimates, Detailed Table B01001, selected states. Measures: published male and female population estimates and total population. Add the specific source or reproducible request link and actual retrieval date; omit the API key. Identify derived calculations separately from published estimates.

## 9. Common Errors and Misinterpretations

| Mistake | Correction |
|---|---|
| Stacking categories that overlap | Use disjoint categories or separate charts |
| Reading the upper edge of a middle band as that band's value | Interpret its thickness, not its cumulative boundary |
| Failing to show totals or denominator | Label the unit and publish the underlying table |
| Comparing 100% areas as if they show population growth | Use counts when changes in total size matter |
| Connecting data across a missing year | Break the sequence or state the gap explicitly |
| Relying on colors alone | Include labels, boundaries, patterns and a data table |

## 10. Publication Quality Checklist

- [ ] Components are nonnegative, mutually exclusive, exhaustive and reconcile with totals for every year.
- [ ] The zero baseline, category order, units and time period are explicit.
- [ ] Source, ACS release and margin-of-error limitations are identified.
- [ ] Every visible example is a verified, properly attributed image with accurate description.
- [ ] The Python and R examples run in an independent supported environment with analyst-selected credentials and output location.
- [ ] PNG/SVG match the published CSV/HTML table and no simulated values are published as real estimates.
- [ ] Contrast, noncolor distinctions, alt text, table semantics, keyboard use where relevant, and zoom/screen-reader behaviors are tested.

**Related guidance:** [Area Chart](areachart.html), [Line Graph](linegraph.html), [Small Multiples](smallmultiples.html), [Nested or Non-Mutually Exclusive Categories](nested.html), [Visualizing Uncertainty](uncertainty.html).

**Reference:** [Census ACS B01001 variable documentation](https://api.census.gov/data/2024/acs/acs1/groups/B01001.html).

### Standards and Review References

Use the [September 29, 2026 consolidated Census Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), especially E1-6 (replication documentation), E2-2.3 (visualization requirements), and E3-2.4 (visualization review). Retain review findings and corrections separately from the design checklist.

- [Census API query requirements](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html).
- [Section 508 testing methods](https://www.section508.gov/test/testing-overview/).
- [USWDS data visualization guidance](https://designsystem.digital.gov/components/data-visualizations/).
