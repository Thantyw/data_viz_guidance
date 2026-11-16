---
layout: default
title: Bar Chart
permalink: barchart.html
tags: [Comparison]
description: "Use bar charts to compare values across discrete categories using bars whose lengths or heights represent the measured values."
---

# Bar Chart

**Also known as:** bar graph, column chart, vertical bar chart, horizontal bar chart

## Purpose and Overview

A bar chart displays categorical data with rectangular bars whose length or height corresponds to the value of each data point.

Bar charts can use vertical or horizontal bars and are best used to compare values across one or more discrete categories. When comparing more than one category of data, bars can be grouped together to create a grouped bar chart.

Bar charts make differences in magnitude easier to identify because readers compare the lengths of bars along a common scale.

## When to Use

Use a bar chart when the primary analytical goal is to compare values across discrete categories. Bar charts are particularly useful when readers need to identify differences in magnitude, rankings, or patterns across categories.

Horizontal bar charts can be useful when category labels are long because they provide more space for readable labels.

### Essential

- Bars must always start at the zero origin. The heights or lengths of the bars are proportional to the values they represent. For this reason, bar charts that do not start at zero can mislead the viewer's assessment of differences between values.
- Facilitate the most important analytical comparison by placing bars representing relevant quantities next to each other or in logical groupings.
- If categories that would normally be displayed have been removed, include a statement describing the omission or exclusion.
- Use labels that read from left to right. If category labels are too long along the x-axis, use horizontal bars along the y-axis to improve label readability.
- Use the same width for each bar.

### Avoid

- Do not omit the space between categories; otherwise, the bar chart may appear to be a histogram.
- Do not use three-dimensional (3D) graphics because they can distort the image and its interpretation.

## When to Use an Alternative

Consider another visualization when the number of categories makes a bar chart difficult to read or when the analytical objective is better communicated through another visual representation.

A **lollipop chart** may be useful when comparing many categories because it can reduce visual weight while preserving a common baseline.

A **stacked bar chart** may be appropriate when the objective is to compare both overall category values and subgroup composition.

A **table** may be preferable when readers need exact numerical values rather than primarily visual comparisons.

A **slope diagram** may be more appropriate when the main analytical question concerns changes between two time points across several groups.

## Additional Recommendations

### Recommended

- Use visual components purposefully to promote readability, ease of interpretation, transparency, and reduction of redundancy.
- Ensure that bar charts, including stacked bar charts, have labels sufficient to clearly define the categories represented.
- Sort bars in an analytically meaningful order that supports the main purpose of the chart. If there is no natural analytical ordering, consider sorting bars by value.
- Use consistent scales when creating small multiple charts.
- Ensure that bar thickness is greater than the white space between bars.
- Use additional color only when it supports the analytical purpose of the chart.
- Use one color for all bars unless there is a reason to emphasize a particular bar or category.
- Limit the number of bars when possible. Too many bars can make individual categories difficult to distinguish.
- Consider horizontal bars when additional space is needed for category labels.

### Not Recommended

- Do not add colors that do not communicate additional information or meaningful emphasis.
- Avoid displaying so many categories that individual comparisons become difficult to interpret.

## Choosing Between Alternatives

| Analytical Goal | Alternative Visualization | Why It May Be Preferable |
|---|---|---|
| Compare many category values | Lollipop Chart | Reduces visual weight while retaining a common scale for comparison. |
| Compare category totals and subgroup composition | Stacked Bar Chart | Shows both overall category magnitude and subgroup composition. |
| Present exact numerical values | Table | Allows readers to look up and compare precise values directly. |
| Compare changes between two time points | Slope Diagram | Emphasizes the direction and magnitude of change between two points. |

## Data Requirements and Statistical Considerations

> **TODO (Phase 2):** Complete during individual enhancement work using applicable Census Bureau data and statistical guidance.

