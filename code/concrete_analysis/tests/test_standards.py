"""Tests for the country standard profiles in concrete_analysis.standards.

Every profile is checked for the values an instructor must be able to defend:
specimen geometry and loaded area, slump-class coverage, and the presence of
an acceptance rule with an explicit teaching-simplification label.
"""

import pytest

from concrete_analysis.standards import CYL_150x300, CUBE_150, STANDARDS, get_standard

CUBE_AREA = 150.0 * 150.0


# ------------------------------------------------------------------ registry
def test_registry_has_four_countries():
    assert set(STANDARDS) == {"US", "UK", "IN", "BD"}


def test_get_standard_is_case_insensitive():
    assert get_standard("uk") is STANDARDS["UK"]
    assert get_standard("Bd") is STANDARDS["BD"]


def test_get_standard_unknown_key_raises():
    with pytest.raises(KeyError):
        get_standard("XX")


# --------------------------------------------------------------- geometry
@pytest.mark.parametrize("key,specimen,area", [
    ("US", "cylinder", CYL_150x300),
    ("UK", "cube", CUBE_150),
    ("IN", "cube", CUBE_150),
    ("BD", "cube", CUBE_150),
])
def test_specimen_and_area(key, specimen, area):
    profile = STANDARDS[key]
    assert profile.specimen == specimen
    assert profile.area_mm2 == pytest.approx(area)


def test_cylinder_area_value():
    # 150 mm diameter circle
    import math
    assert CYL_150x300 == pytest.approx(math.pi * 75.0 ** 2, rel=1e-4)


def test_us_is_the_only_cylinder_profile():
    assert [k for k, p in STANDARDS.items() if p.specimen == "cylinder"] == ["US"]


# ------------------------------------------------------- rates and standards
def test_en_rate_is_0_6_plus_minus_0_2():
    # EN 12390-3:2019 specifies a constant rate of 0.6 +/- 0.2 MPa/s
    # (re-verified against public sources, Oct 2026; v1.1 briefly shipped 0.05).
    for key in ("UK", "BD"):
        assert "0.6 +/- 0.2 MPa/s" in STANDARDS[key].loading_rate_note


def test_us_rate_is_astm_c39_tolerance():
    assert "0.25 +/- 0.05 MPa/s" in STANDARDS["US"].loading_rate_note


def test_india_profiles_cite_current_revisions():
    assert "IS 1199:2018" in STANDARDS["IN"].slump_standard
    assert "IS 516 (Part 1/Sec 1): 2019" in STANDARDS["IN"].strength_standard


def test_us_profile_has_no_slump_classes():
    assert STANDARDS["US"].slump_classes == {}


def test_en_family_covers_s1_to_s5():
    for key in ("UK", "BD"):
        assert set(STANDARDS[key].slump_classes) == {"S1", "S2", "S3", "S4", "S5"}


def test_india_bands_are_non_overlapping_and_ascending():
    bands = list(STANDARDS["IN"].slump_classes.values())
    for (lo_a, hi_a), (lo_b, hi_b) in zip(bands, bands[1:]):
        assert hi_a <= lo_b  # bands may share a boundary; classifier takes the first match


# ------------------------------------------------- acceptance and simplification
@pytest.mark.parametrize("key", ["US", "UK", "IN", "BD"])
def test_acceptance_rule_present(key):
    assert STANDARDS[key].acceptance_rule.strip() != ""


def test_simplification_labels_present():
    # The instructor must be able to defend every number: simplified rules
    # must say so in the profile itself.
    assert "Teaching simplification" in STANDARDS["IN"].acceptance_rule
    assert "Teaching simplification" in STANDARDS["UK"].acceptance_rule
