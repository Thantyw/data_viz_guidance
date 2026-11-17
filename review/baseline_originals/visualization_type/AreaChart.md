---
layout: default
title: Area Chart
permalink: areachart.html
tags: [Distribution]
description: "Short Description of Area Chart"
---

# Area Chart 

Area charts combine elements from a line chart and a bar chart to show changes in quantities over time. Like a line graph, area charts have a series of data points connected by line segments. But in area charts the space between the x-axis and each line in the graph is filled with color. The x-axis can display continuous or ordinal data such as days, years, or percentile groups and the y-axis is typically a continuous variable but can also be ordinal.  In either case, data on the y axis must allow for 0. 

Area charts transform the purpose of the line graph from simply showing relative change over time to also showing volume or quantity. The shading helps to emphasize which group has the largest value based on which group’s color is visible. Area charts are useful when showing data that have significant variation among series/lines and change over time and where the purpose of the plot is to show overall trends rather than individual values.  Nonetheless, there is a risk of area charts getting very cluttered when more series overlap. Like a pie chart or bubble chart, judging relative areas might be difficult in area charts. 

Area graphs can also be useful in a small-multiple chart (See Small Multiple Chart Page). Instead of overlapping them all on one graph, you can display each of them as a small, single graph in a regularly ordered series of similar charts.  This can help compare quantity and change-over-time across the panels without the need of overlapping areas. This is useful with handline many series that overlap. 

## Best Practices 

### Essential 

* The y-axis must start at zero. 
* High contrast colors/greyscale should always be used—see the categorical color guidance. 
* Order the series if the categories are ordinal. 

### Avoid

* Do not use area charts where the dimensions being measured have no relationship to zero. 

## Additional Recommendations 

### Recommended 

* Consider grouping smaller series to limit the number of series so that the main trends become more apparent. 
* Use transparency where areas overlap, and important information is hidden behind another layer. 
* Place highly variable data on the top of the chart and low variability on the bottom. 
* Keep the number of overlapping areas at a single point to three to four.  
* If the number of overlapping areas at a single point is greater than four, use an interactive plot or a static, small-multiple chart if there are more series. 
* Use a line plot instead of an area chart when there is one series and no comparisons are being made to other plots, like in a small-multiple plot or a marginal plot (See the examples). 

### Not recommended 

* Area charts are not recommended for showing volatile data over times or when differences are very small. 
* If the data on the x axis is categorical, an area chart is not ideal. Instead, consider using a bar chart.

## Examples

 ***Example 1.*** Estimated and Projected World Population by Age Group: 2010-2060 

![Area Plot 1](assets/areaplot1.jpeg)

 Source: U.S. Census Bureau https://www.census.gov/library/stories/2023/11/world-population-estimated-eight-billion.html

* The graph includes zero and uses high contrast colors to distinguish the different groups being represented.   
* The groups are displayed logically using ascending age groupings and the data are not volatile.

***Example 2:*** FRED Real Median Household Income and Real Median Family Income 

![Area Plot 2](assets/areaplot2.png)

Source: FRED https://fred.stlouisfed.org/series/MEHOINUSA672N#

* The graph includes zero and uses high contrast colors to distinguish the different groups being represented.
* Transparency used when areas overlap to show 'hidden' values

