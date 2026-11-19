# From Trend To Waste: A Data-Driven Analysis Of Fast-Fashion Consumer Behaviour And Excess-Inventory Risk

Fast fashion's environmental cost is linked to overproduction (sources in the report). This project studies the shop end
of it: stock delivered to shops that customers never buy. It uses real data from one Italian fast-fashion chain, Nuna Lie
(the VISUELLE 2.0 dataset: 5,355 products in 110 shops over six seasons, 2017-2019, and 3,184,162
loyalty-card purchase lines), and a survey of 122 consumers. It measures how much stock is left over, shows that the
risk can be predicted before launch and after two weeks of sales, and estimates what acting early would be worth.

**What is bad for the planet is also bad for the margin.**

The full report: [From_Trend_To_Waste_Report.pdf](From_Trend_To_Waste_Report.pdf)

## Key results

- **A third of stock is left over.** 31.6% of the 2,334,430 units delivered were still unsold after
  12 weeks, although shops rarely ran out (2.0% of shop-weeks).
- **Demand peaks early, markdowns come late.** 70% of products sell best in their first three weeks, but
  the first markdown comes in week 8 on median, when demand is down to 53% of its peak.
- **The risk is predictable.** Before launch, a model ranks high-leftover products with ROC-AUC 0.69;
  after two weeks of sales, a forecast cuts the error from 60% to 39% and flags 55% of the
  products that end badly.
- **Acting at week 2 pays.** Replaying the unseen 2019 seasons, a week-2 rule (cut later deliveries, mark down earlier)
  would have reduced unsold stock by 11.9% with revenue -0.7%, and raised gross profit by
  +8.7% (unit cost assumed at 50% of full price).
- **Consumers value durability but wear clothes briefly.** A 3+ year lifespan was the most important feature in a
  conjoint experiment (31% of the decision), yet 36% stop wearing a fast-fashion item after
  ten wears or fewer.

## Methods

| Stage | Question | Methods |
|---|---|---|
| Before launch | Which new products will end with high leftover? | Logistic regression (odds ratios), decision tree, gradient boosting |
| After two weeks | How much will sell in weeks 3-12? | Naive, category profile, Poisson regression and gradient-boosting forecasts |
| End of season | What happened, and who bought? | k-means demand lifecycles, markdown timing, customer segments and CLTV |
| What if | What would acting at week 2 change? | Week-by-week stock simulation, financial statements, pilot power analysis |
| Consumers | How are clothes used and disposed of? | Survey, rating-based conjoint, shopper groups |

Models are trained on the 2017-2018 seasons and tested on the 2019 seasons, which they never see.

## Repository

| Path | Contents |
|---|---|
| `From_Trend_To_Waste_Report.pdf` | The report: problem, literature, data, methods, results, dashboards and recommendations |
| `src/` | The analysis pipeline, one module per analysis; `run_all.py` runs them in order |
| `dashboard/` | Two Streamlit apps: a guided demo (`demo_app.py`) and an early-warning dashboard (`app.py`) |
| `outputs/tables/`, `outputs/figures/` | The result tables and charts |
| `outputs/models/` | The trained pre-launch risk model used by the dashboard (a scikit-learn pipeline saved with joblib) |
| `survey/` | The Google Apps Script that builds the survey form, and the conjoint design |
| `reports/claims_register.csv` | Every reported number with the script that produced it |

## Running it

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m src.run_all
.venv/bin/streamlit run dashboard/demo_app.py
```

The raw data is not in this repository. VISUELLE 2.0 is available from its authors through a request form
(https://humaticslab.github.io/forecasting/visuelle); place it in `visuelle2/`. The survey responses are personal data and
are not shared; the survey analysis reads its export from `data/raw/survey/`. The dashboards read the pipeline's outputs,
so run the pipeline first. Tested with Python 3.14 and the versions in `requirements.txt`.

## Data notes

All retail data comes from one retailer, Nuna Lie, through VISUELLE 2.0 (Humatics Lab, University of Verona), used under
the dataset's terms and not redistributed here. The dataset's prices are normalised, so money is in index units and the
results are reported as ratios; unit cost is not in the data, so margins use an assumed cost of 40-60% of full price.
Environmental figures are estimates, and the data covers deliveries and sales, not production.

M.Tech course project, 21CSE668T Business Data Analytics, SRM Institute of Science and Technology, 2026.
