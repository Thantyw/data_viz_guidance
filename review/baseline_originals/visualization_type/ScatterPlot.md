---
layout: default
title: Scatter Plot
permalink: scatterplot.html
tags: [Correlation,Distribution]
description: "Short Description of Scatter Plot"
---

# Scatter Plot


Also known as: scatterplot, scatter graph, scatter chart, scattergram, scatter diagram

See Also: Bubble Chart.

A scatter plot is a two-dimensional chart that shows the relationship between two numeric variables, X and Y.  It may also show a third dimension by using differing color or data point markers but the main purpose of the graph is to show the relationship between the two dimensions. The scatter plot is similar to a bubble chart which allows the relationship between three numeric variables to be plotted by using the x-axis, y-axis and the size of the data point marker or bubble.

Each data point within the scatter plot represents a single observation found at Cartesian coordinates (x,y).  When the data points are plotted against these two axes, scatter plots communicate the strength and type of relationship that exists between these variables.

Often, a scatter plot is used to show the results of a regression analysis and will include a line from the predicted values of Y for a given value of X, as seen in the example 1.

## Guidance

In addition to the guidance provided in this section, relevant guidance can also be found in the Agency Logo, Axes, Colors, Grids, Legends, Source, Titles, Typography sections.

### Essential

* Ensure the units of analysis and variables being plotted are explained in the title of the chart or axes labels.

### Avoid

* For static visualizations, never overlap labels for data points.
*	Never use symbols for data point markers that do not have a proportionate width and height.
  *	A symbol that has an equal width and height is a more accurate way to present a given data value.


## Additional Recommendations

### Recommended
*	Include point labels or point markers for specific observations (See Example 3).
*	Use jittering, data point transparency, sampled data, or other mitigation strategy to avoid overlapping data points (See Wilke, 2019).  Mention the mitigation strategy being used within the chart footnotes, labels or chart description.
  
### Not Recommended

*	Don’t use a scatter plot if there are an excessive number of overlapping data points. 

## Examples

***Example 1:*** Percent Labor Force Covered by Public Pensions vs Percent of Former Wages Replaced by Pensions in Select Asian Countries.

![Scatter Plot 1](assets/ScatterPlot1.png)

In Example 1 we notice the following consistencies with our standards:
* The variables and units of analysis are explained in the title of the graph.
* Labels are being used for specific observations and the labels do not overlap point markers.
* Circles are being used as point markers, which are proportional in height and width.
* There is not an excessive number of observations.


***Example 2:*** Median Estimated Earnings by Sex and Occupation

![Scatter Plot 2](assets/ScatterPlot2.png)

This plot is a good example of the following:
* The units of analysis on this dashboard scatter plot are clearly identified as dollars using the dollar signs in front of the axis labels.
* The symbol used for each data point is a circle.


***Example 3:*** Uninsured Rate in 2013 and Change from 2013 to 2014 for Occupations

![Scatter Plot 3](assets/ScatterPlot3.png)

This plot is a good example of the following:
*	The data is represented using circles that are shaded in two different colors.  
*	The colors are defined in a legend on the graph.
*	Units of analysis are clearly defined in the axis labels. 
*	All labels do not interfere with the data points on the graph using leader lines to connect the label to each data point being identified.
