---
layout: default
title: Visualizing Uncertainty
permalink: uncertainty.html
description: "Short Description of Visualizing Uncertainty"
---

# Visualizing Uncertainty

Data uncertainty refers to the inherent variability or doubt in measurements or estimates. It can result from sampling, measurement errors, modeling assumptions, or other sources. Effectively visualizing uncertainty is essential for accurate data interpretation and informed decision-making. Poor representation—or omission—of uncertainty can lead to misleading conclusions.

Most estimates provided by the U.S. Census Bureau are not precise measures but have a range of uncertainty. Common measures for indicating uncertainty include: 
* Standard Error (SE):   A measure of the deviation of a sample estimate from the average of all possible samples.
* Margin of Error (MOE): The difference between an estimate and its upper or lower confidence bounds.
* Confidence Interval (CI): The sample estimate and its standard error permit the construction of a confidence interval that represents the degree of uncertainly about the estimate.  

A standard deviation (SD) and coefficient of variation (CV) are sometimes also included with an estimate. SD is a measure of the dispersion or spread of a set of values. It quantifies the average distance of each data point from the mean of the dataset. A CV is a normalized measure of dispersion, defined as the ratio of the standard deviation to the mean. It is useful for comparing the relative variability between datasets with different units or means. 

## Guidance  

## Best Practices 

### Essential 

* Use trusted and accurate data in your visualizations.
* Include measures of uncertainty (when applicable) and define within the chart or through a caption which measure of uncertainty is being displayed within the chart.
* Consider your audience’s level of statistical understanding to determine if and how to show uncertainty.
* If any differences are identified (e.g., with a footnote) as statistically significant in any comparison within a visualization, then all statistically significant differences must be similarly identified in the visualization. 
* Indicate that the data are subject to error arising from a variety of sources, including (as appropriate) sampling error, nonsampling error, model error, and any other sources of error.  (See the [U.S. Census Bureau Statistical Quality Standards](https://uscensus.sharepoint.com/sites/policyportal/Policy%20Repository/Statistical_Quality_Standards.pdf#search=statistical%20standards): E2-2#3)
* For 508 compliance, [alternative text](https://www.w3.org/WAI/WCAG21/Understanding/text-alternatives.html)—an alt attribute, concise, descriptive text that accurately describes an image—should describe the uncertainty in the data. Example phrasing includes, "this is an estimated number between ## and ##.”


### Avoid

* Highlight results as meaningful if they are not statistically significant. For example, do not show a bar chart with two bars if the estimates for those bars are not significantly different.
* Omit uncertainty information when it could meaningfully affect interpretation
   
 
## Additional Recommendations 

### Recommended  

* If the interpretation could differ depending on the margin of error, such as ranking lists with estimates that are not statistically different, consider showing the uncertainty range visually. 
* Where estimates could fall into the highest and lowest category (or could cross multiple categories) because their MOE range is so large, reconsider the utility of the data.
* In cases where integrated design to flag statistical significance is not feasible, such as static choropleth maps, reliability should be explicitly addressed in the technical notes or through supplemental callouts.


### Not Recommended  

* Using overly technical plots without sufficient guidance for non-expert audiences.

## Examples for Visualizing Uncertainty

Different strategies can help communicate uncertainty to audiences effectively. The choice depends on the data, visualization type, goals, and audience expertise.

***Example 1:*** Error bars and confidence bands

* [U.S Exporting Firms by Demographics in 2021](https://www.census.gov/library/visualizations/2024/econ/exports-2021.html)
*   ![Uncertainty 1](assets/Uncertainty1.png)

* [The Population 65 Years and Older: 2016](https://www.census.gov/library/visualizations/interactive/population-65-years.html)
*   ![Uncertainty 2](assets/Uncertainty2.png)

Error bars and confidence bands visually indicate the possible range within which true values are expected to fall. They give an idea of how precise an estimate is. 

Pros:
-	Simple and familiar to many users.
-	Based on statistical measures (e.g. confidence interval)
-	Easy to implement in most visualizations.

Cons:
-	Error bars can be used to show different metrics (SE, MOE, etc.), and it is not always clear which one is being shown.
-	Viewers can overestimate the certainty of the estimate.
-	The glyph of a bar provides a false metaphor of containment, where values within the bar are seen as likelier than values outside the bar.
-	Not all readers understand that non-overlapping error bars implies statistical difference. 
-	Readers may assume that overlapping error bars means that the difference between the estimates is not statistically different, when that is not necessarily accurate.

---

***Example 2:*** Signifying statistical difference

* [Population Without Health Insurance Coverage by State: 2019 and 2021](https://www.census.gov/library/visualizations/interactive/population-without-health-insurance-coverage-2019-and-2021.html)
*   ![Uncertainty 3](assets/Uncertainty3.png)

* [Coupled Households by County: 2017-2021](https://www.census.gov/library/visualizations/interactive/coupled-households-by-county-2017-2021.html)
*   ![Uncertainty 4](assets/Uncertainty4.png)

Symbols, colors, or annotations can be used to explicitly indicate when differences between estimates are statistically significant.

Pros
-	Easy for readers to interpret
-	Avoids misinterpretation based on overlapping confidence intervals

Cons 
-	Limited to specific comparisons (e.g., 2021 vs 2019)
-	Does not convey the degree of variability of uncertainty in each estimate

---

***Example 3:*** Displaying measures of uncertainty as text

* [Married Couple Place of Birth and Current State of Residence: 1900-2018](https://www.census.gov/library/visualizations/interactive/married-couple-place-of-birth-and-current-state-of-residence-1900-2018.html)
*   ![Uncertainty 5](assets/Uncertainty5.png)

Measures of uncertainty (e.g., MOE or SE) can be shown alongside point estimates in graphs, tooltips, or in tables.  

Pros
-	Allows readers to assess significance for any comparison
-	Shows degree of uncertainty for each estimate
-	Efficient use of space, especially in interactive formats

Cons
-	May not always be clear whether the value refers to MOE or SE
-	Uncertainty values in footnotes or separate tables are often overlooked or separated from the graphic.
-	Users have to do a calculation to determine if estimates are significantly different

---

***Example 4:*** Probability or distribution plots

* [Error Bars Considered Harmful: Exploring Alternate Encodings for Mean and Error](https://vis.csail.mit.edu/classes/6.859/readings/pdfs/Corell-ErrorBarsConsideredHarmful.pdf)
*   ![Uncertainty 6](assets/Uncertainty6.png)

Charts such as histograms, density plots, box-plots, jitter plots and violin-plots provide visual insight into the shape, spread, and central tendency of the data distribution. 

Pros
-	Show full distribution and variance
-	Reveal skewness, Irregular patterns, or outliers, giving more context to the estimate

Cons
-	Higher cognitive load than simple bar or line charts
-	May require explanation for general audiences
-	May be unable to fully disaggregate for the charts due to disclosure avoidance

---

***Example 5:*** More options for visualizing uncertainty:
 	
These examples are just a starting point for visualizing uncertainty. The field is continuously evolving, with new techniques being developed and tested through robust research. Consider if visualizations like **hypothetical outcome plots** align best with your audience's needs and your project goals. Ultimately, developers should conduct their own research to determine how to effectively incorporate measures of uncertainty into their unique visualizations.
