---
layout: default
title: Mobile Design for Interactive Visualizations 
permalink: mobiledesign.html
description: "How to design interactive data visualizations for mobile screens, touch controls, and slower networks."
---

# Mobile Design for Interactive Visualizations

## Purpose and Overview

People interact with data visualizations on smartphones and tablets as well as desktop and laptop computers. Mobile design helps users read, navigate, and explore data on smaller screens.

Most interactive visualization techniques were originally developed for desktop displays. They may not work well on mobile devices because screen size, screen shape, and interaction methods differ. One-handed use and slower mobile networks also affect the experience.

Mobile users may have different goals from desktop users. For example, they may want the main findings rather than a full set of options for exploring the data. Consider these needs when developing an interactive visualization.

## When This Guidance Applies

Apply this guidance when creating or updating an interactive chart, map, or dashboard that people may use on a smartphone or tablet.

In addition to this section, relevant guidance is in the 508 Compliance, Color, Interactive Chart, and Typography sections.

## Essential Requirements

* Make links, buttons, search fields, and other controls large enough and sufficiently separated to avoid accidental selections. When targeting WCAG 2.2 AA, criterion 2.5.8 specifies targets of at least 24 by 24 CSS pixels, with exceptions for spacing, equivalent controls, inline links, unmodified browser controls, and essential presentations. This is a WCAG 2.2 criterion, not a WCAG 2.1 AA requirement. Do not treat CSS pixels as a fixed physical size in millimeters.[^4]
* Maintain a contrast ratio of at least 4.5:1 between normal-sized text and its background. WCAG permits 3:1 for large text. Good contrast is especially important on mobile devices because users may be outdoors or in other environments with glare.[^3][^6]
* Present repeated components consistently across pages at each screen size and orientation. For example, navigation buttons should stay in a consistent location across related dashboard views.[^3]
* Order visualization elements by priority. Show essential information first and let users explore details if they wish. Keeping important information near the beginning helps users with low vision and users with cognitive impairments.[^3]

## Recommended Practices

* Follow the relevant Census web survey design guidance when designing controls and mobile layouts.[^1]
* Aim for touch targets of at least 44 by 44 CSS pixels where practical, especially for frequently used controls. This is the WCAG enhanced Level AAA target-size criterion, not an AA requirement.[^5] Platform guidance, such as Android accessibility guidance, can also help with touch-target design.[^2]
* Wrap text and adjust chart formatting to avoid unnecessary horizontal scrolling. Vertical scrolling is generally easier to discover and use on mobile devices.[^1]
* Use responsive web design so the layout adjusts and wraps to fit the available screen size.[^1]
* Support both portrait and landscape use rather than requiring users to turn their device to read the visualization.
* If a dashboard scrolls, make it clear that more content is available below the screen. For example, keep part of the next section visible at the bottom.[^7]
* Position interactive elements so they are easy to reach when the device is held in different positions.[^3]
* Improve performance on slower mobile networks by reducing image sizes, optimizing data extracts, limiting the number of marks, and using efficient calculations.
* Make additional information available on tap rather than relying on mouse hover. Keep essential information available without opening a tooltip.
* Limit the number of dashboard objects and focus on the story or measure that matters most.[^3]
* Simplify navigation and filtering. Use compact controls, such as dropdowns and single-select filters, when they meet the user's needs.
* For wide tables, consider a mobile-friendly list or chart for the main view while keeping the underlying data available.
* Test the visualization on a range of real iOS and Android devices and browsers, including Chrome, Safari, and Firefox.

## Practices to Avoid

* Do not shrink a desktop dashboard to fit a phone without adjusting its text, controls, and layout.
* Do not crowd small touch controls together.
* Do not require horizontal scrolling to read ordinary text.
* Do not require landscape orientation just to make the visualization usable.
* Do not rely on hover alone to reveal information.
* Avoid complex multi-select filters or long filter lists when simpler controls meet the user's needs.
* Do not fill the screen with low-priority objects that hide the main finding or make the dashboard slow to load.

## Census Data Examples

***Example 1:*** State Government Spending

