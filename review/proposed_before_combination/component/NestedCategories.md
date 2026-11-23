---
layout: default
title: "Nested or Non-Mutually Exclusive Categories"
permalink: nested.html
tags: [Comparison, Distribution]
description: "Guidance for showing nested and overlapping Census categories without double counting or misleading part-to-whole comparisons."
---

# Nested or Non-Mutually Exclusive Categories

## Applying this guidance

Use the [consolidated Census Statistical Quality Standards](https://www2.census.gov/about/policies/quality/quality-standards.pdf), revised September 29, 2026, within their stated scope. Separate formal requirements from the practical design recommendations and implementation choices described here. Coordinate this guidance with [Titles and Subtitles](title.html), [Legends](legend.html), and [Sources](source.html).

## 1. Purpose and Overview

A **nested category** is a subgroup within a larger category (for example, private insurance is a subset of people with insurance). **Mutually exclusive categories** do not overlap at a defined level and universe. **Non-mutually exclusive categories** overlap: one person or item may belong to more than one category. A parent total must never be added to its own child as if they were separate observations; overlapping categories must not be stacked as a single additive whole.

Tables can communicate nesting through indentation, but chart readers may miss the hierarchy or an explanatory footnote. The denominator and membership rules must be visible where readers interpret the result.

## 2. When to Use

Use this guidance whenever charted series have a parent–child relationship, when membership can overlap, or when a comparison implies categories sum to a whole.

### Essential

- **State explicitly which categories overlap**, in an associated note, title, subtitle, annotation, or legend. Place the explanation where readers will encounter it while interpreting the chart.
- State the **universe and denominator** for every proportion, especially whether it describes all people or only people with a particular attribute.
- Identify parent totals and child categories so readers cannot mistake them for disjoint series.
- Check whether displayed groups form a mutually exclusive and exhaustive partition **before** using a 100% stacked or other part-to-whole display.

### Avoid

- Adding a parent and its child or summing overlapping categories to imply a population total.
- Using a pie or 100% stacked chart for overlapping categories without first creating an explicitly valid disjoint classification.
- Hiding a critical overlap caveat in small-print notes; implying distinct groups through color alone.

### Additional Recommendations

**Recommended:** Where defensible, construct mutually exclusive categories that reconcile to the relevant whole; label overlap explicitly; consider remainder bars, several coordinated charts, or a table when those formats communicate membership more clearly. (Consolidated from the original.)

**Not recommended:** A visually complex graphic whose group structure cannot be interpreted without substantial mental arithmetic, or any display that silently changes the denominator across panels.

## 3. When to Use an Alternative

Prefer a **structured table** when nested rows and category membership must be inspected precisely. Prefer separate labeled bars or **remainder bars** to show each overlapping category as a percentage of the *same defined universe*. Use a 100% stacked chart only for a verified mutually exclusive and exhaustive partition. Use multiple charts or small multiples when a single display obscures these distinctions.

## 4. Choosing Between Alternatives

| Analytical goal | Prefer | Why |
|---|---|---|
| Show a valid insured/uninsured split | 100% stacked bar or labeled table | Those two categories form a partition when defined for the same universe |
| Compare overlapping insurance types | Separate labeled bars/remainder bars | Each type is evaluated against a stated denominator without pretending categories sum to 100% |
| Show parent and nested subtypes | Indented accessible table or separate panels | Makes the hierarchy explicit |
| Explain multiple overlapping groups | Cross-tabulation or carefully annotated table | Displays membership and intersection explicitly where available |

## 5. Data Requirements and Statistical Considerations

Document dataset name, table/variable identifiers, reference year, geography, universe, units, category membership rules, denominator, and suppression/missing-value conventions. Distinguish **counts**, **percentages of everyone**, and **percentages of the insured**; these are not interchangeable. Do not infer category intersections from marginal totals alone.

For ACS published estimates, retain associated margins of error where applicable, distinguish sampling uncertainty from arithmetic consistency, and cross-reference [Visualizing Uncertainty](uncertainty.html). Additivity checks must respect the published variables, estimates, and Census guidance; do not assume derived estimate MOEs equal the sum of component MOEs.

## 6. Visualization-Specific Considerations

- Use consistent ordering, labels, and denominators across panels. Explicitly identify overlap in text near the graphic.
- If using remainder bars, label each bar as “has characteristic” versus “does not have characteristic” for the **same denominator**; do not stack different overlapping characteristics together.
- When showing a nested category, use indentation, headings, and explanatory labels; do not communicate nesting solely through darker/lighter colors.

### Accessibility

Provide meaningful alternative text describing **which groups overlap** and what the viewer should conclude. Include an accessible HTML table with column and row headers, group labels, counts/percentages, denominators, and relevant notes; a CSV may supplement but does not replace it. Check text contrast, noncolor cues, logical reading order, keyboard operation where applicable, and screen-reader comprehension on the published GitHub page. Review against applicable Section 508/WCAG criteria; do not assert compliance on the basis of automated tests alone.

### Design comparison

| Problematic approach | Why it matters | Preferred approach |
|---|---|---|
| Parent and child appear as equal additive segments | The same members are counted twice | Show the hierarchy explicitly or plot mutually exclusive children only |
| Public and private insurance shares form a 100% stack | A person may have both forms of coverage | Use separately labeled bars/remainder bars with a common stated universe |
| Overlap is disclosed only in a remote footnote | Readers interpret the graphic before finding the caveat | Put a visible membership note beside the chart and repeat the explanation in accessible text |
| Denominator changes from everyone to insured people between panels | Identical percentages acquire different meanings | Label each denominator and align panels only when comparisons are valid |

The original permits disclosure in notes, titles, subtitles or legends. Placing the explanation near the graphic is a practical accessibility and interpretation recommendation, not a newly asserted Census mandate. If no defensible simple chart communicates the membership, use a table.

## 7. Census Data Examples

**Primary instructional example — health insurance coverage.** The original Census guidance discusses the *Health Insurance Coverage in the United States: 2022* presentation. “Has insurance” versus “does not have insurance” can be presented as a partition of the same population, whereas **public** and **private** insurance types can overlap because a person may have more than one kind of coverage. Its original illustrations are `assets/Nested1.png` (table) and `assets/Nested2.jpg` (chart). Retain those visual references in the repository and check paths, permissions, legibility, alt text, and continuing relevance before publishing.

**Additional example — remainder bars.** The original page references [Most Parents Don’t Have Any Formal Child Care Arrangements](https://www.census.gov/library/stories/2023/11/child-care.html), illustrated as `assets/Nested3.png`. Remainder bars can compare the presence/absence of each overlapping arrangement without suggesting the arrangement categories make one additive whole.

**Reproducible ACS example.** Evaluate 2024 ACS 1-Year table **B03002 (Hispanic or Latino Origin by Race)** at the state level. The mutually exclusive origin groups “Not Hispanic or Latino” and “Hispanic or Latino” can be checked against the total. The more complex race/origin combinations should be interpreted by their official variable labels, not added across parents and children. A useful cross-classification demonstration can compare a valid partition with a deliberately labeled invalid double count. Verify variable IDs/definitions against the year-specific Census group metadata before implementing. This example illustrates a different type of category relationship from insurance overlap; it should **supplement, not replace**, the original insurance discussion.

### Reading the original insurance and child-care examples

The original insurance table uses indentation to communicate parent/child relationships. Preserve that hierarchy with semantic row headers or explicit parent labels; indentation and font weight alone are insufficient. The original chart discussion identifies four risks: inconsistent bold/light styling, subgroups that do not total 100%, an easily missed overlap note, and uncertainty about whether percentages use everyone or only insured people as the denominator.

A valid insured/uninsured split can use a labeled 100% stack for the same defined universe. Public/private insurance types should remain separate because their memberships may overlap. A remainder bar represents one category and its complement within the named universe; it does not make several overlapping types an additive partition.

The original child-care example illustrates this distinction through several remainder bars. Each bar has its own characteristic and complement, and the bars must not be summed across arrangements.

<!-- Preserve original illustration targets: assets/Nested1.png (insurance table), assets/Nested2.jpg (insurance chart), assets/Nested3.png (child-care remainder bars). The source text was recovered; the three image files were not supplied in this archive. Inspect actual figures and provide accessible equivalents before activating image links. -->

### Auditable ACS category mapping

The 2024 ACS B03002 metadata defines the following estimates. These variables demonstrate a valid partition and a nested subgroup, not the public/private insurance overlap itself.

| Variable | Published category | Relationship |
|---|---|---|
| `B03002_001E` | Total | Whole population for this table |
| `B03002_002E` | Not Hispanic or Latino | One part of the total |
| `B03002_012E` | Hispanic or Latino | The other, nonoverlapping origin part |
| `B03002_003E` | Not Hispanic or Latino: White alone | Child within `B03002_002E` |

Check `B03002_002E + B03002_012E = B03002_001E`. Adding `B03002_003E` to those two parent groups would count that child again. This is an explicitly invalid demonstration, not a new Census total. Denominators must identify whether a child share is relative to the whole population or to its parent.

For two genuinely overlapping categories A and B, marginal totals alone do not determine the intersection. Do not invent an overlap count, recode an exclusive partition without defensible data, or assume that the sum of displayed categories is the union.

## 8. Developer Implementation

### 8.1 Data Preparation

Retrieve 2024 ACS 1-Year B03002 and its official metadata. Use `B03002_001E`, `B03002_002E`, `B03002_012E`, and `B03002_003E` with corresponding annotations and available MOEs. Validate one record per selected state, finite valid counts, a positive denominator for percentages, and stable universe/period definitions. Keep a category relationship field such as `whole`, `exclusive_part`, or `nested_child`; a flat label alone does not encode membership.

### 8.2 Python

The existing draft names `examples/python/nested_categories.py`. Verify the actual file and supported input modes before publishing its implementation claims. The script should validate the valid partition, keep the nested child separate from its parent total, and produce correctly labeled figures, numerical tables, descriptive text and validation results.

### 8.3 R

Reproduce the same mapping and reconciliation in R when a verified R counterpart is available. Record its actual filename, dependencies and configuration rather than inventing a download link. Apply the same source definitions, missing-data handling and numerical tolerance in both languages.

### 8.4 Reproducibility and Adaptation

A personal Census API key is required for data queries under the [current API guidance](https://www.census.gov/data/developers/guidance/api-user-guide.Query_Limits.html). Read `CENSUS_API_KEY` from the analyst's environment. Redact the key from logged URLs, errors, saved notebooks, and manifests; do not commit it. Save source variables, the full reference period, geography, transformations, exclusions, retrieval time, and tested dependency versions with the outputs.

Save category IDs, parent IDs, membership definitions, counts, percentage denominators, applicable source MOEs, and reconciliation results. Parent-minus-child estimates and derived percentages need appropriate uncertainty methods; subtracting or adding their MOEs is not a valid general method. Label any intentionally invalid sum as a teaching example and keep it separate from published source estimates.

### 8.5 Output Verification

| Check | Expected evidence |
|---|---|
| Origin partition | Valid `002E + 012E = 001E` for each included state |
| Nesting | Valid `003E ≤ 002E ≤ 001E`; child is never added to its own parent to form a claimed whole |
| Percentages | Whole-population and within-parent shares use explicitly different, correctly labeled denominators |
| Overlap | Any intersection/union claim has supporting joint-membership data, not only marginal totals |
| Accessible explanation | The narrative and table expose the same hierarchy, denominator and overlap caveats as the chart |

## 9. Common Errors and Misinterpretations

| Issue | Why it matters | Correction |
|---|---|---|
| Parent and subgroup summed | Double counts members | Represent parent separately or use disjoint children |
| Two overlapping types shown as a 100% whole | Implies false additivity | Use separate bars/remainder bars and explicit overlap note |
| Percentage denominator unstated | Changes the meaning of the comparison | Label the universe and denominator |
| Intersections inferred from marginal totals | Intersection is not uniquely determined | Use an authoritative cross-tabulation or appropriate microdata |
| Overlap indicated only by color | Excludes some users | Add labels, notes, patterns/structure, and accessible table |

## 10. Publication Quality Checklist

- [ ] Source page and original examples reconciled against existing repository content.
- [ ] Universe, denominators, hierarchy, and overlapping groups clearly identified.
- [ ] Valid part-to-whole partitions checked; overlapping categories never combined misleadingly.
- [ ] Census table/variables and source year verified against official metadata.
- [ ] Python code executes with documented input options; source values and derived measures are checked independently.
- [ ] Figure and accessible HTML data table generated and verified.
- [ ] Alternative text, text contrast, noncolor cues, reading order, and applicable manual tests documented.
- [ ] Original image paths and external links verified on GitHub Pages.

## Related Pages and References

- [Visualizing Uncertainty](uncertainty.html)
- [Small Multiples](smallmultiples.html)
- [Stacked Area Chart](stackedareachart.html)
- [Population Pyramid](populationpyramid.html)
- [ACS B03002 variable metadata (2024 ACS 1-year)](https://api.census.gov/data/2024/acs/acs1/groups/B03002.html)
- [Most Parents Don’t Have Any Formal Child Care Arrangements](https://www.census.gov/library/stories/2023/11/child-care.html)

### Standards and Review References

Use the September 29, 2026 consolidated Census standards, especially E1-6, E2-2.3 and E3-2.4, within their stated scope. Record the implementation review, applicable statistical methods and actual rendered-site accessibility findings separately from this guidance checklist.
