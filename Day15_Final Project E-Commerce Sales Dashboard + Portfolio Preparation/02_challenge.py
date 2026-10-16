"""challenge.py - build the dashboard, optionally per region.

Usage:
    python challenge.py                 # one dashboard per region (loop) + an 'all' version
    python challenge.py --region North  # only North -> figures/dashboard_north.png
"""

# ======================= 1. DATA (was data.py) =======================
import os
import numpy as np
import pandas as pd

REQUIRED = {"date", "category", "region", "amount"}


def make_demo_csv(path, n=1500, seed=7):
    """Create a demo CSV with the expected columns (only used when no CSV exists)."""
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


def load_data(path="sales.csv"):
    """Read the sales CSV (date, category, region, amount; optional age)."""
    if not os.path.exists(path):
        make_demo_csv(path)
    df = pd.read_csv(path, parse_dates=["date"])
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"{path} is missing columns: {sorted(missing)}")
    return df


# =================== 2. STYLE (was chart_style.py) ===================
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


def save_fig(fig, name, folder="figures", dpi=300, close=True):
    """Save a figure as PNG (at `dpi`) and PDF, optionally close it, return the PNG path."""
    os.makedirs(folder, exist_ok=True)   # safe to call repeatedly
    png_path = os.path.join(folder, f"{name}.png")
    pdf_path = os.path.join(folder, f"{name}.pdf")
    fig.savefig(png_path, dpi=dpi, bbox_inches="tight")
    fig.savefig(pdf_path, bbox_inches="tight")
    if close:
        plt.close(fig)
    return png_path


# =================== 3. DASHBOARD (was dashboard.py) =================
import argparse

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import FuncFormatter


BAR_COLOR = PALETTE["blue"]
ACCENT = PALETTE["vermillion"]


def money(v, _=None):
    return f"${v:,.0f}"


def tmoney(v):
    """Money for titles: escape $ so pairs of them aren't read as math mode."""
    return money(v).replace("$", r"\$")


def kpi(ax, label, value, note=""):
    ax.axis("off")
    ax.text(0.5, 0.68, value, ha="center", va="center", fontsize=24, fontweight="bold", color=BAR_COLOR)
    ax.text(0.5, 0.25, label, ha="center", va="center", fontsize=12)
    if note:
        ax.text(0.5, 0.05, note, ha="center", va="center", fontsize=9, color="#6B6B6B")


def monthly_revenue(df):
    m = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()
    m.index = m.index.to_timestamp()
    return m


def summarize(df):
    """Headline numbers used by both the KPI strip and the printed summary."""
    m = monthly_revenue(df)
    return {
        "revenue": df["amount"].sum(),
        "orders": len(df),
        "best_month": m.idxmax(),
        "best_value": m.max(),
    }


