---
layout: default
title: Line Graph
permalink: linegraph.html
tags: [Distribution]
description: "Short Description of Line Graph"
---

# Line Graph

Also known as: line chart, line diagram, line plot, spaghetti plot

A line graph is a chart that displays a series of data points connected by line segments. A spaghetti plot is a line plot with many lines displayed together.
Line graphs can be used to show how data changes over time and are often used to communicate trends, such as how household income changes each year. The x-axis can display continuous or discrete data such as days, years, or categories, and the y-axis is typically a continuous variable but can also be discrete. Line graphs can also be used to compare multiple trend lines, whereas bar charts can only represent one trend line. A line graph emphasizes changes in value, rather than the magnitude of the values themselves.
When multiple lines are being displayed, we encourage the use of the interactive line graph which may be more effective.

## Guidance
In addition to the guidance provided in this section, relevant guidance can also be found in the [Agency Logo](https://xdgov.github.io/data-design-standards/components/agency-logo), [Axes](https://xdgov.github.io/data-design-standards/components/axes), [Colors](https://xdgov.github.io/data-design-standards/components/colors), [Grids](https://xdgov.github.io/data-design-standards/components/grids), [Legends](https://xdgov.github.io/data-design-standards/components/legends), [Source](https://xdgov.github.io/data-design-standards/components/source), [Titles](https://xdgov.github.io/data-design-standards/components/titles), [Typography](https://xdgov.github.io/data-design-standards/components/typography) sections.## Best Practices 

### Essential 

* Ensure that each line is legible.
* Only use color if there are 6 or fewer lines being displayed.
* When more than 1 line is shown, it should be clear what each line represents, whether through a legend, direct label, or hover feature.

### Avoid

* Never use a legend for a graph with a single line.
* Never connect dots with lines that are not in some natural ordering.
* Do not connect dots where there is a gap (e.g., missing data for certain years). Use a dotted line or gap instead.

## Additional Recommendations 

### Recommended 

* Y-axis should be scaled appropriately to show variation.
* Use an interactive plot when possible or when more than 6 or more lines are shown (e.g., 50 lines to show all US states).
o In the interactive plot, utilize the shade-out and highlighting on hover feature.
o Allow the selected line to be bolder and thicker while the other lines fade to a lighter shade. This allows the viewer to easily see the line of interest and compare the general trends.
* If the graph must be non-interactive, choose a small multiples graph with single lines highlighted.  (See the [Small Multiples Section](https://xdgov.github.io/data-design-standards/components/small-multiples))

## Examples

 ***Example 1.*** Line chart of the poverty rate and the number of people in poverty: 1959 to 2022.

![Area Plot 1](assets/LineGraph1.png)

This chart is a good example of the following:
* Color is being used with purpose and the meaning behind the color is shown through clear labeling of the chart. 
* Only one line is shown on each chart and the units of analysis are clearly identified on both.
* A gap is displayed where appropriate and is explained in the notes of the graph.

***Example 2:*** Line chart of Number of Children in Poverty by Supplemental Poverty Measure Components 

![Area Plot 2](assets/LineGraph2.png)

This graph is a good example of the following:
* Four lines are displayed with clear labels for each line along with labels for each data point on the line.  
* Definitions for the lines are provided in the notes section so there is no question as to what each line represent.
* Color is being used to distinguish the lines from each other.

***Example 3:*** National Median Monthly Rent Paid by Renter Households: 2017, 2019, 2021.  From SEHSD Working Paper Number FY 2024-15.

![Area Plot 3](assets/LineGraph3.png)

This graph is a good example of the following:
* A legend is used to define each line.
* Labels are used for each data point.
* Error bars are used for each data point and the notation is clearly defined in the notes of the chart.

***Example 4:*** Percentage of men using different types of leave in the 12 weeks after the birth of their first child, by year of birth 

![Area Plot 4](assets/LineGraph4.png)

This chart is a good example of the following:
* A legend clearly defines the lines being presented on the chart.
* Gridlines are used to help the reader interpret the values being displayed on the chart since the values within the lines are not labeled.
