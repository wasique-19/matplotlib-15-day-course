"""
dashboard_2.py - Personal Study Tracker dashboard (Day 15 Mini Assignment)

THREE QUESTIONS (written first, one chart each; a 4th added for depth)
  Q1. Am I studying consistently, and do I hit my weekly target?   -> line chart
  Q2. Where does my study time actually go?                        -> horizontal bar
  Q3. At what time of day do I focus best?                         -> bar chart
  Q4. Do longer sessions cost me focus?                            -> scatter + trend

DATA: study_log.csv with columns  date, subject, time_of_day, hours, focus (1-10).
If the file is missing, a demo log is generated so the script always runs.
Replace it with your own log to make the dashboard real.

OUTPUT (saved next to this script): dashboard_2.png (300 dpi), dashboard_2.pdf,
dashboard_2_summary.txt (the four-sentence insight summary).
"""
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "study_log.csv"
WEEKLY_TARGET = 14          # hours per week
TIME_ORDER = ["Morning", "Afternoon", "Evening", "Night"]

# Okabe-Ito colour-blind-safe palette, used everywhere
BLUE, ORANGE, GREEN, VERMILLION = "#0072B2", "#E69F00", "#009E73", "#D55E00"
GREY = "#6B6B6B"


# ----------------------------------------------------------------- data
def make_demo_csv(path, seed=21):
    """12 weeks of fake sessions (starts on a Monday). Replace with your real log."""
    rng = np.random.default_rng(seed)
    days = pd.date_range("2026-07-20", periods=84, freq="D")
    subjects = ["Python", "Matplotlib", "Pandas", "English vocab", "Maths"]
    sub_p = [0.30, 0.25, 0.20, 0.15, 0.10]
    tod_bonus = {"Morning": 0.9, "Afternoon": 0.0, "Evening": -0.3, "Night": -1.1}
    rows = []
    for i, day in enumerate(days):
        n_sessions = rng.choice([0, 1, 2, 2, 3], p=[0.10, 0.25, 0.30, 0.20, 0.15])
        if day.weekday() >= 5:
            n_sessions += 1                              # weekends: a bit more
        for _ in range(n_sessions):
            tod = rng.choice(TIME_ORDER, p=[0.30, 0.20, 0.30, 0.20])
            hours = float(np.clip(rng.normal(1.2 + i * 0.004, 0.6), 0.3, 4.0))
            focus = 8.0 + tod_bonus[tod] - 0.9 * (hours - 1.3) + rng.normal(0, 0.8)
            rows.append({"date": day, "subject": rng.choice(subjects, p=sub_p),
                         "time_of_day": tod, "hours": round(hours, 2),
                         "focus": round(float(np.clip(focus, 1, 10)), 1)})
    pd.DataFrame(rows).to_csv(path, index=False)


def load_log(path=CSV_PATH):
    if not path.exists():
        make_demo_csv(path)
    df = pd.read_csv(path, parse_dates=["date"])
    need = {"date", "subject", "time_of_day", "hours", "focus"}
    if need - set(df.columns):
        raise ValueError(f"{path.name} is missing columns: {sorted(need - set(df.columns))}")
    return df


def longest_streak(df):
    """Longest run of consecutive calendar days with at least one session."""
    studied = set(df["date"].dt.normalize())
    best = run = 0
    for day in pd.date_range(df["date"].min(), df["date"].max(), freq="D"):
        run = run + 1 if day in studied else 0
        best = max(best, run)
    return best


# ------------------------------------------------------------- analysis
def analyse(df):
    a = {}
    a["total_hours"] = df["hours"].sum()
    a["study_days"] = df["date"].dt.normalize().nunique()
    a["span_days"] = (df["date"].max() - df["date"].min()).days + 1
    a["avg_focus"] = df["focus"].mean()
    a["streak"] = longest_streak(df)

    weekly = df.set_index("date")["hours"].resample("W-SUN").sum()
    a["weekly"] = weekly
    a["weeks_on_target"] = int((weekly >= WEEKLY_TARGET).sum())
    a["first4"], a["last4"] = weekly.head(4).mean(), weekly.tail(4).mean()

    a["by_subject"] = df.groupby("subject")["hours"].sum().sort_values(ascending=False)
    a["focus_by_tod"] = df.groupby("time_of_day")["focus"].mean().reindex(TIME_ORDER)
    a["r"] = df["hours"].corr(df["focus"])
    a["slope"], a["intercept"] = np.polyfit(df["hours"], df["focus"], 1)
    return a


def insight_summary(a):
    """Exactly four sentences, every number computed from the data."""
    subj = a["by_subject"]
    tod = a["focus_by_tod"]
    best_t, worst_t = tod.idxmax(), tod.idxmin()
    n_weeks = len(a["weekly"])
    s1 = (f"Over {n_weeks} weeks I logged {a['total_hours']:.0f} hours on {a['study_days']} study days, "
          f"and I hit my {WEEKLY_TARGET}-hour weekly target in {a['weeks_on_target']} of {n_weeks} weeks.")
    s2 = (f"{subj.index[0]} took the largest share of my time ({subj.iloc[0] / subj.sum():.0%}), "
          f"while {subj.index[-1]} got the least ({subj.iloc[-1] / subj.sum():.0%}).")
    s3 = (f"My focus averaged {tod[best_t]:.1f}/10 in the {best_t.lower()} but only "
          f"{tod[worst_t]:.1f}/10 at {worst_t.lower()}, so I should schedule my hardest topics early.")
    link = "negatively" if a["r"] < 0 else "positively"
    s4 = (f"Session length and focus are {link} associated (r = {a['r']:.2f}), which suggests, "
          f"but does not prove, that shorter sessions work better for me.")
    return [s1, s2, s3, s4]


