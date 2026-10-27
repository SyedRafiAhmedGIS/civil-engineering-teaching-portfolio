# Open Datasets for Teaching — Verified List

Curated by **Syed Rafi Ahmed** ([github.com/SyedRafiAhmedGIS](https://github.com/SyedRafiAhmedGIS)).
Part of the [resources index](README.md). These datasets serve all three courses: surveying

**Ownership note:** every entry below links to the original external source; nothing on this page is hosted, mirrored, or copied here. Licensing and verification details: see the [resources index](README.md).
students need real coordinates, GIS students need layers to analyse, and concrete students need
realistic context for specification and sitework discussions. All are free to access under the
terms stated by each provider.

## Satellite imagery and earth observation

- [USGS EarthExplorer](https://earthexplorer.usgs.gov) — the United States Geological Survey's
  download portal for Landsat archives, aerial photography, and elevation products, searchable
  by map or place name. Lab exercise: each GIS student extracts one recent Landsat scene of
  their home district and comments on land-cover change against the oldest available scene.
- [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu) — the European Union's
  open access point for Sentinel-1 radar and Sentinel-2 optical imagery at ten-metre resolution.
  Sentinel-2 previews work directly in lectures because no login is needed to browse;
  registered students can then download a full scene for a supervised classification exercise.
- [NASA Earthdata](https://earthdata.nasa.gov) — NASA's catalogue of earth-observation data
  across atmosphere, ocean, and land missions. *(Blocks automated checkers but opens normally
  in a browser — please verify manually.)* Suitable for advanced learners; its
  MODIS products are the reference examples when discussing resolution trade-offs in the
  remote-sensing lecture.
- [NRSC / Bhuvan (ISRO)](https://www.nrsc.gov.in) — India's national remote sensing centre with
  satellite products and thematic services for the subcontinent. For the regional context, a
  good exercise is to compare its thematic layers with the students' own vector digitising of
  the same area.

## Vector data and administrative boundaries

- [OpenStreetMap](https://www.openstreetmap.org) — the free, community-built world map whose
  raw data can be downloaded and reused under the Open Database License. First exercise of the
  course: inspect your own street in OSM, then discuss positional accuracy and completeness —
  students learn that all maps are edited data, not neutral truth.
- [Geofabrik extracts](https://download.geofabrik.de) — regularly updated OpenStreetMap data
  split by country and region, ready for offline QGIS work. The local country
  extract fits week two, so every student loads an identical, manageable dataset.
- [Natural Earth](https://www.naturalearthdata.com) — free public-domain map data at three
  scales, designed for clean small-scale cartography. Its country and rivers layers suit
  the first choropleth exercise because licensing worries can be set aside entirely.
- [GADM](https://gadm.org) — consistently built administrative boundaries for all countries,
  down to districts and sub-districts. When the GIS class maps district-level census data,
  GADM provides the exact polygon file, including for Bangladesh and India levels that other
  sources often omit.

## Elevation and terrain

- [OpenTopography](https://opentopography.org) — a service providing high-resolution lidar
  topography and standard DEMs with convenient processing tools. Advanced learners derive slope
  and hillshade for a small site, which feeds directly into the surveying course's grading and
  earthwork discussion.

## Socioeconomic context data

- [World Bank Open Data](https://data.worldbank.org) — free country-level indicators on
  infrastructure, urbanisation, and development. In the GIS course's final practical, students
  join a World Bank indicator to GADM country polygons — their first attribute join, using
  entirely open data.

## Note on standards texts

Official concrete and surveying standards (ASTM, BS EN, IS, BDS EN, BNBC) are copyrighted and
are **not** reproduced or linked to copies here; the [concrete-technology page](concrete-technology.md)
links the issuing bodies, whose sites provide official summaries.
