---
layout: default
title: Legends 
permalink: legend.html
description: "Guidance for designing clear, consistent, and accessible legends that help users interpret data visualizations."
---

# Legends 

Legends identify the meaning of various elements in a data visualization and can be used as an alternative to labeling data directly. 

Legends are commonly used with data visualizations when there is more than one color or line type being used – most commonly in maps. By moving labels outside of a visualization, legends can help to reduce clutter and make your data visualization more user-friendly. 

Legends include a series of item markers with corresponding labels and can optionally include a title. When using legends, be sure to follow the guidance below. 

## Guidance  

In addition to the guidance provided in this section, relevant guidance can also be found in the Agency Logo, Colors, Choropleth Maps, Grids, Labels, Map Layout, Scale Bars, Source, Titles, and Typography sections.  

## Best Practices 

### Essential 

* Legends should be placed in a prominent location near the visualization without detracting from the visualization itself. They are commonly placed below or parallel to a data visualization; however, depending on the type of data being displayed and the available space surrounding the data visualization, placement above the visualization is also acceptable.
* Legend Placement Examples:

  ![Legend 01](assets/Legend01.png)

  ![Legend 02](assets/Legend02.png)

* A legend title is not always necessary. When it is included however, it should be descriptive and provide additional information not presented in the main title.  Instead of using a generic title like “Legend” or “Key,” try to use a title that captures the meaning of the data being labeled, such as “Population per square mile.”
* When using a vertical legend with sequential data, where values progress from low to high, ensure that the highest number appears first at the top of the legend and the lowest number appears last at the bottom of the legend. For diverging data, where values diverge away from a midpoint (e.g., increase, no change, decrease), a vertical legend is also recommended, with the most extreme values at the opposite ends of the legend.
* Always include a legend, unless the data are only one class or all the data are clearly labeled within the visualization. 
*	For quantitative data in a vertical legend, display numeric values in descending order (highest to lowest). For a horizontal legend, display highest to lowest from left to right.
*	Use sequential or diverging color scheme for numeric (quantitative) data. Use a categorical color scheme for non-numeric (qualitative) data.
*	Data values specified in the legend should match the precision of data used to create the visualization. For example, if the data are rounded to a tenth of a percent, the class descriptions in the legend should be rounded to a tenth of a percent.
*	The fill color of the legend swatch should match the colors in the map or chart. This includes if there is a transparency applied to the symbols. Note that background colors or basemaps may also change a color’s appearance. The legend swatch should be representative of how the color appears in the map or chart.
*	For qualitative data, if the data is visualized in a specific order, such as in a bar chart, list the legend in the same order. 
*	The data unit of measure must be identified on the visualization. Include the measure (e.g., dollars, percent) in the legend title or within class descriptions for legends without a title.
*	The unit of geography for which data are being mapped should be identified on the map. If not part of the main title, include the geographic unit in the legend title.
*	Keep legend elements grouped together on the page, so they appear as a legend unit. 

### Avoid

*	For survey data, never incorporate the national average/value/median into the legend display with the data class breaks. This is only acceptable when using data without sampling error, such as decennial census data.
    *	The national value can be included below the data classification section of the legend for additional context.
      
 
## Additional Recommendations 

### Recommended  

* Position the legend in available space so it does not distract from the visualization or the title. Preferred placement is below or parallel to a data visualization.
*	Organize the legend elements vertically, especially when showing quantitative data. If there are space considerations, horizontal legends may be acceptable.
*	Include a legend title that describes the data. 
*	For maps in a series (e.g., time series) that use a standard legend only shown once, include a note that specifies if a data class is not represented on a specific map. 
*	On individual maps, especially in interactive visualizations with multiple geographic levels (e.g., state, county, tract), make sure the correct classes are shown in the legend for what is shown on the map. Do not include classes not on the map.
  *	If a user can zoom to a smaller geography (e.g., counties within a single state), the assumption is that the legend still applies to the entire country. If the legend is being recalculated for the smaller geography (i.e., the range and distribution is only for counties within the single state), add a note or descriptive text.
