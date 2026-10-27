# Lecture 2 Outline — Coordinate Reference Systems and Map Projections

**Duration:** 50 minutes · **Format:** lecture + broken-data exercise ·
**Course:** Introductory GIS · **Week:** 4-5 (CRS block)

## Learning objectives

Students will be able to: (1) explain the difference between geographic and projected
coordinate reference systems; (2) diagnose the three classic CRS failure symptoms in a GIS
project; (3) reproject a dataset to a stated CRS and verify the result; and (4) choose an
appropriate projection for a given engineering task with a one-sentence justification.

## Slide deck (titles and key points)

1. **The dataset that put a bridge in the sea**
   - True incident pattern: lon/lat values loaded as metres; everything 100x off
2. **Coordinates need a reference**
   - Datum, ellipsoid, prime meridian - "coordinates are answers to a stated question"
3. **Geographic vs projected**
   - Degrees on a sphere vs metres on a flat sheet; why engineering needs metres
4. **Projections and their distortions**
   - Conformal / equal-area / equidistant; area vs shape vs distance - pick your poison
5. **The workhorses**
   - UTM zones, national grids, local site grids; where each is the right answer
6. **Three failure symptoms and their cures**
   - Points in the ocean; one-metre features; layers 200 m apart - diagnose live
7. **Reprojection drill**
   - Two-layer exercise: fix the offset, verify against a known feature
8. **Wrap-up clicker**
   - Given a corridor design task, which projection and why?

## In-class activities

- Broken-data exercise (12 minutes): pairs receive a deliberately mismatched pair of
  datasets; they must name the symptom, cause and fix. Answers argued in plenary.
- The drill is repeated in the week 5 lab with their own digitised data.

## Assessment hook

Quiz 3 presents the three symptoms and asks for the diagnosis; the project rubric reserves
explicit marks for a stated CRS with justification, keeping this block honest all semester.

## Common misconceptions to address

- "WGS84 is always fine" - engineering analysis needs metres and defensible distortion.
- "On-the-fly display means data is aligned" - display is not transformation; store what you mean.
