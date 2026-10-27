"""Edge-case tests for the concrete analysis toolkit.

These cover the degenerate inputs students actually produce: empty sheets,
negative readings, single specimens, and values outside every class band.
"""

import pytest

from concrete_analysis.analysis import (
    characteristic_strength,
    compressive_strength,
    mean_acceptance_check,
    slump_classify,
)
from concrete_analysis.standards import STANDARDS


# ---------------------------------------------------------------- degenerate inputs
def test_characteristic_strength_empty_raises():
    with pytest.raises(ValueError):
        characteristic_strength([])


def test_characteristic_strength_single_value_raises():
    with pytest.raises(ValueError):
        characteristic_strength([42.0])


def test_characteristic_strength_identical_values_equal_mean():
    # Zero spread: mean - 1.64 * 0 == mean
    assert characteristic_strength([30.0, 30.0, 30.0]) == pytest.approx(30.0)


def test_compressive_strength_negative_area_raises():
    with pytest.raises(ValueError):
        compressive_strength(100_000.0, -22_500.0)


def test_compressive_strength_negative_force_raises():
    with pytest.raises(ValueError):
        compressive_strength(-100_000.0, 22_500.0)


def test_compressive_strength_tiny_load_is_valid():
    # A single near-zero load is physically meaningless but must not crash.
    assert compressive_strength(1.0, 22_500.0) == pytest.approx(1.0 / 22_500.0)


# ------------------------------------------------------------------ classification
def test_slump_below_every_band():
    assert slump_classify(5, STANDARDS["UK"].slump_classes) == "below range"


def test_slump_above_every_closed_band():
    # S5 is open-ended, so a huge slump still classifies as S5.
    assert slump_classify(300, STANDARDS["UK"].slump_classes) == "S5"


def test_slump_in_tolerance_gap_is_boundary():
    assert slump_classify(45, STANDARDS["UK"].slump_classes) == "boundary"


def test_slump_negative_value_is_below_range():
    assert slump_classify(-10, STANDARDS["UK"].slump_classes) == "below range"


def test_slump_empty_classes_reports_value():
    assert "no classes" in slump_classify(80, {})


def test_india_slump_label_matches_updated_bands():
    classes = STANDARDS["IN"].slump_classes
    assert slump_classify(50, classes) == "Low - mass/PCC (25-75)"
    assert slump_classify(100, classes) == "Medium - beams/slabs (75-125)"


# -------------------------------------------------------------------- acceptance
def test_acceptance_exact_boundary_passes():
    ok, required = mean_acceptance_check(mean_mpa=34.0, fck_target=30.0, margin_mpa=4.0)
    assert ok is True and required == pytest.approx(34.0)


def test_acceptance_zero_margin():
    ok, _ = mean_acceptance_check(mean_mpa=29.0, fck_target=30.0, margin_mpa=0.0)
    assert ok is False




def test_acceptance_negative_margin_behaves_as_stricter_threshold():
    # margin -1.0 -> required = fck - 1; the documented formula is applied
    # literally, so the caller is responsible for a sensible margin.
    ok, required = mean_acceptance_check(mean_mpa=1.0, fck_target=30.0, margin_mpa=-1.0)
    assert ok is False and required == pytest.approx(29.0)
