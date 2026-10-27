"""GIS concept demo without heavy dependencies (NumPy + Matplotlib only).

A first-week teaching demo for the Introductory GIS course: it takes a small
set of survey points (synthetic elevations), produces an interpolated surface
(Inverse Distance Weighting), draws a buffer ring around a feature of interest
and renders a choropleth of synthetic zones. It shows the *concepts* GIS
software implements - it is not a replacement for QGIS / ArcGIS / geopandas.

Run:  python code/gis_demo/gis_intro_demo.py    (writes PNGs to ./figures)
"""

from __future__ import annotations

import os

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource

COLOR_MAIN = "#2f6f8f"
COLOR_ACCENT = "#c25b34"
CMAP = "YlGnBu"

DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "concrete_analysis", "data",
)


def idw_interpolate(points_xy, values, grid_xy, power: float = 2.0):
    """Inverse Distance Weighting interpolation on a grid.

    z(grid) = sum(v_i / d_i^p) / sum(1 / d_i^p). Classic teaching interpolator:
    simple, deterministic, exactly reproduces the input points.
    """
    pts = np.asarray(points_xy, dtype=float)
    val = np.asarray(values, dtype=float)
    gx = np.asarray(grid_xy[0], dtype=float)
    gy = np.asarray(grid_xy[1], dtype=float)
    # distances: (n_points, n_grid)
    d = np.sqrt(
        (gx[None, :, :] - pts[:, 0][:, None, None]) ** 2
        + (gy[None, :, :] - pts[:, 1][:, None, None]) ** 2
    )
    d[d < 1e-9] = 1e-9  # avoid divide-by-zero at exact sample locations
    w = 1.0 / d ** power
    return (w * val[:, None, None]).sum(axis=0) / w.sum(axis=0)


def synthetic_zones(nx: int = 6, ny: int = 4, seed: int = 7):
    """A tiny synthetic 'land parcel' grid with an attribute (e.g. land use score)."""
    rng = np.random.default_rng(seed)
    scores = rng.integers(1, 5, size=(ny, nx)).astype(float)
    return scores


def plot_idw_and_buffers(points, values, out_path: str) -> str:
    gx, gy = np.meshgrid(np.linspace(0, 1000, 160), np.linspace(0, 700, 120))
    z = idw_interpolate(points, values, (gx, gy))

    fig, ax = plt.subplots(figsize=(7.2, 4.8), constrained_layout=True)
    ls = LightSource(azdeg=315, altdeg=45)
    rgb = ls.shade(z, cmap=plt.get_cmap(CMAP), vert_exag=0.1, blend_mode="soft")
    ax.imshow(rgb, origin="lower", extent=(0, 1000, 0, 700), aspect="auto")
    cs = ax.contour(gx, gy, z, levels=8, colors="white", linewidths=0.5, alpha=0.5)
    ax.clabel(cs, fmt="%.0f m", fontsize=7)

    pts = np.asarray(points)
    ax.scatter(pts[:, 0], pts[:, 1], c="white", edgecolors="black", s=28,
               label="survey points", zorder=3)
    # buffer: 120 m radius around the highest point (concept only, drawn as circle)
    hi = int(np.argmax(values))
    ax.add_patch(plt.Circle((pts[hi, 0], pts[hi, 1]), 120, fill=False,
                            color=COLOR_ACCENT, linewidth=2, label="120 m buffer"))
    ax.plot(pts[hi, 0], pts[hi, 1], marker="*", color=COLOR_ACCENT, markersize=14,
            linestyle="none", zorder=4)

    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 700)
    ax.set_xlabel("Easting (m)")
    ax.set_ylabel("Northing (m)")
    ax.set_title("IDW surface from survey points, contours and a 120 m buffer")
    ax.legend(frameon=False, loc="upper left")
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def plot_choropleth(out_path: str) -> str:
    scores = synthetic_zones()
    fig, ax = plt.subplots(figsize=(7.2, 4.2), constrained_layout=True)
    cmap = plt.get_cmap(CMAP)
    norm = plt.Normalize(vmin=1, vmax=4)
    for i in range(scores.shape[0]):
        for j in range(scores.shape[1]):
            v = scores[i, j]
            ax.add_patch(
                plt.Rectangle((j * 100, 560 - i * 140), 100, 140,
                              facecolor=cmap(norm(v)), edgecolor="white", linewidth=1.5)
            )
            ax.text(j * 100 + 50, 560 - i * 140 + 70, f"zone {i * 6 + j + 1}\n{v:.0f}",
                    ha="center", va="center", fontsize=8, color="#22303a")
    ax.set_xlim(0, 600)
    ax.set_ylim(0, 560)
    ax.set_xlabel("Easting (m)")
    ax.set_ylabel("Northing (m)")
    ax.set_title("Synthetic zone choropleth (attribute = land-use score)")
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, shrink=0.85, ticks=[1, 2, 3, 4])
    cbar.set_label("land-use score")
    ax.set_xticks([]), ax.set_yticks([])
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def demo_run(out_dir: str = "figures") -> None:
    os.makedirs(out_dir, exist_ok=True)
    csv_path = os.path.join(DATA_DIR, "gis_sample_points.csv")
    df = pd.read_csv(csv_path)
    p1 = plot_idw_and_buffers(
        df[["x_m", "y_m"]].values, df["elevation_m"].values,
        os.path.join(out_dir, "demo_gis_idw_map.png"),
    )
    p2 = plot_choropleth(os.path.join(out_dir, "demo_gis_choropleth.png"))
    print(f"IDW map written to: {os.path.abspath(p1)}")
    print(f"Choropleth written to: {os.path.abspath(p2)}")


if __name__ == "__main__":
    demo_run()
