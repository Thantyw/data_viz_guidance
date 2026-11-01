---
layout: default
title: Slope Diagram
permalink: slopediagram.html
tags: [Comparison]
description: "Use slope diagrams to compare levels and changes in values between two time points across multiple categorical groups."
---

# Slope Diagram

**Also known as:** slope chart, slopegraph

## Purpose and Overview

Slope diagrams show levels and changes in values between two time points and represent the simplest form of a line plot. They are most often used to show differences in levels and changes of a variable across different categorical groups. They are also useful for illustrating changes in rank between two time points and provide more information than a rank-specific bump chart.

A slope diagram consists of two vertical axes representing the two time points. The points for each group are plotted on each axis, and a line connects the two points for each group.

Slope diagrams may be used when only two data points are available or when the start and end data points of a longer series are all that are necessary to illustrate important patterns.

Authors should carefully consider whether absolute or relative change in values is of greatest interest. Slope diagrams, especially with small values, can overemphasize absolute change and mask important differences in relative change.

## When to Use

Use a slope diagram when the primary analytical objective is to compare levels and changes across two time points for multiple categorical groups.

Slope diagrams are particularly useful when readers need to identify:

- Which categories increased or decreased.
- Differences in starting and ending values.
- Differences in the magnitude of change across categories.
- Changes in relative position or rank.
- Categories that experienced little or no change.

A slope diagram may also be appropriate when only two data points are available or when the start and end points of a longer series are sufficient to communicate the important analytical pattern.

### Essential

- Directly label all lines in static slope diagrams.
- Clearly identify the two time points being compared.
- Ensure that each line accurately connects the values for the same categorical group.
- Use consistent units and definitions across the two time points.
- Use consistent axis scales when multiple slope diagrams or small multiples are intended to be compared.

### Avoid

- Avoid using slope diagrams when relative change is the primary analytical objective.
- Avoid using slope diagrams when trends between the two time points are known to be highly variable or when reducing the data to two time points masks important trends.
- Avoid displaying so many lines that individual categories become difficult to distinguish.
- Avoid inconsistent scales across comparable slope diagrams.

## When to Use an Alternative

Consider a **line chart** when the analytical objective is to show trends across three or more time points or when important variation occurs between the starting and ending points.

Consider a **bar chart** when the primary objective is to compare category values at a single point rather than emphasize change.

Consider a **dot plot** when category values need to be compared without emphasizing a connection between two time points.

Consider a **table** when readers need exact values rather than primarily visual comparisons of change.

If relative rather than absolute change is the main analytical objective, consider an alternative presentation that communicates relative differences more directly.

## Additional Recommendations

### Recommended

- Limit the number of lines included in a static slope diagram to 15, especially when many lines overlap.
- Incorporate flags to denote when slopes are statistically significant.
- If more lines are necessary, consider building an interactive slope diagram where individual lines can be selected and details about the selected line can be provided.
- Directly label lines or endpoints to reduce dependence on a legend.
- Maintain adequate spacing between labels and lines.
- Use visual emphasis selectively when a particular category or change is central to the analytical message.

### Not Recommended

- Do not use slope diagrams when the goal is to highlight relative change.
- Do not use slope diagrams when trends between the two time points are known to be highly variable or when reducing the data to two time points masks important trends in the data.
- Do not add unnecessary visual elements that compete with the connecting lines and labels.

## Choosing Between Alternatives

| Analytical Goal | Alternative Visualization | Why It May Be Preferable |
|---|---|---|
| Compare change between exactly two time points | Slope Diagram | Emphasizes differences in levels, direction, and magnitude of change across categories. |
| Show trends across three or more time points | Line Chart | Shows the shape and progression of change over multiple periods. |
| Compare category values at one point | Bar Chart | Provides a common baseline for straightforward magnitude comparison. |
| Compare category values without emphasizing change | Dot Plot | Emphasizes position along a common scale without connecting two time points. |
| Present exact values | Table | Allows readers to retrieve and compare precise values directly. |

## Data Requirements and Statistical Considerations

> **TODO (Phase 2):** Complete during individual enhancement work using applicable Census Bureau data and statistical guidance.

Future development of this section should address the two comparison points, category definitions, measurement units, geographic level and reference periods, missing or suppressed values, margins of error and uncertainty where applicable, and comparability between the two time points.

Particular attention should be given to ensuring that definitions, geographic boundaries, universes, and measurement methods are sufficiently comparable across the two points being connected.

Statistical significance should also be considered when apparent changes between time points are interpreted.

## Visualization-Specific Considerations

The direction and steepness of each connecting line communicate change between the two points. An upward line indicates an increase, a downward line indicates a decrease, and a relatively flat line indicates little absolute change.

Slope diagrams can overemphasize absolute changes, particularly when values are small. Authors should therefore determine whether absolute or relative change is the more appropriate analytical measure before selecting this visualization.

Crossing lines can reveal changes in relative position or ranking, but excessive line crossings can make individual categories difficult to follow.

When small multiples are used, each panel should use the same axis scale when the panels are intended to support direct comparison.

