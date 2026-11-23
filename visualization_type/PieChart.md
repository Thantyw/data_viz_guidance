---
layout: default
title: Pie Chart
permalink: piechart.html
tags: [Distribution]
description: "When to use pie charts, when to choose alternatives, and how to present part-to-whole Census data clearly."
---

<style>
  .custom-sidebar h3,
  .main-content h3 { color: #137e55; }
  .tag-link { background: #137e55; }
  .main-content .highlight,
  .main-content .highlight pre,
  .main-content pre,
  .main-content code {
    color: #1b1b1b;
    background: #f6f8fa;
    max-width: 100%;
    box-sizing: border-box;
  }
  .main-content .highlight span { color: #1b1b1b !important; }
  .main-content .highlight,
  .main-content .highlight pre,
  .main-content pre,
  .main-content code,
  .main-content .highlight span {
    overflow: visible !important;
    white-space: pre-wrap !important;
    overflow-wrap: anywhere;
  }
  .code-details { margin: 1rem 0 1.5rem; }
  .code-details summary {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    background: #137e55;
    color: #ffffff;
    font-weight: 700;
    border: 2px solid #0c5a3c;
    border-radius: 4px;
    padding: 0.7rem 1rem;
    cursor: pointer;
    list-style: none;
  }
  .code-details summary::-webkit-details-marker { display: none; }
  .code-details summary::marker { content: ""; }
  .code-details-icon {
    width: 0;
    height: 0;
    border-top: 0.35rem solid transparent;
    border-bottom: 0.35rem solid transparent;
    border-left: 0.5rem solid #ffffff;
  }
  .code-details[open] .code-details-icon {
    border-left: 0.35rem solid transparent;
    border-right: 0.35rem solid transparent;
    border-top: 0.5rem solid #ffffff;
    border-bottom: 0;
  }
  .code-details summary:focus {
    outline: 3px solid #1e6bb8;
    outline-offset: 3px;
  }
</style>

# Pie Chart

**Also known as:** Circle chart

## Purpose and Overview

A pie chart presents values as wedges of a circle, with each wedge representing a share of a whole.

Pie charts are familiar, but readers can find it difficult to compare wedge sizes, especially when categories have similar values. Consider a bar chart, stacked bar chart, table, donut chart, or directly displayed numbers before choosing a pie chart. A donut chart is another part-to-whole display, not a solution to every comparison problem.

## When to Use

* The main question concerns how a small number of categories contribute to one whole.
* The categories are mutually exclusive and together cover the whole.
* Broad differences in shares matter more than precise comparisons between similar values.
* The chart can remain near three or four slices.

## When to Use an Alternative

* Use another display when readers need precise comparisons, when there are many categories, or when shares are similar.
* Avoid using several pie charts to compare places, groups, or time periods. A display with a common baseline is usually easier to compare.
* Do not use a pie chart for overlapping categories or values that do not form one meaningful whole.

## Choosing Between Alternatives

| Analytical Goal | Alternative Visualization | Why It May Be Preferable |
|---|---|---|
| Compare category values or similar shares precisely | Bar chart | Lengths on a common baseline are easier to compare than angles. |
| Compare composition across groups | Stacked bar chart | Shows the groups together without requiring comparisons between separate circles. |
| Provide exact values and uncertainty | Table | Readers can look up detailed values directly. |
| Communicate one or two key values | Directly displayed numbers | Avoids an unnecessary chart. |
| Use a circular part-to-whole layout | Donut chart | Provides space for a central label, although similar slice-comparison limitations remain. |

## Data Requirements and Statistical Considerations

* Define the whole, including its population, geography, reference period, and units.
* Use mutually exclusive categories that together account for the whole. The underlying shares should total 100 percent; explain any differences caused by rounding.
* If small categories are combined, explain the grouping and keep the original categories available in a data table.
* Explain missing or suppressed values. Do not treat them as zero or silently redefine the whole by excluding them.
* When appropriate, provide measures of uncertainty and identify the measure used. See the Visualizing Uncertainty guidance.
* If statistical significance is indicated with patterns or other markings, explain what those markings mean. Do not rely on color alone.

## Visualization-Specific Considerations

### Essential Requirements

* Include a legend or label wedges directly.
* Make clear what each wedge represents and what constitutes the whole.
* Provide descriptive alt text and an accessible data table.
* Do not use three-dimensional effects, which distort perceived wedge sizes.

### Recommended Practices

* Stay near three or four slices. Consider a bar chart when more categories are needed.
* Use distinguishable colors and consider outlines or patterns to help separate wedges.
* Include category names and shares so readers do not have to interpret color alone.
* Follow the related Agency Logo, Color, Legends, Notes, Sources, Titles, Typography, and 508 Compliance guidance where applicable.

### Practices to Avoid

* Do not use large gaps between wedges, as in an exploded pie chart.
* Do not use multi-level pies or nested donut rings when they make the display difficult to interpret.
* Do not rely on comparisons between separate pie charts when a bar chart would make the differences clearer.
* Do not imply that a small visual difference establishes statistical significance.

## Accessibility
 
* Write alt text that states the main part-to-whole takeaway, not only that the image is a pie chart. Include the dataset, geography, and reference period when they are not already in nearby text.
* Provide the values in a data table or an equivalent text format so readers do not have to rely on the wedges alone.
* Label each wedge with the category and value (or percent). Color can support the display, but it should not be the only way to tell slices apart.
* Keep text at a contrast of at least 4.5:1 against its background. Keep wedge fills or outlines at least 3:1 against the background and against neighboring slices so the boundaries stay visible.
* For full requirements, see the [508 Compliance](508.html) and [Color](color.html) pages. Meeting these bullets does not by itself mean a chart is 508 compliant.
 

## Census Data Example

### How Maryland workers got to work, 2020–2024

This example is a part-to-whole chart. It uses four slices, because this page recommends staying near three or four. The smallest published ways of getting to work are added together in the last slice. The table under the chart lists each of those published numbers on its own.

The picture description states the result. The caption names the chart. The source line is “U.S. Census Bureau, 2020–2024 American Community Survey 5-Year Estimates, Table B08301.” The same numbers, including margins of error for the counts and the percents, are in a table that opens from the keyboard.

{% include accessible-figure.html
   id="md-commute"
   src="assets/family-d/md-means-of-transportation.png"
   alt="Pie chart of how workers in Maryland got to work in 2020 to 2024. 72.4 percent used a car, truck, or van. 19.3 percent worked from home. 4.2 percent used public transportation. 4.0 percent walked, biked, used a taxi or ride-hailing service, rode a motorcycle, or used another means."
   caption="How Maryland workers got to work, 2020–2024. Each slice is a share of workers age 16 and over."
   source="U.S. Census Bureau, 2020–2024 American Community Survey 5-Year Estimates, Table B08301"
   source_detail="Maryland. Workers 16 years and over."
   source_url="https://data.census.gov/table/ACSDT5Y2024.B08301?g=040XX00US24"
   summary="Show the data table"
   table_caption="Means of transportation to work, Maryland, 2020–2024"
   headers="Means of transportation|Workers|Margin of error|Percent of workers|Margin of error for the percent"
   rows="Car, truck, or van|2,265,958|±9,545|72.4%|±0.23||Worked from home|604,400|±7,547|19.3%|±0.24||Public transportation|131,271|±3,568|4.2%|±0.11||Walking, taxi or ride-hailing, bicycle, motorcycle, or other means|126,056|±3,650 (calculated)|4.0%|±0.12 (calculated)||All workers|3,127,685|±8,544|100%|"
   note="The four modes add up to all workers. The last mode is the sum of five published estimates, listed in the next table. Its count margin of error is the Census Bureau formula for a sum: the square root of the sum of the squared margins. The percent margin of error is the Census Bureau formula for a proportion. Percents are rounded to one decimal place. Estimates were checked against the published 2024 ACS 5-year table on November 8, 2026."
   table_caption_2="Published estimates added together in the last slice"
   headers_2="Means of transportation|Workers|Margin of error|Percent of workers|Margin of error for the percent"
   rows_2="Walked|63,417|±2,622|2.0%|±0.08||Taxi or ride-hailing services|14,954|±1,317|0.5%|±0.04||Other means|37,130|±1,929|1.2%|±0.06||Bicycle|8,406|±910|0.3%|±0.03||Motorcycle|2,149|±408|0.1%|±0.01"
%}

### Ownership share of all businesses by sex, 2021

This chart draws on the Census Bureau's 2021 Nonemployer Statistics by Demographics company summary. It counts employer and nonemployer firms. Each pie shows firms owned by women, owned equally by men and women, owned by men, or unclassifiable. States sit in a tile grid near their places on a map, and a larger pie shows the United States. The number under each name is the number of firms in that place. The table shows the same counts.

{% include accessible-figure.html
   id="ownership-pies-2021"
   src="assets/family-d/ownership-by-sex-2021.png"
   alt="A map of small pies, one in each state's place, plus a larger United States pie, for the sex of business owners in 2021. Of all U.S. firms, 38.6 percent are female-owned, 4.2 percent are owned equally by men and women, 54.1 percent are male-owned, and 3.1 percent are unclassifiable. The number under each name is the total number of firms. The Maine pie is omitted because the female-owned count is suppressed."
   caption="Ownership share of all businesses by sex, 2021. States are arranged like a map, and a larger pie shows the United States."
   source_detail="Nonemployer Statistics by Demographics (NES-D): Company Summary, 2021, table AB2100NESD01. Variable FIRMALL, all sectors."
   source_url="https://data.census.gov/table/ABSNESD2021.AB2100NESD01"
   summary="Show the data table"
   table_caption="Employer and nonemployer firms by sex of owner, 2021"
   headers="Place|Sex of owners|Firms|Share of all firms|Relative standard error (percent)|Margin of error"
   rows="United States|All firms|34,373,425|100%|0.0|±0||United States|Female|13,275,523|38.6%|0.0|±0||United States|Equally male/female|1,427,939|4.2%|0.3|±7,047||United States|Male|18,605,656|54.1%|0.0|±0||United States|Unclassifiable|1,061,306|3.1%|0.2|±3,492||Alabama|All firms|444,218|100%|0.1|±731||Alabama|Female|180,234|40.6%|0.4|±1,186||Alabama|Equally male/female|15,477|3.5%|2.7|±687||Alabama|Male|238,451|53.7%|0.4|±1,569||Alabama|Unclassifiable|10,653|2.4%|1.4|±245||Alaska|All firms|75,439|100%|0.2|±248||Alaska|Female|28,260|37.5%|0.9|±418||Alaska|Equally male/female|4,102|5.4%|6.8|±459||Alaska|Male|40,422|53.6%|0.9|±598||Alaska|Unclassifiable|2,406|3.2%|3.5|±139||Arizona|All firms|675,930|100%|0.1|±1,112||Arizona|Female|266,144|39.4%|0.3|±1,313||Arizona|Equally male/female|34,252|5.1%|3.1|±1,747||Arizona|Male|357,455|52.9%|0.2|±1,176||Arizona|Unclassifiable|17,580|2.6%|2.0|±578||Arkansas|All firms|278,651|100%|0.1|±458||Arkansas|Female|105,014|37.7%|0.4|±691||Arkansas|Equally male/female|14,803|5.3%|3.6|±877||Arkansas|Male|151,729|54.5%|0.4|±998||Arkansas|Unclassifiable|7,603|2.7%|3.4|±425||California|All firms|4,204,010|100%|0.0|±0||California|Female|1,607,305|38.2%|0.1|±2,644||California|Equally male/female|175,828|4.2%|1.4|±4,049||California|Male|2,299,191|54.7%|0.1|±3,782||California|Unclassifiable|121,688|2.9%|0.8|±1,601||Colorado|All firms|711,957|100%|0.1|±1,171||Colorado|Female|277,098|38.9%|0.3|±1,367||Colorado|Equally male/female|36,944|5.2%|2.7|±1,641||Colorado|Male|376,821|52.9%|0.3|±1,860||Colorado|Unclassifiable|20,595|2.9%|1.3|±440||Connecticut|All firms|364,654|100%|0.1|±600||Connecticut|Female|133,611|36.6%|0.6|±1,319||Connecticut|Equally male/female|13,628|3.7%|3.2|±717||Connecticut|Male|204,884|56.2%|0.4|±1,348||Connecticut|Unclassifiable|12,631|3.5%|1.7|±353||Delaware|All firms|104,249|100%|0.3|±514||Delaware|Female|36,068|34.6%|0.8|±475||Delaware|Equally male/female|5,179|5.0%|6.1|±520||Delaware|Male|53,069|50.9%|0.6|±524||Delaware|Unclassifiable|10,431|10.0%|1.1|±189||District of Columbia|All firms|76,101|100%|0.5|±626||District of Columbia|Female|32,965|43.3%|0.8|±434||District of Columbia|Equally male/female|1,744|2.3%|13.7|±393||District of Columbia|Male|36,725|48.3%|0.8|±483||District of Columbia|Unclassifiable|4,866|6.4%|3.7|±296||Florida|All firms|3,257,455|100%|0.0|±0||Florida|Female|1,304,282|40.0%|0.2|±4,291||Florida|Equally male/female|130,258|4.0%|0.8|±1,714||Florida|Male|1,677,713|51.5%|0.2|±5,520||Florida|Unclassifiable|144,704|4.4%|0.3|±714||Georgia|All firms|1,315,831|100%|0.1|±2,165||Georgia|Female|576,204|43.8%|0.1|±948||Georgia|Equally male/female|36,086|2.7%|1.6|±950||Georgia|Male|671,256|51.0%|0.2|±2,208||Georgia|Unclassifiable|31,784|2.4%|1.3|±680||Hawaii|All firms|138,620|100%|0.2|±456||Hawaii|Female|57,774|41.7%|0.7|±665||Hawaii|Equally male/female|6,105|4.4%|4.5|±452||Hawaii|Male|70,669|51.0%|0.9|±1,046||Hawaii|Unclassifiable|4,671|3.4%|4.3|±330||Idaho|All firms|199,314|100%|0.2|±656||Idaho|Female|72,823|36.5%|0.5|±599||Idaho|Equally male/female|16,647|8.4%|3.7|±1,013||Idaho|Male|104,811|52.6%|0.7|±1,207||Idaho|Unclassifiable|5,130|2.6%|2.9|±245||Illinois|All firms|1,307,015|100%|0.1|±2,150||Illinois|Female|495,616|37.9%|0.2|±1,631||Illinois|Equally male/female|43,503|3.3%|2.3|±1,646||Illinois|Male|712,412|54.5%|0.3|±3,516||Illinois|Unclassifiable|55,481|4.2%|0.6|±548||Indiana|All firms|564,826|100%|0.1|±929||Indiana|Female|214,759|38.0%|0.4|±1,413||Indiana|Equally male/female|24,548|4.3%|3.2|±1,292||Indiana|Male|307,532|54.4%|0.3|±1,518||Indiana|Unclassifiable|17,988|3.2%|2.0|±592||Iowa|All firms|280,355|100%|0.1|±461||Iowa|Female|99,383|35.4%|0.5|±817||Iowa|Equally male/female|16,865|6.0%|2.9|±805||Iowa|Male|153,662|54.8%|0.5|±1,264||Iowa|Unclassifiable|10,044|3.6%|2.9|±479||Kansas|All firms|264,383|100%|0.1|±435||Kansas|Female|96,327|36.4%|0.5|±792||Kansas|Equally male/female|16,161|6.1%|3.9|±1,037||Kansas|Male|143,577|54.3%|0.6|±1,417||Kansas|Unclassifiable|8,517|3.2%|2.4|±336||Kentucky|All firms|377,011|100%|0.1|±620||Kentucky|Female|138,173|36.6%|0.4|±909||Kentucky|Equally male/female|15,438|4.1%|4.4|±1,117||Kentucky|Male|211,780|56.2%|0.4|±1,394||Kentucky|Unclassifiable|11,618|3.1%|1.5|±287||Louisiana|All firms|495,729|100%|0.1|±815||Louisiana|Female|204,865|41.3%|0.3|±1,011||Louisiana|Equally male/female|20,268|4.1%|3.1|±1,034||Louisiana|Male|257,096|51.9%|0.4|±1,692||Louisiana|Unclassifiable|12,601|2.5%|1.6|±332||Maine|All firms|155,980|100%|0.1|±257||Maine|Female|Suppressed|Suppressed|Suppressed|Suppressed||Maine|Equally male/female|8,065|5.2%|6.8|±902||Maine|Male|87,211|55.9%|0.9|±1,291||Maine|Unclassifiable|5,540|3.6%|1.9|±173||Maryland|All firms|663,579|100%|0.1|±1,092||Maryland|Female|272,615|41.1%|0.4|±1,794||Maryland|Equally male/female|19,740|3.0%|4.6|±1,494||Maryland|Male|350,176|52.8%|0.5|±2,880||Maryland|Unclassifiable|21,049|3.2%|1.4|±485||Massachusetts|All firms|717,483|100%|0.1|±1,180||Massachusetts|Female|259,668|36.2%|0.5|±2,136||Massachusetts|Equally male/female|23,442|3.3%|3.5|±1,350||Massachusetts|Male|410,309|57.2%|0.3|±2,025||Massachusetts|Unclassifiable|25,068|3.5%|1.3|±536||Michigan|All firms|938,416|100%|0.0|±0||Michigan|Female|368,012|39.2%|0.3|±1,816||Michigan|Equally male/female|34,186|3.6%|2.5|±1,406||Michigan|Male|507,778|54.1%|0.3|±2,506||Michigan|Unclassifiable|28,938|3.1%|1.5|±714||Minnesota|All firms|542,176|100%|0.1|±892||Minnesota|Female|194,529|35.9%|0.5|±1,600||Minnesota|Equally male/female|27,127|5.0%|4.4|±1,963||Minnesota|Male|304,887|56.2%|0.4|±2,006||Minnesota|Unclassifiable|15,030|2.8%|1.3|±321||Mississippi|All firms|280,795|100%|0.1|±462||Mississippi|Female|114,775|40.9%|0.5|±944||Mississippi|Equally male/female|9,341|3.3%|6.2|±953||Mississippi|Male|149,730|53.3%|0.2|±493||Mississippi|Unclassifiable|6,849|2.4%|1.9|±214||Missouri|All firms|572,180|100%|0.1|±941||Missouri|Female|213,534|37.3%|0.5|±1,756||Missouri|Equally male/female|29,591|5.2%|2.4|±1,168||Missouri|Male|313,080|54.7%|0.4|±2,060||Missouri|Unclassifiable|16,074|2.8%|2.6|±687||Montana|All firms|136,191|100%|0.3|±672||Montana|Female|48,574|35.7%|0.6|±479||Montana|Equally male/female|11,581|8.5%|3.1|±591||Montana|Male|70,894|52.1%|0.8|±933||Montana|Unclassifiable|4,742|3.5%|3.0|±234||Nebraska|All firms|187,391|100%|0.1|±308||Nebraska|Female|65,530|35.0%|0.6|±647||Nebraska|Equally male/female|13,392|7.1%|2.0|±441||Nebraska|Male|102,023|54.4%|0.4|±671||Nebraska|Unclassifiable|6,345|3.4%|3.1|±324||Nevada|All firms|333,130|100%|0.2|±1,096||Nevada|Female|131,585|39.5%|0.5|±1,082||Nevada|Equally male/female|14,486|4.3%|5.8|±1,382||Nevada|Male|173,519|52.1%|0.6|±1,713||Nevada|Unclassifiable|13,542|4.1%|2.2|±490||New Hampshire|All firms|142,742|100%|0.4|±939||New Hampshire|Female|50,016|35.0%|0.7|±576||New Hampshire|Equally male/female|6,458|4.5%|7.4|±786||New Hampshire|Male|80,373|56.3%|0.5|±661||New Hampshire|Unclassifiable|5,593|3.9%|1.9|±175||New Jersey|All firms|973,051|100%|0.1|±1,601||New Jersey|Female|337,776|34.7%|0.2|±1,111||New Jersey|Equally male/female|44,156|4.5%|2.1|±1,525||New Jersey|Male|555,405|57.1%|0.1|±914||New Jersey|Unclassifiable|35,210|3.6%|0.9|±521||New Mexico|All firms|165,630|100%|0.2|±545||New Mexico|Female|68,508|41.4%|0.5|±563||New Mexico|Equally male/female|8,984|5.4%|6.1|±901||New Mexico|Male|83,102|50.2%|0.6|±820||New Mexico|Unclassifiable|5,136|3.1%|2.1|±177||New York|All firms|2,211,082|100%|0.0|±0||New York|Female|764,865|34.6%|0.3|±3,775||New York|Equally male/female|71,910|3.3%|1.0|±1,183||New York|Male|1,233,802|55.8%|0.2|±4,059||New York|Unclassifiable|140,504|6.4%|0.4|±925||North Carolina|All firms|1,043,624|100%|0.1|±1,717||North Carolina|Female|421,669|40.4%|0.3|±2,081||North Carolina|Equally male/female|44,864|4.3%|2.0|±1,476||North Carolina|Male|548,054|52.5%|0.4|±3,606||North Carolina|Unclassifiable|29,038|2.8%|1.0|±478||North Dakota|All firms|76,112|100%|0.5|±626||North Dakota|Female|26,285|34.5%|1.0|±432||North Dakota|Equally male/female|4,738|6.2%|5.2|±405||North Dakota|Male|42,336|55.6%|1.1|±766||North Dakota|Unclassifiable|3,153|4.1%|4.7|±244||Ohio|All firms|1,041,537|100%|0.0|±0||Ohio|Female|393,598|37.8%|0.3|±1,942||Ohio|Equally male/female|36,224|3.5%|2.9|±1,728||Ohio|Male|578,058|55.5%|0.1|±951||Ohio|Unclassifiable|32,655|3.1%|1.6|±859||Oklahoma|All firms|379,609|100%|0.1|±624||Oklahoma|Female|141,385|37.2%|0.3|±698||Oklahoma|Equally male/female|20,847|5.5%|3.9|±1,337||Oklahoma|Male|206,205|54.3%|0.4|±1,357||Oklahoma|Unclassifiable|10,969|2.9%|2.4|±433||Oregon|All firms|406,681|100%|0.1|±669||Oregon|Female|166,247|40.9%|0.5|±1,367||Oregon|Equally male/female|25,855|6.4%|2.4|±1,021||Oregon|Male|204,116|50.2%|0.5|±1,679||Oregon|Unclassifiable|11,159|2.7%|2.1|±385||Pennsylvania|All firms|1,117,379|100%|0.1|±1,838||Pennsylvania|Female|394,464|35.3%|0.2|±1,298||Pennsylvania|Equally male/female|41,355|3.7%|1.9|±1,293||Pennsylvania|Male|644,537|57.7%|0.2|±2,121||Pennsylvania|Unclassifiable|36,521|3.3%|1.5|±901||Rhode Island|All firms|109,937|100%|0.2|±362||Rhode Island|Female|39,573|36.0%|0.6|±391||Rhode Island|Equally male/female|6,086|5.5%|7.5|±751||Rhode Island|Male|60,133|54.7%|0.8|±791||Rhode Island|Unclassifiable|4,344|4.0%|3.0|±214||South Carolina|All firms|502,764|100%|0.1|±827||South Carolina|Female|206,063|41.0%|0.3|±1,017||South Carolina|Equally male/female|17,222|3.4%|3.6|±1,020||South Carolina|Male|266,293|53.0%|0.4|±1,752||South Carolina|Unclassifiable|12,787|2.5%|1.9|±400||South Dakota|All firms|94,003|100%|0.2|±309||South Dakota|Female|30,976|33.0%|0.8|±408||South Dakota|Equally male/female|8,014|8.5%|3.3|±435||South Dakota|Male|51,303|54.6%|1.1|±928||South Dakota|Unclassifiable|3,811|4.1%|3.8|±238||Tennessee|All firms|705,016|100%|0.1|±1,160||Tennessee|Female|285,258|40.5%|0.3|±1,408||Tennessee|Equally male/female|20,271|2.9%|2.8|±934||Tennessee|Male|382,672|54.3%|0.3|±1,888||Tennessee|Unclassifiable|16,216|2.3%|3.1|±827||Texas|All firms|3,320,431|100%|0.0|±0||Texas|Female|1,321,604|39.8%|0.2|±4,348||Texas|Equally male/female|110,924|3.3%|1.0|±1,825||Texas|Male|1,807,780|54.4%|0.2|±5,948||Texas|Unclassifiable|80,124|2.4%|0.6|±791||Utah|All firms|352,005|100%|0.1|±579||Utah|Female|122,567|34.8%|0.6|±1,210||Utah|Equally male/female|27,887|7.9%|3.6|±1,651||Utah|Male|189,937|54.0%|0.6|±1,875||Utah|Unclassifiable|11,213|3.2%|1.5|±277||Vermont|All firms|80,263|100%|0.3|±396||Vermont|Female|28,812|35.9%|1.0|±474||Vermont|Equally male/female|4,184|5.2%|8.4|±578||Vermont|Male|43,444|54.1%|0.9|±643||Vermont|Unclassifiable|3,527|4.4%|2.8|±162||Virginia|All firms|845,379|100%|0.1|±1,391||Virginia|Female|338,515|40.0%|0.3|±1,671||Virginia|Equally male/female|31,406|3.7%|2.1|±1,085||Virginia|Male|452,259|53.5%|0.3|±2,232||Virginia|Unclassifiable|23,698|2.8%|1.5|±585||Washington|All firms|665,958|100%|0.1|±1,096||Washington|Female|257,968|38.7%|0.5|±2,122||Washington|Equally male/female|44,149|6.6%|2.3|±1,670||Washington|Male|347,617|52.2%|0.4|±2,287||Washington|Unclassifiable|17,425|2.6%|1.6|±459||West Virginia|All firms|113,628|100%|0.3|±561||West Virginia|Female|42,307|37.2%|0.9|±626||West Virginia|Equally male/female|5,008|4.4%|6.8|±560||West Virginia|Male|61,354|54.0%|0.7|±706||West Virginia|Unclassifiable|4,759|4.2%|1.8|±141||Wisconsin|All firms|478,191|100%|0.1|±787||Wisconsin|Female|171,331|35.8%|0.5|±1,409||Wisconsin|Equally male/female|25,427|5.3%|5.1|±2,133||Wisconsin|Male|267,449|55.9%|0.5|±2,200||Wisconsin|Unclassifiable|14,480|3.0%|2.2|±524||Wyoming|All firms|77,280|100%|0.3|±381||Wyoming|Female|25,179|32.6%|0.5|±207||Wyoming|Equally male/female|8,141|10.5%|3.0|±402||Wyoming|Male|37,945|49.1%|0.7|±437||Wyoming|Unclassifiable|5,913|7.7%|1.8|±175"
   note="The share is the owner group's percent of all firms in that place. The groups are rounded separately from the total, so the shares may not add to 100. The margin of error is calculated from the published relative standard error for an approximate 90 percent level: firms times the relative standard error times 1.645, rounded to the nearest firm. The Maine pie is omitted because the female-owned count is suppressed."
%}

#### Reproduce the ownership example

To draw this picture again, from the project folder:
```
export CENSUS_API_KEY=your_key_here
python3 examples/family_d/make_ownership_pies.py
```

<a href="{{ '/examples/family_d/make_ownership_pies.py' | relative_url }}">Download the Python script</a>. It needs Python 3 and the matplotlib package. Leave the key out of the program and the saved table. If `CENSUS_API_KEY` is not set, the program tries the Census Data API once and otherwise uses `examples/family_d/absnesd_2021_firms_by_sex.csv`.

<details class="code-details">
<summary><span class="code-details-icon" aria-hidden="true"></span>Show Python code for the state pies</summary>
{% highlight python %}
#!/usr/bin/env python3
"""Draw small pies for the sex of owners of all U.S. businesses in 2021.

Source: U.S. Census Bureau
Dataset: 2021 Nonemployer Statistics by Demographics Series (NES-D): Company Summary
Table: AB2100NESD01
API: https://api.census.gov/data/2021/absnesd
Count: FIRMALL, employer and nonemployer firms
Industry: NAICS2017 code 00 (total for all sectors)
Sex: 001 total, 002 female, 003 male, 004 equally male/female, 098 unclassifiable
The unclassifiable row is published with ethnicity 098, race 98, and veteran status 098.
The other sex rows use ethnicity 001, race 00, and veteran status 001.

Set a Census Data API key only in the environment. Do not paste it into this file:

    export CENSUS_API_KEY=your_key_here
    python3 examples/family_d/make_ownership_pies.py

If CENSUS_API_KEY is not set, the program still tries the API once. If that
does not return the table, it uses absnesd_2021_firms_by_sex.csv.
"""

from __future__ import annotations

import csv
import json
import math
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "absnesd_2021_firms_by_sex.csv"
OUT_PATH = HERE.parents[1] / "assets" / "family-d" / "ownership-by-sex-2021.png"
API_URL = "https://api.census.gov/data/2021/absnesd"

# Published relative standard error is a percent. Census uses 1.645 to turn
# that percent into an approximate 90 percent margin of error.
MOE_FACTOR = 1.645

SEX_ORDER = ("001", "002", "004", "003", "098")
PIE_SEX = ("002", "004", "003", "098")
SEX_LABELS = {
    "001": "Total",
    "002": "Female",
    "004": "Equally male/female",
    "003": "Male",
    "098": "Unclassifiable",
}
# Fills are dark enough to stand apart from a white page, and from each other
# for common kinds of color blindness. Black outlines separate the slices.
COLORS = {
    "002": "#D55E00",
    "004": "#009E73",
    "003": "#0072B2",
    "098": "#AA4499",
}
ABBREV = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
    "District of Columbia": "DC", "Florida": "FL", "Georgia": "GA", "Hawaii": "HI",
    "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA",
    "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME",
    "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN",
    "Mississippi": "MS", "Missouri": "MO", "Montana": "MT", "Nebraska": "NE",
    "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM",
    "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
    "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI",
    "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX",
    "United States": "US", "Utah": "UT", "Vermont": "VT", "Virginia": "VA",
    "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY",
}


def read_saved_rows(path: Path):
    """Read the saved table, skipping the source notes at the top."""
    lines = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            lines.append(line)
    return list(csv.DictReader(lines))


def _keep_api_row(row):
    sex = row.get("SEX", "")
    eth = row.get("ETH_GROUP", "")
    race = row.get("RACE_GROUP", "")
    vet = row.get("VET_GROUP", "")
    if row.get("NAICS2017") not in (None, "", "00") and "NAICS2017" in row:
        if row["NAICS2017"] != "00":
            return False
    if sex in {"001", "002", "003", "004"}:
        return eth in ("", "001") and race in ("", "00") and vet in ("", "001")
    if sex == "098":
        return eth in ("", "098") and race in ("", "98") and vet in ("", "098")
    return False


def _rows_from_api_table(table):
    header, *body = table
    records = []
    for values in body:
        item = dict(zip(header, values))
        if not _keep_api_row(item):
            continue
        flag = (item.get("FIRMALL_F") or "").strip()
        if flag in {"null", "None"}:
            flag = ""
        firms = "" if flag == "S" else str(item.get("FIRMALL", "")).strip()
        if firms in {"null", "None"}:
            firms = ""
        rse = "" if flag == "S" else str(item.get("FIRMALL_S", "")).strip()
        if rse in {"null", "None"}:
            rse = ""
        sex = item["SEX"]
        records.append(
            {
                "geo_id": item.get("GEO_ID", ""),
                "geo_label": item.get("NAME") or item.get("geo_label") or "",
                "sex": sex,
                "sex_label": item.get("SEX_LABEL") or SEX_LABELS.get(sex, sex),
                "firms": firms,
                "firm_flag": flag,
                "relative_standard_error": rse,
            }
        )
    return records


def _api_request(params, api_key):
    """Call the Census Data API. The key is not printed or saved."""
    query = dict(params)
    if api_key:
        query["key"] = api_key
    url = API_URL + "?" + urllib.parse.urlencode(query)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "data-viz-guidance family-d example"},
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        raise SystemExit(
            f"The Census Data API returned status {error.code}. "
            "Check that CENSUS_API_KEY is valid."
        )
    except urllib.error.URLError:
        raise SystemExit("The Census Data API could not be reached.")
    if raw.lstrip().startswith("<"):
        return None
    try:
        table = json.loads(raw)
    except json.JSONDecodeError:
        return None
    if not isinstance(table, list) or len(table) < 2:
        return None
    return table


def fetch_live_rows(api_key):
    """Download the sex rows for the United States and the states."""
    common = {
        "get": "NAME,SEX,FIRMALL,FIRMALL_F,FIRMALL_S,NAICS2017,ETH_GROUP,RACE_GROUP,VET_GROUP",
        "NAICS2017": "00",
    }
    calls = (
        {**common, "ETH_GROUP": "001", "RACE_GROUP": "00", "VET_GROUP": "001"},
        {**common, "SEX": "098", "ETH_GROUP": "098", "RACE_GROUP": "98", "VET_GROUP": "098"},
    )
    collected = []
    for predicates in calls:
        for geography in ("us:1", "state:*"):
            table = _api_request({**predicates, "for": geography}, api_key)
            if table is None:
                return None
            collected.extend(_rows_from_api_table(table))
    if not collected:
        return None
    return collected


def load_rows():
    """Use the live API when it answers, and the saved CSV otherwise."""
    api_key = os.environ.get("CENSUS_API_KEY", "").strip()
    if api_key:
        print("Reading live 2021 NES-D estimates from the Census Data API.")
        rows = fetch_live_rows(api_key)
        if rows is None:
            raise SystemExit(
                "The Census Data API did not return the firm table. "
                "Check that CENSUS_API_KEY is valid."
            )
        return rows
    print("No CENSUS_API_KEY set. Trying the Census Data API once.")
    rows = fetch_live_rows(None)
    if rows:
        print("Using live 2021 NES-D estimates from the Census Data API.")
        return rows
    print("The Census Data API did not return the table. Using the saved CSV.")
    return read_saved_rows(CSV_PATH)


def _number(text):
    text = (text or "").strip()
    if not text:
        return None
    return float(text)


def group_geographies(rows):
    """Group rows into United States first, then states A to Z."""
    grouped = {}
    for row in rows:
        label = row["geo_label"]
        grouped.setdefault(label, {})[row["sex"]] = row
    names = sorted(name for name in grouped if name != "United States")
    if "United States" in grouped:
        names.insert(0, "United States")
    places = []
    for name in names:
        sexes = grouped[name]
        total_row = sexes.get("001", {})
        total = _number(total_row.get("firms", ""))
        published = []
        for code in PIE_SEX:
            item = sexes.get(code, {})
            suppressed = (item.get("firm_flag") or "").strip() == "S" or not (item.get("firms") or "").strip()
            firms = None if suppressed else int(float(item["firms"]))
            rse = None if suppressed else _number(item.get("relative_standard_error"))
            published.append(
                {
                    "code": code,
                    "label": SEX_LABELS[code],
                    "firms": firms,
                    "suppressed": suppressed or firms is None,
                    "rse": rse,
                }
            )
        shown = [item for item in published if not item["suppressed"]]
        shown_total = sum(item["firms"] for item in shown)
        places.append(
            {
                "label": name,
                "abbrev": ABBREV.get(name, name),
                "total": None if total is None else int(total),
                "groups": published,
                "shown_total": shown_total,
            }
        )
    return places


def margin_of_error(firms, rse):
    """Approximate 90 percent margin of error from the published RSE."""
    if firms is None or rse is None:
        return None
    return int(round(firms * (rse / 100.0) * MOE_FACTOR))


# Row, column on a tile grid that follows the shape of the United States.
# This is the usual small-multiple state map: Alaska and Hawaii sit at the
# lower left and upper left, and the East Coast is on the right.
TILE = {
    "AK": (0, 0), "ME": (0, 10),
    "WI": (1, 5), "VT": (1, 9), "NH": (1, 10),
    "WA": (2, 0), "ID": (2, 1), "MT": (2, 2), "ND": (2, 3), "MN": (2, 4),
    "IL": (2, 5), "MI": (2, 6), "NY": (2, 8), "MA": (2, 9),
    "OR": (3, 0), "NV": (3, 1), "WY": (3, 2), "SD": (3, 3), "IA": (3, 4),
    "IN": (3, 5), "OH": (3, 6), "PA": (3, 7), "NJ": (3, 8), "CT": (3, 9),
    "RI": (3, 10),
    "CA": (4, 0), "UT": (4, 1), "CO": (4, 2), "NE": (4, 3), "MO": (4, 4),
    "KY": (4, 5), "WV": (4, 6), "VA": (4, 7), "MD": (4, 8), "DE": (4, 9),
    "AZ": (5, 1), "NM": (5, 2), "KS": (5, 3), "AR": (5, 4), "TN": (5, 5),
    "NC": (5, 6), "SC": (5, 7), "DC": (5, 8),
    "OK": (6, 3), "LA": (6, 4), "MS": (6, 5), "AL": (6, 6), "GA": (6, 7),
    "HI": (7, 0), "TX": (7, 3), "FL": (7, 8),
}


def _draw_pie(axis, place, title_size):
    # If any owner group is suppressed, do not draw a pie. Drawing the
    # remaining slices would renormalize them and misstate each group's
    # share of all firms. Do not invent a residual or suppressed count.
    if any(item["suppressed"] for item in place["groups"]):
        axis.set_axis_off()
        axis.text(
            0.5,
            0.5,
            "Chart not shown\n"
            "because an ownership\n"
            "category is suppressed.\n"
            "See the data table\n"
            "for published values.",
            ha="center",
            va="center",
            fontsize=7 if title_size <= 8 else 8,
            color="#1b1b1b",
            linespacing=1.15,
            transform=axis.transAxes,
        )
    else:
        sizes = [
            item["firms"]
            for item in place["groups"]
            if not item["suppressed"] and item["firms"]
        ]
        colors = [
            COLORS[item["code"]]
            for item in place["groups"]
            if not item["suppressed"] and item["firms"]
        ]
        if sizes:
            axis.pie(
                sizes,
                colors=colors,
                startangle=90,
                counterclock=False,
                wedgeprops={"edgecolor": "#1b1b1b", "linewidth": 0.6},
            )
    title = place["abbrev"] if place["abbrev"] != "US" else "United States"
    if place["total"] is not None:
        title = f"{title}\n{place['total']:,}"
    axis.set_title(title, fontsize=title_size, color="#1b1b1b", pad=1)


def draw_chart(places, out_path: Path):
    """Save state pies in a map-shaped tile grid, with the U.S. pie above."""
    plt.rcParams["font.family"] = "DejaVu Sans"
    by_abbrev = {place["abbrev"]: place for place in places}
    missing = [code for code in TILE if code not in by_abbrev]
    if missing:
        raise SystemExit(f"Missing a state for the map: {', '.join(missing)}")
    fig = plt.figure(figsize=(13.2, 11.6), dpi=110)
    fig.patch.set_facecolor("#ffffff")
    grid = fig.add_gridspec(
        9,
        11,
        left=0.02,
        right=0.98,
        top=0.86,
        bottom=0.07,
        wspace=0.08,
        hspace=0.55,
    )
    united = by_abbrev.get("US")
    if united:
        _draw_pie(fig.add_subplot(grid[0, 4:7]), united, 11)
    for abbrev, (row, col) in TILE.items():
        _draw_pie(fig.add_subplot(grid[row + 1, col]), by_abbrev[abbrev], 8)

    handles = [
        Patch(facecolor=COLORS[code], edgecolor="#1b1b1b", label=SEX_LABELS[code])
        for code in PIE_SEX
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.965),
        ncol=4,
        frameon=False,
        fontsize=11,
    )
    fig.text(
        0.03,
        0.975,
        "Ownership share of all businesses by sex, 2021",
        fontsize=16,
        fontweight="bold",
        color="#1b1b1b",
        ha="left",
        va="top",
    )
    fig.text(
        0.03,
        0.028,
        "States sit where they do on a map. Each pie uses the published owner groups. "
        "The number under the name is all firms. "
        "Groups are rounded separately from that total. "
        "In Maine, the female-owned count is suppressed.",
        fontsize=8,
        color="#1b1b1b",
        ha="left",
    )
    fig.text(
        0.03,
        0.012,
        "Source: U.S. Census Bureau. NES-D Company Summary, 2021, table AB2100NESD01.",
        fontsize=8,
        color="#1b1b1b",
        ha="left",
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, facecolor="#ffffff")
    plt.close(fig)


