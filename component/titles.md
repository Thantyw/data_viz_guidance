---
layout: default
title: Titles and Subtitles
permalink: title.html
description: "Developer guidance for writing clear, accurate, and accessible titles and subtitles for Census data visualizations."
tags:
  - Accessability
  - Informational
---

# Titles and Subtitles

Titles and subtitles help readers understand what a Census data visualization presents before they begin interpreting its marks, values, geographic patterns, or comparisons. A well-written title identifies the subject and analytical focus. A subtitle adds the context needed to interpret the information correctly, such as the reference period, population, geographic coverage, units, or an important qualification.

This page provides practical guidance for developers creating charts, maps, tables, and dashboards with Census data. It distinguishes statistical accuracy and transparency principles in the U.S. Census Bureau's *Statistical Quality Standards* from additional design recommendations intended to improve usability. The standards apply to Census Bureau information products within their stated scope; the layout and wording suggestions below are developer best practices, not prescribed title templates or character limits.

## 1. Purpose and Overview

A title tells readers what the visualization is about. It should identify the subject, measure, and analytical focus without overstating what the data demonstrate. A subtitle provides supporting context that would make the title too long or difficult to scan.

The two elements serve different purposes:

- **Title:** Names the subject and measure, and when useful signals the main comparison or analytical focus.
- **Subtitle:** Supplies context needed to interpret the displayed data, such as the population or statistical universe, geographic level, reference period, units, source population, or a concise qualification.

Together, they establish an interpretation frame. Before reading a visualization, a reader should be able to determine:

- What is being measured?
- Which people, households, businesses, governments, or other units are represented?
- Where does the data apply?
- What time period does it cover?
- What do the values represent (counts, percentages, rates, ratios, dollars, or another unit)?
- Is the visualization showing an estimate, a projection, a comparison, or a derived measure?
- Are there important limitations that change how the results should be read?

Titles should describe the data rather than imply a cause. For example, a chart showing an increase in median age does not, by itself, establish that declining fertility caused the increase. Causal explanations belong in supporting analysis only when the evidence and methodology support them.

A title should not be expected to carry every methodological detail. Put the most important interpretive information in the title or subtitle, then use captions, notes, footnotes, source statements, or linked methodology documentation for details that readers may need to verify or understand.

## 2. When to Use

Use a clear title for charts, maps, tables, dashboard visuals, and standalone data graphics. The title should remain understandable when the visualization is viewed outside its original report or dashboard context.

A useful title normally identifies:

- **Subject:** The topic, population, or characteristic being examined.
- **Measure:** The variable or statistic displayed, such as total population, median household income, or percentage of households with broadband access.
- **Analytical focus:** The comparison, distribution, trend, or relationship the visualization is designed to show, when this can be stated accurately.

Use a subtitle when the title alone would leave a meaningful ambiguity. Subtitles are particularly useful when a Census measure needs a reference period, population or universe, geographic level, unit, or qualification to be interpreted correctly.

| Visualization type | Title should identify | Subtitle may clarify |
|---|---|---|
| Chart | Measure and comparison or trend | Reference period, population, units, geography, and whether values are estimates |
| Map | Measure and geographic subject | Geographic level, reference period, population, classification or denominator context |
| Table | Subject and tabulated measure | Universe, units, reference period, geography, and table scope |
| Dashboard | Overall subject or analytical purpose | Current reporting period, selected geography, population, or active filters |

**Census data use cases**

- A population chart may use a title such as *Total Population by State* and a subtitle identifying the year and whether values are counts or estimates.
- A labor force map may need the reference period, geographic level, and definition of the labor force measure.
- An American Community Survey (ACS) table visualization may need to identify the population universe and whether the displayed values are estimates or percentages calculated from estimates.
- A dashboard with user-selected geography or year may need a dynamic subtitle so the visible context changes with the data.

A subtitle is optional when the title and nearby labels already provide enough context. Do not add one simply to fill space or repeat information that is clearly and consistently displayed elsewhere.

## 3. When to Use an Alternative

