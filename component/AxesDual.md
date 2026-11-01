---
layout: default
title: Axes-Dual or Double-Y
permalink: axesdual.html
description: "Guidance for avoiding dual or double-Y axes except when displaying equivalent scales for the same data or in limited, appropriate applications such as Pareto charts."
---

# Double-Y or Dual Axes

## Purpose and Overview

A double-Y axis, also known as a dual-axis chart, uses two vertical scales, usually one on the left and one on the right.

Dual-axis charts should **not** generally be used. Because the two axes can use independently selected scales, their appearance can be manipulated to suggest arbitrary or misleading relationships between data series.

There are two limited situations identified in this guidance where dual axes may be appropriate because the axes have defined relationships or purposes that cannot be arbitrarily manipulated.

The first is when the second axis provides an **alternative scale for the same data**. For example, one vertical axis may display temperature in Fahrenheit while the other displays the same temperature in Celsius. Only one data series is shown; the second axis expresses the same measurements in different units.

![Dual axes showing the same temperature data using Fahrenheit and Celsius scales](assets/axes03.png)

The second limited application is a **Pareto chart**. Pareto charts are typically used in quality-related analysis to examine the frequency or cost of events. Bars are arranged in descending order, and some Pareto charts include a line representing the cumulative percentage. These charts are not expected to be used frequently, if at all, at the Census Bureau.

![Pareto chart example using a secondary axis for cumulative percentage](assets/axes04.png)

## When to Use

Use dual axes only in limited situations where the relationship between the scales is clearly defined and cannot be arbitrarily manipulated.

Appropriate situations identified in the existing guidance include:

- Showing an alternative unit or scale for the **same data series**, such as Fahrenheit and Celsius.
- Using a Pareto chart where bars represent frequency or cost and a line represents cumulative percentage.

For ordinary comparisons between two different data series, use another visualization approach.

### Essential

- Label the x- and y-axes clearly.
- When a dual axis shows alternative scales for the same data, clearly label both scales and their units.
- Be consistent in how tick marks are labeled.
- Use consistent axes for data visualizations that are intended to be compared.
- Make the relationship between the two scales explicit.
- Ensure that the second axis does not create a misleading visual relationship.

### Avoid

- **Do not use dual axes for two independent data series.**
- Do not select separate scales that make unrelated series appear correlated.
- Do not require readers to determine visually which series belongs to which axis.
- Do not use dual axes simply because two series have substantially different ranges.
- Do not use dual axes when side-by-side charts, small multiples, normalization, percent change, or a table would communicate the comparison more faithfully.

## When to Use an Alternative

For two different data series, alternatives should generally be preferred.

Consider **side-by-side charts or small multiples** when the series require different scales. Each series can then have its own clearly labeled axis while preserving a visual structure that supports comparison.

Consider placing both series on a **single common scale** when the values and units permit meaningful direct comparison.

Consider transforming values into a common analytical measure, such as **percent change**, when relative change rather than raw magnitude is the primary analytical question.

Consider a **table** when readers need exact values or when a small number of observations can be communicated more clearly without a potentially misleading visual relationship.

## Additional Recommendations

### Recommended

- See the [Axes](axes.html) component guidance for general recommendations on scales, tick marks, labels, and axis consistency.
- Prefer a common scale whenever two data series can be meaningfully compared on one axis.
- Use direct labeling when it helps readers associate data series with their values.
- When separate scales are genuinely necessary, consider separate aligned charts rather than combining them into one dual-axis plot.
- Clearly communicate units and measurement definitions.

### Not Recommended

- Do not use independently adjustable axes to create visual alignment between unrelated series.
- Do not rely only on color to indicate which data series corresponds to which axis.
- Do not use a second axis simply to make differences or trends appear more dramatic.
- Do not assume that point labels compensate for a misleading dual-axis structure.

## Choosing Between Alternatives

| Analytical Situation | Recommended Approach | Why |
|---|---|---|
| Same data expressed in two equivalent units | Dual axes may be appropriate | The second scale is mathematically tied to the first and represents the same data. |
| Pareto analysis | Pareto chart may use a secondary axis | The secondary line represents cumulative percentage in a defined analytical structure. |
| Two different series with comparable units and ranges | Single common axis | Supports direct and faithful comparison. |
| Two different series requiring different scales | Side-by-side charts or small multiples | Keeps each scale explicit and reduces the risk of false visual relationships. |
| Comparing relative change | Percent-change visualization | Places series on a common analytical basis. |
| Small number of exact observations | Table | Communicates exact values without implying a visual relationship between incompatible scales. |

## Why Dual Axes Can Mislead

Dual-axis charts can create apparent relationships that depend more on the selected scales than on the underlying data.

Changing the minimum, maximum, or interval of either vertical axis can alter the apparent relationship between two lines without changing the data. Readers may interpret line crossings, relative heights, or similar slopes as meaningful even when the series use different units and scales.

A dual-axis visualization can therefore create unnecessary cognitive effort. Readers must determine which line corresponds to which scale while also interpreting values and trends.

When two different series must be compared, a common scale, separate aligned charts, normalization, percent change, or a table will often communicate the relationship more clearly.

## Accessibility

