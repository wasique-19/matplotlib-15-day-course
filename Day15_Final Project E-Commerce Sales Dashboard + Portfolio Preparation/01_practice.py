"""Sales dashboard: KPI strip, line, bars, hexbin, histogram. Titles computed from data."""
"""Sales dashboard: KPI strip, line, bars, hexbin, histogram. Titles computed from data."""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import FuncFormatter

# ---- helpers (inlined from chart_style.py so this file runs on its own) ----
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

# ---- end helpers ----

BAR_COLOR = PALETTE["blue"]       # Q1: one Okabe-Ito colour for every bar chart
ACCENT = PALETTE["vermillion"]    # highlight colour
CSV_PATH = "sales.csv"


def make_demo_csv(path, n=1500, seed=7):
    """Create a demo CSV with the columns the dashboard expects (only if none exists)."""
    rng = np.random.default_rng(seed)
    dates = pd.to_datetime("2025-01-01") + pd.to_timedelta(rng.integers(0, 365, n), unit="D")
    age = np.clip(rng.normal(36, 9, n), 18, 75).round()
    amount = np.clip(age * 1.5 + rng.normal(40, 25, n) + (dates.month == 11) * 30, 5, None).round(2)
    pd.DataFrame({
        "date": dates,
        "category": rng.choice(["Electronics", "Clothing", "Groceries", "Books"], n, p=[.35, .25, .3, .1]),
        "region": rng.choice(["North", "South", "East", "West"], n, p=[.3, .2, .3, .2]),
        "amount": amount,
        "age": age,
    }).to_csv(path, index=False)


def load_data(path):
    """Q5: read a real CSV (date, category, region, amount; optional age)."""
    if not os.path.exists(path):
        make_demo_csv(path)
    df = pd.read_csv(path, parse_dates=["date"])
    missing = {"date", "category", "region", "amount"} - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing columns: {sorted(missing)}")
    return df


def money(v, _=None):
    return f"${v:,.0f}"


def tmoney(v):
    """Money for titles: escape $ so matplotlib doesn't read pairs of them as math mode."""
    return money(v).replace("$", r"\$")


def kpi(ax, label, value, note=""):
    ax.axis("off")
    ax.text(0.5, 0.68, value, ha="center", va="center", fontsize=24, fontweight="bold", color=BAR_COLOR)
    ax.text(0.5, 0.25, label, ha="center", va="center", fontsize=12)
    if note:
        ax.text(0.5, 0.05, note, ha="center", va="center", fontsize=9, color="#6B6B6B")


set_report_style()
df = load_data(CSV_PATH)

# ---- aggregates (every title below is computed from these) ----
monthly = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()
monthly.index = monthly.index.to_timestamp()
peak_month, peak_val = monthly.idxmax(), monthly.max()
by_cat = df.groupby("category")["amount"].sum().sort_values(ascending=False)
by_region = df.groupby("region")["amount"].sum().sort_values(ascending=False)   # Q3: high to low
total = df["amount"].sum()

fig = plt.figure(figsize=(17, 11))
gs = GridSpec(3, 4, figure=fig, height_ratios=[0.55, 2, 2])   # Q2: 4 KPI tiles

# ---- KPI strip (Q2: fourth KPI = Best Month) ----
kpi(fig.add_subplot(gs[0, 0]), "Total revenue", money(total))
kpi(fig.add_subplot(gs[0, 1]), "Orders", f"{len(df):,}")
kpi(fig.add_subplot(gs[0, 2]), "Average order", money(df["amount"].mean()))
kpi(fig.add_subplot(gs[0, 3]), "Best month", peak_month.strftime("%b %Y"), money(peak_val))

# ---- Line: monthly revenue, peak highlighted ----
ax = fig.add_subplot(gs[1, 0:2])
ax.plot(monthly.index, monthly.values, marker="o", linewidth=2.5, color=BAR_COLOR)
ax.scatter([peak_month], [peak_val], s=120, color=ACCENT, zorder=3)
ax.set_title(f"Revenue peaked in {peak_month.strftime('%B')} at {tmoney(peak_val)}")
ax.yaxis.set_major_formatter(FuncFormatter(money))
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%b"))
ax.set_ylabel("Revenue")

# ---- Bar: category ----
ax = fig.add_subplot(gs[1, 2])
ax.bar(by_cat.index, by_cat.values, color=BAR_COLOR)
ax.set_title(f"{by_cat.index[0]} earns {by_cat.iloc[0] / total:.0%} of revenue")
ax.yaxis.set_major_formatter(FuncFormatter(money))
ax.tick_params(axis="x", rotation=25)

# ---- Q3: horizontal bar of region revenue, sorted high to low ----
ax = fig.add_subplot(gs[1, 3])
ax.barh(by_region.index, by_region.values, color=BAR_COLOR)
ax.invert_yaxis()                      # biggest on top
ax.set_title(f"{by_region.index[0]} leads regions, {by_region.index[-1]} trails")
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v/1000:,.0f}k"))
ax.xaxis.set_major_locator(plt.MaxNLocator(4))
ax.grid(axis="y", visible=False)
for i, v in enumerate(by_region.values):
    ax.text(v, i, f" {v / total:.0%}", va="center", fontsize=10)

# ---- Q4: hexbin of age vs amount (only if the CSV has an age column) ----
if "age" in df.columns:
    ax = fig.add_subplot(gs[2, 0:2])
    hb = ax.hexbin(df["age"], df["amount"], gridsize=28, cmap="YlGnBu", mincnt=1)
    fig.colorbar(hb, ax=ax, label="Orders per hexagon")
    a1, a3 = df["age"].quantile([.25, .75])
    m1, m3 = df["amount"].quantile([.25, .75])
    ax.set_title(f"Core customers: ages {a1:.0f}-{a3:.0f}, spending {tmoney(m1)}-{tmoney(m3)}")
    ax.set_xlabel("Customer age (years)")
    ax.set_ylabel("Order amount")
    ax.yaxis.set_major_formatter(FuncFormatter(money))

# ---- Histogram of order values ----
ax = fig.add_subplot(gs[2, 2:4])
ax.hist(df["amount"], bins=25, color=BAR_COLOR, edgecolor="white")
med = df["amount"].median()
ax.axvline(med, color=ACCENT, linestyle="--", linewidth=2)
ax.set_title(f"Half of all orders are under {tmoney(med)}")
ax.set_xlabel("Order amount")
ax.set_ylabel("Number of orders")
ax.xaxis.set_major_formatter(FuncFormatter(money))

fig.suptitle("Sales Dashboard", fontsize=20, fontweight="bold")
fig.tight_layout(rect=[0, 0.02, 1, 0.96])
fig.text(0.01, 0.005, f"Source: {CSV_PATH} ({len(df):,} orders)", fontsize=9, color="#6B6B6B")
print("Saved:", save_fig(fig, "sales_dashboard"))