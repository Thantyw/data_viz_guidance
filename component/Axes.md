---
layout: default
title: Axes
permalink: axes.html
description: "Guidance for designing and labeling chart axes, scales, and tick marks to support accurate, readable, and consistent data visualizations."
---

# Axes

## Purpose and Overview

Axes provide essential reference information that helps users associate data points with values, particularly when values are not labeled directly in a visualization.

Many data visualizations contain two axes: an x-axis (horizontal) and a y-axis (vertical). Axes establish the coordinate system, categories, values, units, or other reference information needed to interpret the data.

For categorical visualizations such as bar charts, one axis identifies categories while the other represents the quantitative values associated with those categories.

For line charts and scatter plots, axes commonly represent continuous or quantitative values such as time, age, percentages, dollar amounts, or counts.

Axes are not always necessary or appropriate, but they should be considered by default. For example, an axis title may be unnecessary when the same information is already communicated clearly in the visualization title. Similarly, direct data labels may sometimes reduce the amount of axis information required.

The goal is to provide enough reference information for accurate interpretation without introducing unnecessary repetition or clutter.

## Axis Titles and Labels

Axes should be clearly labeled so users understand what is being displayed.

Axis titles should provide useful contextual information about the values represented by the axis, including the unit of measurement where relevant.

For example, an axis displaying percentages can use a descriptive title such as **Percentage of Voters** rather than requiring a percentage symbol on every labeled tick mark.

Axis labels, visualization titles, subtitles, legends, and annotations should work together to communicate context efficiently without unnecessary duplication.

### Essential

- Clearly identify what each axis represents.
- Include the unit of measurement in the axis title when relevant.
- Use terminology that is consistent with the visualization title, subtitle, legend, and source information.
- Ensure labels are readable and clearly associated with the appropriate axis.

### Avoid

- Avoid ambiguous axis titles.
- Avoid repeating information unnecessarily when the same context is already communicated clearly elsewhere.
- Avoid abbreviations or terminology that users may not understand without explanation.
- Avoid axis labels that are visually disconnected from the corresponding axis.

## Scales

A scale defines how data values are mapped to positions along an axis.

The scale should support accurate interpretation of the data and should not exaggerate, minimize, or otherwise distort meaningful differences.

When multiple visualizations are intended to support direct comparison, use consistent axes and scales for the same measure. This is especially important for small multiples and other comparison layouts.

### Zero Baselines

**Bar charts must include zero.** Because the length or height of a bar encodes its value, a truncated quantitative axis can exaggerate differences between categories.

For other visualization types, whether zero should be included depends on the analytical purpose, audience, data range, and clarity of the visualization.

When a nonzero baseline is appropriate, the scale should still be presented clearly so users can interpret differences accurately.

For guidance about the risks associated with multiple vertical scales, see [Axes-Dual or Double-Y](axesdual.html).

### Essential

- Use scales that accurately represent the underlying values.
- Use consistent scales for directly comparable visualizations representing the same measure.
- Include zero on the quantitative axis of bar charts.
- Make scale ranges and intervals clear to users.

### Avoid

- Avoid changing scales across directly comparable charts when doing so could create misleading visual differences.
- Avoid truncated bar-chart axes.
- Avoid scale choices intended primarily to exaggerate or minimize differences.
- Avoid dual-axis plots except for the limited appropriate applications described in the Dual Axes guidance.

## Tick Marks

Tick marks provide reference points along an axis and function similarly to markings on a ruler.

Not every tick mark needs to be labeled, but tick marks should establish a consistent interval. The spacing between tick marks should be equal for a standard linear scale, and the number of unlabeled tick marks between labeled ticks should remain consistent.

Too many tick marks or labels can create visual clutter and make values harder to interpret.

### Essential

- Use consistent intervals between tick marks on a standard linear scale.
- Be consistent in how tick marks are labeled.
- Ensure labeled ticks clearly communicate their corresponding values.

### Recommended

- Reduce clutter by avoiding labels on every tick mark when they are unnecessary.
- When appropriate, use different tick-mark lengths to establish visual hierarchy, similar to a ruler.
- For example, a longer tick mark may be used at every fifth interval while intermediate marks remain shorter.
- Select tick intervals that support easy interpretation of the scale.

### Not Recommended

- Do not crowd an axis with more tick marks or labels than users can interpret easily.
- Do not use irregular tick intervals on a standard linear scale.
- Do not remove so much axis information that users can no longer estimate or interpret values accurately.

## Guidance

### Essential

- Label each axis when a label is necessary to interpret the visualization.
- Be consistent in how tick marks are labeled.
- Use consistent axes for data visualizations that are intended to be compared and represent the same measure.
- Do not use dual-axis plots except for alternative scales representing the same data or appropriate Pareto charts, as described in the [Dual Axes](axesdual.html) guidance.
- Include zero on the quantitative axis of bar charts.

### Avoid

