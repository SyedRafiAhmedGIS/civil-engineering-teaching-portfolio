"""Core calculations and plots for the concrete slump / cube strength lab.

All functions are deliberately small, pure and tested (see tests/). Educational
simplification notes are inline; for real quality control always consult the
current official standard text.

Run as a script to produce demo figures from the synthetic dataset:

    python code/concrete_analysis/analysis.py     # writes to ./figures
"""

from __future__ import annotations

import os
import sys

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")  # headless-safe import order for scripts and tests
import matplotlib.pyplot as plt

try:  # package import (pytest, python -m concrete_analysis.analysis)
    from .standards import get_standard
except ImportError:  # direct script run: python code/concrete_analysis/analysis.py
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from concrete_analysis.standards import get_standard

# Match the repository's figure style (single hue family, clean axes)
COLOR_MAIN = "#2f6f8f"
COLOR_ACCENT = "#c25b34"
COLOR_MUTED = "#8a9aa5"

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


# --------------------------------------------------------------------- calcs
def compressive_strength(force_n: float, area_mm2: float) -> float:
    """Return compressive strength in MPa from force (N) and area (mm2).

    f = P / A.  Example: 300,000 N on a 150 mm cube (22,500 mm2) -> 13.33 MPa.
    """
    if force_n <= 0:
        raise ValueError("force_n must be positive")
    if area_mm2 <= 0:
        raise ValueError("area_mm2 must be positive")
    return force_n / area_mm2


def characteristic_strength(values) -> float:
    """Teaching characteristic strength: mean - 1.64 s (sample std, n-1).

    This is the classic normal-distribution 5% fractile estimate used for
    teaching; real codes apply additional rules (minimum margins, group
    definitions). Requires n >= 2 samples.
    """
    arr = np.asarray(values, dtype=float)
    if arr.size < 2:
        raise ValueError("need at least 2 strength values")
    return float(np.mean(arr) - 1.64 * np.std(arr, ddof=1))


def slump_classify(slump_mm: float, classes: dict) -> str:
    """Classify a slump value against a profile's class bands.

    Returns the class label, or 'boundary' when the value falls in a
    tolerance gap between classes (intentional in EN 206), or 'below range' /
    'above range' outside the table.
    """
    if not classes:
        return "reported value (no classes in this profile)"
    for label, (low, high) in classes.items():
        if low <= slump_mm and (high is None or slump_mm <= high):
            return label
    lows = sorted(v[0] for v in classes.values())
    if slump_mm < lows[0]:
        return "below range"
    if slump_mm > max(v[0] for v in classes.values()) and all(
        v[1] is not None for v in classes.values()
    ):
        return "above range"
    return "boundary"


def mean_acceptance_check(mean_mpa: float, fck_target: float, margin_mpa: float = 4.0):
    """EN-style initial-production teaching rule: mean >= fck + margin.

    Returns (passes: bool, required_mean: float). Default margin 4.0 MPa
    follows the EN 206 initial-production teaching simplification used in the
    lab manual; adjust per your profile's rule.
    """
    required = fck_target + margin_mpa
    return bool(mean_mpa >= required), float(required)


# -------------------------------------------------------------------- loaders
def load_slump_csv(path: str) -> pd.DataFrame:
    """Load a slump results CSV with columns: batch, slump_mm, target_class."""
    df = pd.read_csv(path)
    missing = {"batch", "slump_mm"} - set(df.columns)
    if missing:
        raise ValueError(f"slump CSV missing columns: {sorted(missing)}")
    if (df["slump_mm"] <= 0).any():
        raise ValueError("slump_mm must be positive")
    return df


def load_cube_strength_csv(path: str) -> pd.DataFrame:
    """Load cube/cylinder results CSV: batch, age_days, force_kn, area_mm2."""
    df = pd.read_csv(path)
    missing = {"batch", "age_days", "force_kn", "area_mm2"} - set(df.columns)
    if missing:
        raise ValueError(f"strength CSV missing columns: {sorted(missing)}")
    if (df["force_kn"] <= 0).any() or (df["area_mm2"] <= 0).any():
        raise ValueError("force_kn and area_mm2 must be positive")
    df["strength_mpa"] = df["force_kn"] * 1000.0 / df["area_mm2"]
    return df


