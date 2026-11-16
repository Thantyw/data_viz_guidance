---
layout: default
title: Sankey Diagram
permalink: sankeydiagram.html
tags: [Distribution]
description: "A Sankey diagram shows how amounts flow from one stage or group to another."
---

# Sankey Diagram

**Also known as:** Parallel sets, Alluvial chart, Flow diagram

## Purpose and Overview

A Sankey diagram is a flow chart that shows how data flows and changes from one stage to the next. Entities (nodes) are shown as rectangular bars whose height represents their value. Links show the connection (flow) between two nodes, and each flow's width is proportional to its size.

Sankey diagrams usually have two parallel sets of nodes. Alluvial charts have more than two parallel sets of nodes and show how data flows and changes through multiple stages.

## When to Use

Sankey diagrams show how data moves across stages. Use them to show change, not comparison.

Use a Sankey diagram when:

* You want to show where amounts come from and where they go, such as graduates moving from degree programs into industries.
* The data moves through two or more stages, and each stage splits or combines amounts.
* The total amount is kept from one stage to the next, so the flows add up on each side.
* Readers need to see the largest flows and how groups shift between stages.

## When to Use an Alternative

* Sankey diagrams are not recommended for comparisons between different metrics.
* If all links have similar widths, consider a stacked bar chart or another alternative.
* Avoid Sankey diagrams when there are many nodes and flows. Complexity can quickly make large changes hard to interpret.
* Avoid Sankey diagrams when readers need exact values. Flow widths are hard to compare precisely.

## Choosing Between Alternatives

| Analytical Goal | Alternative Visualization | Why It May Be Preferable |
|---|---|---|
| Compare values across groups | Bar chart or dot plot | Lengths and positions on a shared axis are easier to compare than flow widths. |
| Compare the makeup of several groups | Stacked bar chart or proportion plot | Shows each group's parts side by side without crossing flows. |
| Compare many measures for each item | Parallel coordinate plot | Shows several measures at once without needing flows that add up. |
| Show parts of one whole at a single stage | Pie, donut, or treemap | Simpler when there is no movement between stages. |
| Show exact values | Table | Readers can read each number directly. |

## Data Requirements and Statistical Considerations

* The data needs a source group, a destination group, and an amount for each flow.
* Amounts must be zero or positive, and flows into a node should equal flows out of it, unless the difference is explained.
* State the measure, units, geographic area, and reference period.
* For survey estimates, report margins of error in a note or data table.
* Explain how small, suppressed, or combined categories are handled, such as an "Other" category.

## Visualization-Specific Considerations

In addition to the guidance provided in this section, relevant guidance can also be found in the Agency Logo, Colors, Source, Titles, and Typography sections.

* The width of flows must be proportional to the quantity it represents.
* Keep the number of crossings between flows as low as possible.
* Collapse smaller nodes or make an "Other" category to avoid clutter.
* For static Sankey diagrams, limit the number of nodes. If the diagram has many nodes and flows, consider an interactive version that highlights flows on hover. Interactive versions should still provide a data table.
* Use qualitative colors for nodes or to show groupings of nodes.
* If using color for flows, alternate colors to keep high contrast, or outline flows so readers can follow each one from one side to the other.
* When flows of the same color cross, use a darker color for the intersection.
* Label nodes directly with text so color is not the only way to identify them.

## Accessibility
 
* Write alt text that states the main flow or transfer takeaway (what moves from where to where, and the scale), not only that the image is a Sankey diagram.
* Provide a data table of the flows, with source, target, and value, so readers do not have to trace bands to recover the numbers.
* Label nodes directly. Color can group nodes or distinguish flows, but it should not be the only way to identify them. When flows of the same color cross, use an outline or a darker intersection so each path stays easy to follow.
* Keep node and flow labels at a contrast of at least 4.5:1 against their background. Keep flow fills or outlines at least 3:1 against the background so bands remain visible.
* If hover highlighting is used to trace a flow, do not make hover the only way to read that path. For full requirements, see the [508 Compliance](508.html) and [Color](color.html) pages. Meeting these bullets does not by itself mean a chart is 508 compliant.
 

