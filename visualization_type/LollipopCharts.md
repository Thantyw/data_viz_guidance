---
layout: default
title: Lollipop Charts
permalink: lollipopcharts.html
tags: [Comparison]
description: "Use lollipop charts to compare values across categories, particularly when displaying many categories or large values."
---

# Lollipop Charts

**Also known as:** Lollipop Graph, Dot Plot

## Purpose and Overview

A lollipop chart is a chart type with a categorical axis and a length or height that corresponds to the value of each data point. Each value is represented by a marker connected to a baseline by a line or stem.

Lollipop charts can be useful alternatives to bar charts when many categories have large values or when comparing more than ten categories. The reduced visual weight of the stems can make differences among many values easier to assess.

One drawback of a lollipop chart is that the size of the dot used to mark each value can interfere with interpretation. Dot size should therefore be chosen carefully so that it does not obscure the position of the value or imply an additional quantitative measure.

## When to Use

Use a lollipop chart when the primary analytical objective is to compare values across discrete categories while reducing the visual weight associated with traditional bars.

Lollipop charts can be particularly useful when:

- Many categorical values need to be compared.
- Categories have relatively large values.
- A bar chart would appear visually dense.
- The analytical objective is to emphasize differences among values while retaining a connection to a common baseline.

### Essential

- Lollipop charts must always start at zero. The heights or lengths of the lollipops are proportional to the values they represent. For this reason, lollipop charts that do not start at zero can mislead the viewer's assessment of differences between values.
- Facilitate the most important analytical comparison by placing relevant comparison categories next to each other or in meaningful groupings.
- If categories that would normally be displayed have been removed, include a statement describing the omission or exclusion.
- Never omit the space between lollipops.
- Use labels that read from left to right. If category labels are too long along the x-axis, use horizontal lollipops along the y-axis to improve label readability.

### Avoid

- Avoid dot sizes that obscure the position of the represented value or make differences difficult to interpret.
- Avoid unnecessary colors that do not communicate meaningful information or emphasis.
- Avoid category ordering that makes important comparisons unnecessarily difficult.
- Avoid inconsistent scales when multiple lollipop charts are intended to be compared.

## When to Use an Alternative

Consider a **bar chart** when the number of categories is manageable and traditional bars provide a clearer or more familiar comparison.

Consider a **dot plot** when the position of values along a common scale is sufficient and stems connecting values to zero are unnecessary.

Consider a **table** when readers need exact numerical values rather than primarily visual comparisons.

Consider another visualization when the number of categories, labels, or overlapping values makes individual lollipops difficult to interpret.

## Additional Recommendations

### Recommended

- Use visual components purposefully to promote readability, ease of interpretation, transparency, and reduction of redundancy.
- Balance the use of axis labels, data labels, tick marks, color, legends, emphasis, and spacing.
- Ensure category labels clearly define the categories represented.
- Sort categories in an analytically meaningful way that supports the main purpose of the chart.
- If there is no natural analytical ordering, such as an ordinal variable, consider sorting categories by value in descending order.
- Use consistent scales when creating small multiple charts.
- Use additional color only when it highlights or supports the key analytical purpose of the chart.
- Use a consistent dot size unless dot size intentionally represents an additional variable and that encoding is clearly explained.

### Not Recommended

- Do not use decorative colors or visual effects that do not communicate additional information.
- Do not use excessively large markers that interfere with interpretation of the represented values.
- Do not use inconsistent category ordering across comparable lollipop charts.

## Choosing Between Alternatives

| Analytical Goal | Alternative Visualization | Why It May Be Preferable |
|---|---|---|
| Compare a manageable number of categorical values | Bar Chart | Provides a familiar representation using bar length along a common baseline. |
| Compare many categorical values with less visual weight | Lollipop Chart | Uses stems and markers instead of filled bars, reducing visual density. |
| Compare category values without emphasizing a zero baseline | Dot Plot | Uses position along a common scale without stems connecting values to zero. |
| Present exact numerical values | Table | Allows readers to retrieve and compare precise values directly. |

## Data Requirements and Statistical Considerations

> **TODO (Phase 2):** Complete during individual enhancement work using applicable Census Bureau data and statistical guidance.

Future development of this section should address category definitions, measurement units, geographic level and reference period, aggregation and denominators, missing or suppressed values, margins of error and uncertainty where applicable, and comparability across groups, geographies, or time periods.

## Visualization-Specific Considerations

