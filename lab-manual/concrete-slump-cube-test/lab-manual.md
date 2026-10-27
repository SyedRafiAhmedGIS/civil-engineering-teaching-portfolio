# Laboratory Manual — Concrete Slump Test and Cube Compressive Strength Test

**Course:** Concrete Technology (or equivalent materials course) · **Sessions:** two, 2
hours each · **Prepared by:** Syed Rafi Ahmed · **Data policy:** measure real values in
class, or use the synthetic dataset in `code/concrete_analysis/data/` when running the
exercise remotely.

## 1. Objectives

1. Determine the consistency of fresh concrete by the slump cone test and classify it into
   the correct workability class for the governing standard family.
2. Determine the compressive strength of 150 mm cubes (or 150 x 300 mm cylinders in the US
   profile) at 7 and 28 days and compute the characteristic strength of a batch series.
3. Practise disciplined data recording on the standard data sheet and statistical
   interpretation with the provided Python toolkit.

## 2. Standards referenced (educational orientation)

| Region | Slump test | Strength test | Specimen | Loading rate |
|---|---|---|---|---|
| United States | ASTM C143 | ASTM C39 | 150 x 300 mm cylinder | 0.25 +/- 0.05 MPa/s |
| United Kingdom / Ireland | BS EN 12350-2 | BS EN 12390-3:2019 | 150 mm cube | 0.6 +/- 0.2 MPa/s (constant rate) |
| India | IS 1199:2018 | IS 516 (Part 1/Sec 1): 2019 | 150 mm cube | 14 N/mm2 per minute |
| Bangladesh | BDS EN 12350-2 | BDS EN 12390-3 | 150 mm cube | 0.6 +/- 0.2 MPa/s (constant rate, adopted EN) |

The official standard texts are copyrighted; only the numbers needed for teaching
(classification bands, rates, tolerances) are summarised here and in the code profiles.

## 3. Apparatus

- Slump cone (base 200 mm, top 100 mm, height 300 mm) with handles and foot pieces
- Tamping rod: 16 mm diameter, 600 mm long, rounded end
- Ruler (mm) and base plate (rigid, non-absorbent, level)
- Compression testing machine (calibrated), auxiliary platens as required
- Cube moulds 150 mm (or cylinder moulds 150 x 300 mm), tamping bar or vibrating table
- Curing tank at 27 +/- 2 C (IS practice; EN 12390-2 uses 20 +/- 2 C and ASTM C31/C192 uses 23 +/- 2 C - always follow the standard your country profile specifies), damp hessian, gloves, safety glasses

## 4. Safety

Wear safety glasses and gloves at all times. Keep hands clear of the platens during
loading; the failure event is sudden and may eject fragments. Report any machine anomaly to
the demonstrator immediately and do not continue loading.

### 4.1 Personal protective equipment and chemical handling

- Minimum PPE: safety glasses, chemical-resistant (nitrile) gloves, covered shoes,
  long trousers, and a lab coat or apron. Dust masks when handling dry cement.
- **Fresh concrete is alkaline (pH ~12-13) and causes alkali burns.** Remove any paste
  from skin immediately and rinse under running water for several minutes; report any
  skin redness or eye contact to the demonstrator at once. Never wash hands or tools
  into the storm drain - use the washout settlement basin.
- Cut hazards: cured cubes are heavy (approx. 13.5 kg each) and sharp-edged; carry
  with both hands and gloves, and use a trolley for batches.

### 4.2 Compression testing machine

- The machine must have a fixed or interlocked guard around the platen zone; keep the
  guard closed for the whole loading stroke.
- Verify the machine is within its calibration certificate validity (see Section 4.4.2)
  before the first test; check the reset and emergency-stop controls at the start of
  the session.
- Only the demonstrator operates the loading valve for the first session; students
  may take over under supervision.

### 4.3 If a cube fails explosively

Explosive (sudden brittle) failure can eject fragments at speed.

1. Stand back - do not approach the platens until loading has fully stopped and the
   ram has retracted.
2. Switch the machine to unload/release; press the emergency stop if fragments jam
   the platens.
3. The demonstrator removes fragments wearing gloves and eye protection; inspect the
   machine platens and guards before any further test.
4. Record the failure type (normal cone/shear vs explosive) on the data sheet; an
   explosive failure with a plausible cause is still a valid result, but the machine
   must be checked before continuing.

### 4.4 Measurement uncertainty and calibration

*Subsections 4.4.1-4.4.3 are instructor-authored teaching guidance; institutional
calibration intervals and any stricter local rules always take precedence.*

#### 4.4.1 Reading uncertainty (teaching values)

| Measurement | Typical reading uncertainty | Dominant source |
|---|---|---|
| Slump | +/- 5 mm (ASTM C143 precision) | operator lift speed, ruling to the displaced top |
| Load | +/- 1 % of indicated load | machine class (usually class 1.0 or better) |
| Strength (150 mm cube) | approx. +/- 1.5-2 % | load + area tolerances combined |
| Age / curing temperature | +/- 2 C | bath thermostat and thermometer resolution |

