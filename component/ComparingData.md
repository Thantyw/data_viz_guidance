---
layout: default
title: Comparing Data and Values
permalink: comparison.html
description: "Guidance for designing data visualizations that support accurate comparison of values, categories, trends, and related datasets."
---

# Comparing Data and Values

## Purpose and Overview

When designing data visualizations for comparison, the goal is to facilitate the user's ability to identify trends, patterns, similarities, and differences across datasets or subsets of a single dataset.

Comparison visualizations leverage the human visual system's capacity for parallel processing, allowing users to make quick and intuitive comparisons when visual elements are presented consistently.

Comparison data visualizations may present two or more visual representations in close proximity or combine related series within a single view. The selected approach should make the intended comparison clear while avoiding visual differences caused by inconsistent scales, encodings, or layouts.

## Comparison Approaches

### Small Multiples

**Small multiples** are a common and highly effective form of comparison visualization. They consist of a series of identical or very similar graphs, each displaying a different subset of data using the same axes and scales.

Small multiples allow users to scan across related views while maintaining a consistent visual structure.

### Juxtaposed Views

**Juxtaposed views** present different chart types or different views of the same data side by side.

While scales may differ because of the nature of the data, consistent visual encodings and clear labeling are important for connecting related information across the views.

For example, a bar chart showing totals might appear beside another visualization showing the distribution of those totals across categories.

### Superimposed or Overlaid Views

**Superimposed or overlaid views** plot multiple data series on the same set of axes within a single chart. Series may be distinguished using line styles, colors, markers, or other visual encodings.

This approach can be effective for comparing a limited number of time series or distributions but requires careful design to avoid clutter.

### Linked Views

**Linked views** are interactive visualizations in which selections or filters applied to one visualization dynamically update or highlight related information in other visualizations.

For example, selecting observations in a scatter plot may highlight corresponding bars in a histogram or geographic areas on a map.

Linked views can help users explore relationships across different dimensions and representations of the data.

### Difference or Deviation Plots

**Difference plots or deviation plots** emphasize the magnitude and direction of differences between datasets or between a dataset and a reference point.

Instead of displaying only raw values, these visualizations may display a calculated difference, such as year-over-year percentage change or deviation from a baseline.

### Animation or Temporal Sequencing

**Animation or temporal sequencing** presents change over time through a sequence of frames representing different time periods.

Although this is not a simultaneous comparison, movement can help users perceive change and evolution over time. However, animation can make precise quantitative comparisons more difficult because users must remember values or positions from previous frames.

When precise comparison is important, consider providing static views, small multiples, or another comparison method in addition to or instead of animation.

## Scales

When data visualizations are intended to be compared, use consistent axes and scales whenever the same measure is being compared.

For example, if several charts display the same measure on their vertical axes, those axes should use the same range. This allows users to compare values across charts without having to compensate mentally for differences in axis starting points, ending points, or intervals.

Inconsistent scales can create false impressions of similarity or difference even when the underlying data do not support those impressions.

## Aspect Ratios

The apparent shape and slope of a line can change depending on the aspect ratio of the plotting area.

The aspect ratio is the relationship between the width and height of a visualization. A square has an aspect ratio of 1:1, while a wide landscape display may use an aspect ratio such as 16:9.

The same data can therefore appear to have substantially different patterns when displayed using different aspect ratios.

The figure below illustrates how the same data can produce visually different lines or curves when the plotting area's aspect ratio changes.

![The same data displayed using different aspect ratios, illustrating how chart dimensions can change the apparent shape of a line](assets/Comparison1.png)

## Guidance

### Essential

- Always maintain consistent scales and axes when visualizations are intended to support direct comparison and represent the same measure. If scales differ, visual differences may be misleading.
- Always use consistent visual encoding. If a particular color represents a category in one visualization, it should represent the same category in related comparison visualizations.
- Apply the same consistency to shapes, line types, symbols, and other encodings.
- Clearly label measures, units, categories, and time periods so users understand what is being compared.
- Where appropriate, make it clear which comparisons are statistically significant.
- Ensure that the datasets, categories, measures, or time periods being compared have a logical relationship.

### Avoid

- Avoid inconsistent axes or scales for directly comparable measures.
- Avoid changing colors, symbols, line styles, or category ordering between related charts without a meaningful reason.
- Avoid comparing unrelated data simply because they can be placed side by side.
- Avoid layouts that require excessive eye movement or make it difficult to associate related information.
- Avoid aspect-ratio differences that unintentionally change the apparent pattern of comparable data.
- Avoid overcrowding overlaid visualizations with too many series.
- Avoid animation when users need to make precise comparisons between values that are not visible simultaneously.

## Additional Recommendations

### Recommended

- Provide clear and consistent labeling. Axis labels, titles, legends, and annotations should use consistent terminology across related visualizations.
- Align elements for easy scanning. Arrange charts in a grid or clear horizontal or vertical sequence to facilitate comparison.
- Provide sufficient context. Each visualization should remain understandable on its own to an appropriate degree.
- Use a consistent visual hierarchy so the same types of information receive similar emphasis across related charts.
- Highlight important differences or similarities when they are central to the analytical message.
- Use subtle annotations or visual cues when they help users identify the intended comparison.
- Keep category ordering consistent across related visualizations whenever possible.
- Use direct labeling where it reduces the effort required to connect categories or series across views.

### Not Recommended

