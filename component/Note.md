Add Accessibility and Related Pages to Family D guidance pages.
 
Pie, Donut, Treemap, Sankey, and both Grid files get a short Accessibility section before the Census Data Example(s), without claiming 508 compliance. The Pie Chart Accessibility Review is kept as developer checks, and its "4.5 to 1" typo is fixed to "4.5:1". All pages in the set get Related Pages with existing permalinks. Component pages other than Grids get Related Pages only. The 508 page's Color sentence is now a real link. No shared layout, workflow, or JavaScript files are changed.
---
layout: default
title: Notes 
permalink: note.html
description: "How to use notes and captions to explain data visualization terms, context, limitations, and sources."
---

# Notes

## Purpose and Overview

Visualizations should be understandable on their own, even when embedded in a larger document, such as a working paper. Readers should be able to understand the main points without moving back and forth between the figure and the surrounding text.

Along with clear titles, subtitles, and axes, notes and captions provide:

* Clarity: Explain the meaning and intent of the visualization.
* Context: Supply background information needed to understand the data.
* Emphasis: Highlight important findings or qualifications.

Notes provide additional context, such as definitions of terms and symbols, information about the universe and sampling, and explanations of comparisons that are not statistically significant. Notes generally appear below the graphics within the visualization frame and begin with “Notes:”.

In some publications, captions provide a concise summary of the visualization and insights that may not be immediately apparent. Captions should be informative and understandable to readers unfamiliar with the subject. They appear directly below the visualization, outside its frame.

## When This Guidance Applies

Apply this guidance when a static or interactive visualization needs definitions, context, limitations, or other explanations beyond its title, axes, and legend.

In addition to this section, relevant guidance is in the 508 Compliance, Interactive Chart, Legends, and Titles sections.

## Essential Requirements

* In a static visualization, place notes at the bottom, either within the frame or adjacent to the graphic. Include only source statements below the notes.
* Place captions outside the visualization frame and adjacent to the visualization.
* In an interactive visualization, place notes at the bottom of the graphic or make them available through a clearly identified information button or pop-up. Use an accessible button with a descriptive name that can be operated with a keyboard; do not make notes available only on hover.

  Example information control:

  ![Information icon shown as a lowercase i inside a circle.](assets/Note3.png)

* Include DMS and DRB identifiers when required by the applicable review or publication process. Consult the Statistical Quality Standards and the requirements for the specific product.

## Recommended Practices

* Define jargon and symbols that are not explained in the legend.
* State the universe, meaning the population covered by the data, if it is not already clear from the title, legend, axes, or other nearby text.
* Explain relevant sampling information and statistical limitations.
* Identify comparisons that are not statistically significant when needed to prevent misinterpretation.
* Explain whether categories overlap when readers might otherwise assume that each observation belongs to only one category.
* Use plain language and include the details readers need to draw accurate conclusions.
* Keep notes close to the visualization and make them readable.
* Use a consistent source citation style. A recommended format is:

  Source: U.S. Census Bureau, [Program/Publication], [Page number], [Posted date/Date of source data], [Project No. ####### / Approval CBDRB-FY##-###], [URL or DOI], Accessed on [Date].

  Include the fields and identifiers that apply to the product.

## Practices to Avoid

* Do not leave technical terms or unexplained symbols for readers to interpret on their own.
* Do not omit information about the universe when its absence could change how readers interpret the data.
* Do not leave overlapping categories unexplained when readers might assume they are mutually exclusive.
* Do not hide essential qualifications in hover-only content.
* Do not make readers search the surrounding document for information needed to understand the visualization.

## Census Data Examples

***Example 1:*** Land Improvements to Pre-1950 Owner-Occupied Single Family Homes: 2019–2021

The note explains exclusions from the universe and defines a term used in the visualization. If a home can have more than one type of land improvement, the note should also explain that the categories are not mutually exclusive.

![Horizontal bar chart showing land improvements to pre-1950 owner-occupied single-family homes in 2019–2021. Landscaping or sprinkler system replacement is most common at 9.4 percent. The note explains that replacement includes additions, defines recreational structures, and excludes improvements to multiunit buildings because they were not asked about.](assets/Note1.png)

***Example 2:*** A Demographic Portrait of Supplemental Nutrition Assistance Program (SNAP) in Select States

The note at the bottom provides additional context and includes DRB approval information. Include approval identifiers when required for the product.

![SNAP eligibility dashboard for Arizona, with tabs for Eligibility, Access, and Characteristics. Two county maps compare eligibility for the full population and children aged 0–17. Statewide estimates are 25.3 percent overall and 36.9 percent for children, with margins of error shown below. Notes and source information appear beneath the maps and summary graphics.](assets/Note2.png)

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Terms or symbols are not defined | Readers may misunderstand the data. | Define them in the note if they are not explained elsewhere. |
| The universe is unclear | Readers may assume the data cover a different population. | State the universe and relevant exclusions. |
| Overlapping categories are not explained | Readers may assume categories are mutually exclusive or add them incorrectly. | Explain that an observation can belong to more than one category, when applicable. |
| Relevant statistical limitations are missing | Readers may draw unsupported conclusions from comparisons. | Explain the limitations and relevant statistical significance information. |
| Notes are available only on hover | Touchscreen and keyboard users may not be able to access them. | Provide visible notes or an accessible information button. |
| Applicable approval identifiers are missing | Required review information may be incomplete. | Include the identifiers required for the specific product. |

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
 
* [Sources](source.html): source lines and notes often sit together under a chart.
* [Titles](title.html): the title, subtitle, and notes should work as one information hierarchy.
* [Interactive Chart](interactivechart.html): do not place essential notes only in a hover popup.
* [Mobile Design for Interactive Visualizations](mobiledesign.html): notes need to remain readable when the layout reflows.
* [508 Compliance](508.html): text alternatives and visibility requirements that apply to notes as well as to the chart.
