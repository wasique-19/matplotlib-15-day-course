"""chart_style.py - reusable branded chart style and export helpers."""

import os

import matplotlib.pyplot as plt
from cycler import cycler

# Okabe-Ito colour-blind-safe palette (five of its eight colours)
PALETTE = {
    "blue": "#0072B2",
    "orange": "#E69F00",
    "green": "#009E73",
    "vermillion": "#D55E00",
    "sky": "#56B4E9",
}
NOTE_GREY = "#6B6B6B"


def set_report_style():
    """Apply the branded look to every chart drawn afterwards."""
    plt.rcParams.update({
        "figure.figsize": (8, 5),
        "font.size": 12,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": "#CCCCCC",
        "grid.alpha": 0.5,
        "grid.linestyle": "--",
        "axes.prop_cycle": cycler(color=list(PALETTE.values())),
        "pdf.fonttype": 42,   # embed real fonts so PDF text stays text
    })


def add_source_note(fig, text):
    """Reserve a strip at the bottom of the figure and write a source note in it."""
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    fig.text(0.01, 0.015, text, fontsize=9, color=NOTE_GREY,
             ha="left", va="bottom")


def save_fig(fig, name, folder="figures", dpi=300):
    """Save a figure as PNG (at `dpi`) and PDF, close it, return the PNG path."""
    os.makedirs(folder, exist_ok=True)   # safe to call repeatedly
    png_path = os.path.join(folder, f"{name}.png")
    pdf_path = os.path.join(folder, f"{name}.pdf")
    fig.savefig(png_path, dpi=dpi, bbox_inches="tight")
    fig.savefig(pdf_path, bbox_inches="tight")
    plt.close(fig)
    return png_path