## Census Data Example

***Example 1:*** Post-Secondary Employment Outcomes Explorer

![Sankey diagram from the Census Bureau's Post-Secondary Employment Outcomes Explorer showing where master's graduates from three selected programs at the University of Virginia end up, for all graduation cohorts. On the left, the three selected program bars show each program's share of graduates in that selection: Engineering 67 percent, Social Sciences 21 percent, and Mathematics and Statistics 12 percent. Gray flows run from each program to two outcomes on the right: Employed, 51 percent, and No or very low earnings observed, 49 percent.](assets/SankeyDiagram1.png)

Full visualization can be found at [Post-Secondary Employment Outcomes Explorer](https://lehd.ces.census.gov/applications/pseo/?type=flows&specificity=2&state=51&institution=00374500&degreelevel=07&gradcohort=0000-5&filter=1&display=share&program=45,14,27&destination=none)

Note: The screenshot reflects an earlier PSEO data release (2021–2023). In the current release (2026Q2), the same selection shows Engineering 65 percent, Social Sciences 18 percent, and Mathematics and Statistics 17 percent, with 53 percent Employed and 47 percent No or very low earnings observed, so the live explorer will not match the screenshot.

This chart is a good example of the following:

* The chart is not cluttered, with only two flows crossing over the other flows.
* The crossover points use shading to show where flows of the same color intersect.
* The original is an interactive chart that highlights flows on hover, which helps readers understand the diagram.

***Example 2:*** United States Energy-related Carbon Dioxide Emissions in 2021: 4,863 million metric tons (Lawrence Livermore National Laboratory and U.S. Department of Energy, not Census Bureau data)

![Sankey diagram from Lawrence Livermore National Laboratory showing U.S. energy-related carbon dioxide emissions in 2021, totaling 4,863 million metric tons. Colored flows run from energy sources on the left, mainly petroleum at 2,223, natural gas at 1,637, and coal at 1,003, either directly to end-use sectors or through electricity generation (1,537). The end-use sectors are transportation at 1,801, industrial at 965, residential at 321, and commercial at 239. Those four sectors plus electricity generation add to 4,863. Gray flows then join to form total carbon dioxide emissions on the right. Solar, nuclear, hydro, wind, geothermal, and biomass show 0.](assets/SankeyDiagram2.png)

Full visualization can be found at [Annual Energy and Carbon Flow Charts](https://flowcharts.llnl.gov/commodities/carbon)

This chart is a good example of the following:

* Each flow has a different color, which helps readers see where each flow comes from and read the crossover points.

## Developer Implementation

A reproducible Python example using U.S. Census Bureau data will be added in a later update.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Flow widths not proportional to values | Readers see the wrong size for each flow. | Scale every flow width to its value. |
| Too many nodes and crossing flows | The diagram becomes hard to follow. | Combine small nodes into "Other," or make it interactive. |
| Flows in and out of a node do not match | Readers may think data was lost or added. | Balance the totals or explain the difference in a note. |
| Using a Sankey to compare different metrics | Flows imply movement that does not exist. | Use a bar chart or dot plot. |
| Color as the only way to identify nodes | Readers with color blindness cannot match flows. | Add direct text labels on nodes. |

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
 
* [Stacked Bar Chart](stackedbarchart.html): a simpler way to show composition when the story does not depend on flows from one stage to another.
* [Interactive Chart](interactivechart.html): guidance if hover is used to highlight a flow; essential information should not live only in the hover.
* [Color](color.html): contrast and color-vision guidance for nodes and crossing flows.
* [Notes](note.html): how to explain selected programs, omitted flows, or other caveats.
* [508 Compliance](508.html): general accessibility requirements, including a data table of flows.
