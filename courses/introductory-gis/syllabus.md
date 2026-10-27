# Introductory GIS — One-Page Syllabus

**Course code (template):** CE 3XX / GE 2XX · **Credits:** 3 (2 lecture + 1 lab hour) ·
**Prerequisite:** none beyond basic programming exposure · **Instructor (template):**
[Instructor name]

## Course description

Civil engineering decisions are spatial: where to align a road, which parcels a pipeline
crosses, which neighbourhoods a flood defends. This course introduces the geographic
information systems that answer such questions - vector and raster data models, coordinate
reference systems, data acquisition, attribute handling, spatial analysis (buffers,
overlays, interpolation) and cartographic communication. Laboratories use open-source QGIS
and a small Python toolkit so every student can reproduce every result on any machine.

## Course outcomes (CO)

- **CO1** Explain what a GIS is, its components, and the geospatial way of thinking
  (layers, scale, generalisation).
- **CO2** Distinguish vector and raster data models and choose the appropriate model for a
  given engineering task.
- **CO3** Manage coordinate reference systems correctly: reproject data, diagnose the
  classic "one metre vs one degree" errors.
- **CO4** Acquire, clean and join spatial and attribute data from open sources.
- **CO5** Perform buffer/overlay/interpolation analyses and communicate results on a
  properly designed map (layout, symbology, legend, sources).

## Assessment

| Component | Weight | Notes |
|---|---|---|
| Lab exercises (5 of 6) | 25% | QGIS-based, checked in lab |
| Quizzes (best 4 of 5) | 10% | Concepts and CRS diagnosis |
| Spatial analysis project | 25% | Individual; site-suitability analysis with open data |
| Midterm examination | 15% | Weeks 1-6 |
| Final examination | 25% | Comprehensive |

## Learning resources

- Original lecture outlines and lab workbooks in this repository (QGIS 3.x labs).
- `code/gis_demo/` for the no-install introduction used in week 1-2.
- Open data portals relevant to the class (national mapping agencies, OpenStreetMap).
- Any recent introductory GIS text for optional depth; the course is self-contained.

## Policies

Labs build cumulatively - miss one and the next doubles in difficulty, so attend. Projects
must use open data and document sources precisely (URL, licence, date downloaded).map
outputs without sources and scale bars receive zero for communication marks.