A lollipop chart combines a line or stem with a marker positioned at the represented value. Because the length or height of the lollipop communicates magnitude relative to a baseline, lollipop charts should begin at zero.

Marker size requires particular attention. A marker that is too large can obscure its precise position and interfere with comparisons. Unless marker size intentionally represents another variable, markers should use a consistent size.

Category ordering also affects interpretation. Use a natural or ordinal sequence when one exists. Otherwise, ordering categories by value can help readers identify rankings and differences.

Relevant component guidance should also be consulted for axes, color, grids, legends, sources, titles, and typography.

## Accessibility

- **Alt text:** Describe the primary comparison or takeaway rather than simply identifying the visualization as a "lollipop chart."
- **Data table alternative:** Provide the underlying category values in an accessible table or downloadable format when appropriate.
- **Do not rely on color alone:** Use labels, annotations, symbols, or other cues when color distinguishes categories or highlights values.
- Ensure markers, stems, labels, and axes remain sufficiently visible and distinguishable.
- Use direct labels when they improve interpretation and reduce dependence on a legend.
- See [508 Compliance](508.html), [Color](color.html), and [Typography](typography.html) for general accessibility and presentation guidance.

## Census Data Example

> **TODO (Phase 2):** Document and validate the existing Census Bureau example below with its dataset and table identifier, geography, reference period, measure, units, and applicable statistical limitations.

The existing example is retained in this Phase 1 revision. Additional Census data documentation can be added during Phase 2 after the underlying source has been validated.

## Developer Implementation

> **TODO (Phase 2):** Add reproducible implementation guidance and code examples.

Future implementation guidance may include data preparation and reproducible Python and R examples, with documentation explaining how developers can adapt the example to other Census datasets or geographic levels.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Nonzero baseline | Can exaggerate apparent differences because lollipop length represents value. | Start lollipop charts at zero. |
| Excessively large markers | Can obscure the precise position of values and interfere with comparison. | Use a consistent marker size appropriate to the display. |
| Poor category ordering | Makes important comparisons unnecessarily difficult. | Use a natural, ordinal, or analytically meaningful order. |
| Missing space between lollipops | Makes discrete categories more difficult to distinguish. | Maintain visible spacing between categories. |
| Excessive categories or labels | Can create visual clutter and make individual values difficult to interpret. | Reduce categories or consider another visualization when necessary. |
| Inconsistent scales | Can create misleading comparisons across multiple charts. | Use consistent scales when lollipop charts are intended to be compared. |
| Unnecessary color | Adds visual noise without improving interpretation. | Use color selectively to communicate meaning or emphasis. |

## Publication Quality Checklist

- [ ] A lollipop chart is appropriate for the analytical question.
- [ ] Lollipops begin at zero.
- [ ] Categories are ordered in an analytically meaningful way.
- [ ] Category labels clearly identify the values represented.
- [ ] Marker sizes do not interfere with interpretation.
- [ ] Marker sizes are consistent unless size intentionally encodes another variable.
- [ ] Adequate space separates individual lollipops.
- [ ] Long category labels are presented in a readable orientation.
- [ ] Comparable charts use consistent scales.
- [ ] Omitted categories are documented.
- [ ] Color is used purposefully and is not the only means of communicating information.
- [ ] Missing or suppressed values are documented where applicable.
- [ ] Relevant accessibility guidance has been followed.
- [ ] Data source, geography, reference period, and units are documented where applicable.
- [ ] Relevant limitations and statistical uncertainty are addressed where applicable.

## Examples

### Example: Percentage of People in Poverty by Different Poverty Measures, 2021

![Lollipop chart showing the percentage of people in poverty using different poverty measures in 2021](assets/LollipopChart1.png)

This existing Census Bureau example is retained for Phase 1. Additional documentation about the underlying Census dataset, table identifier, geography, measures, and statistical considerations can be added during Phase 2 after the source has been validated.

## Related Pages

- [Bar Chart](barchart.html): use when a traditional bar representation provides a clearer categorical comparison.
- [Dot Plot Chart](dotplotchart.html): use when values can be compared through position without stems connecting them to zero.
- [Tables](table.html): use when exact numerical values are the primary requirement.
- [Axes](axes.html): guidance for axis labels, scales, and tick marks.
- [Comparing Data and Values](comparison.html): guidance for designing accurate comparisons.
- [Typography](typography.html): guidance for readable labels and text.
- [508 Compliance](508.html): general accessibility requirements.
- [Color](color.html): guidance for appropriate and accessible use of color.