- Do not force comparisons between data that do not have a meaningful analytical relationship.
- Do not manipulate axis ranges or aspect ratios to exaggerate or minimize differences.
- Do not use inconsistent visual encodings for the same categories across related charts.
- Do not add unnecessary visual variation merely to make individual charts look different.
- Do not assume that proximity alone makes two visualizations meaningfully comparable.

## Choosing a Comparison Approach

| Comparison Need | Approach | Consideration |
|---|---|---|
| Compare the same measure across categories, groups, or geographies | Small multiples | Use consistent axes, scales, encodings, and layout. |
| Compare different but related views | Juxtaposed views | Clearly communicate the relationship between the views. |
| Compare a limited number of related series on the same scale | Superimposed or overlaid view | Avoid clutter and distinguish series consistently. |
| Explore relationships interactively across several views | Linked views | Ensure interactions and selections are understandable and accessible. |
| Emphasize change from a baseline or reference | Difference or deviation plot | Clearly define the reference point and calculation. |
| Show evolution across time | Animation or temporal sequencing | Consider static alternatives when precise comparisons are important. |
| Compare exact values | Table | Useful when numerical precision is more important than pattern recognition. |

## Accessibility

- Do not rely on color alone to communicate differences among categories or series.
- Use consistent labels, symbols, patterns, line styles, or direct labeling where appropriate.
- Maintain sufficient contrast for text and graphical elements.
- Ensure related charts have clear titles or labels so users can determine what is being compared.
- Provide accessible alternatives for interactive or animated comparison views.
- When animation is used, provide controls that allow users to pause, stop, or navigate the sequence where applicable.
- Provide underlying values in an accessible table or equivalent format when precise values are important.
- Alt text should communicate the primary comparison, important differences, and relevant trends rather than merely listing chart types.
- See [508 Compliance](508.html), [Color](color.html), and [Typography](typography.html) for general accessibility and presentation guidance.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Inconsistent scales | Can make similar values appear different or different values appear similar. | Use the same scale for directly comparable measures. |
| Inconsistent visual encoding | Forces users to relearn colors, symbols, or categories between views. | Use consistent encodings across related visualizations. |
| Different aspect ratios | Can change the apparent shape or steepness of patterns. | Use consistent dimensions when visual shape is part of the comparison. |
| Excessive overplotting | Makes individual series difficult to distinguish. | Reduce the number of series or use small multiples. |
| Unrelated comparisons | Can imply relationships that have little analytical meaning. | Compare data with a clear logical or analytical relationship. |
| Animation for precise values | Requires users to remember previous frames. | Use small multiples, static comparisons, or a table when precision is important. |
| Inconsistent category ordering | Makes scanning and comparison unnecessarily difficult. | Maintain a consistent order across related views. |

## Publication Quality Checklist

- [ ] The analytical purpose of the comparison is clear.
- [ ] The datasets, categories, measures, or time periods have a meaningful relationship.
- [ ] Directly comparable charts use consistent scales and axes.
- [ ] Comparable visualizations use consistent aspect ratios where appropriate.
- [ ] Colors, symbols, line styles, and other encodings are used consistently.
- [ ] Category ordering is consistent across related views where appropriate.
- [ ] Titles, labels, units, and legends use consistent terminology.
- [ ] Important differences or similarities are identifiable without unnecessary visual complexity.
- [ ] Statistical significance is communicated where appropriate.
- [ ] Overlaid views do not contain excessive series or clutter.
- [ ] Animation is not being used when precise static comparison would be more effective.
- [ ] Color is not the only means of communicating differences.
- [ ] Accessible alternatives are available for interactive or animated content where applicable.
- [ ] The comparison does not create a misleading impression through inconsistent scales, dimensions, or visual encodings.

## Examples

### Example 1: Inconsistent Y-Axes

The following pair of bar charts demonstrates why consistent axes are important when visualizations are intended for comparison.

![Two bar charts using inconsistent y-axis scales, making the left-most bars appear more similar than their values indicate](assets/Comparison2.png)

#### Why It Fails

In both charts, the "Col 1" values appear nearly identical. However, examining the tick marks on each y-axis shows that the "Col 1" value in the second chart is thirty percentage points lower than the value in the first chart.

A data visualization adds visual structure to data, but if that structure gives users a false impression of the underlying values, the visualization does not support accurate interpretation.

For this reason, the y-axis should remain consistent across visualizations that are intended for direct comparison.

### Example 2: Consistent Y-Axes

The following example uses the same underlying data but applies consistent y-axis scales.

![Two bar charts using consistent y-axis scales so differences in values correspond to visible differences between the charts](assets/Comparison3.png)

#### Why It Meets the Requirements

Using consistent y-axis scales makes differences between the charts easier to interpret accurately. Changes in the underlying values correspond more directly to changes in the visual representation.

The effectiveness of comparison visualization depends on consistency in design elements and a clear analytical intention to highlight meaningful differences or similarities.

## Related Pages

- [Axes](axes.html): guidance for scales, tick marks, labels, and consistent axes.
- [Axes-Dual or Double-Y](axesdual.html): guidance on the risks and limited appropriate uses of dual axes.
- [Bar Chart](barchart.html): guidance for comparing categorical values.
- [Dot Plot Chart](dotplotchart.html): guidance for comparing categorical values using position.
- [Slope Diagram](slopediagram.html): guidance for comparing values and changes between two points.
- [Tables](table.html): guidance for comparisons requiring exact values.
- [Typography](typography.html): guidance for consistent and readable text.
- [508 Compliance](508.html): general accessibility requirements.
- [Color](color.html): guidance for consistent and accessible color use.
