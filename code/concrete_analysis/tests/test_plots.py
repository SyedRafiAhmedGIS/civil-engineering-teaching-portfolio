"""Tests for the plotting functions and end-to-end demo runs.

Figures are written to pytest's tmp_path so the suite never touches the
repository's own docs/ or figures/ folders.
"""

import os

import pandas as pd
import pytest

import matplotlib

matplotlib.use("Agg")

from concrete_analysis.analysis import demo_run, plot_control_chart, plot_strength_vs_age


@pytest.fixture
def strength_df():
    rows = []
    for batch in ("B1", "B2"):
        for age in (7, 28):
            for rep in (1, 2, 3):
                rows.append({
                    "batch": batch,
                    "age_days": age,
                    "strength_mpa": age * 1.1 + rep * 0.3,
                })
    return pd.DataFrame(rows)


def test_plot_strength_vs_age_writes_file(strength_df, tmp_path):
    out = str(tmp_path / "strength.png")
    assert plot_strength_vs_age(strength_df, out) == out
    assert os.path.getsize(out) > 10_000


def test_plot_strength_vs_age_single_rep_has_no_errorbars(strength_df, tmp_path):
    # std of one replicate is NaN -> fillna(0) path must still render.
    out = str(tmp_path / "one_rep.png")
    assert plot_strength_vs_age(strength_df.iloc[:1], out) == out


def test_plot_control_chart_marks_failures(tmp_path):
    out = str(tmp_path / "control.png")
    values = [35.0, 32.0, 36.5, 31.0]   # 2 below fck + 4
    assert plot_control_chart(values, fck_target=30.0, margin_mpa=4.0, out_path=out) == out
    assert os.path.getsize(out) > 10_000


def test_plot_control_chart_single_value(tmp_path):
    out = str(tmp_path / "one.png")
    assert plot_control_chart([36.0], fck_target=30.0, margin_mpa=4.0, out_path=out) == out


def test_demo_run_creates_all_figures(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)   # keep repo clean
    out_dir = str(tmp_path / "figs")
    demo_run(out_dir=out_dir)
    expected = {"demo_strength_vs_age.png", "demo_control_chart.png"}
    files = set(os.listdir(out_dir))
    assert expected.issubset(files), f"missing: {expected - files}"
