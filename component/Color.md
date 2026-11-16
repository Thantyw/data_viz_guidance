---
layout: default
title: Color 
permalink: color.html
description: "Guidance for selecting accessible color palettes for data visualizations, including sequential, qualitative, and diverging color schemes."
---

# Color

## Purpose and Overview

Use color carefully in data visualizations to clearly convey the information presented. Color within any part of the visualization needs to be considered, including but not limited to color used in:

* Data points
* Axis labels
* Data labels
* Foreground
* Background
* Legend
* Text

Section 508 considerations are mentioned here, but for more information, see the [508 Compliance page](508.html).

The colors featured in this section follow the U.S. Census Bureau's brand guidelines and can be customized to fit your needs. Text placed on these colors must meet a contrast ratio of at least 4.5:1, as required by the latest Web Content Accessibility Guidelines (WCAG) 2.1 AA.

## When This Guidance Applies

Apply this guidance to every chart, map, table, and dashboard that uses color, including text, backgrounds, and legends.

In addition to this section, relevant guidance is in the 508 Compliance, Legends, Interactive Chart, and Typography sections.

## Census Color Palettes

This palette mixes warm and cool tones. Its simple design helps users tell categories and ordered data apart more easily.

We encourage everyone using these standards to reference their own agency's brand guidelines and the Text Accessibility guidance below for 508-compliant colors.

### Featured Census Colors

![Four featured Census colors shown as swatches: teal (hex 0095A8), navy (hex 112E51), orange (hex FF7043), and grey (hex 78909C), each with its RGB, CMYK, and hex values.](assets/Color01.png)

### Sequential Colors

Each featured Census color can be used to create a sequential color palette. Use this type of palette when data values can be ordered from low to high. To show that the data are sequential (also known as continuous), use shades of the same color, with lower values lighter and higher values darker.

![Teal sequential palette of seven shades, from darkest teal (hex 00282E) through teal (hex 0095A8) to lightest teal (hex D4F4F8).](assets/Color02.png)

![Blue sequential palette of seven shades, from darkest blue (hex 081627) through blue (hex 2E78D2) to lightest blue (hex C1D7F2).](assets/Color03.png)

![Orange sequential palette of seven shades, from darkest orange (hex 5D2818) through orange (hex FF7043) to lightest orange (hex FFE4DC).
](assets/Color04.png)

![Grey sequential palette of seven shades, from darkest grey (hex 222C31) through grey (hex 78909C) to lightest grey (hex E8EFF2).](assets/Color05.png)

### Qualitative Colors

The four Census colors can also be used to create a qualitative color palette. Qualitative colors show categorical data, such as sex or race, that has no natural order. Colors next to each other must have enough difference in hue and brightness, a contrast ratio of at least 3:1 (WCAG 1.4.11), so all categories can be told apart.

![Example qualitative palette of seven distinct colors: teal, navy, orange, grey, blue, dark teal, and light orange.](assets/Color06.png)

### Highlight Colors

A highlight color can be used with a qualitative palette to draw attention to one category. This type of palette draws the reader toward the highlighted color, so use it with caution.

***Example Palette with Highlight***

![Example palette with highlight: bright orange stands out against four pale colors, which are lighter orange, lighter blue, lighter grey, and lightest teal.](assets/Color07.png)

### Diverging Colors

Like sequential colors, diverging colors are used when data values can be ordered from low to high. The difference is that diverging colors draw attention to an important break point in the data, such as zero or the national average. Each end of the scale uses a different color, and the break point, or middle value, is a neutral color. Values furthest from the break point are darker, and values closer to it are lighter.

***Example Palette***

![Example diverging palette: navy and lighter blue on one end, lightest grey as the neutral middle, and lighter orange and darker orange on the other end.](assets/Color08.png)

### No Data Colors

Sometimes elements with no data still need color, such as areas on a map. In these cases, use a neutral color for a "No Data" class, define it in the legend, and describe it in the alt text. For diverging or sequential color schemes, use a dark gray that won't be mistaken for a color in the range of valid values.

