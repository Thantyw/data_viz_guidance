# Diagnosing example generation failures

Version 0.2 saved a generic failure reason, obscuring the real causes. Version 0.3 prints failure summaries and saves `outputs/<page>/execution.log`, masking the configured API key. It does not claim the Census API request has been verified.

1. Upload the **v0.3 ZIP** to the notebook. If an earlier project folder is already in Colab, use **Runtime > Restart session** first, or remove the old `ACS_Examples_Builder` folder; otherwise Cell 1 may skip the ZIP upload and run the old code.
2. Use **the v0.3 notebook** and execute cells in order. Set `ONLY_PAGES = None` for all 11.
3. Inspect `execution_status.csv`, the printed failure summaries, and the `execution.log` for a failed chart. Never share an API key; logs mask the key from the configured environment.
4. If the result says `HTTP 403`, `HTTP 400`, a timeout, a DNS error, an invalid API variable, or missing output, address the specific error before changing the chart's statistical logic.
5. The generated results ZIP contains real figures only on successful live API executions. Do not publish incomplete or test outputs as Census results.