![Mobile view of Allocation of State Government Spending: 2022, with Public welfare selected in a dropdown. A green-shaded U.S. map shows public welfare as a percentage of total state expenditure. Below it, an Arizona table shows 47.1 percent for public welfare compared with 35.6 percent nationally. Additional spending categories continue down the screen.](assets/MobileDesign1.png)

The existing example illustrates these mobile design choices:

* Font sizes and component sizes were adjusted for the smaller screen, with additional space between touch controls.
* Content follows a priority order: title, filter, highest-priority visual, lower-priority visual, source, then logo.
* The table continues below the screen, indicating that the dashboard can be scrolled.
* Tooltips and an information button provide additional details without filling the main view.
* A dropdown filter and map-based filtering save space compared with a list filter.
* Information is pared down to what matters most for the story.

Access the full visualization: [State Government Spending: 2022](https://www.census.gov/library/visualizations/interactive/state-government-spending.html).

***Example 2:*** Digital Equity Act Population Viewer

![Mobile view of the Digital Equity Act Population Viewer, with a state map above an open legend panel. Purple shading shows the percentage of residents in at least one covered population category, from less than 75 percent to 90 percent or more. Map navigation controls appear along the right edge, and explanatory text continues below the legend.](assets/MobileDesign2.png)

The existing example illustrates these mobile design choices:

* The map appears above a panel containing the legend and explanatory text.
* The legend panel has a visible scrollbar, indicating that more information is available below.
* Menu and map navigation controls remain available alongside the map.

Access the full visualization: [Digital Equity Act Population Viewer](https://www.census.gov/programs-surveys/geography/data/interactive-maps/DigitalEquity.html).

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Desktop dashboard is simply reduced in size | Text becomes hard to read, and controls become hard to select. | Adjust the layout, text, and controls for smaller screens. |
| Touch controls are small or crowded | Users may activate the wrong control. | Increase target sizes and check spacing against the applicable guidance. |
| Text requires horizontal scrolling | Users may miss content or struggle to follow it. | Wrap text and use a responsive layout. |
| Details appear only on hover | Touchscreen users may not be able to reveal them. | Provide tap access and keep essential information visible. |
| Too many objects or large data loads | The main message is harder to find, and loading may be slow. | Prioritize content and optimize images, data, marks, and calculations. |
| More content is hidden below the screen | Users may not realize they can scroll. | Provide a visible cue that content continues. |
| A target size in pixels is treated as a fixed size in millimeters | The physical size can vary across devices and viewing conditions. | Use the units specified by the applicable standard and test on real devices. |

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

## Additional Resources

[^1]: [Design Guidelines for U.S. Census Bureau Web Surveys and Censuses](https://uscensus.sharepoint.com/sites/DICE/Baselined%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FDICE%2FBaselined%20Documents%2FISR%20%2D%20Web%20Survey%20Design%20Guidelines%2Epdf&parent=%2Fsites%2FDICE%2FBaselined%20Documents), version 1.07, October 1, 2024. Internal Census resource.

[^2]: [Touch target size — Android Accessibility Help](https://support.google.com/accessibility/android/answer/7101858?hl=en).

[^3]: [Mobile Accessibility: How WCAG 2.0 and Other W3C/WAI Guidelines Apply to Mobile](https://www.w3.org/TR/mobile-accessibility-mapping/), February 26, 2015.

[^4]: [Understanding Success Criterion 2.5.8: Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), WCAG 2.2, Level AA.

[^5]: [Understanding Success Criterion 2.5.5: Target Size (Enhanced)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html), Level AAA.

[^6]: [Understanding Success Criterion 1.4.3: Contrast (Minimum)](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html), Level AA.

[^7]: [Tips for designing device-specific dashboards that make everyone happy](https://www.tableau.com/blog/tips-designing-device-specific-dashboards-make-everyone-happy-57548), August 15, 2016.
 
## Related Pages
 
* [Interactive Chart](interactivechart.html): dashboard and interactive behavior that often needs a mobile layout.
* [508 Compliance](508.html): accessibility requirements that also apply on phones and tablets.
* [Color](color.html): contrast guidance, including text at 4.5:1 and meaningful non-text contrast.
* [Typography](typography.html): readable type sizes when the layout reflows to a small screen.
* [Notes](note.html): notes need to remain readable when hover is unreliable on touch devices.