Future development of this section should address required variables and units, geographic level and reference period, aggregation and denominators, missing or suppressed values, margins of error and uncertainty where applicable, and comparability across groups, geographies, or time periods.

## Visualization-Specific Considerations

Bar length is the primary visual encoding in a bar chart and should remain proportional to the value represented. Because viewers compare bar lengths, the zero baseline is essential for avoiding exaggerated visual differences.

The order of categories should support the analytical purpose of the visualization. Categories with a natural or ordinal sequence should retain that sequence. Otherwise, an analytical ordering, such as ranking by value, may make comparisons easier.

Relevant component guidance should also be consulted for axes, color, grids, legends, sources, titles, and typography.

## Accessibility

- **Alt text:** Describe the chart's main comparison or takeaway rather than simply identifying it as a "bar chart."
- **Data table alternative:** Provide the underlying data in an accessible table or downloadable format when appropriate.
- **Do not rely on color alone:** Use labels, patterns, direct annotation, or other visual cues when color is used to distinguish categories.
- See [508 Compliance](508.html) and [Color](color.html) for general accessibility guidance.

## Census Data Example

> **TODO (Phase 2):** Add an example using public Census Bureau data.

The future example should identify the analytical question, Census dataset and table, geography, reference period, measure and units, reason for selecting a bar chart, and relevant limitations.

## Developer Implementation

> **TODO (Phase 2):** Add reproducible implementation guidance and code examples.

Future implementation guidance may include data preparation and reproducible Python and R examples, with documentation explaining how developers can adapt the examples to other Census datasets or geographic levels.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Truncated baseline | Can exaggerate apparent differences between categories. | Start bar charts at zero. |
| No spacing between categories | Can make the visualization appear to be a histogram and blur the distinction between discrete categories. | Maintain visible spacing between bars representing separate categories. |
| 3D effects | Can distort perceived bar dimensions and make accurate comparisons more difficult. | Use a two-dimensional presentation. |
| Excessive categories | Makes individual bars and labels difficult to compare. | Reduce categories or consider a lollipop chart or table. |
| Unnecessary color | Adds visual noise without improving interpretation. | Use color selectively to communicate meaning or emphasis. |
| Inconsistent scales across comparable charts | Can create misleading visual comparisons. | Use consistent scales when charts are intended to be compared. |

## Publication Quality Checklist

- [ ] The bar chart is appropriate for the analytical question.
- [ ] Bars begin at zero.
- [ ] Categories are ordered in an analytically meaningful way.
- [ ] Labels clearly identify categories and units.
- [ ] Bar widths and spacing are consistent.
- [ ] Omitted categories are documented.
- [ ] Color is used purposefully and is not the only means of communicating information.
- [ ] The visualization does not use 3D effects.
- [ ] Relevant accessibility guidance has been followed.
- [ ] Data source, geography, reference period, and units are documented where applicable.
- [ ] Relevant limitations, missing values, and statistical uncertainty are addressed where applicable.
- [ ] Related component guidance has been reviewed.

## Examples

Existing Census Bureau bar chart examples should be retained here as they are reviewed and incorporated into the standardized page structure.

The current guidance references figures 7–13 on pages 24–28. These examples should be reviewed during the next content-validation step before being modified or replaced.

## Related Pages

- [Stacked Bar Chart](stackedbarchart.html): use when comparisons also involve subgroup composition.
- [Lollipop Charts](lollipopcharts.html): consider when comparing many categories.
- [Tables](table.html): use when precise numerical values are the primary requirement.
- [Slope Diagram](slopediagram.html): use for comparisons between two time points.
- [Axes](axes.html): guidance for axis labels, scales, and tick marks.
- [Typography](typography.html): guidance for readable labels and text.
- [Comparing Data and Values](comparison.html): guidance for designing accurate comparisons.
- [508 Compliance](508.html): general accessibility requirements.
- [Color](color.html): guidance for appropriate and accessible use of color.