## Essential Requirements

* Text and its background must have a contrast ratio of at least [4.5:1](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html) (WCAG 1.4.3). Use a tool such as the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) to test it.
* Chart shapes, such as bars, lines, and map areas, must have a contrast ratio of at least 3:1 against nearby colors (WCAG 1.4.11).
* Color must not be the only way to show meaning (WCAG 1.4.1). Where color carries information, define it in a legend or label it directly, and describe it in the alt text.
* Choose a sequential, diverging, or qualitative scheme that matches the data, and consider a highlight color to show the main point of the chart.
* If a dark background is used, use light text, and if a light background is used, use dark text.
* If opacity is used, make sure the final color still meets the contrast requirements.

### Text Accessibility

Text colors must also meet the 4.5:1 contrast ratio. The examples below show color combinations that meet Section 508 foreground and background contrast requirements. To keep text accessible, use only these combinations. If you customize beyond this palette, test every combination with the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/).

## Recommended Practices

* Label data directly with text to rely less on color.
* Use color the same way across related visualizations.
* Consider what colors mean for your topic. For example, red usually signals a warning, error, or problem.
* With a qualitative palette, avoid color pairs that are hard to tell apart, especially for readers with color blindness:
   * red and green
   * green and brown
   * green and blue
   * blue and gray
   * blue and purple
   * green and gray
   * green and black
* Use tools such as [ColorBrewer](https://colorbrewer2.org/) to pick palettes that work for readers with color blindness.

## Practices to Avoid

* Don't use a sequential or diverging scheme if the data don't have that kind of order.
* Don't use too many colors. Too many colors distract from the purpose of the visualization.
* Don't use colors that clash with what you are showing, because it makes the chart harder to read. For example, coloring Asian as blue, Hispanic or Latino as black, Black or African American as white, and White as gray makes this chart harder to interpret. Use the recommended qualitative palette instead.

  ![Not recommended example from the 2023 Deloitte Digital Citizen Survey: three radial bar charts of challenges accessing digital government services by race, with Asian shown in blue, Hispanic or Latino in black, Black or African American in white, and White or Caucasian in gray. The white bars almost disappear against the light background.](assets/Color09.png)

## Census Data Examples

***Example 1:*** Accessible Text Combinations

![Accessible text on a white background: the darkest, darker, and dark shades of teal, orange, blue, and grey used as text color on white.](assets/Color10.png)

![Accessible white text on colored backgrounds: white text on the darkest, darker, and dark shades of teal, orange, blue, and grey.](assets/Color11.png)

***Example 2:*** Failed versus Preferred Example

![Side-by-side bar charts. In the failed example, white percentage labels of 20 percent and 15 percent sit on bright teal bars with too little contrast. In the preferred example, the same labels sit on darker teal bars that meet the contrast requirement.](assets/Color12.png)

**Failed example.** Why it fails: Text labels can go inside chart elements, but the text color must contrast with the background enough to meet Section 508 guidelines. See Text Accessibility above.

**Preferred example.** Why it meets the requirements: The background color was changed to meet the minimum contrast ratio with white text. Text can also be placed just outside the chart elements.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Low-contrast text on colored shapes | Labels are hard or impossible to read. | Use at least 4.5:1 contrast, or move labels outside. |
| Sequential colors for unordered categories | Readers assume an order that does not exist. | Use a qualitative palette. |
| Color is the only way to tell groups apart | Readers with color blindness cannot match groups. | Add direct labels or patterns. |
| No-data areas colored like real values | Readers mistake missing data for low values. | Use a distinct neutral color and add it to the legend. |
| Colors with unintended meanings | Readers may read in meaning that isn't there. | Use the recommended palette. |

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
 
* [508 Compliance](508.html): general accessibility requirements, including that color cannot be the only way to communicate meaning.
* [Legends](legend.html): how to identify colors and categories in a key when direct labels are not used.
* [Typography](typography.html): contrast and size for colored text and labels.
* [Interactive Chart](interactivechart.html): hover highlights and other color changes still need a non-color cue.
