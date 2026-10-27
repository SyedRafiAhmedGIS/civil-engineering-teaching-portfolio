# Software and Tools — Verified List

Curated by **Syed Rafi Ahmed** ([github.com/SyedRafiAhmedGIS](https://github.com/SyedRafiAhmedGIS)).
Part of the [resources index](README.md). Every tool below is free or offers a meaningful free

**Ownership note:** every entry below links to the original external source; nothing on this page is hosted, mirrored, or copied here. Licensing and verification details: see the [resources index](README.md).
tier, and each one is either used directly in this repository's code or recommended to students
as the professional next step.

## Desktop GIS

- [QGIS](https://qgis.org) — the open-source desktop GIS in which all Introductory GIS labs are
  taught and all course screenshots are produced. Its identical behaviour across operating
  systems means a single set of lab instructions works for every student.
- [GRASS GIS](https://grass.osgeo.org) — veteran open-source geoprocessing suite with strong
  raster and terrain modules. Demonstrations only: students see that the
  QGIS interface is one door into a larger ecosystem.

## Spatial databases and web services

- [PostGIS](https://postgis.net) — spatial extension for the PostgreSQL database, turning
  standard SQL into a spatial query engine. Teaching use: one live query in the data-models
  lecture is enough to motivate the database unit of the course.
- [GeoServer](https://geoserver.org) — open-source map server publishing layers as WMS and WFS.
  Advanced learners configure it once in class to understand how a published map service feeds
  the web maps they use daily.

## Python for engineering data (used in this repository)

- [Python](https://www.python.org) — the language of every script in
  [`code/`](../code/). Chosen for its readable syntax, which lets first-year students focus on
  the engineering calculation rather than the programming.
- [NumPy](https://numpy.org) — array computation and statistics; powers the IDW interpolation
  and gridding inside [`code/gis_demo/`](../code/gis_demo/). Students meet it as the engine
  behind the maps they generate.
- [pandas](https://pandas.pydata.org) — tabular data analysis; reads the laboratory CSV
  worksheets and computes group-wise strength summaries in
  [`code/concrete_analysis/`](../code/concrete_analysis/). The direct bridge from the
  spreadsheet skills students already have.
- [Matplotlib](https://matplotlib.org) — plotting library behind every chart and the animated
  test demonstrations in [`docs/demo/`](../docs/demo/). Its figure code is reused in class to
  teach what a proper engineering plot must label.
- [GeoPandas](https://geopandas.org) — spatial vectors in Python; the first assignment after
  the dependency-free GIS demo is to repeat one analysis in GeoPandas and compare the code.
- [Shapely](https://shapely.readthedocs.io) — geometry operations (buffers, intersections,
  unions) that GeoPandas builds on. It demonstrates why the buffer distance question
  has an exact geometric answer.
- [Rasterio](https://rasterio.readthedocs.io) — reading and writing geospatial rasters.
  Recommended to advanced learners who want to handle the satellite downloads from the
  [datasets page](datasets.md) in Python rather than in QGIS.
- [Folium](https://python-visualization.github.io/folium) — Python bindings for Leaflet web
  maps. As a take-home extension, students turn one course map into an interactive web map —
  consistently the most enjoyed exercise.
- [Jupyter](https://jupyter.org) — the notebook environment in which all teaching notebooks are
  written. Its mix of narrative and executable code models the lab-report format the course
  requires.
- [Google Colab](https://colab.research.google.com) — free hosted notebooks that run the four
  country-standard concrete notebooks and the GIS demo with zero installation, directly from
  the badges in the main [README](../README.md).

## Structural and analysis extras

- [OpenSees](https://opensees.berkeley.edu) — the open-source finite-element framework from the
  Pacific Earthquake Engineering Research Center. For structural-minded students: the free
  path beyond spreadsheet structural analysis.
- [SkyCiv](https://skyciv.com) — browser-based structural analysis with a free tier. Its
  zero-install access lets every student verify one frame problem from the mechanics service
  course without a licence barrier.