Relevant component guidance should also be consulted for axes, color, grids, legends, sources, titles, and typography.

## Accessibility

- **Alt text:** Describe the primary changes or comparisons rather than simply identifying the visualization as a "slope diagram."
- **Data table alternative:** Provide values for both comparison points in an accessible table or downloadable format when appropriate.
- **Direct labeling:** Clearly associate labels with their corresponding lines or endpoints.
- **Do not rely on color alone:** Use direct labels, line styles, annotations, or other cues when necessary to distinguish categories.
- Ensure endpoint labels and values remain readable and clearly associated with the correct connecting lines.
- Avoid excessive line crossings and overlapping labels that make relationships difficult to follow.
- See [508 Compliance](508.html), [Color](color.html), and [Typography](typography.html) for general accessibility and presentation guidance.

## Census Data Example

> **TODO (Phase 2):** Document and validate the existing Census Bureau examples below with dataset and table identifiers, geography, reference periods, measures, units, and applicable statistical limitations.

The existing examples are retained in this Phase 1 revision. Additional data documentation can be added during Phase 2 after the underlying Census sources have been validated.

## Developer Implementation

> **TODO (Phase 2):** Add reproducible implementation guidance and code examples.

Future implementation guidance may include data preparation and reproducible Python and R examples, with documentation explaining how developers can adapt the examples to other Census datasets, geographic levels, or comparison periods.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Using more than two points | Changes the analytical purpose and may make the visualization difficult to follow. | Consider a line chart when trends across three or more points are important. |
| Focusing on relative change | Slope diagrams can overemphasize absolute change, especially for small values. | Use an alternative presentation when relative change is the primary analytical objective. |
| Inconsistent scales | Makes comparisons across slope diagrams or small multiples difficult and potentially misleading. | Use consistent scales when plots are intended to be compared. |
| Excessive lines | Creates overlapping lines and labels that are difficult to interpret. | Limit static displays to approximately 15 lines or consider an interactive alternative. |
| Missing direct labels | Makes individual lines difficult to identify. | Directly label all lines in static slope diagrams. |
| Ignoring statistical significance | Apparent changes may not represent statistically meaningful differences. | Use appropriate indicators or flags when statistical testing is applicable. |
| Masking intermediate trends | Comparing only endpoints may hide important variation between the two time points. | Use a line chart when intermediate trends are analytically important. |
| Reliance on color alone | Can create accessibility problems and make categories difficult to distinguish. | Use direct labels or additional visual cues. |

## Publication Quality Checklist

- [ ] A slope diagram is appropriate for comparing the selected two time points.
- [ ] Both comparison points are clearly identified.
- [ ] The values, units, and definitions are comparable across the two time points.
- [ ] All lines in a static slope diagram are directly labeled.
- [ ] The number of lines remains interpretable.
- [ ] Static displays generally contain no more than 15 lines.
- [ ] Labels and lines do not overlap excessively.
- [ ] Comparable panels or small multiples use consistent scales.
- [ ] Absolute versus relative change has been considered.
- [ ] Intermediate trends are not being hidden in a way that changes the analytical interpretation.
- [ ] Statistical significance is communicated where applicable.
- [ ] Color is not the only means of identifying categories.
- [ ] Missing or suppressed values are documented where applicable.
- [ ] Relevant accessibility guidance has been followed.
- [ ] Data source, geography, reference periods, and units are documented where applicable.

## Examples

### Example 1: Median Earnings for Full-Time, Year-Round Retail Workers, 2022

This example uses direct labeling in a slope diagram. Most of the lines are relatively flat, which makes it difficult to accurately interpret changes. This figure would have benefited from flags denoting statistical significance.

![Slope diagram showing median earnings for full-time, year-round retail workers in 2022](assets/SlopeDiagram1.png)

### Example 2: Percentage with Health Insurance Coverage for Adults 19 to 64 Years, 2021–2022

The example below uses small multiples with slope diagrams. It is a good example of direct labeling and incorporating statistical testing into a slope diagram. While the majority of slopes are not steep, the asterisk denoting statistical significance helps users better interpret the visualization and changes across time.

However, each small multiple uses a different y-axis scale. This makes comparisons across the plots difficult. As stated in the small multiple standards, each panel should use the same axis scale when the panels are intended to be compared.

![Small-multiple slope diagrams showing health insurance coverage for adults ages 19 to 64 from 2021 to 2022](assets/SlopeDiagram2.png)

## Related Pages

- [Bar Chart](barchart.html): use when comparing category values at a single point.
- [Dot Plot Chart](dotplotchart.html): use for category comparisons without emphasizing change between two endpoints.
- [Tables](table.html): use when exact numerical values are the primary requirement.
- [Axes](axes.html): guidance for scales, labels, and axis presentation.
- [Comparing Data and Values](comparison.html): guidance for designing accurate comparisons.
- [Typography](typography.html): guidance for readable labels and text.
- [508 Compliance](508.html): general accessibility requirements.
- [Color](color.html): guidance for appropriate and accessible use of color.
