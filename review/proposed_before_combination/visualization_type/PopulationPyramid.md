---
layout: default
title: Population Pyramid
permalink: populationpyramid.html
tags: [Comparison]
description: "Guidance for accessible, statistically sound age-by-sex population pyramids with reproducible ACS examples."
---

# Population Pyramid

Also known as: *age-sex pyramid*.

## Applying this guidance

Apply the [Census Bureau Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), revised September 29, 2026, within their stated scope. The chart-selection advice and implementation checks on this page explain practical design choices; they do not create additional agency mandates. Treat **Essential** items as the core design conditions for this chart, and confirm formal applicability through the program's review process.

Coordinate this page with [Titles and Subtitles](title.html), [Legends](legend.html), [Sources](source.html), and [Visualizing Uncertainty](uncertainty.html). Keep detailed component guidance in those shared pages rather than duplicating it here.

## 1. Purpose and Overview

A population pyramid displays the distribution of a population by **age and sex**, with horizontal bars extending from a shared zero line. Conventionally, males are on the left and females on the right. The shape need not resemble a triangle. Pyramids show counts or the percentage of the **whole population** in each age-by-sex group.

## 2. When to Use

### Essential

- Label the geographic area, reference period, age groups, measure, and units.
- Center the dividing axis at **zero**; use matching magnitudes and tick intervals on both sides.
- Put males on the left, females on the right, and younger groups at the bottom.
- Use a consistent age-band definition, ordinarily five-year groups with an open-ended oldest group.
- When plotting percentages, divide **every age-sex group by the total population**, not its sex-specific subtotal. Both sides must add to **100% combined**, subject to rounding.
- Use the same scale across panels when comparing multiple populations.

### Avoid

- Mixing different age-band widths or denominators without a conspicuous explanation.
- Showing a 200% combined total through sex-specific percentages labeled as whole-population percentages.
- Using unequal left and right scales, or presenting displayed negative bar positions as negative population estimates.
- Relying on color alone to communicate sex or age grouping.

## 3. When to Use an Alternative

**Recommended:** Use a population pyramid to compare age structure by sex for one population or a small number of populations with aligned age categories. Use small multiples with identical scales for comparison across states or periods.

**Not recommended:** For detailed comparisons among many geographies or many age-sex categories, an accessible table or another chart may communicate values more effectively. Use a line graph when the primary question concerns a trend over time rather than population composition at one date.

## 4. Choosing Between Alternatives

| Question | Representation | Interpretation caution |
|---|---|---|
| How many people are in each age-sex group? | Mirrored count bars | Larger geographic areas often have larger bars because population sizes differ. |
| What share of a population falls in each group? | Mirrored percent-of-total bars | Both sides together sum to 100%; labels must name the denominator. |
| How do two populations differ? | Small-multiple pyramids | Keep age bins, units, and axis scales consistent. |
| Do users need exact estimates? | Accessible data table | Provide the table alongside—not solely through—the image. |

## 5. Data Requirements and Statistical Considerations

- Data require mutually exclusive age-sex groups that exhaust the reported total population; confirm that each category is counted once.
- **2024 ACS 1-Year Detailed Table B01001 (Sex by Age)** provides total population, male and female subtotals, and detailed age-by-sex estimates. The example combines adjacent source rows to make five-year age bands, with **85 years and over** as the last open-ended band.
- Check whether male plus female equals the total, whether age groups reconcile to the sex subtotals, and whether percentages total 100% before plotting.
- ACS figures are survey estimates. Published count margins of error exist for detailed source rows; aggregating rows and calculating percentages requires appropriate variance methods. This demonstration **does not claim calculated margins of error** for aggregated bins or percentages.
- Ensure geography, dataset vintage, and definitions are comparable when creating multiple panels. A 1-year ACS release is not appropriate for every geography.

## 6. Visualization-Specific Considerations and Accessibility

