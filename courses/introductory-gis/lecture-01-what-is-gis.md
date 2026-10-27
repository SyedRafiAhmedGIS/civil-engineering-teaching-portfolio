# Lecture 1 Outline — What is GIS? Geospatial Thinking for Civil Engineers

**Duration:** 50 minutes · **Format:** lecture + live demo ·
**Course:** Introductory GIS · **Week:** 1

## Learning objectives

Students will be able to: (1) define a GIS and name its components; (2) describe the layer
concept and the scale/generalisation trade-off; (3) give two engineering examples where
spatial analysis changes the decision; and (4) render a map from a CSV of points using the
provided no-install demo.

## Slide deck (titles and key points)

1. **Four maps that decided an engineering project**
   - Alignment choice, floodplain, land acquisition, noise envelope
2. **A working definition**
   - GIS = data + analysis + display, organised around location; five components
3. **The layer idea**
   - Reality generalised into stacked themes; overlay as the core operation
4. **Scale and generalisation**
   - 1:1,000 vs 1:250,000 - what survives simplification, what silently disappears
5. **Where the data comes from**
   - Surveying (link back to the surveying course), GNSS, remote sensing, open data
6. **Live demo (10 min)**
   - `code/gis_demo/gis_intro_demo.py` on the projector: points -> interpolated surface
7. **What GIS is not**
   - Not just a map viewer; not GPS; the analysis is the product
8. **Wrap-up poll**
   - One-minute paper: state a campus problem a buffer analysis would answer

## In-class activities

- The live demo doubles as the students' first lab: every student runs the same script on
  the sample CSV during the week and submits the resulting PNG (checked, not graded).
- Think-pair-share on the four opening maps: which layer decided it, and at what scale?

## Assessment hook

Quiz 1 reuses the one-minute-paper prompts. The demo's synthetic dataset is replaced in
week 2 by the students' own digitised features - the continuity makes the vector/raster
lecture land on familiar ground.

## Common misconceptions to address

- "GIS equals Google Maps" - consumer maps are products; GIS lets you rebuild the analysis.
- "More layers is better" - each layer adds assumptions; discipline beats accumulation.