A title or subtitle may not be the best place for every explanation. Use another presentation method when the information is too detailed, changes independently of the visualization, or needs a specific visual relationship to a data point.

Consider these alternatives:

- **Caption:** Use a caption for a short explanation of the visualization's purpose, scope, or interpretation that does not fit naturally in the title hierarchy.
- **Annotation:** Attach a concise explanation to a specific value, event, break in a time series, or unusual pattern. An annotation is more effective than a general subtitle when the explanation applies to only one part of the visualization.
- **Footnote or data note:** Use notes for definitions, denominator details, rounding, exclusions, suppression, or other qualifications that readers need but that would make the subtitle unwieldy.
- **Source statement:** Identify the data source and release or table details in the source area or documentation, rather than crowding the title with a citation.
- **Methodology or definitions panel:** Present lengthy universe definitions, formulae, survey design information, and comparability limitations separately. Link to the documentation from the visualization when appropriate.
- **Accessible descriptive text:** Provide a concise text description or longer explanation outside the visual title when readers need a fuller account of the chart's structure or main findings.

Avoid dynamic titles that attempt to narrate every filter, selected category, and data condition. If the selection state becomes complex, use a stable title and a separate filter summary, subtitle, or visible selection panel. If no selection or an ambiguous selection is active, display a clear fallback such as *All selected states* or *Multiple years selected* rather than an empty label or misleading default.

Additional context is especially important when the visualization could otherwise imply a comparison that is not supported, such as comparing different population universes, incompatible periods, or estimates with different definitions. A short title cannot compensate for a flawed comparison. Correct the analysis and explain the limitation in a note or methodology statement.

## 4. Choosing Between Alternatives

| Analytical Goal | Alternative Visualization | Why It May Be Preferable |
|---|---|---|
| Identify exactly what is measured | Descriptive title rather than a generic title | A descriptive title names the measure and subject; a generic label such as *Population* leaves readers to infer the question and scope. |
| Add context without overloading the heading | Title with a concise subtitle rather than title alone | The title remains scannable while the subtitle supplies period, universe, geography, or units. Use title alone when the context is already explicit nearby. |
| Reflect interactive selections | Dynamic subtitle or filter summary rather than a fully dynamic title | A stable title preserves the subject while a separate context line can update with filters without creating long or awkward headings. |
| Explain a specific event or value | Annotation rather than a general subtitle | An annotation can point directly to the relevant feature; a subtitle may incorrectly suggest that the explanation applies to the entire visualization. |
| Explain definitions or methodological qualifications | Footnote, data note, or linked methodology rather than a detailed subtitle | Longer information is easier to read and maintain outside the title hierarchy. The note can provide precise definitions without making the heading difficult to scan. |
| Distinguish related graphics in a dashboard | Shared title with specific subtitles rather than repeated generic titles | Consistent naming makes the dashboard easier to navigate while each subtitle identifies the individual measure, period, or population. |

## 5. Data Requirements and Statistical Considerations

Developers should identify the statistical meaning of the data before writing a title or subtitle. Do not generate wording solely from a display label or field name. Confirm the measure, units, universe, geography, period, calculation, and limitations from the dataset's metadata and technical documentation.

### Measure and units

Determine the exact measure shown:

- **Counts:** Identify what is counted (for example, people, households, housing units, or establishments).
- **Percentages:** Identify the numerator and denominator or population universe. A percentage of households is not interchangeable with a percentage of people.
- **Rates:** State the event or population to which the rate applies and the rate base when needed (for example, per 1,000 people).
- **Ratios:** Confirm the numerator and denominator and whether the ratio is expressed as a percentage, decimal, or rate.
- **Dollar values:** Identify whether values are nominal or adjusted for inflation, and the relevant dollar year where applicable.
- **Medians and averages:** Use the statistic's correct name. Do not call a median an average unless the term is explicitly defined and appropriate.

Use consistent terminology and units across the title, subtitle, axes, legends, table headers, and tooltips.

### Geography and reference period

Identify the geographic level and selected area precisely: nation, state, county, county subdivision, place, tract, or another geography. Avoid ambiguous labels such as *local areas* when the data are actually county-level.