- Avoid unnecessary differences in scales, labels, units, or tick intervals across directly comparable visualizations.
- Avoid axis designs that create a misleading impression of the magnitude or direction of differences.
- Avoid unnecessary duplication between axis titles and other visualization text.
- Avoid excessive tick labels that create clutter.

## Additional Recommendations

### Recommended

- Include zero when appropriate based on the visualization type, analytical purpose, audience, and clarity.
- Add the unit of measurement to the axis title when relevant, such as **Percentage of Voters**.
- Reduce clutter by not labeling every tick mark when intermediate labels are unnecessary.
- Use a clear hierarchy of tick marks when unlabeled intermediate ticks are useful.
- Maintain consistent terminology and number formatting across related axes.
- Consider direct data labels when they communicate values more clearly than extensive axis labeling.

### Not Recommended

- Do not remove axes merely for visual simplicity when doing so makes values difficult to interpret.
- Do not use inconsistent measurement units across comparable charts without clearly communicating the difference.
- Do not rotate or crowd labels unnecessarily when another orientation or layout would improve readability.
- Do not use an axis scale that visually exaggerates a difference without a clear analytical reason.

## Accessibility

- Ensure axis titles and tick labels are readable at the intended display size.
- Use sufficient contrast between axis text, tick marks, and the background.
- Do not rely on color alone to distinguish axes or related data series.
- Use clear, descriptive axis titles and measurement units.
- Avoid unnecessarily small or densely packed tick labels.
- Ensure that axis information remains understandable when the visualization is magnified or viewed on different screen sizes.
- Alt text should communicate important values, trends, or comparisons rather than relying on users to visually inspect axis positions.
- When precise values are important, provide an accessible table or equivalent data representation.
- See [508 Compliance](508.html), [Color](color.html), and [Typography](typography.html) for general accessibility and presentation guidance.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Missing axis title or unit | Users may not know what values represent. | Clearly identify the measure and unit where relevant. |
| Inconsistent scales across comparable charts | Can make differences appear larger or smaller than they are. | Use consistent scales for directly comparable measures. |
| Truncated bar-chart axis | Exaggerates differences because bar length encodes magnitude. | Start the quantitative axis at zero. |
| Excessive tick labels | Creates clutter and reduces readability. | Label only the intervals necessary for interpretation. |
| Irregular tick spacing | Can imply an incorrect numerical relationship. | Use consistent intervals on standard linear scales. |
| Unnecessary dual axes | Can create misleading relationships between series. | Use a common scale or separate charts unless a documented exception applies. |
| Missing measurement units | Forces users to infer whether values represent counts, percentages, dollars, or another measure. | Include units in the axis title when relevant. |
| Redundant labels | Adds clutter without improving understanding. | Coordinate axis titles, chart titles, subtitles, and direct labels. |

## Publication Quality Checklist

- [ ] Each necessary axis is clearly identified.
- [ ] Measurement units are included where relevant.
- [ ] Axis terminology is consistent with the rest of the visualization.
- [ ] Scales accurately represent the underlying data.
- [ ] Directly comparable charts use consistent axes and scales for the same measure.
- [ ] Bar charts include zero on the quantitative axis.
- [ ] Any nonzero baseline used for another visualization type has a clear analytical justification.
- [ ] Tick intervals are consistent for standard linear scales.
- [ ] Tick labels are readable and not unnecessarily dense.
- [ ] Axis labels do not duplicate other information unnecessarily.
- [ ] Dual axes are avoided except for the documented limited applications.
- [ ] Axis text and graphical elements have sufficient contrast.
- [ ] Users can interpret the visualization without relying on color alone.
- [ ] Accessible alternatives are provided when precise values are important.

## Examples

### Example 1: Axis Title Without the Unit of Measurement

![Chart with a y-axis title that does not include the percentage unit represented by the tick labels](assets/axes01.png)

#### Why It's Only Acceptable

The axis title misses an opportunity to include the unit of measurement represented by the y-axis.

As a result, each labeled tick mark includes a percentage symbol, while the axis title provides less useful context than it could.

Moving the unit of measurement into the axis title can simplify the tick labels and make the meaning of the axis clearer.

### Example 2: Unit Included in the Axis Title

![Chart with the percentage unit incorporated into the y-axis title, allowing simpler tick labels](assets/axes02.png)

#### Why It's Better

The improved axis title includes the unit of measurement, so the percentage symbol does not need to be repeated after every labeled tick.

The more descriptive title also makes the visualization easier to interpret by clearly communicating what the values represent.

## Related Pages

- [Axes-Dual or Double-Y](axesdual.html): guidance on the risks and limited appropriate uses of dual axes.
- [Comparing Data and Values](comparison.html): guidance for consistent axes and scales across comparison visualizations.
- [Bar Chart](barchart.html): guidance for categorical comparisons and zero baselines.
- [Typography](typography.html): guidance for readable axis labels and text.
- [508 Compliance](508.html): general accessibility requirements.
- [Color](color.html): guidance for accessible use of color.
