---
layout: default
title: Axes 
permalink: axes.html
description: "Best practices for designing and labeling chart axes to improve readability, accuracy, and interpretation of data visualizations."
---

# Axes

Axes provide vital reference information for users to associate data points with values, especially when data points are not labeled directly in a chart.

Typically, data visualizations (graphs, charts) contain two axes: an x-axis (horizontal) and a y-axis (vertical). (Note that some line graphs could have a third z-axis.) Other types of visualizations that should include axes are bar charts, dual axes, scatter plots, and line graphs.

Bar charts are used for categorical (discrete) data. The horizontal axis indicates the group/category, and the vertical axis (height of the bar) is proportional to the value (frequency) of the corresponding category. Note that this describes a horizontal bar chart, and the axes are flipped for vertical bar charts. 

The axes in line graphs and scatter plots represent continuous values (e.g., time, age), while the other axis is used to map a data point against that value (e.g. a percentage, dollar amount, or integer). 

Axes are not always necessary or possible in data visualizations but should be considered for use by default. For example, if the information normally included in an axis label is conveyed in the title, then an axis label is not needed. When using data labels, you might be able to omit the axis information. 

## Axes Titles or Labels

Axes should be clearly labeled so viewers understand what is being displayed. Axis labels should provide helpful contextual information about the tick marks of a given axis, such as the unit of measurement. When axis labels are used in conjunction with titles and subtitles, users will be able to more easily understand what a visualization is about. See appropriate section (bars, etc.)

## Scales

Axes should have scales associated with them. A scale in this section refers to a ruler by which we measure or convey the data in the graph. A scale in visualizations could also mean the number of units per distance measure or the proportions of a map to the original geographic area on maps. When creating data visualizations that are designed to be compared, as in small multiples , always use consistent axes.

## Tick Marks

Tick marks are used to indicate a reference value at a given point in a chart. Tick marks function similar to the lines on a ruler. Not all tick marks need to be labeled, but they do need to establish a continuous interval by ensuring the number of tick marks between each labeled tick mark is always the same.

When using tick marks, try not to label too many elements or use too many marks along an axis. If tick marks appear cluttered, users will not be able to determine the value of various data points.

The spacing between tick marks on an axis should be equal. 

## Guidance  

## Best Practices 

### Essential 

* Label each axis.
*	Be consistent in how you label tick marks.
*	Use consistent axes for data visualizations that are being compared.
*	Never use dual-axes plots, unless it is for showing alternative scales (e.g., temperature) or a Pareto chart. 
*	Include zero in bar charts.

### Avoid

## Additional Recommendations 

### Recommended  

* Include zero depending on the goal of the visualization, the audience, and clarity. 
*	Add the unit of measurement to the axis title (i.e. “Percentage of Voters”), if relevant.
*	Reduce clutter by not labeling every tick mark.
*	Use different size tick marks (like a ruler) when not labeling each tick mark, i.e. use a longer tick mark for every 5th mark.

### Not Recommended  


## Examples 

***Example 1:***

![Axes 1](assets/axes01.png)

### Why it’s Only Acceptable

The axis title missed an opportunity to include the unit of measurement for the tick marks in the y-axis. As a result, the tick marks include a percentage symbol after each labeled tick and the title isn’t that useful.

***Example 2:*** 

![Axes 2](assets/axes02.png)

### Why it’s Better

Now that the title features the unit of measurement, the tick marks no longer need a percentage symbol. The title also makes it easier for users to understand what the visualization is about as a result.
