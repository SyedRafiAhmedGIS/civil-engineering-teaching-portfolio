# Introductory GIS — Verified Teaching Resources

Curated by **Syed Rafi Ahmed** ([github.com/SyedRafiAhmedGIS](https://github.com/SyedRafiAhmedGIS)).
Part of the [resources index](README.md). Entries support the Introductory GIS syllabus in

**Ownership note:** every entry below links to the original external source; nothing on this page is hosted, mirrored, or copied here. Licensing and verification details: see the [resources index](README.md).
[`courses/introductory-gis/`](../courses/introductory-gis/) — data models, coordinate systems,
vector and raster analysis, and cartographic output.

## Tutorials and documentation

- [QGIS Training Manual](https://docs.qgis.org/latest/en/docs/training_manual/) — the official
  step-by-step QGIS tutorial, with worked exercises on import, digitising, analysis, and map
  layout. This is the practical backbone of the lab sessions: students complete the module on
  vector analysis in week four, and a local dataset is layered on top of each exercise.
- [QGIS Documentation](https://docs.qgis.org/latest/en/docs/) — the full user guide and API
  documentation for the current QGIS release. Advanced learners use it to go beyond the taught
  syllabus; report-writing students should head to the cartography chapter when their maps need
  proper legends and scale bars.

## Desktop and server GIS software

- [QGIS](https://qgis.org) — the free, open-source desktop GIS used for every lab in the course.
  Because it runs identically on Windows, macOS, and Linux, all students work in the same
  environment — a practical precondition for demonstration videos and shared rubrics.
- [GRASS GIS](https://grass.osgeo.org) — a long-established open-source suite for raster and
  vector geoprocessing. Suitable for advanced learners; its terrain modules are worth
  demonstrating when introducing interpolated surfaces, which also prepares students for the
  interpolation ideas in [`code/gis_demo/`](../code/gis_demo/).
- [PostGIS](https://postgis.net) — the spatial extension for PostgreSQL databases. Teaching
  use: a five-minute live query in the "spatial data models" lecture so students see that a
  database can answer questions such as "which parcels lie within 100 m of the flood line".
- [GeoServer](https://geoserver.org) — an open-source server for publishing map services
  (WMS/WFS). For advanced learners: a live layer published from a laptop shows the
  difference between storing data and serving data.

## Programming and cloud platforms

- [GeoPandas](https://geopandas.org) — the Python library that extends pandas to spatial
  objects, the natural next step after our dependency-light demo. Its one-liner plotting
  shows in class how a full analysis becomes reproducible as a script.
- [Google Earth Engine](https://earthengine.google.com) — a cloud platform for petabyte-scale
  satellite data analysis, free for research and education. In the final week, first-year
  students open the pre-built timelapse of their own city — a memorable demonstration of
  why remotely sensed archives matter.

## Community help

- [GIS Stack Exchange](https://gis.stackexchange.com) — the main question-and-answer site for
  GIS problems, moderated by an active expert community. *(Blocks automated checkers but opens
  normally in a browser — please verify manually.)* Students are asked to search it before
  asking software questions; reading well-posed questions is itself a lesson in troubleshooting.