*	For visualizations showing quantitative data, it is preferred that the ordinal legend swatches abut one another. However, if another category, such as “no data” is included, it should not touch the rest of the swatches. For qualitative data sets, it is preferred that the legend swatches do not touch each other. 
*	The legend title should be in initial caps. All categories of a legend should be in initial caps unless proper nouns or subject matter experts indicate otherwise.

### Not Recommended  


## Examples 

***Example 1:*** Choropleth map with quantitative (sequential) data and with a “no data” class

![Legend 03](assets/Legend03.png)

***Example 2:*** Choropleth map with a diverging data set. “Gain” and “Loss” are included in the description for the extreme values to help clarify the type of change

![Legend 04](assets/Legend04.png)

***Example 3:*** Choropleth map with a diverging data set and an integrated national value from 2020 Census data. (Avoid for survey data.) 

![Legend 05](assets/Legend05.png)
  
***Example 4:*** Choropleth map with diverging data set by state (identified in the main title). In addition to the state layer, the map includes Census Region boundaries. Additional notes also included. 
 
![Legend 06](assets/Legend06.png)

***Example 5:*** Choropleth map with diverging data expressing the state value as compared to national average. Values sorted with statistical significance must include a “*” in the legend title and a note about the confidence level for survey data above the source note. 
 
![Legend 07](assets/Legend07.png)

![Legend 19](assets/Legend19.png)

***Example 6:*** Proportional symbol map with two variables, where the circle size shows the total number of events and color fill illustrates the breakdown by year 
 
![Legend 08](assets/Legend08.png)

***Example 7:*** Graduated symbol map, with a color ramp fill to more clearly illustrate classified data
 
![Legend 09](assets/Legend09.png)

***Example 8:*** Qualitative choropleth map. The color swatches do not touch, as it is qualitative data.
 
![Legend 10](assets/Legend10.png)

***Example 9:*** Dot distribution map
 
![Legend 10](assets/Legend20.png)

***Example 10:*** Legends with items organized horizontally. In these examples, respectively, the legends list the classes in the order they are read in the chart (left to right), in the logical time order, and with the directionality of the visualization.
 
![Legend 11](assets/Legend11.png)

![Legend 12](assets/Legend12.png)

![Legend 13](assets/Legend13.png)

[Poverty in the United States: 2023](https://www2.census.gov/library/publications/2024/demo/p60-283.pdf)

***Example 11:*** Not recommended, but acceptable in limited cases. If there are no better options and the legend cannot graphically describe the classes, a text note may be used. In this example, it explains what the size of the circles means.
 
![Legend 14](assets/Legend14.png)

***Example 12:*** Not recommended: legend has classes with different precisions of data. Here, this also leaves the class for a data value of 0.95 undetermined.
 
![Legend 15](assets/Legend15.png)

[Demobase Angola and Namibia](https://www.census.gov/library/visualizations/time-series/demo/demobase-angola-and-namibia.html)

***Example 13:*** Not recommended: Overlapping class ranges. Cartographic convention would read these as classes “up to, but not including” the higher number (i.e., 40 is in the third class). However, this convention is not widely understood, so explicitly not including overlaps is highly preferred.
 
![Legend 16](assets/Legend16.png)

***Example 14:*** Not recommended: qualitative data using a quantitative color scheme. Here, the most common language spoken does not provide ordered meaning to the data, as this sequential color scheme would suggest. Instead, the languages are categorical and unordered and should use a qualitative color scheme.
 
![Legend 17](assets/Legend17.png)

***Example 15:*** Not recommended: quantitative data using a qualitative color scheme. Here, the classes are ordered. A qualitative color scheme implies the classes have no order or sequence.
 
![Legend 18](assets/Legend18.png)
