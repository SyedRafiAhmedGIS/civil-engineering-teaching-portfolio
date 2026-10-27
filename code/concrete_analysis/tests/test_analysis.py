"""Pytest suite for the concrete analysis toolkit.

Run from the repository root:  pytest code/ -v
"""

import os

import numpy as np
import pytest

from concrete_analysis.analysis import (
    characteristic_strength,
    compressive_strength,
    load_cube_strength_csv,
    load_slump_csv,
    mean_acceptance_check,
    slump_classify,
)
from concrete_analysis.standards import STANDARDS, get_standard

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
SLUMP_CSV = os.path.join(DATA_DIR, "slump_test_results.csv")
STRENGTH_CSV = os.path.join(DATA_DIR, "cube_strength_results.csv")


# ------------------------------------------------------- compressive strength
def test_strength_known_value_cube():
    # 300 kN on a 150 mm cube: 300000 / 22500 = 13.333... MPa
    assert compressive_strength(300_000.0, 22_500.0) == pytest.approx(13.3333, rel=1e-3)


def test_strength_known_value_cylinder():
    # 250 kN on a 150x300 cylinder: 250000 / 17671.5 = 14.148 MPa
    assert compressive_strength(250_000.0, STANDARDS["US"].area_mm2) == pytest.approx(
        14.148, rel=1e-3
    )


def test_strength_rejects_bad_inputs():
    with pytest.raises(ValueError):
        compressive_strength(-1.0, 22500.0)
    with pytest.raises(ValueError):
        compressive_strength(1000.0, 0.0)


# -------------------------------------------------- characteristic strength
def test_characteristic_strength_simple_series():
    vals = [20.0, 21.0, 22.0, 23.0, 24.0]   # mean 22.0, sample std ~1.5811
    expected = 22.0 - 1.64 * np.std(np.array(vals), ddof=1)
    assert characteristic_strength(vals) == pytest.approx(expected, rel=1e-6)


def test_characteristic_strength_needs_two_values():
    with pytest.raises(ValueError):
        characteristic_strength([25.0])


# --------------------------------------------------------- slump classification
def test_slump_classes_en_band_midpoints():
    classes = STANDARDS["UK"].slump_classes
    assert slump_classify(25, classes) == "S1"
    assert slump_classify(70, classes) == "S2"
    assert slump_classify(120, classes) == "S3"
    assert slump_classify(180, classes) == "S4"
    assert slump_classify(230, classes) == "S5"


def test_slump_classes_boundaries():
    classes = STANDARDS["UK"].slump_classes
    assert slump_classify(10, classes) == "S1"
    assert slump_classify(40, classes) == "S1"
    assert slump_classify(45, classes) == "boundary"   # tolerance gap 40-50
    assert slump_classify(5, classes) == "below range"


def test_slump_us_profile_has_no_classes():
    assert "reported value" in slump_classify(80, STANDARDS["US"].slump_classes)


def test_india_profile_bands():
    classes = STANDARDS["IN"].slump_classes
    assert slump_classify(50, classes) == "Low - mass/PCC (25-75)"
    assert slump_classify(100, classes) == "Medium - beams/slabs (75-125)"


# ------------------------------------------------------------ acceptance rule
def test_acceptance_rule_pass_fail():
    ok, required = mean_acceptance_check(mean_mpa=35.0, fck_target=30.0, margin_mpa=4.0)
    assert ok is True and required == pytest.approx(34.0)
    ok, required = mean_acceptance_check(mean_mpa=33.5, fck_target=30.0, margin_mpa=4.0)
    assert ok is False and required == pytest.approx(34.0)


# --------------------------------------------------------------------- loaders
def test_load_slump_csv_valid():
    df = load_slump_csv(SLUMP_CSV)
    assert len(df) >= 5
    assert (df["slump_mm"] > 0).all()


def test_load_cube_strength_csv_computes_strength():
    df = load_cube_strength_csv(STRENGTH_CSV)
    assert "strength_mpa" in df.columns
    # spot check one row: strength = force_kn * 1000 / area
    row = df.iloc[0]
    assert row["strength_mpa"] == pytest.approx(
        row["force_kn"] * 1000.0 / row["area_mm2"], rel=1e-6
    )
    ages = set(df["age_days"].unique())
    assert ages == {7, 28}


def test_loaders_reject_missing_columns(tmp_path):
    bad = tmp_path / "bad.csv"
    bad.write_text("batch,slump\nA,50\n")
    with pytest.raises(ValueError):
        load_slump_csv(str(bad))


# --------------------------------------------------------------- profiles
def test_get_standard_case_insensitive_and_error():
    assert get_standard("bd").key == "BD"
    with pytest.raises(KeyError):
        get_standard("Mars")


def test_all_profiles_have_core_fields():
    for key, prof in STANDARDS.items():
        assert prof.area_mm2 > 0
        assert prof.slump_standard and prof.strength_standard
        assert prof.acceptance_rule