Report results with the appropriate significant figures and never quote strength to
more than one decimal place.

#### 4.4.2 Calibration requirements

- Compression testing machine: verified against a calibrated proving ring or load
  cell on a scheduled institutional interval (commonly 12 months); the certificate
  must be visible in the lab or available on request.
- Slump cone, ruler and thermometers: check dimensional conformity and legibility
  at the start of each term; replace dented cones (out-of-round or damaged rims
  change the measured slump).
- Record which machine and which certificate were used on the data sheet.

#### 4.4.3 Risk assessment summary

| Hazard | Likelihood | Severity | Control | Residual action |
|---|---|---|---|---|
| Alkali burn from fresh concrete | Medium | Low-Med | Gloves, immediate washing, washout basin | First-aid kit and eyewash within 10 m |
| Fragments from explosive cube failure | Low | High | Machine guard closed, stand back, demonstrator removes debris | Face shields during strength tests |
| Crush/pinch at platens | Low | High | Hands-clear rule, guard interlock | Two-person rule for loading |
| Heavy cube handling | Medium | Low | Gloves, trolley, two-person lift | Max 4 cubes per carry trip |
| Slips on wash water | Medium | Low | Squeegee after each session, warning sign | Mop immediately after washout |
| Cement dust | Low | Low | Damp sweeping, dust mask when handling dry cement | Ventilation check each term |

*Which rule is whose:* items marked as teaching guidance above are set by the
instructor; institutional safety policies, national workshop regulations, and the
compression-machine manufacturer's manual always override them, and the local
institution's risk-assessment form must be completed before the first session.

## 5. Procedure A — slump test (per batch)

1. Dampen the cone and base plate; stand on the foot pieces; set the cone against the plate.
2. Fill in three layers of approximately one-third depth each; rod each layer 25 times
   uniformly over the cross-section.
3. Strike off flush with the top; clean spillage around the base.
4. Lift the cone vertically, steadily, in 2-5 seconds without twisting.
5. Measure the slump to the nearest 5 mm (10 mm in some profiles) as the difference between
   the mould height and the highest point of the slumped concrete.
6. Record slump type: **true**, **shear** (redo once; if again shear, record and note), or
   **collapse**.
7. Classify using the standard's bands (S1-S5 in EN/BDS profiles; reported value in US
   practice) - `analysis.py::slump_classify` reproduces the bands used in class.

## 6. Procedure B — cube compressive strength (150 mm cubes)

1. Sample and mould the fresh concrete in two (or three) equal layers, compacting each with
   35 strokes (or vibration to full compaction).
2. Label specimens with batch code and casting date; cover; demould after 24 +/- 0.5 h.
3. Cure in the water tank at the standard temperature until the test age (7 and 28 days).
4. At test: wipe surfaces, check for obvious defects, weigh and measure the specimen; record
   cross-sectional area (cube: 150 x 150 = 22,500 mm2; cylinder: 176.7 cm2 for 150 dia).
5. Centre the specimen on the platen; bring the machine to contact without shock.
6. Load at the standard rate (see table in Section 2) until failure; record maximum load.
7. Compute strength f = P / A. Compute batch statistics: mean, standard deviation (n >= 3),
   and characteristic strength fck = fmean - 1.64 s (teaching definition; see limitations).
8. Compare against the grade target (e.g. M20 -> fck = 20 MPa) and the acceptance rule for
   the chosen profile, e.g. EN-style initial production rule: mean of set >= fck + 4 MPa.

## 7. Data sheet

Use `data-sheet-template.md` (printable) or the CSV layout in `code/concrete_analysis/data/`.
Every field on the data sheet must be filled; crossed-out errors stay legible with initials.

## 8. Analysis with the toolkit

```bash
pytest code/ -v                                  # confirm the toolkit passes its tests
python code/concrete_analysis/analysis.py        # demo run on synthetic data -> ./figures
```

In the notebook version (see `code/notebooks/`), select your country profile, upload your
class CSV through the upload widget (or press Cancel to use the built-in synthetic data),
and generate the strength-versus-age plot and the quality-control chart.

## 9. Report requirements (marked with the shared grading rubric)

- Complete data sheet scan/appendix; specimen photos optional but encouraged
- Slump classification with justification against tolerance bands
- Strength table (individual, mean, s, fck) and comparison with target grade
- Discussion: at least three plausible sources of variance in your batch
- One-paragraph conclusion stating pass/fail against the acceptance rule and the evidence

## 10. Discussion questions

1. Your cube set failed the acceptance margin although the mean exceeded the grade. What
   does the scatter tell you about the production process?
2. Why does the standard forbid re-testing a sheared slump more than once?
3. How would using a 100 mm cube change your measured strength, and why?
4. A site batch shows S4 slump but the specification asked for S2. List two compliant ways
   to recover and one non-compliant shortcut, and say why the shortcut is a quality crime.

## 11. References (numbers only; texts not reproduced)

ASTM C143 / C39 · BS EN 12350-2 / 12390-3 / EN 206 · IS 1199 / 516 / 456 ·
BDS EN 12350-2 / 12390-3 · BNBC (Bangladesh National Building Code)
