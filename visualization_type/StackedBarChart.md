---
layout: default
title: Stacked Bar Chart
permalink: stackedbarchart.html
tags: [Comparison]
description: "Use stacked bar charts to compare category totals and show how subgroups contribute to each category, including part-to-whole comparisons."
---

# Stacked Bar Chart

**Also known as:** stacked bar graph

## Purpose and Overview

A stacked bar chart is a type of bar chart that displays categorical data using rectangular bars whose length or height corresponds to the value of each category. Each bar is divided into segments that represent subgroups within the main category.

Stacked bar charts can display subgroup information using whole-number values or percentages that do not necessarily sum to 100%, or as percentages of a whole in a 100% stacked bar chart.

In a standard stacked bar chart, the total length of each bar represents the total value of the main category, while the length of each segment represents the value of its subgroup. In a 100% stacked bar chart, every bar has the same overall length and the segments represent each subgroup's proportional contribution to the whole.

## When to Use

Use a stacked bar chart when the analytical objective is to compare categories while also showing subgroup composition.

Stacked bar charts are particularly useful for showing large differences in subgroup composition or providing a high-level view of part-to-whole relationships across categories.

A 100% stacked bar chart is useful when relative composition is more important than differences in total magnitude.

Stacked bar charts are less effective for communicating small or subtle differences among subgroup values because only the subgroup closest to the baseline has a common baseline across categories. As the number of subgroups increases, comparisons become more difficult.

If one subgroup is the primary focus of the analysis, place that subgroup closest to the baseline so differences can be interpreted more easily.

### Essential

- Bars must start at the zero origin. The heights or lengths of the categories and subgroups are proportional to the values they represent. A nonzero baseline can mislead the viewer's assessment of differences between values.
- Include a legend or use direct labels so readers can identify the subgroups.
- If categories are ordinal, preserve their natural order within the display.
- Order subgroups consistently across categories.
- Maintain an even amount of space between bars unless the axis represents dates. When using dates, spacing should accurately reflect the time intervals; for example, a missing year should result in a proportional gap.

### Avoid

- Avoid using a stacked bar chart when precise comparison of several subgroup values across categories is the primary analytical objective.
- Avoid excessive numbers of subgroups that make individual segments difficult to identify and compare.
- Avoid changing the order of subgroup segments from one category to another.

## When to Use an Alternative

Consider a regular **bar chart** or grouped bar chart when accurate comparison of individual subgroup values is more important than showing part-to-whole composition.

Consider a **table** when readers need exact values for many categories and subgroups.

Consider another visualization or multiple coordinated charts when the number of subgroups makes the stacked display difficult to interpret.

If the analytical objective is to compare relative composition rather than total values, a **100% stacked bar chart** may be preferable to a standard stacked bar chart.

## Additional Recommendations

### Recommended

- Use analytical reasoning to determine the order of subgroup categories.
- If the primary focus is on one subgroup compared with the remaining subgroups, place the subgroup of interest closest to the baseline to facilitate comparison.
- Use a sequential color scheme when subgroups have a meaningful order.
- Use a qualitative color scheme when subgroups do not have an inherent order.
- Use a diverging color scheme when the data have a meaningful midpoint and the graduated color scheme supports interpretation.
- Ensure that text size and emphasis support interpretation of the chart.
- Keep subgroup ordering consistent across all bars.

### Not Recommended

- Do not order subgroups alphabetically by default unless alphabetical order serves the analytical purpose.
- Use caution when displaying more than five subgroups for each category. If many subcategories are required, consider whether another visualization would communicate the information more clearly.

## Choosing Between Alternatives

| Analytical Goal | Alternative Visualization | Why It May Be Preferable |
|---|---|---|
| Compare individual category values | Bar Chart | Provides a common baseline that supports more precise comparisons. |
| Compare individual subgroup values across categories | Grouped Bar Chart | Places comparable values on a common baseline instead of stacking them. |
| Compare proportional composition across categories | 100% Stacked Bar Chart | Standardizes each category to 100%, emphasizing relative composition. |
| Present exact category and subgroup values | Table | Allows readers to look up and compare precise numerical values directly. |

## Data Requirements and Statistical Considerations

> **TODO (Phase 2):** Complete during individual enhancement work using applicable Census Bureau data and statistical guidance.

Future development of this section should address category and subgroup definitions, measurement units, geographic level and reference period, aggregation and denominators, missing or suppressed values, margins of error and uncertainty where applicable, and comparability across groups, geographies, or time periods.

## Visualization-Specific Considerations

The effectiveness of a stacked bar chart depends on both the number and ordering of subgroups. Segments farther from the baseline are more difficult to compare because they do not share a common starting position.

When subgroup comparison is the primary analytical objective, place the most important subgroup closest to the baseline or consider an alternative visualization.

For 100% stacked bar charts, the emphasis is on proportional composition rather than differences in total magnitude. The distinction between standard and 100% stacked bars should therefore be clear to readers.

