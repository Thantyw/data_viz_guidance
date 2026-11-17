# Combined Census guidance with executed ACS additions

Prepared for Maya R. Jackson, November 14, 2026. Status: proposed sponsor-review contribution; publication checks remain.

The ten assigned pages now display **28 original illustrations plus 12 ACS figures**. The original examples retain their varied datasets, dates and teaching purposes. ACS supplies a separate reproducible teaching workflow. All 28 original image files are active under their original filenames, and their bytes are unchanged.

## Start the review

Read Section 7 on each page: original examples first, additional ACS demonstration second, then how they work together. Section 7.2 includes actual figures, source/period/universe notes, interpretation, selected values, and links to readable HTML tables and CSV downloads. Keep the repository directory structure when reviewing or submitting it: an individual Markdown file cannot carry its image assets by itself.

- `review/PAGE_AND_ASSET_INDEX.md`: ten-page inventory and preview links.
- `review/previews/`: static HTML reading copies, with local assets resolved. These are reviewer previews, not a production Jekyll build.
- `review/baseline_originals/`: unchanged original Census Markdown pages.
- `review/proposed_before_combination/`: proposed guidance used in the combination.
- `review/diffs/`: exact original-to-current differences.
- `review/page_inventory.json`: page/figure/data mapping and original asset hashes.
- `assets/examples/`: integrated ACS PNG/SVG, data, tables and supplied per-job metadata.
- `review/evidence/ACS_Actual_Results/`: unchanged files extracted from the supplied results ZIP.
- `review/evidence/RUN_ALL_ACS_EXAMPLES_v03_executed.ipynb`: the supplied notebook with saved outputs. It has no execution counters; the results ZIP contains the completed-run record.
- `ACS_Examples_Builder/`: supplied Python workflow. Its additional Small Multiples job is retained as supporting material; this package edits only the ten assigned website pages.

## Evidence and changes

The supplied run completed November 10, 2026 UTC. All eleven runner jobs, including the ten assigned examples, report `generated_unreviewed`. This execution status is preserved in the evidence. Integration review adds sixteen saved-data checks: income interval arithmetic and cross-page agreement, poverty ratios, chained dollar conversions, population partitions, boxplot summaries and histogram frequencies. All passed. The checks establish consistency of the supplied files; they do not constitute a fresh API retrieval or a full independent source audit.

Four ACS figures were rebuilt from the supplied CSVs to separate labels/legends and footers. The two stacked-area figures now share a 0–25 million scale. No values were changed. The unchanged run outputs remain in the evidence directory. `review/rebuild_reviewed_acs_layouts.py` reproduces these four layouts without API access. `review/ACS_LAYOUT_REVIEW.json` records the changes and the versions used.

The readable data tables add captions and explicit row/column header associations. Image alternatives and interpretation appear beside each figure. This improves the review package but does not establish Section 508 conformance.

## Remaining work before publication

- Review the published pages with assistive technology and complete contrast, noncolor, text resize/reflow, reading-order and keyboard checks where applicable. Original illustrations also require review; their preservation is not a conformance endorsement.
- The nested-category CSV contains plotted percentages and a derived overlap count, but omits raw B03002 child counts and raw DP03 counts. Export those fields on the next run to support an independent audit of the full category arithmetic. The code contains category checks, but the export alone cannot rerun all of them. No MOE was calculated for the derived overlap.
- Verified R counterparts and Python/R numerical agreement remain outstanding if required for the sponsor's accepted scope.
- Run the production Jekyll build and test the live links and rendering under the configured `/data_viz_guidance` base URL.
- Obtain sponsor review of the proposed guidance, source interpretation and publication choices.

## Retained original improvements

Original text and visuals are preserved alongside clearer selection, statistical and accessibility guidance. The world-population area illustration is identified as stacked; the original histogram’s demographic-analysis high/middle/low series are distinguished from ACS MOEs; insurance examples retain their separate dates; interval overlap is not treated as a universal significance test; and original min–max boxplot whiskers are distinguished from the ACS 1.5 × IQR convention. Do not merge values across these different sources or relabel a historical image as a new ACS output.

## Reproduce the integrated review

From this repository root, run:

```sh
python review/check_supplied_acs_data.py
python review/rebuild_reviewed_acs_layouts.py
```

These commands use the included real-data CSVs and require Python, pandas, NumPy and Matplotlib. They make no API requests. The supplied notebook and builder support a separate new retrieval using the analyst's own credentials. API keys must not be saved in source, notebooks, logs or manifests.
