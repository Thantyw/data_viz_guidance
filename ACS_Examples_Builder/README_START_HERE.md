# ACS examples for all 11 Census visualization guidance pages

## What this package does

`build_acs_examples.py` orchestrates the latest existing Python implementations to retrieve **real ACS estimates** and write PNG/SVG figures, CSV tables, and HTML/text outputs into a single folder. Each page's specialized validations remain in its original script. Nothing in this package fabricates ACS results. The package intentionally **does not include chart images**, because live API responses and a user API key were not available when the package was assembled.

## Recommended execution: VS Code, Jupyter, or local terminal

1. Unzip the package, keeping the `ACS_Examples_Builder` folder intact.
2. With Python 3.10+ installed, open a terminal in `ACS_Examples_Builder` and run:

   ```bash
   python -m pip install -r requirements.txt
   python build_acs_examples.py --dry-run
   ```

3. Obtain your own activated Census API key, then configure it securely:

   - macOS/Linux, in your shell: `read -s CENSUS_API_KEY; export CENSUS_API_KEY`.
   - Windows PowerShell: `$env:CENSUS_API_KEY = Read-Host 'Census API key' -MaskInput` (supported PowerShell versions).
   - Or use the companion Jupyter notebook, which prompts through `getpass()` without echoing the key.

4. Generate the examples:

   ```bash
   python build_acs_examples.py --output-root ./acs_generated_examples --continue-on-error
   ```

   Start with one page for quicker troubleshooting:

   ```bash
   python build_acs_examples.py --only scatter_plot --output-root ./acs_generated_examples
   ```

5. Open `acs_generated_examples/MARKDOWN_IMAGE_SNIPPETS.md` and copy the appropriate figure link into your public page. After inspecting and verifying chart contents, replace the generic image description with actual findings, e.g., observed range, outliers, or direction. Keep original Census examples alongside ACS demonstrations.

## Google Colab

Upload **the entire ZIP**, not only the notebook. Open `RUN_ALL_ACS_EXAMPLES.ipynb` in Colab, run its cells in sequence, and upload the package ZIP when prompted. The notebook extracts the public code, asks for an API key securely, and invokes the runner.

## Output layout

```
acs_generated_examples/
  assets/examples/<chart-key>/<generated PNG, SVG, CSV, HTML, text, JSON files>
  outputs/<chart-key>/<script output files>
  MARKDOWN_IMAGE_SNIPPETS.md
  execution_status.csv
  execution_manifest.json
```

The image references use `{{ '/assets/examples/<chart-key>/<chart>.png' | relative_url }}` for GitHub Pages. A source-code preview on GitHub does **not** evaluate Jekyll expressions; for raw repository preview use `../assets/examples/<chart-key>/<chart>.png` instead.

**Do not publish until the actual image files are copied to the repository** and links resolve in the rendered GitHub Pages site. SVG and HTML tables should be inspected and accessible alternatives tested, including alt text, contrast, focus order for any interactions, and meaningful data tables.

## Statistical provenance

| Page | Source | Time representation |
|---|---|---|
| Uncertainty | 2024 ACS 1-year B19013 | Cross-section: state estimates and published 90% MOE |
| Nested Categories | 2024 ACS 1-year B03002 and profile DP03 | State partition + overlapping health insurance categories |
| Line Graph | 2021–2024 ACS 1-year B19013 | Annual state income; 2024-dollar adjustments documented in code |
| Area Chart | 2021–2024 ACS 1-year B17001 | Annual state poverty counts; not stacked |
| Bubble Chart | 2024 ACS 1-year B19013, B17001, B01003 | State income, poverty percentage, and population |
| Scatter Plot | 2024 ACS 1-year B19013, B17001 | State income and poverty percentage |
| Small Multiples | 2021–2024 ACS 1-year B17001 | Annual state poverty percentages, shared axes |
| Population Pyramid | 2024 ACS 1-year B01001 | Age by sex; percentages of total population |
| Boxplot | 2020–2024 ACS 5-year B19013 | County **median estimates**, not individual household incomes |
| Stacked Area Chart | 2021–2024 ACS 1-year B01001 | Annual mutually exclusive male/female totals |
| Histogram | 2020–2024 ACS 5-year B19013 | Distribution of county **median estimates** |

**Temporal safeguard:** ACS 2020–2024 **5-year** estimates represent one pooled multiyear period, not five annual or 60 monthly observations. The annual charts use separate 2021–2024 1-year releases. The standard 2020 1-year ACS release is unavailable.

**Authentication:** The Census Bureau documents current API-key requirements at <https://api.census.gov/data/2024/acs/acs1/examples.html>. Do not put keys in tracked files. If your organization restricts API access, use the individual flexible-input scripts with appropriately documented local datasets instead.

**Status:** Runner and packaged Python syntax checked offline. Actual ACS values, successful live API retrieval, numerical output validity, rendering, and manual Section 508 checks remain to be confirmed in the user's environment. This package is a reproducible **generator**, not a collection of completed live-data images.