- Clearly identify every axis and its measurement unit.
- Do not rely on color alone to associate a series with an axis.
- Prefer direct labeling where practical.
- Ensure axis labels, tick labels, and annotations are readable and clearly associated with the relevant data.
- Alt text should explain the analytical relationship and, where relevant, why the dual-axis presentation may be misleading rather than simply stating that the image is a dual-axis chart.
- When exact values are important, provide an accessible table or equivalent data representation.
- See [508 Compliance](508.html), [Color](color.html), and [Typography](typography.html) for general accessibility and presentation guidance.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Independent scales for different series | Scale choices can create arbitrary visual relationships. | Use a common scale or separate aligned charts. |
| Unclear series-to-axis association | Readers may interpret values using the wrong scale. | Avoid the dual-axis design or clearly and directly label the series. |
| Different ranges that visually align | May imply correlation or similarity that is not supported by the data. | Use separate charts or a common analytical measure. |
| Unlabeled axes or units | Prevents accurate interpretation of values. | Clearly label axes and measurement units. |
| Reliance on color | Creates accessibility problems and can make axis association difficult. | Use direct labels and other visual cues. |
| Using point labels to compensate for incompatible scales | Readers still face conflicting spatial relationships. | Redesign the visualization rather than relying on labels alone. |

## Publication Quality Checklist

- [ ] Dual axes are necessary for one of the limited appropriate applications described in this guidance.
- [ ] The chart is not using two independently adjustable scales for unrelated data series.
- [ ] Both axes and measurement units are clearly labeled.
- [ ] Tick marks and labels are consistent.
- [ ] The relationship between the two scales is explicit.
- [ ] Readers can clearly identify which data correspond to each scale.
- [ ] A common scale has been considered.
- [ ] Side-by-side charts or small multiples have been considered.
- [ ] Percent change or another common analytical measure has been considered where appropriate.
- [ ] A table has been considered when exact values would communicate the information more clearly.
- [ ] Color is not the only method used to communicate meaning.
- [ ] Relevant accessibility guidance has been followed.
- [ ] The selected scales do not create a misleading visual relationship.

## Examples

### Example 1: International Monetary Fund (IMF) Working Paper

The following example of a dual-axis chart is taken from an International Monetary Fund working paper, WP/16/121.

Several aspects of the graph make interpretation difficult. The vertical axes are not clearly labeled, and it is unclear which line corresponds to which scale. If both axes represent income, the reason for using two different scales is also unclear.

This illustrates several of the problems with dual-axis or double-Y plots and why they generally should not be used.

![Example of a problematic dual-axis chart from an IMF working paper](assets/axes05.png)

### Example 2: Office for National Statistics UK

The following example comes from the UK Office for National Statistics and shows employment and unemployment rates using a dual-axis graph.

![Dual-axis chart showing UK employment and unemployment rates](assets/axes06.png)

Viewers may miss the y-axis on the right or misunderstand the relationship between the two lines. The ranges of the two axis scales are substantially different. A reader could therefore draw an incorrect conclusion from the relative positions of the lines.

As in Example 1, it is also not immediately clear which line corresponds to which axis.

A more faithful representation places the two lines on the same scale and axis, allowing a more direct comparison.

![Employment and unemployment data displayed on a common scale](assets/axes07.png)

The example below demonstrates how changing the axis scales can substantially change the apparent relationship between the same data series.

![Alternative dual-axis scaling demonstrating how scale choices can alter interpretation](assets/axes08.png)

Often, two axes are used because important details become difficult to see when the series have very different ranges. A better approach can be to display the trends in separate vertical or horizontal side-by-side charts, where each series has its own clearly labeled scale.

This approach also demonstrates useful visualization practices, including consistent changes between vertical tick marks, consistent horizontal scales, and direct labeling of the Employment and Unemployment series.

![Employment and unemployment displayed in separate aligned charts](assets/axes09.png)

### Example 3: Total Number of Workers — Census Bureau

The following example is a dual-axis plot published by the Census Bureau.

![Census Bureau dual-axis chart showing government and private-sector employment](assets/axes10.png)

The chart illustrates the difficulty of connecting each line to the correct axis scale. Although points on the lines are labeled, the reader must still determine which axis corresponds to each series.

For example, from 2019 through 2021, one line appears above the other even though it represents a much smaller number of workers. This creates cognitive dissonance because a value around 19.7 million can appear visually above a value around 127.7 million.

A common-scale representation provides a more faithful comparison:

![Government and private-sector employment displayed using a common scale](assets/axes11.png)

The article's key takeaway concerns the different employment recoveries of private industry and state and local government following the COVID-19 pandemic. That comparison is not communicated clearly by the original dual-axis presentation.

Using two annotated charts, similar to the alternative in the ONS example, could communicate the comparison more clearly.

Because the article also discusses percent changes in employment, another approach would be to display percent changes directly rather than asking readers to mentally compare raw values across very different scales.

Finally, because only five discrete points are shown for each series, a table may also be an effective way to communicate the values.

## References and Further Reading

The existing guidance identifies several resources that explain the risks associated with dual-axis charts:

- Lisa Muth, *Why not to use two axes, and what to use instead: The case against dual axis charts*, Datawrapper.
- UK Office for National Statistics, *Dueling with axis: the problems with dual axis charts*.
- American Society for Quality guidance on Pareto charts.
- Tyler Vigen's examples of spurious correlations.

These resources provide additional demonstrations of how scale selection can create misleading apparent relationships.

## Related Pages

- [Axes](axes.html): general guidance for scales, tick marks, axis labels, and consistency.
- [Comparing Data and Values](comparison.html): guidance for designing accurate comparisons.
- [Bar Chart](barchart.html): use for straightforward categorical comparisons.
- [Tables](table.html): use when exact values are more important than visual comparison.
- [Typography](typography.html): guidance for readable labels and text.
- [508 Compliance](508.html): general accessibility requirements.
- [Color](color.html): guidance for appropriate and accessible use of color.
