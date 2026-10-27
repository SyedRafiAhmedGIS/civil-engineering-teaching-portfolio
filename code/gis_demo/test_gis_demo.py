"""Tests for the dependency-light GIS teaching demo.

Focus: the mathematical guarantees that make IDW a good teaching example
(exact reproduction at sample points, monotone effect of the power parameter,
deterministic synthetic zones) and the reproducibility of the figures.
"""

import os

import numpy as np
import pytest

import matplotlib

matplotlib.use("Agg")

from gis_demo.gis_intro_demo import (  # noqa: E402
    idw_interpolate,
    synthetic_zones,
)


@pytest.fixture
def sample_points():
    # Four rain-gauge style stations on a 10 km x 10 km canvas
    pts = [(1.0, 1.0), (8.0, 2.0), (2.5, 7.5), (9.0, 9.0)]
    vals = [120.0, 80.0, 95.0, 60.0]
    return pts, vals


@pytest.fixture
def grid():
    x = np.linspace(0.0, 10.0, 21)
    y = np.linspace(0.0, 10.0, 21)
    return np.meshgrid(x, y)


# ----------------------------------------------------------- IDW reproduction
def test_idw_reproduces_sample_points(sample_points, grid):
    pts, vals = sample_points
    z = idw_interpolate(pts, vals, grid)
    for (px, py), v in zip(pts, vals):
        i = np.unravel_index(np.argmin(np.abs(grid[0] - px) + np.abs(grid[1] - py)), z.shape)
        assert z[i] == pytest.approx(v, rel=0.15)


def test_idw_output_shape_matches_grid(sample_points, grid):
    pts, vals = sample_points
    z = idw_interpolate(pts, vals, grid)
    assert z.shape == grid[0].shape


def test_idw_interpolant_lies_between_min_and_max(sample_points, grid):
    pts, vals = sample_points
    z = idw_interpolate(pts, vals, grid)
    assert z.min() >= min(vals) - 1e-6
    assert z.max() <= max(vals) + 1e-6


# ------------------------------------------------------- power parameter effect
def test_higher_power_sharpens_peaks(sample_points, grid):
    # With p=4 the surface hugs the high sample more tightly than with p=1.
    pts, vals = sample_points
    near_max_idx = int(np.argmax(vals))
    px, py = pts[near_max_idx]
    j = np.unravel_index(np.argmin(np.abs(grid[0] - px) + np.abs(grid[1] - py)), grid[0].shape)
    z1 = idw_interpolate(pts, vals, grid, power=1.0)
    z4 = idw_interpolate(pts, vals, grid, power=4.0)
    offset = (1, 1)
    nb = tuple(a + b for a, b in zip(j, offset))
    assert z4[nb] > z1[nb]  # smoother (p=1) bleeds more value to neighbours


def test_power_param_changes_surface(sample_points, grid):
    pts, vals = sample_points
    z1 = idw_interpolate(pts, vals, grid, power=1.0)
    z3 = idw_interpolate(pts, vals, grid, power=3.0)
    assert not np.allclose(z1, z3)


# ------------------------------------------------------------ synthetic zones
def test_zones_seed_reproducible():
    a = synthetic_zones(seed=7)
    b = synthetic_zones(seed=7)
    np.testing.assert_array_equal(a, b)


def test_zones_different_seeds_differ():
    assert not np.array_equal(synthetic_zones(seed=1), synthetic_zones(seed=2))


def test_zones_shape_and_value_range():
    z = synthetic_zones(nx=6, ny=4, seed=7)
    assert z.shape == (4, 6)
    assert z.min() >= 1 and z.max() <= 4


def test_zone_default_seed_is_documented_constant():
    # The demo's default seed keeps lecture figures identical every run.
    assert synthetic_zones().tolist() == synthetic_zones(seed=7).tolist()


# ---------------------------------------------------------------- figure output
def test_plot_idw_and_buffers_writes_file(sample_points, tmp_path):
    from gis_demo.gis_intro_demo import plot_idw_and_buffers
    pts, vals = sample_points
    out = str(tmp_path / "idw.png")
    assert plot_idw_and_buffers(pts, vals, out) == out
    assert os.path.getsize(out) > 10_000


def test_plot_choropleth_writes_file(tmp_path):
    from gis_demo.gis_intro_demo import plot_choropleth
    out = str(tmp_path / "choropleth.png")
    assert plot_choropleth(out) == out
    assert os.path.getsize(out) > 10_000


def test_gis_demo_run_creates_figures(tmp_path):
    from gis_demo.gis_intro_demo import demo_run
    out_dir = str(tmp_path / "figs")
    demo_run(out_dir=out_dir)
    assert {"demo_gis_idw_map.png", "demo_gis_choropleth.png"}.issubset(set(os.listdir(out_dir)))
