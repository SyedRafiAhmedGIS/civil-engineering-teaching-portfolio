# Roadmap

This file states honestly what is **complete**, what is **planned**, and what is
**not started**. Planned items are intentions, not commitments; target windows are
guidance and move with teaching duties. Nothing on this list is claimed as existing.

## Complete (as of v1.1.0, October 2026)

- Course documentation for all three courses: syllabi, weekly plans,
  outcomes-to-assessment maps, and two sample lecture outlines per course.
- Laboratory manual for the slump and cube compressive strength tests, with
  data-sheet template, safety guidance, measurement uncertainty and a risk
  assessment table.
- Grading rubric template and teaching-philosophy statement.
- `concrete_analysis` package with four country standard profiles, synthetic
  datasets, and 67 passing tests (96 % line coverage).
- Dependency-light GIS demo (IDW interpolation, buffers, choropleth).
- Five Google Colab notebooks (US, UK, India, Bangladesh standards + GIS demo),
  executed end to end in CI.
- Verified teaching-resources index (`resources/`), contribution guide, weekly
  link checker, dual licensing (MIT code, CC BY 4.0 documents).

## Planned - next teaching term (target: before the Spring 2027 term)

| Item | Status | Notes |
|---|---|---|
| Concrete Technology lecture outlines 03-14 | Planned, not started | Same format as outlines 01-02; standards cited by number only |
| Quiz bank with auto-marking script (3 courses x 25 MCQs) | Planned, not started | Original questions tagged by outcome and difficulty |
| Assignments with marking schemes (3 per course) + instructor-only keys | Planned, not started | Synthetic data only; aligned to the outcomes maps |

## Planned - medium term (target: first half of 2027)

| Item | Status | Notes |
|---|---|---|
| Surveying code module (`surveying_tools`) with levelling, traverse and area tools | Planned, not started | NumPy/pandas/matplotlib only; teaching simplifications labelled |
| Surveying Colab notebook with synthetic traverse and adjustment plot | Planned, not started | Follows the surveying module |
| Mix-design teaching calculator (DOE-style and IS 10262-style, simplified) | Planned, not started | Placeholder table values flagged for instructor replacement |
| CRS notebook using pyproj (WGS84 vs UTM, distance-error demo) | Planned, not started | Adds a dependency; would move to requirements extras |
| QGIS lab workbook (3 labs using openly licensed data) | Planned, not started | Complements the existing dependency-free demo |
| Installable package (`pyproject.toml`) with a small CLI | Planned, not started | `concrete-analysis --standard UK --csv file.csv` |
| Six slide decks (lectures 01-02 per course) with speaker notes | Planned, not started | Consistent clean design; one figure per lecture |
| GitHub Pages one-page site + profile README + issue/PR templates | Planned, not started | Static, generated from the repository content |

## Not planned for now

- Reproducing any official standard text (copyrighted by publishers).
- Hosting real student data or evidence: evidence templates, when added, stay
  blank and are filled only with genuine, anonymized material.