def format_count(value):
    if value is None:
        return "Suppressed"
    return f"{value:,}"


def main():
    places = group_geographies(load_rows())
    draw_chart(places, OUT_PATH)
    us = next(place for place in places if place["label"] == "United States")
    print(f"United States, all firms: {us['total']:,}")
    for item in us["groups"]:
        if item["suppressed"]:
            print(f"United States, {item['label']}: suppressed")
        else:
            print(f"United States, {item['label']}: {item['firms']:,}")
    print(f"Places: {len(places)}")
    print(f"Saved {OUT_PATH}")


if __name__ == "__main__":
    main()
{% endhighlight %}
</details>

#### Related interactive visualization

The related interactive chart is [Ownership Share of All Businesses by Demographics on census.gov](https://www.census.gov/library/visualizations/interactive/ownership-share-of-businesses-by-demographics.html).

Its legend and hover details provide additional information, including values and margins of error. Hover details can supplement a chart, but essential information should also be available to keyboard and touchscreen users.

This example uses multiple pies arranged geographically. Consider a bar chart when the main task is precise comparison between places.

## Developer Implementation

The ownership example's Python instructions appear with that example above. The following instructions reproduce the Maryland commute chart.

### Reproduce the Maryland commute example

<a href="{{ '/examples/family_d/make_md_commute_chart.py' | relative_url }}">Download the Python script</a>. It saves the Maryland commute chart. It needs Python 3 and the matplotlib package.

To download the live 2020–2024 estimates, request a free Census Data API key at https://api.census.gov/data/key_signup.html and set it in your terminal. Leave the key out of the program, this page, and the saved table:

```
export CENSUS_API_KEY=your_key_here
python3 examples/family_d/make_md_commute_chart.py
```

If `CENSUS_API_KEY` is not set, the program uses the saved file `examples/family_d/md_b08301_means_of_transportation.csv`. Those numbers are the published 2020–2024 ACS 5-year estimates for Maryland: 3,127,685 workers in total, 2,265,958 by car, truck, or van, 131,271 by public transportation, and 604,400 who worked from home.

<details class="code-details">
<summary><span class="code-details-icon" aria-hidden="true"></span>Show Python code for the commute chart</summary>
{% highlight python %}
#!/usr/bin/env python3
"""Draw a part-to-whole chart of how Maryland workers got to work.

The numbers are published Census estimates for the 2020-2024 American
Community Survey 5-year estimates, table B08301, Maryland (FIPS 24),
workers 16 years and over.
Published table: https://data.census.gov/table/ACSDT5Y2024.B08301?g=040XX00US24
API: https://api.census.gov/data/2024/acs/acs5

To download the live estimates, set a Census Data API key in the environment.
Do not paste the key into this file:

    export CENSUS_API_KEY=your_key_here
    python3 examples/family_d/make_md_commute_chart.py

If CENSUS_API_KEY is not set, the program uses the saved estimates in
md_b08301_means_of_transportation.csv. Those saved numbers were copied from
the published 2024 ACS 5-year table on 2026-11-08.
"""

from __future__ import annotations

import csv
import json
import math
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "md_b08301_means_of_transportation.csv"
OUT_PATH = HERE.parents[1] / "assets" / "family-d" / "md-means-of-transportation.png"
API_URL = "https://api.census.gov/data/2024/acs/acs5"
STATE_FIPS = "24"

# variable, label, chart group. The total is not given a group.
PUBLISHED_LINES = (
    ("B08301_001", "Total", ""),
    ("B08301_002", "Car, truck, or van", "car"),
    ("B08301_021", "Worked from home", "home"),
    ("B08301_010", "Public transportation", "transit"),
    ("B08301_019", "Walked", "other"),
    ("B08301_016", "Taxi or ride-hailing services", "other"),
    ("B08301_020", "Other means", "other"),
    ("B08301_018", "Bicycle", "other"),
    ("B08301_017", "Motorcycle", "other"),
)

# These colors stay distinct for common kinds of color blindness.
# Each fill has at least a 3 to 1 contrast with the white page, and the
# black outline has at least a 3 to 1 contrast with each fill.
COLORS = {
    "car": "#0072B2",
    "home": "#D55E00",
    "transit": "#009E73",
    "other": "#AA4499",
}

GROUP_LABELS = {
    "car": "Car, truck, or van",
    "home": "Worked from home",
    "transit": "Public transportation",
    "other": "Walking, taxi or ride-hailing, bicycle, motorcycle, or other means",
}

# Same words as GROUP_LABELS, with a line break so the legend fits.
LEGEND_LABELS = {
    "car": "Car, truck, or van",
    "home": "Worked from home",
    "transit": "Public transportation",
    "other": "Walking, taxi or ride-hailing,\nbicycle, motorcycle, or other means",
}


def read_published_rows(path: Path):
    """Read the saved table, skipping the source notes at the top."""
    data_lines = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            data_lines.append(line)
    return list(csv.DictReader(data_lines))


def rows_from_api_payload(raw: str):
    """Turn a Census Data API JSON table into the same rows as the CSV."""
    try:
        table = json.loads(raw)
    except json.JSONDecodeError:
        raise SystemExit(
            "The Census Data API did not return a data table. "
            "Check that CENSUS_API_KEY is valid."
        )
    if (
        not isinstance(table, list)
        or len(table) < 2
        or not isinstance(table[0], list)
        or not isinstance(table[1], list)
    ):
        raise SystemExit(
            "The Census Data API returned an unexpected table. "
            "Check that CENSUS_API_KEY is valid."
        )

    by_name = dict(zip(table[0], table[1]))
    if by_name.get("state") != STATE_FIPS:
        raise SystemExit(
            "The Census Data API response did not include Maryland. "
            "Check that CENSUS_API_KEY is valid."
        )

    rows = []
    for code, label, group in PUBLISHED_LINES:
        estimate_name = f"{code}E"
        margin_name = f"{code}M"
        if estimate_name not in by_name or margin_name not in by_name:
            raise SystemExit(f"The Census Data API response is missing {code}.")
        try:
            estimate = str(int(by_name[estimate_name]))
            margin = str(int(by_name[margin_name]))
        except (TypeError, ValueError):
            raise SystemExit(
                f"The Census Data API returned a non-numeric value for {code}."
            )
        rows.append(
            {
                "variable": code,
                "label": label,
                "estimate": estimate,
                "margin_of_error": margin,
                "chart_group": group,
            }
        )
    return rows


def fetch_live_rows(api_key: str):
    """Download B08301 for Maryland. The key is not printed or saved."""
    fields = ["NAME"]
    for code, _label, _group in PUBLISHED_LINES:
        fields.extend((f"{code}E", f"{code}M"))
    params = urllib.parse.urlencode(
        {
            "get": ",".join(fields),
            "for": f"state:{STATE_FIPS}",
            "key": api_key,
        }
    )
    request = urllib.request.Request(
        f"{API_URL}?{params}",
        headers={"User-Agent": "data-viz-guidance family-d example"},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        raise SystemExit(
            f"The Census Data API returned status {error.code}. "
            "Check that CENSUS_API_KEY is valid."
        )
    except urllib.error.URLError:
        raise SystemExit(
            "The Census Data API could not be reached. "
            "Check your network connection."
        )
    return rows_from_api_payload(raw)


def load_rows():
    """Use the live API when a key is set, and the saved CSV otherwise."""
    api_key = os.environ.get("CENSUS_API_KEY", "").strip()
    if not api_key:
        print("No CENSUS_API_KEY set. Using the saved CSV.")
        return read_published_rows(CSV_PATH)
    print(
        "Using live 2020-2024 ACS 5-year estimates for Maryland "
        "from the Census Data API."
    )
    return fetch_live_rows(api_key)


def build_slices(rows):
    """Turn the published rows into the four slices drawn on the chart."""
    total = None
    total_margin = None
    grouped = {
        key: {"estimate": 0, "squared_margins": 0}
        for key in GROUP_LABELS
    }

    for row in rows:
        estimate = int(row["estimate"])
        margin = int(row["margin_of_error"])
        group = row["chart_group"].strip()
        if row["variable"] == "B08301_001":
            total = estimate
            total_margin = margin
            continue
        if group not in grouped:
            raise SystemExit(f"Unknown chart group '{group}' in {row['variable']}.")
        grouped[group]["estimate"] += estimate
        grouped[group]["squared_margins"] += margin ** 2

    if total is None or total_margin is None:
        raise SystemExit("The estimates are missing the published total, B08301_001.")

    slices = []
    for key, values in grouped.items():
        estimate = values["estimate"]
        # For one published row, this is that row's own margin of error.
        # For the combined slice, this is the Census formula for a sum:
        # the square root of the sum of the squared margins.
        margin = math.sqrt(values["squared_margins"])
        share = estimate / total
        # Census proportion margin of error. If the usual term under the
        # square root is negative, the Census approximation adds the terms.
        under_root = margin ** 2 - (share ** 2) * (total_margin ** 2)
        if under_root < 0:
            under_root = margin ** 2 + (share ** 2) * (total_margin ** 2)
        percent_margin = 100.0 * math.sqrt(under_root) / total
        slices.append(
            {
                "key": key,
                "label": GROUP_LABELS[key],
                "estimate": estimate,
                "margin": margin,
                "percent": 100.0 * share,
                "percent_margin": percent_margin,
                "color": COLORS[key],
            }
        )

    added = sum(item["estimate"] for item in slices)
    if added != total:
        raise SystemExit(
            f"The slices add to {added:,}, but the published total is {total:,}."
        )
    return total, total_margin, slices


def draw_chart(total, total_margin, slices, out_path: Path):
    """Save a pie chart with labels in a legend, not color alone."""
    plt.rcParams["font.family"] = "DejaVu Sans"

    fig, ax = plt.subplots(figsize=(12.4, 7.0), dpi=120)
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#ffffff")

    wedges, _ = ax.pie(
        [item["estimate"] for item in slices],
        colors=[item["color"] for item in slices],
        startangle=90,
        counterclock=False,
        wedgeprops={"edgecolor": "#1b1b1b", "linewidth": 1.8},
    )

    legend_labels = [
        f"{LEGEND_LABELS[item['key']]}\n{item['percent']:.1f}% ± {item['percent_margin']:.2f}"
        for item in slices
    ]
    legend = ax.legend(
        wedges,
        legend_labels,
        loc="center left",
        bbox_to_anchor=(0.98, 0.52),
        frameon=False,
        fontsize=12,
        handlelength=1.4,
        handleheight=1.4,
        labelspacing=1.15,
        borderaxespad=0.2,
    )
    for text in legend.get_texts():
        text.set_color("#1b1b1b")

    ax.set_title(
        "How Maryland workers got to work, 2020–2024",
        loc="left",
        fontsize=18,
        color="#1b1b1b",
        fontweight="bold",
        pad=14,
    )

    fig.text(
        0.01,
        0.075,
        f"Share of {total:,} workers age 16 and over (±{total_margin:,.0f}). "
        "Percents are rounded to one decimal place.",
        fontsize=11,
        color="#1b1b1b",
        ha="left",
    )
    fig.text(
        0.01,
        0.03,
        "U.S. Census Bureau, 2020–2024 American Community Survey 5-Year Estimates, Table B08301.",
        fontsize=11,
        color="#1b1b1b",
        ha="left",
    )

    fig.subplots_adjust(left=0.02, right=0.52, top=0.86, bottom=0.16)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, facecolor="#ffffff", bbox_inches="tight", pad_inches=0.35)
    plt.close(fig)


def main():
    total, total_margin, slices = build_slices(load_rows())
    draw_chart(total, total_margin, slices, OUT_PATH)
    print(f"Published total: {total:,} workers (±{total_margin:,.0f})")
    for item in slices:
        print(
            f"{item['label']}: {item['estimate']:,} "
            f"(±{item['margin']:,.0f}), {item['percent']:.1f}% "
            f"(±{item['percent_margin']:.2f})"
        )
    print(f"Saved {OUT_PATH}")


if __name__ == "__main__":
    main()
{% endhighlight %}
</details>

### Accessibility Review

Use this list as developer checks when implementing the examples on this page. It complements the Accessibility section above. More requirements are on the [508 Compliance](508.html) page.

* Say what the chart means in the picture description, and include the main numbers.
* Give the chart a caption that says what it is about.
* Start the source line with "Source: U.S. Census Bureau," then name the survey, the year, and the table.
* Put the same numbers in a table with a title and column headings. A reader should be able to open that table with the keyboard.
* Write the name and percent for every slice. Color can help, but it cannot be the only way to tell the slices apart.
* Choose colors that people with color blindness can tell apart, and give text a contrast of at least 4.5:1.
* Stay near four slices. In this example, the smallest modes are added together, and each published number is still listed in the table.
* Do not use 3D effects or exploded slices. They make the sizes harder to judge.

## Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Categories overlap or do not cover the whole | Wedge sizes imply a part-to-whole relationship that the data do not support. | Use mutually exclusive categories covering the whole, or choose another chart. |
| Too many slices or similar shares | Readers struggle to compare wedge sizes. | Use a bar chart or simplify categories with a documented grouping. |
| Missing or suppressed values are omitted without explanation | The displayed shares may imply a different whole. | Explain the missing information and avoid silently rescaling the remaining categories. |
| Several pies are used for precise comparisons | Readers must compare angles across separate circles. | Consider bars with a common baseline. |
| 3D effects or exploded slices distort the display | Perceived wedge sizes can differ from the data. | Use a flat chart without large gaps. |
| Color or hover is the only way to obtain information | Some readers cannot identify categories or access details. | Provide labels, descriptive alt text, and an accessible data table. |
| A visual difference is treated as statistically significant | Readers may draw conclusions unsupported by the estimates. | Provide relevant uncertainty and explain any significance testing. |

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
 
* [Donut Chart](donutchart.html): another part-to-whole layout that can show a total in the center.
* [Bar Chart](barchart.html): often a clearer choice when the goal is to compare category sizes rather than shares of a whole.
* [Stacked Bar Chart](stackedbarchart.html): a better alternative when comparing composition across more than two groups.
* [Notes](note.html): how to document suppression, missing categories, and other caveats next to the chart.
* [Color](color.html): contrast and color-vision guidance for wedge fills and labels.
* [508 Compliance](508.html): general accessibility requirements for charts and text.
