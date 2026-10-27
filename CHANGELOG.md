# Changelog

All notable changes to this repository are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [1.2.0] - 2026-10-26

### Fixed
- Reverted the BS EN 12390-3 and BDS EN 12390-3 loading rate to **0.6 ± 0.2 MPa/s
  (constant rate)**. The 1.1.0 change to 0.05 MPa/s ± 10 % was a regression:
  re-verification against two independent public sources (the iTeh official
  catalogue summary of EN 12390-3:2019 and a public PN-EN 12390-3:2019 laboratory
  guide; the full standard texts are paywalled) confirms 0.6 ± 0.2 MPa/s. The
  ASTM C39 (0.25 ± 0.05 MPa/s) and IS 516 (14 N/mm² per minute) values were
  re-checked against public sources and are correct as published.
- Corrected the reported test-suite coverage to **96 % line coverage (224
  statements, 9 missed, 67 tests)** - the figure CI actually measures with
  `pytest code/ --cov=concrete_analysis --cov=gis_demo.gis_intro_demo`. Earlier
  documents showed 98 % / 496 statements, a measurement-scope error that counted
  the test files themselves as production code; the verification harness in the
  publication package now measures with the CI scope, and CONTRIBUTING.md records
  the canonical command.

### Changed
- Replaced the static "tests 67 passing" README badge with the live GitHub
  Actions CI badge (it can no longer go stale).
- Moved the fork-rename `sed` note from the README to
  [CONTRIBUTING.md](CONTRIBUTING.md) under "Fork adaptability".
- About-the-author, teaching-philosophy and resources-page wording rewritten in
  neutral, design-intent language, so no teaching-practice claim goes beyond what
  the repository itself evidences. First-person versions await the author's
  confirmed facts (draft-for-review markers retained for that pass).
- `.gitignore` extended (coverage artifacts, test caches, build output, `.env`)
  and the stray `.coverage` binary removed from the repository.
- Publication-package report PDF: author metadata set to Syed Rafi Ahmed, and the
  cover summary now lists the known open items truthfully instead of claiming
  zero open defects.

## [1.1.0] - 2026-10-25

### Added
- `resources/` folder: verified, course-linked teaching-resource index
  (three course pages plus shared datasets and tools pages; 43 links checked).
- `CONTRIBUTING.md`, `mlc_config.json` and a weekly Markdown link-check workflow.
- `LICENSE-CONTENT` (CC BY 4.0 for course documents; code remains MIT).
- `CITATION.cff`, `CHANGELOG.md`, `NOTICE.md`, `CODE_OF_CONDUCT.md`, `.gitattributes`.
- Authorship-and-provenance statement in the README.
- Expanded test suite: standard-profile tests, GIS demo tests, edge-case and
  figure-output tests (67 tests; 96 % line coverage over 224 statements as
  measured by the CI command).
- Automated notebook execution in CI (`nbmake`, Python 3.10 and 3.12) and a
  three-version unit-test matrix (3.9 / 3.10 / 3.12) with a coverage artifact.
- Laboratory-manual safety additions: PPE and alkali-burn handling, machine
  guarding, post-failure procedure, measurement uncertainty, calibration and a
  risk-assessment table.

### Changed
- Adjusted the EN loading-rate wording and added standard citations (the rate
  value introduced here was reverted to the correct 0.6 ± 0.2 MPa/s in 1.2.0 -
  see above); profiles cite BS EN 12390-3:2019, IS 1199:2018 and IS 516
  (Part 1/Sec 1): 2019.
- India slump guidance relabelled as placement-based teaching bands derived
  from IS 456:2000; individual-cube acceptance condition added.
- Curing-temperature note now states the IS, EN and ASTM water-bath temperatures.
- README restructured: About the author, Status, How to cite, License and
  Authorship sections; vague "in progress" labels replaced with specific
  statuses and a `ROADMAP.md`.

## [1.0.0] - 2026-10-23

### Added
- Initial public release: three course folders (syllabus, weekly plan,
  outcomes-to-assessment map, sample lecture outlines), concrete slump and
  cube-strength laboratory manual with data sheet, grading-rubric template,
  teaching-philosophy statement, `concrete_analysis` package with country
  standard profiles and synthetic datasets, dependency-light GIS demo,
  five Google Colab notebooks, demo figures and animations, CI workflow.