def build_dashboard(df, region=None):
    """Return a Figure for df. If region is given, df should already be filtered to it."""
    label = region or "All regions"
    s = summarize(df)
    monthly = monthly_revenue(df)
    by_cat = df.groupby("category")["amount"].sum().sort_values(ascending=False)
    total = s["revenue"]

    fig = plt.figure(figsize=(17, 11))
    gs = GridSpec(3, 4, figure=fig, height_ratios=[0.55, 2, 2])

    # KPI strip
    kpi(fig.add_subplot(gs[0, 0]), "Total revenue", money(total))
    kpi(fig.add_subplot(gs[0, 1]), "Orders", f"{s['orders']:,}")
    kpi(fig.add_subplot(gs[0, 2]), "Average order", money(df["amount"].mean()))
    kpi(fig.add_subplot(gs[0, 3]), "Best month", s["best_month"].strftime("%b %Y"), money(s["best_value"]))

    # Line: monthly revenue
    ax = fig.add_subplot(gs[1, 0:2])
    ax.plot(monthly.index, monthly.values, marker="o", linewidth=2.5, color=BAR_COLOR)
    ax.scatter([s["best_month"]], [s["best_value"]], s=120, color=ACCENT, zorder=3)
    ax.set_title(f"Revenue peaked in {s['best_month'].strftime('%B')} at {tmoney(s['best_value'])}")
    ax.yaxis.set_major_formatter(FuncFormatter(money))
    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%b"))
    ax.set_ylabel("Revenue")

    # Bar: category revenue
    ax = fig.add_subplot(gs[1, 2])
    ax.bar(by_cat.index, by_cat.values, color=BAR_COLOR)
    ax.set_title(f"{by_cat.index[0]} earns {by_cat.iloc[0] / total:.0%} of revenue")
    ax.yaxis.set_major_formatter(FuncFormatter(money))
    ax.tick_params(axis="x", rotation=25)

    # Right-hand bar panel: regions when showing everything,
    # average order by category when filtered (one region = one bar would be pointless)
    ax = fig.add_subplot(gs[1, 3])
    if region is None:
        data = df.groupby("region")["amount"].sum().sort_values(ascending=False)
        ax.barh(data.index, data.values, color=BAR_COLOR)
        ax.set_title(f"{data.index[0]} leads regions, {data.index[-1]} trails")
        ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v/1000:,.0f}k"))
        for i, v in enumerate(data.values):
            ax.text(v, i, f" {v / total:.0%}", va="center", fontsize=10)
    else:
        data = df.groupby("category")["amount"].mean().sort_values(ascending=False)
        ax.barh(data.index, data.values, color=BAR_COLOR)
        if data.max() / data.min() < 1.10:   # under 10% spread: don't oversell a tiny gap
            ax.set_title("Average order is similar across categories")
        else:
            ax.set_title(f"{data.index[0]} has the highest average order")
        ax.xaxis.set_major_formatter(FuncFormatter(money))
        ax.set_xlabel("Average order")
    ax.invert_yaxis()
    ax.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax.grid(axis="y", visible=False)

    # Hexbin: age vs amount (only if the data has an age column)
    if "age" in df.columns:
        ax = fig.add_subplot(gs[2, 0:2])
        hb = ax.hexbin(df["age"], df["amount"], gridsize=24, cmap="YlGnBu", mincnt=1)
        fig.colorbar(hb, ax=ax, label="Orders per hexagon")
        a1, a3 = df["age"].quantile([.25, .75])
        m1, m3 = df["amount"].quantile([.25, .75])
        ax.set_title(f"Core customers: ages {a1:.0f}-{a3:.0f}, spending {tmoney(m1)}-{tmoney(m3)}")
        ax.set_xlabel("Customer age (years)")
        ax.set_ylabel("Order amount")
        ax.yaxis.set_major_formatter(FuncFormatter(money))

    # Histogram of order values
    ax = fig.add_subplot(gs[2, 2:4])
    ax.hist(df["amount"], bins=25, color=BAR_COLOR, edgecolor="white")
    med = df["amount"].median()
    ax.axvline(med, color=ACCENT, linestyle="--", linewidth=2)
    ax.set_title(f"Half of all orders are under {tmoney(med)}")
    ax.set_xlabel("Order amount")
    ax.set_ylabel("Number of orders")
    ax.xaxis.set_major_formatter(FuncFormatter(money))

    fig.suptitle(f"Sales Dashboard: {label}", fontsize=20, fontweight="bold")
    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    fig.text(0.01, 0.005, f"Source: sales.csv, {label} ({s['orders']:,} orders)", fontsize=9, color="#6B6B6B")
    return fig


def summary_line(df, label):
    s = summarize(df)
    return (f"{label:<12} revenue {money(s['revenue'])} | orders {s['orders']:,} | "
            f"best month {s['best_month'].strftime('%b %Y')} ({money(s['best_value'])})")


def export_version(df, region=None):
    """Filter, build, save and close one dashboard version; print its summary."""
    sub = df if region is None else df[df["region"] == region]
    fig = build_dashboard(sub, region)
    name = "dashboard_" + (region.lower() if region else "all")
    save_fig(fig, name, close=False)
    plt.close(fig)                     # free memory before the next version
    print(summary_line(sub, region or "All regions"))


def main():
    df = load_data()
    regions = sorted(df["region"].unique())

    parser = argparse.ArgumentParser(description="Build the sales dashboard.")
    parser.add_argument("--region", help=f"only this region ({', '.join(regions)})")
    args = parser.parse_args()

    set_report_style()
    if args.region:
        match = [r for r in regions if r.lower() == args.region.lower()]
        if not match:
            parser.error(f"unknown region '{args.region}'. Choose from: {', '.join(regions)}")
        export_version(df, match[0])
    else:
        for region in regions:         # one version per region
            export_version(df, region)
        export_version(df, None)       # plus the all-regions version
    plt.rcdefaults()


if __name__ == "__main__":
    main()