State the reference period using the dataset's official period convention. ACS 1-year and 5-year estimates represent different products and should not be presented as interchangeable. A multi-year ACS estimate describes a period of data collection; it should not be described as a single-year estimate. For time comparisons, verify that periods, definitions, geographies, and products are comparable.

### Population or statistical universe

Confirm who or what is included in the measure. Census tables often have a defined universe, such as total population, households, occupied housing units, civilian labor force, or employer firms. Include the universe in the subtitle when omitting it could lead readers to interpret the measure as applying to a different population.

### Denominators and calculations

For derived percentages, rates, ratios, or indexes, document the numerator, denominator, and calculation method. If the denominator changes across geographies or periods, ensure the title does not imply a comparison of equivalent populations when it is not. When a percentage is calculated from table estimates rather than directly supplied, retain enough metadata to describe the calculation accurately.

### Missing, suppressed, or unavailable data

Determine how missing, suppressed, not applicable, and unavailable values are represented. Do not describe a blank or suppressed value as zero. If these conditions materially affect interpretation, explain them in a note or legend and ensure dynamic titles do not imply complete coverage.

### Margins of error and statistical uncertainty

For sample-based estimates, consider margins of error (MOEs), confidence intervals, standard errors, and other relevant measures of uncertainty. A title should not imply a meaningful difference or trend solely because point estimates differ. If the visualization makes a statistical conclusion, the analysis must support it with appropriate uncertainty measures and methods that account for the sample design and multiple comparisons where applicable.

The Census Bureau's *Statistical Quality Standards* (revised September 29, 2026) states in Requirement E1-4 that conclusions derived from sample data must be supported by appropriate measures of statistical uncertainty. Requirement E2-2 also calls for accurate, reliable, transparent, and unbiased reporting. Requirements for uncertainty information vary by information-product type; developers should consult the applicable standard rather than assume that every title must contain a margin of error. For maps, the standard notes that uncertainty need not necessarily be portrayed on the map, but if it is not, a URL to the relevant uncertainty information must be provided. See E1-4 and E2-2 in the current standards.

### Comparability and limitations

Before using words such as *increase*, *decrease*, *higher*, *lower*, *leading*, or *outnumber*, verify that the data support the comparison. Check:

- Whether the same definitions, universes, geographic boundaries, and estimation methods apply.
- Whether a geographic boundary or classification changed during the period.
- Whether estimates come from comparable ACS products and reference periods.
- Whether differences are statistically distinguishable when the analysis makes inferential claims.
- Whether the measure is an estimate, projection, modeled result, or observed count.
- Whether any limitations, breaks in series, or data quality issues affect the interpretation.

Omitting these details can make a technically correct number misleading. For example, a percentage without its universe can appear to describe all residents when it applies only to households. A title saying *State X has the highest rate* may overstate the evidence if the differences are not statistically meaningful or the denominators are not comparable.

## 6. Visualization-Specific Considerations

This section focuses on decisions specific to titles and subtitles. Follow the repository's separate guidance for general typography, accessibility, responsive scaling, color, labels, and source practices.

### Wording and hierarchy

- Use plain, specific language. Prefer *Median Household Income by State* over *Income Overview*.
- Put the subject and measure first. Add the analytical focus when it improves understanding.
- Avoid causal language unless the analysis supports a causal conclusion.
- Use a subtitle for context, not as a second headline competing with the title.
- Preserve the original recommendation to spell out words rather than use symbols in titles and subtitles; for example, write *State and Local Governments* rather than *State & Local Governments*.
- Avoid unnecessary punctuation, abbreviations, and internal dataset field names.

The title should have stronger visual emphasis than the subtitle. A common design approach is to use a larger or heavier title and a smaller, regular-weight subtitle. Keep both close enough to the visualization that readers understand they belong together. Titles should appear above the visualization or as the first element directly adjacent to it; subtitles should appear directly below the title.

### Length and wrapping