Use direct panel headings, age labels, mirrored number labels and a meaningful legend. Bars should have visible separators and sufficient contrast. Male/female positions and text labels must remain interpretable without color. In a chart with multiple panels, use a shared axis to avoid artificial visual differences. Provide short alternative text explaining the display and a separate HTML data table with exact values and clear headers. Review chart readability at 200% zoom and test the rendered page by keyboard and screen reader. Accessibility is not established by image production alone.

### Row labels, spacing, and fills

Use narrow separators between age rows without making the row boundaries dominate the bars. Place age labels outside the bar field, on both outer sides when that improves comparison; do not place labels over the central data marks. Keep the shared zero baseline visually clear. Use two principal sex-category fills, with optional light/dark variation only when it improves row tracking. Text labels and left/right placement must identify the categories even without color. A highlight needs an explicit purpose and a redundant noncolor cue rather than an unexplained extra category.

### Design comparison

Use these comparisons to connect each design choice with its effect on interpretation.

| Problematic approach | Why it matters | Preferred approach |
|---|---|---|
| Each sex is normalized to 100% but the axis says percent of total population | The two sides sum to 200% under a misleading denominator label | Divide all age-sex estimates by the same whole-population total, or clearly name a different measure |
| Left bars have negative value labels | Drawing coordinates look like negative population estimates | Use negative coordinates for placement only; display positive magnitudes in labels and the table |
| Source age rows are treated as equal-width five-year bands | Unequal source intervals distort the intended age grouping | Use the documented row mapping; combine split source intervals before plotting |

### Checking the published example

Test the chart at its intended display size and with enlarged text. Follow the reading sequence from title to explanation, figure, table, and source. Check that labels and meaningful marks remain distinguishable without color and that any controls can be operated by keyboard with visible focus. Read the explanation and table with a screen reader to confirm that they convey the same measures, units, missing-data conditions, and important relationships as the chart.

