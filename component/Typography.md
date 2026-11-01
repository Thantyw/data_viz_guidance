---
layout: default
title: Typography
permalink: typography.html
description: "Guidance for using fonts, text hierarchy, sizing, emphasis, and color to improve readability and communication in data visualizations."
---

# Typography

## Purpose and Overview

Typography is an important tool for communicating the meaning of data. A clear hierarchy of text elements and the use of readable font families help users understand and interact with data visualizations.

Font family, size, weight, emphasis, spacing, and color can help distinguish titles, labels, annotations, categories, and other information. These elements should be used deliberately so that typography supports the analytical message rather than competing with the data.

Typography is especially important for digital content. Text displayed on computer and mobile screens may be affected by screen resolution, contrast, glare, reflections, display size, and viewing conditions. Clear typography and reduced visual clutter can improve readability and reduce unnecessary visual effort.

For typography specifically related to mobile design, see [Mobile Design](mobiledesign.html).

## Font Selection

The **PIO standard font is Gotham**.

Gotham may not be available in all software, including some visualization platforms. When Gotham is unavailable, acceptable alternative fonts include:

- Calibri
- Cambria
- Tableau Book
- Verdana
- Georgia
- Gisha

Use fonts consistently within a visualization and across related visualizations.

For interactive visualizations containing multiple pages or views, maintain a consistent font treatment from page to page.

### Essential

- Use Gotham as the PIO standard font when available.
- When Gotham is unavailable, use an acceptable alternative font.
- Use a text size of at least **8 points (pt)**.
- Use labels that are easily readable without interfering with the visualization content, particularly in maps.
- Use consistent fonts across pages of multipage interactive visualizations.
- Avoid overly thin or light fonts that may be difficult to read.
- Ensure typography provides sufficient contrast against its background.

### Avoid

- Avoid text smaller than 8 pt.
- Avoid overly thin or light font weights that reduce readability.
- Avoid unnecessary changes in font family within the same visualization.
- Avoid decorative typography that competes with the data.
- Avoid using typography solely for visual decoration when it does not communicate hierarchy or meaning.
- Avoid placing labels where they obscure important data or other visual elements.

## Typographic Hierarchy

Typography should establish a clear visual hierarchy so users can quickly distinguish the most important information.

Titles, subtitles, axis titles, category labels, annotations, notes, and source information serve different purposes and should be visually differentiated in a consistent way.

Hierarchy may be created through:

- Font size
- Font weight
- Position
- Spacing
- Limited use of italics
- Deliberate use of color

The strongest emphasis should generally be reserved for the information most important to understanding the visualization.

### Recommended

- Use larger or heavier text for important headings and titles.
- Use consistent formatting for elements that perform the same function.
- Maintain sufficient spacing between text elements and graphical content.
- Keep labels concise where possible.
- Use direct labels when they reduce the need for users to move repeatedly between the visualization and a legend.
- Maintain a consistent hierarchy across related visualizations.

### Not Recommended

- Do not use multiple font families merely to create visual variety.
- Do not emphasize many elements simultaneously.
- Do not use bold, italics, or color without a clear communicative purpose.
- Do not allow secondary information to visually compete with the primary analytical message.

## Text Size and Readability

Use a text size of at least **8 pt**.

Text should remain readable at the visualization's intended publication and display size. Designers should consider that visualizations may be viewed on different devices and screen sizes.

Labels should be positioned so they remain clearly associated with the relevant data without interfering with other content.

When many labels are required, consider whether the visualization can be simplified, reorganized, or supported by direct interaction rather than reducing text below a readable size.

## Use of Color in Text

Be deliberate and thoughtful when using colored text outside the title.

Additional text color should be used primarily when it supports the key purpose of the visualization—for example, to connect a phrase in a title or annotation to the corresponding data series.

Color should not be added merely for decoration.

When color is used for text, ensure that the text maintains sufficient contrast with its background and that color is not the only means of communicating important information.

For additional standards, see [Color](color.html).

## Accessibility

- Use a minimum text size of 8 pt as required by this guidance.
- Avoid overly thin or light font weights.
- Ensure sufficient contrast between text and its background.
- Do not rely on color alone to communicate meaning or hierarchy.
- Use clear and familiar font families.
- Maintain consistent typography across related pages and views.
- Ensure labels remain readable and do not overlap important visualization content.
- Use meaningful heading and text hierarchy to help users distinguish primary and supporting information.
- Consider readability across desktop, mobile, and other intended display environments.
- See [508 Compliance](508.html) for general accessibility requirements.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Text smaller than 8 pt | May be difficult for users to read. | Use text of at least 8 pt. |
| Excessively thin font weight | Reduces legibility, particularly on digital displays. | Use a sufficiently visible font weight. |
| Too many font families | Creates visual inconsistency and unnecessary distraction. | Use Gotham or an approved alternative consistently. |
| Excessive emphasis | Makes it difficult to identify what information is most important. | Reserve emphasis for information central to the analytical message. |
| Decorative colored text | Adds visual noise without improving understanding. | Use color only when it communicates meaning or supports emphasis. |
| Low text contrast | Makes labels and annotations difficult to read. | Ensure sufficient contrast with the background. |
| Inconsistent typography across pages | Makes related views feel disconnected and increases cognitive effort. | Apply consistent font and hierarchy across related pages. |
| Labels interfering with data | Can obscure values or make relationships difficult to interpret. | Reposition, shorten, or reorganize labels. |

## Publication Quality Checklist

- [ ] Gotham is used when available.
- [ ] If Gotham is unavailable, an approved alternative font is used.
- [ ] Text is at least 8 pt.
- [ ] Font families are used consistently.
- [ ] Multipage interactive visualizations use consistent typography across pages.
- [ ] Titles, labels, annotations, and supporting text have a clear hierarchy.
- [ ] Thin or light fonts that reduce readability are avoided.
- [ ] Labels remain readable and do not interfere with visualization content.
- [ ] Colored text is used only when it serves a clear communicative purpose.
- [ ] Text has sufficient contrast against its background.
- [ ] Color is not the only method used to communicate important information.
- [ ] Typography remains readable at the intended publication and display size.
- [ ] Relevant mobile and accessibility guidance has been considered.

## Example

The example below demonstrates both useful and unnecessary applications of color in typography.

Highlighting the text that identifies what is being measured in red can help viewers quickly connect the wording to what the bars represent.

In contrast, using additional colors simply to label the bars does not add meaningful information and introduces unnecessary visual noise.

![Example demonstrating purposeful and unnecessary uses of colored text in a data visualization](assets/Typography1.png)

## Related Pages

- [Mobile Design](mobiledesign.html): guidance for typography and visualization design on mobile devices.
- [Color](color.html): guidance for purposeful and accessible use of color.
- [508 Compliance](508.html): accessibility and compliance guidance.
- [Axes](axes.html): guidance for readable axis titles, labels, and tick marks.
- [Comparing Data and Values](comparison.html): guidance for consistent visual design across related visualizations.