The existing repository guidance recommends caution when titles and subtitles exceed two lines each. This is a readability recommendation, not a formal Census Bureau character or word limit. Rewrite unnecessarily long headings and move supporting detail to notes or documentation. Test line wrapping at narrow widths and avoid truncation that removes the geography, period, or other essential context.

### Dashboards and responsive layouts

Use consistent title conventions across related dashboard visuals. Repeated measures should use consistent names, units, capitalization, and period formatting. For small multiples, use a shared title and concise panel labels where that avoids repeating the same long heading.

On responsive layouts, verify that the title remains associated with the correct visual and that wrapping does not collide with controls, legends, or neighboring cards. If a dashboard uses a global title, keep local titles specific enough that a visual still makes sense when exported or shared independently.

### Dynamic titles and subtitles

Dynamic text should describe the data currently displayed, not merely repeat a default selection. Include the selected geography, period, measure, or population only when it materially changes the interpretation.

Recommended behavior:

- One selected geography: show its full, recognizable name and level.
- Multiple selected geographies: use a clear summary such as *Selected counties* or *Multiple states*; do not concatenate a long list into the title.
- All geographies: say *United States* or *All available geographies*, as appropriate.
- One selected period: show the exact year or period.
- Multiple periods: describe the range or say *Multiple periods selected*.
- No selection or unavailable metadata: use a truthful fallback rather than a blank value.
- Conflicting filters: do not produce a title that implies a single geography or period when the data contain several.

Dynamic text should be tested against filter combinations, empty results, reset states, and exported views. The title and subtitle must remain synchronized with the actual data query.

## 7. Census Data Example