Use [automated and manual accessibility testing](https://www.section508.gov/test/testing-overview/) together. A downloadable CSV supplies values but does not replace the chart's explanatory narrative; see [USWDS visualization guidance](https://designsystem.digital.gov/components/data-visualizations/). Record the page/version, tool or assistive technology, result, and corrective action. Apply the sponsor's agreed accessibility baseline rather than treating a palette simulation as a conformance test.

## 7. Census Data Examples

### Original archive example: age and sex composition in 2000

![Historical population pyramid for the United States in 2000, with males to the left, females to the right, a shared zero baseline, age labels on both outer sides, and a population scale in millions.](assets/originals/population_pyramid_original.jpg)

The source image is titled *A Century of Population Change in the Age and Sex Composition of the Nation* and displays year 2000. It uses mirrored positive magnitude labels, two main fills, and age labels outside the bar field. Notes explain that the open-ended oldest group differs across historical periods. Its source line identifies Census intercensal population estimates for 1990–2000; this is separate from the 2024 ACS example.

**Reading lesson:** the overall shape and the age concentration are visible, but the oldest intervals must be read with the figure's aggregation notes. Do not interpret the historical image as evidence that every displayed row has the same age width or that its source is ACS B01001. Use source data, rather than values estimated from pixels, for exact comparisons.

### Established design examples

Each original image demonstrates a different design choice. Preserve their educational differences instead of reducing the series to one representative figure. Verify the actual source image and captions before publication.

**Example 1 — Shared scales across pyramids.** Comparable axes are essential when reading absolute differences between panels.

![Two population pyramids displayed with a shared horizontal population scale to support meaningful comparisons.](assets/PopulationPyramid1.jpg)

**Example 2 — Distinguishing male and female bars.** The left and right sides must also be identified by text, not color alone.

![Population pyramid with male values on the left of zero and female values on the right, distinguished by labels and fill.](assets/PopulationPyramid2.jpg)

**Example 3 — Highlighting an age group.** Annotations can draw attention to particular generations without changing the scale.

![Population pyramid using a visual highlight to emphasize selected age groups.](assets/PopulationPyramid3.png)

**Example 4 — Superimposed pyramids.** Overlay comparisons require visible outlines, clear notes, and care to avoid hidden distributions.

![Two age-sex distributions superimposed in a population pyramid for comparison.](assets/PopulationPyramid4.png)

**Example 5 — Caution: excessive use of colors.** The original illustrates why too many categories or alternating fills can increase the interpretation burden.

![Population pyramid with many colored age bands; illustrates a design that may overcomplicate interpretation.](assets/PopulationPyramid5.png)

### Reproducible ACS demonstration

**Population by age and sex, selected states, 2024 ACS 1-Year B01001.** The implementation should construct the documented five-year bins, position males on the left, and use count or percent-of-total displays with a shared magnitude scale.

<!-- Verified-output image target: ![ACS population pyramid generated by the accompanying scripts; exact values are available in the generated data table.](assets/examples/population_pyramid_acs.png) -->

### Five-year age-band mapping

Use these estimate fields from [2024 ACS B01001 metadata](https://api.census.gov/data/2024/acs/acs1/groups/B01001.html). Add the listed fields within each cell. Male and female subtotals (`002E`, `026E`) and the total (`001E`) are checks, not additional age bands.

| Output age band | Male estimate fields | Female estimate fields |
|---|---|---|
| 0–4 | `B01001_003E` | `B01001_027E` |
| 5–9 | `B01001_004E` | `B01001_028E` |
| 10–14 | `B01001_005E` | `B01001_029E` |
| 15–19 | `B01001_006E` + `B01001_007E` | `B01001_030E` + `B01001_031E` |
| 20–24 | `B01001_008E` + `B01001_009E` + `B01001_010E` | `B01001_032E` + `B01001_033E` + `B01001_034E` |
| 25–29 | `B01001_011E` | `B01001_035E` |
| 30–34 | `B01001_012E` | `B01001_036E` |
| 35–39 | `B01001_013E` | `B01001_037E` |
| 40–44 | `B01001_014E` | `B01001_038E` |
| 45–49 | `B01001_015E` | `B01001_039E` |
| 50–54 | `B01001_016E` | `B01001_040E` |
| 55–59 | `B01001_017E` | `B01001_041E` |
| 60–64 | `B01001_018E` + `B01001_019E` | `B01001_042E` + `B01001_043E` |
| 65–69 | `B01001_020E` + `B01001_021E` | `B01001_044E` + `B01001_045E` |
| 70–74 | `B01001_022E` | `B01001_046E` |
| 75–79 | `B01001_023E` | `B01001_047E` |
| 80–84 | `B01001_024E` | `B01001_048E` |
| 85 and over | `B01001_025E` | `B01001_049E` |

The oldest group is open-ended and is not a five-year-width interval. Retain its full label. A missing source age cell does not become zero: flag the affected aggregate, explain the exclusion, and do not renormalize a partial population as complete. The source classifies sex as published in B01001; do not relabel that classification as a different demographic construct.

## 8. Developer Implementation

The following contract defines the intended behavior of the linked examples. Confirm the files, commands, dependencies, and generated results against the repository before publication.

### 8.1 Data Preparation

**Inputs:** 2024 ACS 1-Year B01001 state-level total, sex subtotals, detailed age-sex estimates, source MOEs, and annotations, with an explicit output age-band mapping.

Use the mapping below to construct mutually exclusive five-year age bands. Reconcile source age rows to sex subtotals and the whole-population total before computing shares. Preserve all source MOEs; derived bin or percentage uncertainty requires a separately documented calculation.

### 8.2 Python

[Python script](examples/python/population_pyramid.py) or [notebook](examples/notebooks/population_pyramid_colab.ipynb); dependencies: `requests`, `pandas`, `numpy`, and `matplotlib`. Configure `PYRAMID_STATES`, `PYRAMID_OUTPUT_DIR`, and `PYRAMID_MODE`.

### 8.3 R

[R script](examples/R/population_pyramid.R); dependencies: `httr`, `jsonlite`, and `ggplot2`. Use the same configuration, row mapping, whole-population denominator, and output order.

### 8.4 Reproducibility and Adaptation

A personal Census API key is required for data queries under the [current Census API guidance](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html). Read `CENSUS_API_KEY` from the analyst's environment. Do not include keys in source control, saved notebooks, request logs, error messages, or execution manifests; redact the `key` query parameter wherever a request URL is recorded. No shared developer credential or private file path should be required.

For each run, save the validated data, chart PNG/SVG, a semantic HTML table, descriptive-text draft, and a nonsecret manifest in the selected output folder. Include source table/variables, full reference period, geography, units, transformations, exclusions, dependency versions, and retrieval time. Pin or record versions actually tested. For identical inputs, R and Python should reproduce the same analytical values within an explicitly documented tolerance; visual styling need not be pixel-identical.

When changing years or geographies, recheck product coverage, definitions, annotations, and comparability. A successful run does not establish statistical significance or accessibility conformance.

### 8.5 Output Verification

| Check | Expected evidence |
|---|---|
| Reconciliation | All detailed source age rows appear once; age-bin totals equal the corresponding sex subtotals, and both sex subtotals equal B01001_001E |
| Percentages | For a positive total, all displayed age-sex shares sum to 100% combined within the stated rounding tolerance |
| Geometry and labels | Both sides and comparison panels use identical magnitude limits; age groups increase upward; table values remain nonnegative |

**Source-statement pattern for this example:** U.S. Census Bureau, American Community Survey, 2024 ACS 1-Year Estimates, Detailed Table B01001, selected states. Five-year age groups derived from source rows; percentage mode uses the total population as denominator. Add the specific source or reproducible request link and actual retrieval date; omit the API key. Identify derived calculations separately from published estimates.

## 9. Common Errors and Misinterpretations

| Error | Correction |
|---|---|
| Each sex summed to 100%, resulting in 200% combined | Divide every group by the total population, or change labels to clearly state a different measure. |
| Male bars interpreted as negative population | Explain that left-side negative coordinates are a drawing convention only. |
| Different axis limits used for side-by-side comparison | Apply the same limits on both sides and across panels. |
| Aggregated bins shown with unverified MOEs | Preserve the original estimates and verify variance methods before reporting derived MOEs. |
| Original image lacks accessible context | Supply a descriptive text alternative and accessible values table. |

## 10. Publication Quality Checklist

- [ ] Source, release year, geography, units, and denominator identified.
- [ ] Original image assets resolve and have meaningful alternative text.
- [ ] All age bins are nonoverlapping and exhaustive; sex and population totals reconcile.
- [ ] Male/female scales match, with 0 at the center.
- [ ] Percent-of-total pyramids sum to 100% combined (allow rounding).
- [ ] Generated PNG uses verified ACS values, and the published data table matches.
- [ ] Python and R can run in an independent environment using analyst-selected destinations.
- [ ] Contrast, zoom, keyboard, screen-reader, and noncolor tests are documented.

Related guidance: [Small Multiples](smallmultiples.html), [Line Graph](linegraph.html), [Visualizing Uncertainty](uncertainty.html).

**Data source:** [2024 ACS 1-Year Table B01001 metadata](https://api.census.gov/data/2024/acs/acs1/groups/B01001.html).

### Standards and Review References

Adapted in part from the *U.S. Data Design Standards* archive, `_visualizations/population-pyramid.md`. The source archive is an earlier site implementation; its layout, front matter, and examples require reconciliation with the current Census repository.

Use the [September 29, 2026 consolidated Census Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), especially E1-6 (replication documentation), E2-2.3 (visualization requirements), and E3-2.4 (visualization review). Retain review findings and corrections separately from the design checklist.

- [Census API query requirements](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html).
- [Section 508 testing methods](https://www.section508.gov/test/testing-overview/).
- [USWDS data visualization guidance](https://designsystem.digital.gov/components/data-visualizations/).
