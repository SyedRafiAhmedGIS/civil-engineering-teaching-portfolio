# `code/` — Runnable teaching toolkit

This folder contains all executable material. It is intentionally decoupled from the
course documents so that the documentation remains useful even if the code is not run.

```
code/
├── concrete_analysis/        Python package for the lab manual
│   ├── standards.py          Country standard profiles (US / UK / India / Bangladesh)
│   ├── analysis.py           Strength, slump and quality-control calculations + plots
│   ├── data/                 Synthetic sample CSV datasets
│   └── tests/                Pytest suite (run with: pytest code/ -v)
├── gis_demo/
│   └── gis_intro_demo.py     Dependency-light GIS concept demo (IDW, buffers, choropleth)
└── notebooks/                Five Google Colab notebooks with country-standard profiles
```

## Design decisions

1. **Only NumPy, pandas and matplotlib are required.** Heavy geospatial stacks (GDAL,
   geopandas) are deliberately avoided so the demos run in any environment, including
   Google Colab, in seconds.
2. **One module per concept.** `standards.py` isolates the country-specific acceptance
   logic so instructors can add a new national profile without touching analysis code.
3. **Every function that produces a number has a test.** The pytest suite covers strength
   calculations, slump classification boundaries and the CSV loaders.

## Run

```bash
pip install -r requirements.txt
pytest code/ -v                        # all tests pass
python code/concrete_analysis/analysis.py
python code/gis_demo/gis_intro_demo.py
```
