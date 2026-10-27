# `code/notebooks/` — Country-specific Google Colab notebooks

Each notebook is a complete, self-contained lab session for the concrete slump and
compressive-strength tests, configured for one national standards family:

| Notebook | Standards family | Specimen | Slump classes used |
|---|---|---|---|
| `concrete_testing_US_ASTM.ipynb` | ASTM C143 + ASTM C39 | 150 x 300 mm cylinder | Typical target ranges (ASTM has no S-classes) |
| `concrete_testing_UK_BSEN.ipynb` | BS EN 12350-2 + BS EN 12390-3 + EN 206 | 150 mm cube | S1-S5 |
| `concrete_testing_India_IS.ipynb` | IS 1199 + IS 516 + IS 456 | 150 mm cube | IS workability buckets |
| `concrete_testing_Bangladesh_BDS.ipynb` | BDS EN 12350-2 + BDS EN 12390-3 (BNBC context) | 150 mm cube | S1-S5 |
| `gis_intro_demo.ipynb` | Concept demo | — | — |

## How to use

**In Google Colab (recommended):** open the notebook from the `code/notebooks/` folder in
GitHub and click the *Open in Colab* badge at the top of the README, or upload the file at
<https://colab.research.google.com/>. The notebook runs immediately on the built-in
synthetic dataset.

**Using your own data:** every *Data* cell (1) builds a CSV template
(`upload_template_*.csv`), previews it in the notebook and, in Colab, downloads it to your
computer automatically; (2) shows a persistent **Upload** button (ipywidgets) that does not
block *Runtime > Run all*; and (3) after you pick your file(s) and re-run the cell that
follows, it validates the columns, loads your data in place of the demo data, and prints a
preview of what was loaded. Upload nothing and the notebook simply keeps the built-in
synthetic dataset, so *Run all* always completes on its own. Locally (Jupyter), the same
cells work - templates are saved next to the notebook and the button appears whenever
ipywidgets is installed.

**Notebook cell order matters** — run cells top to bottom: title → standard summary → setup
→ data → analysis → interpretation → self-check quiz → references.
