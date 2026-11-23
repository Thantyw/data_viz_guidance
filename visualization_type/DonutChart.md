---
layout: default
title: Donut Chart
permalink: donutchart.html
tags: [Distribution]
description: "A donut chart shows parts of a whole as arcs around an empty center."
---

# Donut Chart

**Also known as:** Doughnut chart

## Purpose and Overview

The donut chart is a variant of the pie chart, with a hole in its center, and it displays categories as arcs rather than slices. Both visualize part-to-whole relationships, where each arc's length is proportional to the whole. Each arc in a donut chart represents a different data category.

Compared to pie charts, donut charts take up less space, and the empty middle can hold labels or other data. This makes it ideal for dashboards and other visualizations with limited space. Pie charts require viewers to assess the area of each wedge, while donut charts require them to assess arc length because the arcs are all the same width. Humans perceive differences in length better than differences in volume.

## When to Use

Use a donut chart when:

* To show how parts make up one whole, such as the share of workers using each way of getting to work.
* The categories do not overlap and add up to 100%.
* There are only a few categories, ideally no more than 6.
* Space is limited, such as on a dashboard, and the center can hold a label or total.

## When to Use an Alternative

* Do not use donut charts when negative values are shown alongside positive values, as they are difficult to interpret.
* Do not use donut charts to show change across time. Alternatives include a line chart or stacked area chart.
* Do not use nested donut charts. This draws the eye to compare the smallest part of the outer arc to the largest part of the inner arc, a false comparison.
* Avoid donut charts when readers need exact comparisons between similar values. A bar chart or table is easier to read.

## Choosing Between Alternatives

| Analytical Goal | Alternative Visualization | Why It May Be Preferable |
|---|---|---|
| Compare many categories | Bar chart | Bars are easier to compare than arcs when there are more than 6 categories. |
| Show change over time | Line chart or stacked area chart | Time is shown along an axis instead of across separate donuts. |
| Compare parts of a whole across groups | Stacked bar chart | Groups line up on a shared scale, so differences are easier to see. |
| Show exact values | Table | Readers can read each number directly. |

## Data Requirements and Statistical Considerations

* Categories must be mutually exclusive.
* Ensure that the values of the slices total to 100%. If rounding makes the total 99% or 101%, add a note that explains it.
* State the measure, units, geographic area, and reference period.
* For survey estimates, such as American Community Survey data, report margins of error in a note or data table.
* Explain how missing, suppressed, or combined categories are handled.

## Visualization-Specific Considerations

In addition to the guidance provided in this section, relevant guidance can also be found in the Agency Logo, Axes, Colors, Grids, Legends, Source, Titles, Typography sections.

* Include a legend or label slices directly.
* Never use three-dimensional (3D) graphics, as they distort the visual calculation of volume.
* Use contrasting colors to ensure the wedges stand out. Consider using heavy outlining to make each wedge stand out.
* Limit the number of categories/arcs to no more than 6.
* Comparisons of more than 2 donut charts is ok if only two categories are shown. Use two or more donut charts to compare against each other only when each donut chart has 3 or fewer categories. The human eye is poor at comparing multiple lengths at once. Instead, use stacked bar charts.
* Don't include large gaps between each slice, such as in an exploded pie chart. This distorts the perceived sizes of the pie slices.
* Do not nest donut charts within each other. In the example below, the eyes assess the arc sizes and determine that one is bigger than the other. The brain must then dismiss what the eyes saw and process that they are the same: both are 9%.

![Nested donut chart from the 2023 Deloitte Digital Citizen Survey on change in use of government digital services. The inner ring, since the beginning of the pandemic, shows 55 percent increased, 36 percent stayed the same, and 9 percent decreased. The outer ring, in the new normal, shows 57 percent increased, 34 percent stayed the same, and 9 percent decreased. The two 9 percent arcs are highlighted because they look like different sizes even though they are equal.](assets/Donutchart1.png)

## Accessibility
 
* Write alt text that states the main part-to-whole takeaway, including the center total if that number is part of the message, rather than only naming the chart type.
* Provide the values in a data table or an equivalent text format. This is especially important when two donuts are shown side by side, because comparing arc lengths is difficult.
* Label each arc with the category and value (or percent). Don't rely on color alone to identify slices, and don't nest rings that make equal shares look like different sizes.
* Keep text, including any label in the hole, at a contrast of at least 4.5:1 against its background. Keep arc fills or outlines at least 3:1 against the background and against neighboring arcs.
* For full requirements, see the [508 Compliance](508.html) and [Color](color.html) pages. Meeting these bullets does not by itself mean a chart is 508 compliant.

## Census Data Example

***Example 1:*** Percent Shares of U.S. beef export markets in 2022.

![Donut chart of percent shares of U.S. beef export markets in 2022. Total beef exports were 3.54 billion pounds. Japan 23 percent, South Korea 23 percent, China 18 percent, Mexico 8 percent, Canada 8 percent, and others 21 percent. Shares add to 101 percent because of rounding.](assets/Donutchart2.png)

The original chart can be found at: https://www.ers.usda.gov/data-products/chart-gallery/gallery/chart-detail/?chartId=107281

This chart demonstrates the following well:

* Sections of the donut chart are clearly labeled.
* The sections of the donut chart add up to 101 instead of 100 due to rounding, and a note explaining this is included.

***Example 2:*** 2017 State & Local Governments Combined Expenditure

![Two donut charts of 2017 state and local government spending by category: the U.S. total of $3.3 trillion and Alabama's $45.0 billion. Arcs are colored by category, such as education, health and welfare, and transportation, with a color legend below.](assets/Donutchart3.png)

The full dashboard can be found at: https://www.census.gov/library/visualizations/interactive/state-local-snapshot.html

This example demonstrates the following well:

* A legend is included to identify all the pieces of the donut chart.

This example could use the following improvements:

* Two donut charts are shown side by side with more than 2 categories being represented in each. It is difficult for the reader to understand the differences between the two charts, and these values may be better displayed in bar charts or a table with values clearly labeled for each category.

## Developer Implementation

A reproducible Python example using U.S. Census Bureau data will be added in a later update.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Nested donut charts | Readers compare arcs on different rings and misjudge their sizes. | Use one donut, or a stacked bar chart. |
| 3D effects | Tilting distorts the arc lengths. | Use a flat, two-dimensional chart. |
| Too many categories | Small arcs become hard to tell apart. | Keep to 6 or fewer, or use a bar chart. |
| Slices that do not total 100% | Readers may think data is missing. | Add a note about rounding or missing categories. |
| Color as the only label | Readers with color blindness cannot match arcs to the legend. | Label arcs directly or add patterns and outlines. |

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
 
* [Pie Chart](piechart.html): the same part-to-whole method without a center hole, including when to avoid comparing many pies.
* [Stacked Bar Chart](stackedbarchart.html): a clearer way to compare composition across several groups.
* [Bar Chart](barchart.html): a better choice when readers need to compare category sizes precisely.
* [Color](color.html): contrast and color-vision guidance for arcs and center labels.
* [508 Compliance](508.html): general accessibility requirements for charts and text.