Relevant component guidance should also be consulted for axes, color, grids, legends, sources, titles, and typography.

## Accessibility

- **Alt text:** Describe the primary comparison, composition, or takeaway rather than simply identifying the image as a "stacked bar chart."
- **Data table alternative:** Provide the underlying category and subgroup values in an accessible table or downloadable format when appropriate.
- **Do not rely on color alone:** Use direct labels, patterns, annotations, or other visual cues where necessary so subgroup meaning does not depend solely on color.
- Ensure that legends or direct labels clearly associate each subgroup with its corresponding segment.
- See [508 Compliance](508.html) and [Color](color.html) for general accessibility guidance.

## Census Data Example

> **TODO (Phase 2):** Add or validate an example using public Census Bureau data.

The future example should identify the analytical question, Census dataset and table, geography, reference period, measures and units, reason for selecting a stacked bar chart, and relevant limitations.

## Developer Implementation

> **TODO (Phase 2):** Add reproducible implementation guidance and code examples.

Future implementation guidance may include data preparation and reproducible Python and R examples, with documentation explaining how developers can adapt the examples to other Census datasets or geographic levels.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Too many subgroups | Makes individual segments difficult to distinguish and compare. | Reduce the number of subgroups or consider another visualization. |
| Inconsistent subgroup order | Makes comparisons across categories more difficult. | Maintain the same subgroup order across all bars. |
| Comparing segments without a common baseline | Can make small differences difficult to judge accurately. | Place the subgroup of interest closest to the baseline or use a grouped bar chart. |
| Nonzero baseline | Can visually exaggerate differences in bar or segment lengths. | Start stacked bars at zero. |
| Missing subgroup without explanation | May cause readers to interpret missing data as zero. | Add a note explaining missing, unavailable, or suppressed values. |
| Excessive or inappropriate color | Makes subgroup identification and interpretation more difficult. | Use an appropriate color scheme and maintain consistent subgroup encoding. |

## Publication Quality Checklist

- [ ] A stacked bar chart is appropriate for the analytical question.
- [ ] Bars begin at zero.
- [ ] Categories and subgroups are clearly defined.
- [ ] Subgroup order is consistent across categories.
- [ ] The number of subgroups remains interpretable.
- [ ] The subgroup of greatest analytical importance is positioned appropriately.
- [ ] A legend or direct labels identify all subgroups.
- [ ] Missing or suppressed values are documented where applicable.
- [ ] Color is used purposefully and is not the only means of communicating subgroup meaning.
- [ ] Relevant accessibility guidance has been followed.
- [ ] Data source, geography, reference period, and units are documented where applicable.
- [ ] Relevant limitations and statistical uncertainty are addressed where applicable.
- [ ] Related component guidance has been reviewed.

## Examples

### Example 1: Employed Parents by Full-time/Part-Time Status, Sex and Age of Youngest Child

![100% stacked bar chart comparing employment status of mothers and fathers by age of youngest child](assets/StackedBar1.png)

This chart is a good example of the following:

- The bars are ordered in an analytical manner for mothers and fathers, with the labels for mothers and fathers displayed prominently.
- A limited number of categories within each bar makes the information easier to interpret.
- A qualitative color scheme is appropriate for the categories shown.
- This is an example of a 100% stacked bar chart.

### Example 2: Family Groups, 2023

![Stacked bar chart showing family groups in 2023](assets/StackedBar2.png)

This chart is similar to Example 3. The two examples demonstrate different ways of displaying the same information. Of the two, Example 3's 100% stacked bar chart is preferred when the analytical objective is to compare subgroup composition across categories.

### Example 3: Family Groups, 2023 — 100% Stacked Bar

![100% stacked bar chart showing the composition of family groups in 2023](assets/StackedBar3.png)

The 100% stacked bar chart makes proportional differences among categories easier to compare than the standard stacked bar chart in Example 2.

One subgroup estimate is missing for the married same-sex couple subgroup within the Black alone category.

**Notes on Examples 2 and 3**

- These charts contain many categories, which makes some of the information difficult to interpret. Consider reducing the number of categories when the analytical objective permits.
- A note should explain why the estimate is missing for the Black alone category. For example, the note could indicate when an estimate is unavailable because of applicable statistical quality or suppression requirements.
- The bars and subgroup categories are identified using a legend.
- A qualitative color scheme is appropriate for the categories represented.
- Of the two displays, the 100% stacked bar chart is preferred when the objective is to compare proportional subgroup composition, although both charts could be improved.

## Related Pages

- [Bar Chart](barchart.html): use when the primary objective is to compare category values without displaying subgroup composition.
- [Tables](table.html): use when exact category and subgroup values are the primary requirement.
- [Axes](axes.html): guidance for axis labels, scales, and tick marks.
- [Typography](typography.html): guidance for readable labels and text.
- [Comparing Data and Values](comparison.html): guidance for designing accurate comparisons.
- [508 Compliance](508.html): general accessibility requirements.
- [Color](color.html): guidance for appropriate and accessible use of color.
