---
layout: default
title: Grids and Gridlines
permalink: grids-visualization-type.html
description: "How to use gridlines and map graticules to support data reading without distracting from the data."
---

# Grids and Gridlines

## Purpose and Overview

Grids provide reference lines that help readers understand values and compare data points. They can improve precision in large charts and make subtle differences easier to see.

In line graphs, bar charts, and similar visualizations, gridlines help readers trace data points to values on the x- or y-axis. Gridlines are optional; use them when data points aren't directly labeled.

On maps, reference grids can help readers locate places beyond the geographic boundaries shown, such as county or state lines. Graticules show latitude and longitude. They can provide context on reference maps but are not always needed on thematic maps using Census Bureau data.

## When This Guidance Applies

Apply this guidance when deciding whether to include gridlines in a chart or graticules on a map, and when choosing their appearance.

In addition to the guidance provided in this section, relevant guidance can also be found in the Axes, Color, and Map Layout sections.

## Essential Requirements

* Use a subdued color, such as gray, that keeps gridlines visible without cluttering the visualization.
* Render gridlines behind data marks so they do not obscure points, bars, or lines. Gridlines may cross data marks; the concern is visual layering and readability, not preventing every intersection.
* Keep gridlines from interfering with labels and other text.

## Recommended Practices

* Use gridlines when they help readers trace unlabeled data points to axis values.
* Consider removing gridlines when direct labels already provide the values readers need.
* Keep gridlines visually secondary to the data.
* Use map graticules when latitude and longitude help readers understand location.
* Apply the same subdued styling to graticules so they do not distract from the map's contents.

## Practices to Avoid

* Do not draw gridlines over data marks in a way that obscures them.
* Do not use gridlines so prominent that they compete with the data.
* Avoid unnecessary gridlines when direct labels already make values clear.
* Do not add graticules to a thematic map unless they help readers interpret it.

## Accessibility
 
* Keep axis and tick labels at a contrast of at least 4.5:1 against the background, and make sure gridlines do not cross through text in a way that reduces that contrast.
* If readers must use the gridlines to read values, keep those lines at least 3:1 against the background. Even then, draw them thinner or lighter than the data so the series stays primary.
* Do not rely on gridlines alone when precise values matter. Use direct labels or provide a data table.
* On maps, add graticules only when they help interpretation, and keep their labels readable at the intended size.
* For full requirements, see the [508 Compliance](508.html), [Color](color.html), and [Axes](axes.html) pages. Meeting these bullets does not by itself mean a visualization is 508 compliant.
 

## Census Data Examples

***Example 1:*** Driving Alone is Still Popular

![Horizontal bar chart showing transportation to work in New York using 2016 American Community Survey estimates. Driving alone accounts for 52.6 percent, followed by public transportation at 28.4 percent. Light gray vertical gridlines mark the percentage scale, while each bar also has a direct value label.]({{ '/component/assets/grid1.png' | relative_url }})

This example demonstrates the following practice well:

* Soft gray gridlines remain in the background of the visualization.

This chart could be improved:

* Each bar is directly labeled so that the gridlines may be unnecessary. Consider removing them for a cleaner presentation.

***Example 2:*** Median Sales Price of New Single-Family Homes Sold

![Line chart showing median sales prices of new single-family homes sold from 2019 to 2023 for the United States and four regions, in thousands of dollars. Light gray horizontal gridlines help readers estimate prices. All series end higher than in 2019, with the Northeast highest in 2023. Region names directly label the lines at the right.]({{ '/component/assets/grid2.png' | relative_url }})

[View the Census Bureau housing story containing the example](https://www.census.gov/library/stories/2024/06/national-housing-month.html).

This example demonstrates the following practices well:

* Soft gray gridlines do not interfere with interpretation of the chart.
* Labels remain clear and readable.
* Gridlines help readers estimate values and interpret the chart.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Gridlines are more prominent than the data | Readers may focus on the grid rather than the values or patterns. | Use a subdued color and keep gridlines visually secondary. |
| Gridlines obscure data marks | Points, bars, or lines become harder to read. | Render gridlines behind the data marks. |
| Gridlines interfere with labels | Text becomes harder to read. | Adjust the styling or layout to keep labels clear. |
| Gridlines repeat information already supplied by direct labels | Extra lines can add clutter without helping interpretation. | Consider removing unnecessary gridlines. |
| Graticules add no useful location information | They can distract from the map's main message. | Omit them unless they help readers interpret location. |
| "Behind the data" is interpreted as "never crosses a data position" | Useful reference lines may be removed unnecessarily. | Allow intersections while keeping gridlines behind and visually subordinate to the data. |

## Publication Quality Checklist

- [ ] The visualization fits the analytical question.
- [ ] Relevant alternatives were considered.
- [ ] Data source, geography, reference period, and units are documented.
- [ ] Data transformations and aggregation are appropriate.
- [ ] Missing values and relevant uncertainty are addressed.
- [ ] Existing accessibility, scaling, and axes guidance has been followed.
- [ ] Chart-specific limitations and caveats are explained.
- [ ] Code examples have been executed and verified.
- [ ] The visualization has undergone the appropriate review.
 
## Related Pages
 
* [Axes](axes.html): gridlines support the scale; axis titles, ticks, and baselines are covered there.
* [Line Graphs](linegraph.html): a common use of light gridlines behind a series.
* [Map Layout](maplayout.html): related guidance when considering graticules on a thematic map.
* [Color](color.html): keep gridlines visible enough to use without overpowering the data.
* [Typography](typography.html): keep labels readable so gridlines do not cut through or crowd text.
* [508 Compliance](508.html): contrast and text alternatives that also apply to labeled axes and gridlines.
