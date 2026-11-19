"""Re-run the analysis from the raw files, in dependency order (VISUELLE 2.0 + the consumer survey).

    python -m src.run_all

Needs the raw data, which is not in this repository: VISUELLE 2.0 in visuelle2/ (from the authors' request form,
https://humaticslab.github.io/forecasting/visuelle) and the survey export in data/raw/survey/. Writes the result tables
and charts in outputs/ and every reported number, with its source, in reports/claims_register.csv.
"""
import time

from . import (data_quality, literature, pilot_design, survey_analysis, trends, vis_customers, vis_financials,
               vis_forecast, vis_lifecycle, vis_risk_model)
from .utils import CLAIMS

STEPS = [
    ("Stock, week-2 forecasting, what-if simulation", vis_forecast.main),
    ("Demand lifecycles and markdown timing", vis_lifecycle.main),
    ("Pre-launch excess-stock risk model", vis_risk_model.main),
    ("Customer segments, CLTV, frequency bands", vis_customers.main),
    ("Market trends, seasonality, Google Trends value", trends.main),
    ("Pilot experiment design (power analysis)", pilot_design.main),
    ("Financial statements built from the data", vis_financials.main),
    ("Survey analysis (real responses only)", survey_analysis.run),
    ("Data overview, cleaning log, EDA tables", data_quality.main),
    ("Literature facts -> claims register", literature.main),
]


def main():
    CLAIMS.unlink(missing_ok=True)
    for name, fn in STEPS:
        t = time.time()
        print(f"\n=== {name} ===")
        fn()
        print(f"--- done in {time.time() - t:.0f}s")


if __name__ == "__main__":
    main()
