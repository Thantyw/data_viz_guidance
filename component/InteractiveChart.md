---
layout: default
title: Interactive Chart 
permalink: interactivechart.html
description: "Guidance for building interactive Census Bureau charts that are clear, accessible, and approved for release."
---

# Interactive Chart

## Purpose and Overview

Interactive data visualizations have become an essential way to deliver information to the public. They allow simplified designs and responsive layouts while highlighting essential information and reducing clutter. There are many considerations when creating a new interactive visualization. Review the "Guidelines and Best Practices for Interactive Data Visualizations" located here [interactive data visualizations guidelines (Jan 2023)](https://uscensus.sharepoint.com/:b:/r/sites/adcom/data-visualization-hub/Documents/Guidelines%20%26%20Best%20Practices/interactive%20data%20visualizations%20guidelines%20(Jan%202023).pdf?csf=1&web=1&e=TuqZfW) for more information. The following recommendations come from that document, and we refer readers to the original document for further examples and clarification.

## When This Guidance Applies

Apply this guidance whenever a chart, map, or dashboard lets users hover, click, filter, or make selections, such as Tableau dashboards and interactive web charts on census.gov.

In addition to the guidance provided in this section, relevant guidance can also be found in the Agency Logo, Axes, Colors, Grids, Legends, Source, Titles, Typography, Mobile Design, Section 508, and Showing Uncertainty sections.

## Essential Requirements

* Where applicable, interactive information products shall have the Census Bureau DMS and DRB numbers included on the data visualization the same way that a source statement would be included.
* Visualization creators must get approval for the visualization through the program area. This includes Division Chief or Assistant Division Chief, subject matter experts (SMEs), and statistical SMEs. For data from other agencies, agency approvals are needed, including their preferred referencing.
* When applicable, measures of uncertainty (such as margins of error or coefficients of variation) must be available through a pop-up or a link to another location, and the type of error term must be named.
* Every interactive chart must also offer a data table or link to the published tables, so users who cannot use the interactive features can still get the information.

## Recommended Practices

* Use the most recently released vintage of the data unless showing trends or a historical overview.
* Ensure the visualization works for mobile users. See the Mobile Design section.
* Ensure the maximum width matches the census.gov template and the expected user's device.
* Use a 1000-pixel width to fit on a normal visualization page with no horizontal scrollbar, or a 770-pixel width to fit on a blog post or an America Counts story. There is no restriction on height, but 600 pixels is recommended so users can see the entire visualization on a desktop or laptop without scrolling.
* Use fixed dashboard sizing instead of automatic sizing.
* To share the data behind the visualization, link to existing tables already released on data.census.gov or to the data on the Census program area site. Creators who still want a download option must submit examples of the downloaded tables for review to make sure the data and naming follow Census Bureau standards, best practices, and disclosure rules.
* Use short, clear titles with keywords that help search engines, because interactive visualizations are usually standalone products.
* Use plain language, define all acronyms, and avoid jargon and bureaucratic language.
* Hyperlink every full web address shown in the visualization.
* Tell users up front what they can hover over, click, or select.
* Make sure all buttons, navigation, and filters work, and can be reached with a keyboard.
* Complete a review of the user experience and usefulness of the visualization.

## Practices to Avoid

* Do not use automatic dashboard sizing, which can break the layout on different screens.
* Do not show margins of error without saying what they are, such as a 90 percent margin of error.
* Do not offer data downloads that have not been reviewed for Census Bureau standards and disclosure rules.
* Do not hide essential information, such as the source, notes, or error terms, only in hover pop-ups.
* Do not add interactive features that make the chart harder to use without adding information.

## Census Data Examples

***Example 1:*** Where Irish Eyes Are Smiling

[![Map titled Where Irish Eyes Are Smiling showing Irish ancestry as a percentage of each county's population, from 2019 to 2023 American Community Survey 5-year estimates. Counties are shaded in five green bands from less than 5.0 percent to 20.0 percent or more. Darker counties cluster in the Northeast, especially New England, and in parts of the upper Midwest and Mountain West. The U.S. percent is 9.4 percent, plus or minus 0.1 percent.](assets/InteractiveChart1.png)](https://public.tableau.com/views/IrishEyes/National?:embed=y&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

This chart is a good example of the following:

* The user has a clear indicator at the top that other detailed geography can be displayed by making a selection and clicking a button.
* On hover, estimates and margins of error are displayed along with a link to the detailed data tables the visualization comes from. The data aren't downloadable directly from the visualization; they link to the previously released tables.
* This visualization displays previously released estimates, so the DRB and DMS numbers are not necessary, but a full link to the data source is provided.

This chart could be improved:

* The margin of error is shown for the U.S. total, but users must hover to see county margins of error, and the Map does not say they are 90 percent margins of error.

***Example 2:*** Health Insurance Coverage and Type by State

[![Interactive dashboard titled Health Insurance Coverage and Type by State comparing 2019 and 2023 for all ages in the United States. Paired bars show the percentage with each coverage type, such as any coverage at 90.8 percent in 2019 and 92.1 percent in 2023. A second panel shows percentage point differences, with asterisks marking statistically significant changes. Tabs at the top switch years and comparisons, and drop-down menus filter by state and age group.](assets/InteractiveChart2.png)](https://public.tableau.com/views/HealthInsuranceCoverageandTypebyState/TypebyAgeandStatebarsCO?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

The bar charts in this example can show different age groups and geographies using the selections at the top of the visualization.

This chart is a good example of the following:

* The DMS and DRB numbers are clearly displayed in the notes.
* The notes explain that an asterisk marks statistically significant differences.
* A source statement at the bottom identifies the year and program the data come from.
* On hover, margins of error are displayed, and the notes button defines the term margin of error.

  
***Example 3:*** U.S. Marriage and Divorce Rates for Women by State

[![Introduction page of the U.S. Marriage and Divorce Rates for Women by State dashboard, with definitions, a worked example, and a bar chart comparing national marriage and divorce rates in 2011 and 2021.]({{ '/component/assets/InteractiveChart3.png' | relative_url }})](https://public.tableau.com/app/profile/us.census.bureau/viz/MarriageandDivorceRatesbyState2011and2021/IntroDASH)

This chart is a good example of the following:

* The starting page explains a lot up front, including notes saying that hovering provides more information.
* The error term is clearly defined as a margin of error.
* The DRB number is clearly displayed in the notes.
* The visualization uses interactivity well without making it harder for the user.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Error term not named | Users cannot tell what the uncertainty means. | Label it, such as "90 percent margin of error." |
| Key information only on hover | Mobile, keyboard, and screen reader users may miss it. | Show it in notes or a data table too. |
| Automatic sizing | The layout breaks or scrolls on some screens. | Use fixed sizing at 1000 or 770 pixels wide. |
| Missing DMS or DRB numbers on new estimates | The release cannot be traced to its approval. | Show them like a source statement. |
| Unreviewed data downloads | Data may break naming or disclosure rules. | Link to published tables, or submit downloads for review. |

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
 
* [Mobile Design for Interactive Visualizations](mobiledesign.html): layout, touch targets, and scaling for interactive views on small screens.
* [Notes](note.html): do not hide essential caveats only in a hover popup.
* [Uncertainty](uncertainty.html): how to show margins of error in a way readers can still interpret.
* [Color](color.html): contrast for marks, highlights, and controls.
* [508 Compliance](508.html): keyboard access, text alternatives, and other accessibility requirements for interactive displays.
