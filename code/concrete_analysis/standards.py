"""Country standard profiles for concrete testing (teaching simplifications).

Each profile bundles the reference numbers a student needs for the lab session:
which standard defines the slump test and the strength test, the specimen
geometry, the loading rate, the slump classification bands and the acceptance
rule used in class. The official standard texts are copyrighted and are NOT
reproduced here - only the values needed for the teaching exercise.

Values checked against public sources in October 2026: BS EN 12390-3:2019
(supersedes 2009), ASTM C39, IS 1199:2018 (supersedes 1959) and IS 516
(Part 1/Sec 1): 2019 (supersedes 1959). The EN loading rate (0.6 +/- 0.2 MPa/s
constant) was re-verified against two independent public sources - the iTeh
official catalogue summary of EN 12390-3:2019 and a public PN-EN 12390-3:2019
laboratory guide; the full standard texts themselves are paywalled. Every
simplified value is labelled as a teaching simplification; always consult the
current official standard for real quality-control decisions.

Adding a new country: copy a profile dict, change the values, register it in
STANDARDS. No analysis code needs to change.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class StandardProfile:
    """One national standards family for the slump / strength lab."""

    key: str                       # short key used in code and notebooks
    country: str                   # human-readable region label
    slump_standard: str            # standard defining the slump test
    strength_standard: str         # standard defining the strength test
    specimen: str                  # "cube" or "cylinder"
    specimen_desc: str             # dimensions in mm
    area_mm2: float                # loaded cross-sectional area
    loading_rate_note: str         # rate description for the report
    slump_classes: dict = field(default_factory=dict)  # label -> (low, high) mm, None = open
    classes_note: str = ""         # how to classify in this family
    acceptance_rule: str = ""      # teaching acceptance rule description
    strength_stat_note: str = ""   # characteristic strength convention note


def _en_slump_classes() -> dict:
    """EN 206-style slump classes (mm). Tolerance gaps are intentional."""
    return {
        "S1": (10, 40),
        "S2": (50, 90),
        "S3": (100, 150),
        "S4": (160, 210),
        "S5": (220, None),   # None = open upper bound
    }


CUBE_150 = 150.0 * 150.0            # 22,500 mm2
CYL_150x300 = 3.14159265 * 75.0 * 75.0   # 17,671.5 mm2 (150 mm diameter)

STANDARDS = {
    "US": StandardProfile(
        key="US",
        country="United States (ASTM)",
        slump_standard="ASTM C143",
        strength_standard="ASTM C39",
        specimen="cylinder",
        specimen_desc="150 x 300 mm cylinder",
        area_mm2=CYL_150x300,
        loading_rate_note="0.25 +/- 0.05 MPa/s in the elastic range (ASTM C39)",
        slump_classes={},   # ASTM defines no S-classes; report the measured value
        classes_note="ASTM has no S-classes: record the slump to the nearest 5 mm "
                     "and compare with the specified target range.",
        acceptance_rule="Specification-driven; for teaching, flag any 28-day mean "
                        "below the specified f'c.",
        strength_stat_note="f'c is the specified compressive strength (cylinder); "
                           "characteristic-style margins are not defined in C39.",
    ),
    "UK": StandardProfile(
        key="UK",
        country="United Kingdom / Ireland (BS EN / IS EN)",
        slump_standard="BS EN 12350-2",
        strength_standard="BS EN 12390-3",
        specimen="cube",
        specimen_desc="150 mm cube",
        area_mm2=CUBE_150,
        loading_rate_note="0.6 +/- 0.2 MPa/s constant rate (BS EN 12390-3:2019)",
        slump_classes=_en_slump_classes(),
        classes_note="EN 206 slump classes S1-S5; values in the tolerance gaps "
                     "between classes are reported as 'boundary'.",
        acceptance_rule="EN 206 initial production (teaching): mean of the set "
                        ">= fck + 4.0 MPa. Teaching simplification.",
        strength_stat_note="fck is the characteristic 150 mm cube strength; "
                           "teaching estimate fck = mean - 1.64 s.",
    ),
    "IN": StandardProfile(
        key="IN",
        country="India (BIS / IS)",
        slump_standard="IS 1199:2018",
        strength_standard="IS 516 (Part 1/Sec 1): 2019",
        specimen="cube",
        specimen_desc="150 mm cube",
        area_mm2=CUBE_150,
        loading_rate_note="14 N/mm2 per minute (approx. 0.23 MPa/s; IS 516 "
                          "(Part 1/Sec 1): 2019)",
        slump_classes={
            "Low - mass/PCC (25-75)": (25, 75),
            "Medium - beams/slabs (75-125)": (75, 125),
            "High - columns (125-175)": (125, 175),
            "Very high - pile/pumped (>175)": (176, None),
        },
        classes_note="IS 456:2000 guides slump by placement condition, not fixed "
                     "classes (mass/PCC 25-75, beams and slabs 50-100, columns "
                     "75-150, pile/pumped 150-200 mm). These non-overlapping "
                     "teaching bands are derived from that guidance; report the "
                     "measured slump and discuss placement suitability. Teaching "
                     "simplification.",
        acceptance_rule="IS 456:2000 (teaching): mean of a group of 4 "
                        "non-overlapping results >= fck + 0.825 x established s "
                        "(or the tabulated minimum when s is unknown); "
                        "individual cube >= fck - 4 MPa for grades M20 and "
                        "above. Teaching simplification of Table 11.",
        strength_stat_note="Grades M20/M25/... define fck as the characteristic "
                           "150 mm cube strength at 28 days.",
    ),
    "BD": StandardProfile(
        key="BD",
        country="Bangladesh (BDS EN / BNBC)",
        slump_standard="BDS EN 12350-2",
        strength_standard="BDS EN 12390-3",
        specimen="cube",
        specimen_desc="150 mm cube",
        area_mm2=CUBE_150,
        loading_rate_note="0.6 +/- 0.2 MPa/s constant rate (as adopted in BDS EN 12390-3)",
        slump_classes=_en_slump_classes(),
        classes_note="BDS EN adopts the EN 206 slump classes S1-S5.",
        acceptance_rule="BDS EN 206 (teaching, as EN): mean of the set "
                        ">= fck + 4.0 MPa for initial production.",
        strength_stat_note="fck is the characteristic 150 mm cube strength; "
                           "teaching estimate fck = mean - 1.64 s.",
    ),
}


def get_standard(key: str) -> StandardProfile:
    """Return the profile for a country key (case-insensitive)."""
    try:
        return STANDARDS[key.upper()]
    except KeyError:
        raise KeyError(
            f"Unknown standard key {key!r}. Available: {sorted(STANDARDS)}"
        ) from None
