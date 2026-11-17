---
layout: default
title: Nested or Non-Mutually Exclusive Categories 
permalink: nested.html
tags: [Comparison,Distribution]
description: "Short Description of Nested or Non-Mutually Exclusive Categories"
---

# Nested or Non-Mutually Exclusive Categories

Converting data with nested and mutually exclusive categories into charts can be complex. 

Tables use visual clues such as the indentation of the variables to cue the viewer that these items are breakouts of the row they are indented from. Table notes are used to flag variables that are not mutually exclusive, but notes can be confusing as viewers often overlook notes and/or notes are not the default to display. Depending on the audience, it can be appropriate to present non-mutually exclusive data in table.

Charts do not have an obvious solution for mutually non-exclusive categories and require additional components to ensure the viewer understands the complex relationships.

## Guidance  

## Best Practices 

### Essential 

* When displaying categories that are non-mutually exclusive, always state which categories are not mutually exclusive in the notes, title, subtitle, or legend.


### Avoid

      
 
## Additional Recommendations 

### Recommended  

* Break out the data into mutually exclusive categories so your totals add up to 100%, 
* Be as explicit as possible in showing where categories represent parts of a whole and where categories have overlap.
* For overlapping categories (non-mutually exclusive, people/items can be counted in multiple categories) use remainder bars
* Use several charts to help users understand they are viewing nested data.
* Use a table. Visualization charts and graphics are not always the best way to view statistics.


### Not Recommended  


## Examples 

***Example 1:*** Table Excerpt from Heath Insurance Coverage in the United States 2022

![Nested Categories 1](assets/Nested1.png)

Health insurance data has both nested and non-mutually exclusive categories characteristics. Whether or not one has health insurance is binary, but the categories for displaying types of health insurance are not mutually exclusive. In a given year, people can, and do, have both public and private insurance, and within the those plans they can take advantage of several options. Theoretically, a single person with health insurance could be counted in all of the insured categories. 

***Example 2:*** Chart Excerpt from Heath Insurance Coverage in the United States 2022

![Nested Categories 2](assets/Nested2.jpg)

The left-hand bar charts describe the percentages of people who have insurance and the types of insurance one has. 

There are several visual miscues in Example 2 that contribute to the likelihood of misinterpreting these results. 
* The first bar plot's color and font scheme create a visual inconsistency. While the bolder top bar and lighter subsequent bars in the second and third bar plots correctly imply that the lighter categories are subgroups of the top bolded category, this visual cue is misleading in the first chart.
* The viewer needs to perform math to see that the subgroups in the second and third bar plot do not add to 100%.
* The note stating that these are not mutually exclusive is easy to miss, it is buried beneath the chart among a series of notes. Obviously good charts aspire to be visually clean and the desire to keep the notes small makes sense. But in this case, even bolding that note would increase the chance that it gets read. 
* It’s not entirely clear if the statistics in the second two charts are percents of the entire population or percents of those with insurance. One may conclude that 66% of those with insurance have a private insurance plan, or that 66% of people have a private insurance plan. Again, the nesting in the table allows the viewer to understand that 66% of people have a private insurance plan.
The visualization approach used in Example 2 is acceptable, but not ideal. A simple fix could be to use a stacked bar chart for the first statistic (uninsured vs insured) clearly showing they add up to 100%. Because there are only 2 categories, the stacked bar chart should be easily interpretable and a clear “parts of a whole” depiction. Additionally bolding the chart note could help increase the clarity. 
Handling non-mutually exclusive categories is a common struggle when determining how to depict your data visually. Here are some charts that get increasingly more difficult to interpret and ultimately lead to a very complex task for the viewer. The complexities here need to be avoided. Always consider how long it takes for a viewer to understand the message in your visualization. If you find it takes enormous amounts of mental concentration, explore simpler solutions or a less complex story. If you cannot find a solution, avoid presenting an overly complex chart. Remember, it’s ok and maybe preferable in many cases to use a TABLE.


***Example 3:*** [Most Parents Don’t Have Any Formal Child Care Arrangements](https://www.census.gov/library/stories/2023/11/child-care.html)

![Nested Categories 3](assets/Nested3.png)

Example 3 displays non-mutually exclusive categories through a series of bar charts known as “remainder bars.” Remainder bars show not just the individual statistic, but the remainder of the universe for that statistic. Remainder bars help users understand the parts of a whole and make it easier to see that these individual categories are not mutually exclusive. 