# ------------------------------------------------------------ plotting
def style():
    plt.rcParams.update({
        "font.size": 12, "axes.titlesize": 14, "axes.titleweight": "bold",
        "axes.titlelocation": "left", "axes.spines.top": False,
        "axes.spines.right": False, "axes.grid": True, "axes.axisbelow": True,
        "grid.color": "#CCCCCC", "grid.alpha": 0.5, "grid.linestyle": "--",
        "pdf.fonttype": 42,
    })


def kpi(ax, label, value, note=""):
    ax.axis("off")
    ax.text(0.5, 0.68, value, ha="center", va="center", fontsize=26, fontweight="bold", color=BLUE)
    ax.text(0.5, 0.26, label, ha="center", va="center", fontsize=12)
    if note:
        ax.text(0.5, 0.05, note, ha="center", va="center", fontsize=9, color=GREY)


def build_figure(df, a):
    fig = plt.figure(figsize=(16, 10.5))
    gs = GridSpec(3, 4, figure=fig, height_ratios=[0.55, 2, 2])

    # KPI strip
    kpi(fig.add_subplot(gs[0, 0]), "Total study hours", f"{a['total_hours']:.0f} h")
    kpi(fig.add_subplot(gs[0, 1]), "Days studied", f"{a['study_days']} / {a['span_days']}",
        f"{a['study_days'] / a['span_days']:.0%} of days")
    kpi(fig.add_subplot(gs[0, 2]), "Average focus", f"{a['avg_focus']:.1f} / 10")
    kpi(fig.add_subplot(gs[0, 3]), "Longest streak", f"{a['streak']} days")

    # Q1: weekly consistency
    ax = fig.add_subplot(gs[1, 0:2])
    w = a["weekly"]
    ax.plot(w.index, w.values, marker="o", linewidth=2.5, color=BLUE, label="Weekly hours")
    ax.axhline(WEEKLY_TARGET, color=VERMILLION, linestyle="--", linewidth=2, label=f"Target ({WEEKLY_TARGET} h)")
    trend = "rose" if a["last4"] > a["first4"] else "fell"
    ax.set_title(f"Weekly hours {trend} from {a['first4']:.0f} to {a['last4']:.0f}; "
                 f"target hit in {a['weeks_on_target']} of {len(w)} weeks")
    ax.set_xlabel("Week ending")
    ax.set_ylabel("Hours studied")
    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%d %b"))
    ax.set_ylim(0, max(w.max(), WEEKLY_TARGET) * 1.2)
    ax.legend(loc="lower right")

    # Q2: where time goes
    ax = fig.add_subplot(gs[1, 2:4])
    subj = a["by_subject"]
    ax.barh(subj.index, subj.values, color=BLUE)
    ax.invert_yaxis()
    ax.set_title(f"{subj.index[0]} takes {subj.iloc[0] / subj.sum():.0%} of all study time")
    ax.set_xlabel("Hours studied")
    ax.grid(axis="y", visible=False)
    for i, v in enumerate(subj.values):
        ax.text(v, i, f"  {v:.0f} h", va="center", fontsize=10)
    ax.set_xlim(0, subj.max() * 1.15)

    # Q3: focus by time of day
    ax = fig.add_subplot(gs[2, 0:2])
    tod = a["focus_by_tod"]
    colors = [VERMILLION if t == tod.idxmax() else BLUE for t in tod.index]
    ax.bar(tod.index, tod.values, color=colors)
    ax.set_ylim(0, 10)
    ax.set_title(f"Focus is highest in the {tod.idxmax().lower()} ({tod.max():.1f}/10)")
    ax.set_xlabel("Time of day")
    ax.set_ylabel("Average focus (1-10)")
    for i, v in enumerate(tod.values):
        ax.text(i, v + 0.15, f"{v:.1f}", ha="center", fontsize=11)

    # Q4: session length vs focus
    ax = fig.add_subplot(gs[2, 2:4])
    ax.scatter(df["hours"], df["focus"], s=40, alpha=0.5, color=GREEN, edgecolor="white")
    xs = np.linspace(df["hours"].min(), df["hours"].max(), 50)
    ax.plot(xs, a["slope"] * xs + a["intercept"], color=VERMILLION, linewidth=2.5, label="Trend line")
    if abs(a["r"]) < 0.2:
        title = f"Session length and focus show no clear link (r = {a['r']:.2f})"
    else:
        title = f"Longer sessions go with {'lower' if a['r'] < 0 else 'higher'} focus (r = {a['r']:.2f})"
    ax.set_title(title)
    ax.set_xlabel("Session length (hours)")
    ax.set_ylabel("Focus score (1-10)")
    ax.legend(loc="upper right")

    fig.suptitle("My Study Tracker: 12-Week Review", fontsize=20, fontweight="bold")
    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    fig.text(0.01, 0.005, f"Source: {CSV_PATH.name} ({len(df)} sessions). Demo data unless replaced with your own log.",
             fontsize=9, color=GREY)
    return fig


def main():
    style()
    df = load_log()
    a = analyse(df)
    fig = build_figure(df, a)
    fig.savefig(HERE / "dashboard_2.png", dpi=300, bbox_inches="tight")   # 300 dpi PNG
    fig.savefig(HERE / "dashboard_2.pdf", bbox_inches="tight")            # vector PDF
    plt.close(fig)

    sentences = insight_summary(a)
    (HERE / "dashboard_2_summary.txt").write_text(" ".join(sentences) + "\n", encoding="utf-8")
    print("Saved dashboard_2.png, dashboard_2.pdf, dashboard_2_summary.txt\n")
    print("INSIGHT SUMMARY")
    for i, s in enumerate(sentences, 1):
        print(f"{i}. {s}")
    plt.rcdefaults()


if __name__ == "__main__":
    main()