# --------------------------------------------------------------------- plots
def _style_axis(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.2)


def plot_strength_vs_age(df: pd.DataFrame, out_path: str) -> str:
    """Mean strength +/- one std dev per age, per batch."""
    fig, ax = plt.subplots(figsize=(7, 4.2), constrained_layout=True)
    for batch, grp in df.groupby("batch"):
        g = grp.groupby("age_days")["strength_mpa"].agg(["mean", "std"])
        ax.errorbar(
            g.index, g["mean"], yerr=g["std"].fillna(0), marker="o", capsize=4,
            label=f"{batch}", color=COLOR_MAIN if batch == df["batch"].iloc[0] else COLOR_ACCENT,
            linewidth=2,
        )
    ax.set_xlabel("Age (days)")
    ax.set_ylabel("Compressive strength (MPa)")
    ax.set_title("Compressive strength development")
    _style_axis(ax)
    ax.legend(frameon=False, loc="lower right")
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def plot_control_chart(values, fck_target: float, margin_mpa: float,
                       out_path: str) -> str:
    """Rolling batch-mean chart with the acceptance threshold drawn."""
    arr = np.asarray(values, dtype=float)
    required = fck_target + margin_mpa
    fig, ax = plt.subplots(figsize=(7, 4.2), constrained_layout=True)
    ax.plot(range(1, len(arr) + 1), arr, marker="o", color=COLOR_MAIN, linewidth=2,
            label="batch mean (28 d)")
    ax.axhline(required, color=COLOR_ACCENT, linestyle="--", linewidth=1.5,
               label=f"acceptance: fck + {margin_mpa:g} MPa = {required:g}")
    ax.axhline(fck_target, color=COLOR_MUTED, linestyle=":", linewidth=1.2,
               label=f"target fck = {fck_target:g}")
    for i, v in enumerate(arr, start=1):
        if v < required:
            ax.annotate("fail", (i, v), textcoords="offset points",
                        xytext=(0, -14), ha="center", color=COLOR_ACCENT, fontsize=8)
    ax.set_xlabel("Production batch")
    ax.set_ylabel("Mean strength (MPa)")
    ax.set_title("Quality-control chart")
    _style_axis(ax)
    ax.legend(frameon=False, loc="center right")
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


# ------------------------------------------------------------------ demo run
def demo_run(out_dir: str = "figures") -> None:
    """Produce demo figures from the synthetic datasets (used in README)."""
    os.makedirs(out_dir, exist_ok=True)
    strength_csv = os.path.join(DATA_DIR, "cube_strength_results.csv")
    df = load_cube_strength_csv(strength_csv)
    plot_strength_vs_age(df, os.path.join(out_dir, "demo_strength_vs_age.png"))

    d28 = df[df["age_days"] == 28]
    batch_means = d28.groupby("batch")["strength_mpa"].mean().values
    plot_control_chart(batch_means, fck_target=30.0, margin_mpa=4.0,
                       out_path=os.path.join(out_dir, "demo_control_chart.png"))

    slump_csv = os.path.join(DATA_DIR, "slump_test_results.csv")
    s = load_slump_csv(slump_csv)
    prof = get_standard("UK")
    s["class"] = [slump_classify(v, prof.slump_classes) for v in s["slump_mm"]]
    print(s[["batch", "slump_mm", "class"]].to_string(index=False))

    print("\n28-day batch summaries (per grade - never pool different grades):")
    for batch, grp in d28.groupby("batch"):
        vals = grp["strength_mpa"].values
        print(f"  {batch}: mean {vals.mean():.2f} MPa, "
              f"fck (teaching) {characteristic_strength(vals):.2f} MPa")
    print(f"Figures written to: {os.path.abspath(out_dir)}")


if __name__ == "__main__":
    demo_run()