- **Analytical question:** What is the estimated total population of the United States in the 2024 American Community Survey 1-year data?
- **Dataset and table:** 2024 American Community Survey 1-Year Estimates, Detailed Tables, table B01003 (Total Population); estimate variable `B01003_001E`.
- **Source:** [2024 ACS 1-Year API – B01003, United States](https://api.census.gov/data/2024/acs/acs1?get=NAME,B01003_001E&for=us:1). See also the [ACS data profiles and detailed tables](https://www.census.gov/programs-surveys/acs/data.html).
- **Geographic level:** United States.
- **Reference period:** 2024 ACS 1-year estimates.
- **Measure and units:** Total population, people (count); the estimate variable is `B01003_001E`.
- **Reason for selection:** The measure is a straightforward count with a clearly defined universe (total population). The title identifies the measure and geography; the subtitle identifies the ACS product and reference period.
- **Limitations:** ACS values are survey estimates, not an exact enumeration of every person. Users should consult the table's margin of error and ACS methodology when assessing precision. The example specifies the 1-year product and should not be treated as interchangeable with the ACS 5-year estimates. The API request identifies the estimate field; it does not provide an illustrative or fabricated estimate in this guidance.

**Preferred title**

> Total Population of the United States

**Preferred subtitle**

> 2024 American Community Survey 1-Year Estimates · People

This wording identifies the subject, geographic scope, source product, reference period, and unit. It does not imply a trend, cause, or comparison that the visualization does not establish. If the visualization compares this estimate with another geography or period, the subtitle or a nearby note should identify the comparison scope and the relevant uncertainty information.

### Title and subtitle comparison

| Left: Failed Example | Right: Preferred Example |
|---|---|
| **Title:** Population<br>**Subtitle:** Latest data | **Title:** Total Population of the United States<br>**Subtitle:** 2024 American Community Survey 1-Year Estimates · People |
| **What is missing:** The measure is vague, the geography is not identified, and *latest* is not a reproducible reference period. | **What was corrected:** The measure, geography, data product, period, and unit are explicit. |
| **Why it is ineffective:** Readers cannot tell whether the visual shows people, households, a rate, or another population measure. | **Why it is better:** Readers can interpret the displayed count and identify the estimate period before examining the values. |

| Left: Failed Example | Right: Preferred Example |
|---|---|
| **Title:** Why the Population Is Growing<br>**Subtitle:** More people are moving to the area | **Title:** Change in Total Population by County<br>**Subtitle:** 2019–2024 estimates; differences are descriptive and do not establish cause |
| **What is missing:** The wording asserts a cause that a population comparison alone cannot establish. | **What was corrected:** The title describes the comparison without attributing a cause. |
| **Why it is ineffective:** It turns a descriptive visualization into an unsupported causal claim. | **Why it is better:** It states what is measured and avoids implying that the chart explains why the change occurred. |

No example values are supplied here. Developers should retrieve the current estimate and associated uncertainty directly from the cited Census API before building a visualization.

## 8. Developer Implementation

A reliable implementation separates the data values from the metadata used to describe them. Store title and subtitle fields alongside the visualization's measure, geographic selection, reference period, population universe, and units. This makes the text reproducible and reduces the risk of a title becoming disconnected from a filter or calculation.

### 8.1 Data Preparation

Prepare a metadata object for each visualization. At minimum, consider these fields:

| Field | Example | Purpose |
|---|---|---|
| `measure_name` | `Total Population` | Human-readable name of the measure |
| `geography_level` | `United States` | Geographic level represented |
| `geographies` | `["United States"]` | Selected geography names |
| `period_label` | `2024` | Display-ready reference period |
| `dataset_label` | `2024 ACS 1-Year Estimates` | Source product or release |
| `unit` | `people` | Count, percentage, rate, ratio, or other unit |
| `universe` | `Total population` | Population or statistical universe |
| `qualification` | `Survey estimate` | Short, necessary interpretive caveat |
| `selection_state` | `single` | Single, multiple, all, or none |

Use display labels that have been reviewed for accuracy. Do not expose raw API field names such as `B01003_001E` as the title. Keep the API variable, table ID, source URL, and metadata available for documentation and validation.

Before generating the title and subtitle:

1. Confirm that the measure name matches the field and calculation being plotted.
2. Confirm the selected geography and its level.
3. Confirm that the reference period matches the retrieved data.
4. Confirm the universe and denominator for percentages, rates, and ratios.
5. Determine whether the data are estimates, projections, or counts and whether uncertainty or a qualification needs to be surfaced.
6. Handle missing metadata explicitly. Do not substitute a guessed value or silently fall back to a different period.
7. Derive dynamic text from the same filter state used to query the visualization.

### 8.2 Python

**Packages:** Python 3.9 or later. The example uses only the Python standard library (`dataclasses` and `typing`); no third-party package is required.

**Expected input:** A metadata dictionary containing a measure name, geography, reference period, dataset label, unit, universe, and optional selection state or qualification.

**Expected output:** A dictionary with a descriptive `title` and a context-rich `subtitle`. The function handles single, multiple, all, and unselected geographic states without inserting a misleading default.

```python
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class VisualizationContext:
    # Human-readable labels; do not use raw Census API field names here.
    measure_name: str
    dataset_label: str
    period_label: str
    unit: str
    universe: Optional[str] = None

    # Use the geographic names that match the data currently displayed.
    geographies: Optional[List[str]] = None
    geography_level: Optional[str] = None

    # Expected values: "single", "multiple", "all", or "none".
    selection_state: str = "single"

    # Optional short caveat, such as "Survey estimates".
    qualification: Optional[str] = None


def build_title_and_subtitle(context: VisualizationContext) -> dict:
    """Create display text from verified visualization metadata."""

    # Resolve geography from the actual selection state.
    if context.selection_state == "single":
        geography = (
            context.geographies[0]
            if context.geographies and len(context.geographies) == 1
            else context.geography_level or "Selected geography"
        )
    elif context.selection_state == "multiple":
        geography = (
            f"Selected {context.geography_level.lower()} areas"
            if context.geography_level
            else "Multiple geographies"
        )
    elif context.selection_state == "all":
        geography = "United States" if context.geography_level == "nation" else "All available geographies"
    else:
        geography = "Geography not selected"

    # Keep the title focused on the measure and geographic subject.
    title = f"{context.measure_name} in {geography}"

    # Build the subtitle from the source product, period, and unit.
    subtitle_parts = [
        context.dataset_label,
        context.period_label,
        context.unit,
    ]

    # Add the universe only when it provides useful context and is not
    # already the same as the measure name.
    if context.universe and context.universe.lower() not in context.measure_name.lower():
        subtitle_parts.append(f"Universe: {context.universe}")

    # Include a short qualification when the data require it.
    if context.qualification:
        subtitle_parts.append(context.qualification)

    subtitle = " | ".join(part for part in subtitle_parts if part)

    return {"title": title, "subtitle": subtitle}


# Example metadata for the Census API table B01003_001E.
# This example demonstrates wording only; it does not hard-code an estimate.
context = VisualizationContext(
    measure_name="Total Population",
    dataset_label="2024 American Community Survey 1-Year Estimates",
    period_label="2024",
    unit="People",
    universe="Total population",
    geographies=["United States"],
    geography_level="nation",
    selection_state="single",
    qualification="Survey estimate",
)

text = build_title_and_subtitle(context)
print(text["title"])
print(text["subtitle"])
```

**Expected output**

```text
Total Population in United States
2024 American Community Survey 1-Year Estimates | 2024 | People | Survey estimate
```

For a publication-ready implementation, developers may prefer the wording *Total Population of the United States* and omit the duplicated year if the dataset label already includes it. The example keeps the metadata components visible to demonstrate how the function assembles them. Adjust the formatter to the repository's preferred editorial style, then test the output against the actual data and filter state.

To adapt this example to another Census table, update the measure name, dataset label, period, unit, universe, and geography metadata from that table's official documentation. If the measure is a percentage or rate, include its denominator definition in the universe or qualification field, or provide a nearby note when the definition is too long for a subtitle.

### 8.3 Reproducibility and Adaptation

Keep the title-generation logic separate from data retrieval and chart rendering. A reproducible workflow should:

1. Retrieve data and metadata from a documented Census source.
2. Apply geography, period, and measure filters.
3. Validate that the resulting data match the metadata.
4. Generate title and subtitle text from the same filter state.
5. Render the visualization and text together.
6. Test single, multiple, all, empty, and invalid selection states.
7. Record the source table, variable, API request, retrieval date, and any transformations in project documentation.

**Adapting to other Census data**

- For another dataset, replace the measure and universe labels with the dataset's official definitions.
- For county, tract, or place-level data, include the geographic level and ensure the displayed geography names match the selected records.
- For multi-year estimates, label the complete period using the source's convention rather than presenting it as a single-year value.
- For derived measures, document the numerator, denominator, and formula. Do not label a derived percentage as a direct Census percentage unless it is provided as such.
- For maps and tables, keep the same contextual fields even if the visual design places some information in a map subtitle, table note, or caption instead.

**Dynamic selection behavior**

When multiple filters are active, prioritize the filters that materially change interpretation. Do not list every filter in the title. Use a stable title for the measure and a concise subtitle or separate filter summary for the selected geography and period. If the filter combination returns no records, show a no-data message rather than a title that implies data are present. If metadata are unavailable, use an explicit fallback such as *Reference period unavailable* and surface the issue for correction.

**Platform considerations**

- **Power BI:** Use measures for dynamic text and ensure they read the same filter context as the visual. Test single-select and multi-select slicers, cleared slicers, and cross-filter interactions. Avoid concatenating long lists of selected values into a title card.
- **Tableau:** Use calculated fields and parameters or filter-aware expressions for dynamic titles. Verify behavior when a filter is set to all values, multiple values, or no values. Use a caption or separate text object when the filter summary becomes too long.
- **JavaScript:** Generate text from the same state object used to filter the data. Update the title and subtitle after the data state is resolved, and provide safe fallback text for empty or unavailable selections. Avoid constructing headings from untrusted raw field names.

The examples in this page are implementation patterns, not required platform-specific formats. Validate the final output against the data source and applicable Census Bureau review and release requirements.

## 9. Common Errors and Misinterpretations

| Issue | Why It Matters | Recommended Correction |
|---|---|---|
| Generic title that does not describe the measure | Readers cannot tell what is being counted or compared. | Name the subject and measure, such as *Total Population by State*. |
| Missing reference period | Readers may assume the data are current or compare incompatible periods. | Include the year or full reference period in the subtitle or a clearly associated note. |
| Missing population or universe definition | A measure may be interpreted as applying to all people when it applies only to households or another subset. | Identify the universe when it affects interpretation. |
| Ambiguous geographic description | Terms such as *local areas* do not identify the geographic level. | State the actual level and selected area, such as counties or census tracts. |
| Title implies an unsupported comparison or cause | The wording can turn a descriptive pattern into an unsupported statistical or causal conclusion. | Describe the measure or observed comparison; reserve explanations for supported analysis. |
| Subtitle contains too much information | Long headings are difficult to scan and may wrap poorly on smaller screens. | Keep only essential context in the subtitle and move definitions or methods to notes or documentation. |
| Inconsistent terminology or units | Readers may think two visuals measure different concepts or may misread values. | Use consistent official measure names, unit labels, and period conventions across the product. |
| Dynamic title does not reflect applied filters | The title may describe a different geography or period from the displayed data. | Generate text from the same filter state as the data query and test all selection states. |
| Dynamic title becomes misleading when selections change | A title may imply one geography or year even when multiple values are selected. | Use explicit multiple-selection and all-selection labels; avoid displaying only the first selected value. |
| Missing or unavailable metadata is silently replaced | A guessed period or geography can misrepresent the source. | Use a visible fallback and log or flag missing metadata for correction. |
| Information is repeated in the title, subtitle, and caption | Repetition adds clutter without improving interpretation. | Assign each element a distinct role and remove duplicate wording. |
| Causal wording is used for descriptive data | A chart may show association or change but not explain why it occurred. | Remove causal language unless the analysis establishes causality. |
| MOE or uncertainty is omitted from a claim about differences | Small differences between estimates may be overstated. | Check the applicable uncertainty requirements and qualify conclusions where appropriate. |
| Suppressed or unavailable data are described as zero | Missing information is confused with a measured value. | Use the correct missing or suppression label and explain it in a note or legend. |

## 10. Publication Quality Checklist

- [ ] The title clearly identifies the subject and measure.
- [ ] The title describes the analytical focus without making unsupported causal claims.
- [ ] A subtitle is included when additional context is needed.
- [ ] The title and subtitle identify the correct units, geography, and reference period.
- [ ] The population or statistical universe is identified when it affects interpretation.
- [ ] Denominators and calculation methods are documented for percentages, rates, and ratios.
- [ ] Relevant margins of error, statistical uncertainty, and qualifications are addressed in accordance with applicable requirements.
- [ ] Missing, suppressed, or unavailable values are not presented as zero.
- [ ] The wording matches the data, source metadata, and applied filters.
- [ ] Dynamic titles handle single, multiple, all, empty, and unavailable selections accurately.
- [ ] The title is visually stronger than the subtitle, and both are placed consistently.
- [ ] Text wraps cleanly and remains readable in responsive layouts and exported views.
- [ ] Captions, annotations, footnotes, and methodology notes are used when they are more appropriate than a longer subtitle.
- [ ] Terminology and units are consistent across related visualizations.
- [ ] The source, table, variable, and reference period can be traced to official documentation.
- [ ] The visualization and its text have been reviewed for accuracy, clarity, and potential misinterpretation before publication.

---

## References and Related Resources

- U.S. Census Bureau. (2026). *Statistical Quality Standards* (Revised September 29, 2026). See especially Statistical Quality Standard E1, *Analyzing Data*; E2, *Reporting Results*; and E3, *Reviewing Information Products*. The standards establish requirements for accurate, reliable, transparent, and unbiased reporting; appropriate statistical uncertainty; and review of information products. They do not prescribe a universal title wording, subtitle format, or character limit.
- U.S. Census Bureau. *American Community Survey Data*. https://www.census.gov/programs-surveys/acs/data.html
- U.S. Census Bureau. *2024 ACS 1-Year API: Table B01003, Total Population*. https://api.census.gov/data/2024/acs/acs1?get=NAME,B01003_001E&for=us:1
