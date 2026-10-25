---
layout: default
title: Color 
permalink: color.html
description: "Guidance for selecting accessible color palettes for data visualizations, including sequential, qualitative, and diverging color schemes."
---

# Color 

Careful use of color is needed within data visualizations in order to clearly convey to the reader the information being presented.  Color within any part of the visualization needs to be considered and this includes but is not limited to color used in:
* Data points
* Axes labels 
* Data labels
* Foreground
* Background 
* Legend
* Text

Considerations need to be made for 508 compliance and these are mentioned here but for more information on 508 compliance see our [Components: 508 page](508.html). 

The colors featured in this section adhere to U.S. Census Bureau’s brand guidelines and can be easily customized to fit your needs. Color combinations when used correctly should have a contrast ratio of each color against black or white text and adhere to a contrast ratio of 4.5:1 as per the latest Web Content Accessibility Guidelines (WCAG) 2.1 AA. 

# Palette

This palette is designed to delight users with a mix of warm and cool tones that are as unique as they are vibrant. The simple and minimalistic nature of this palette will ensure users can differentiate categories and sequencing of data more easily.

We encourage everyone using these standards to reference their own Agency’s brand guidelines and to reference the Text Accessibility section below for guidance on using 508-compliant colors.

## Featured Census Colors

![Color 01](assets/Color01.png)

## Sequential Colors

Each of the featured Census colors can be used to create a data visualization with a sequential color palette. This type of palette can be used when data values can be ordered from low to high. To reflect that the data is sequential (also known as continuous), all the data values should be variations of the same color hue, where lower values are lighter and higher values are darker.

![Color 02](assets/Color02.png)

![Color 03](assets/Color03.png)

![Color 04](assets/Color04.png)

![Color 05](assets/Color05.png)

## Qualitative Colors

The four Census colors can also be used to create a qualitative color palette. Qualitative colors are used to render categorical data, such as gender or race, that has no inherent sequential order.
When using this type of palette, colors must have sufficient color contrast (4.5:1) in their hue and brightness to ensure all the categories are represented similarly. 

![Color 06](assets/Color06.png)

## Use of Color for Highlights

Alternatively, a highlight color can be used with a qualitative palette to draw attention to a particular category of data. With this type of palette, a bias is shown towards the highlight color so use this type of palette with caution.

***Example Palette with Highlight***

![Color 07](assets/Color07.png)

## Diverging Colors

Like sequential colors, diverging colors are commonly used to render a single category of data when data values can be ordered from low to high. The key difference however is that diverging colors bring attention to a significant break point in the data. To illustrate this, a different color is used on each end of the value scale and the breakpoint, or middle value, is represented as a neutral color. Data values that are furthest from the break point are shaded darker, while values that are closer are shaded lighter.

***Example Palette***

![Color 08](assets/Color08.png)

## No Data Colors

Occasionally, it is necessary to color in elements of a data visualization where no data exists, such as in maps. In these cases, a neutral color should be used to represent a “No Data” class with a corresponding entry defining the class in the legend and also defined in the ALT text.  For divergent or sequential color schemes we suggest using a dark grey that won’t be mistaken with the range of colors for valid values.

## Color Accessibility

The WCAG (Web Content Accessibility Guidelines) ensure that content is accessible by everyone. To meet these standards, text and interactive elements should have a color contrast ratio of [at least 4.5:1](http://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html). This ensures that viewers who cannot see the full color spectrum are able to read the text. For more information on accessibility see our 508 Page and See WCAG Section 1.4.3 .

## Text Accessibility

In addition to the colors used within the visualization colors used for the text need to meet the color contrast ratio requirement of 4.5:1.  The options in the examples offer color palette combinations that fall within the range of Section 508 compliant foreground/background color contrast ratios. To ensure that text remains accessible, use only these permitted color combinations.

If you choose to customize beyond this palette, this [color contrast tool](http://webaim.org/resources/contrastchecker/) is a useful resource for testing the compliance of any color combination.

## Guidance  

## Best Practices 

### Essential 

* Use a tool such as the Color Brewer [color contrast tool](http://webaim.org/resources/contrastchecker/)  to select a palette that is 508 compliant, meeting the color contrast requirement of 4.5:1.
* Consider the context of your color selection and choose your colors with sensitivity.  For example, where appropriate choose a sequential, divergent or qualitative color scheme and consider a highlight color in order to help communicate the main purpose of the graph or chart.
* Where color is used to convey information in a data visualization, the color should be defined within a legend or clearly labeled within the graph as well as have alt text defining the colors.
* For optimal visualization, if a dark background color is used, light text should be used as a contrast and the reverse if a light background is used.
* If opacity is used, ensure the final outcome meets the color contrast requirement of 4.5:1 using the color brewer contrast tool.

### Avoid

* Don’t use a sequential or divergent color scheme if the data do not reflect that type of relationship.      
 
## Additional Recommendations 

### Recommended  

* Use text elements to label data directly to rely less on color.
* Be consistent in how you use color to label data across data visualizations.
* Be sensitive to how colors correspond to the topic you are depicting. For example, red typically indicates a warning or error or problem.
* When using a qualitative color palette where contrasting is not encouraged, try to avoid conflicting color combinations. Some examples include:
   * red & green
   * green & brown
   * green & blue
   * blue & grey
   * blue & purple
   * green & grey
   * green & black


### Not Recommended  

* Never use an excessive amount of color in a visualization.  Excessive color is distracting and takes away from the purpose of the visualization.
* Never use colors that contradict what you are depicting, this causes dissonance that can make the visual interpretation more difficult to process. See example: encoding Asian as blue, Hispanic or Latino with black, Black or African American with white, and White or Caucasian with grey makes interpreting this chart more difficult. Instead use the qualitative color palette that is recommended.

  ![Color 09](assets/Color09.png)

## Examples 

***Example 1:*** Accessible Text Combinations

![Color 10](assets/Color10.png)

![Color 11](assets/Color11.png)

***Example 2:*** Failed versus Preferred Example

![Color 12](assets/Color12.png)

### Failed Example

Why it Fails: While it is acceptable to place text labels inside of visualization elements, the text color must contrast the background element enough to meet Section 508 guidelines. For more information, refer to the text accessibility section above.

### Preferred Example

Why it Meets the Requirements: In this example, the background color has been changed to meet the minimum contrast ratio when paired with white text. Alternatively, text elements can also be displayed just outside of visualization elements.
