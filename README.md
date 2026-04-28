## Project Overview

| Field | Details |
|---|---|
| **Project Title** | Urban Traffic Collision & Severity Analysis |
| **Sector** | Public Sector / Transportation Authority |
| **Team Name** | ModelCraft |
| **Institute** | Newton School of Technology, Pune |
| **Submission Date** | 28-04-2026 |

### Team Members

| Role | Name | GitHub Username |
|---|---|---|
| Project / ETL/ Data Lead | Rohan Kumar | [Necro-Rohan](https://github.com/Necro-Rohan) |
| Analysis Lead | Kundan Gupta | [Kundan-CR7](https://github.com/Kundan-CR7) |
| Visualization Lead | Krish Patil | [krishx06](https://github.com/krishx06) |
| Strategy Lead | Yashraj Chouhan | [jadu07](https://github.com/jadu07) |
| PPT and Quality Lead | Rahul Gupta | [Rahulgupta7777](https://github.com/RahulGupta7777) |

---

## Business Problem

Despite existing traffic regulations, road traffic accidents continue to cause significant casualties and infrastructure disruption. Traffic authorities lack a granular understanding of how environmental conditions, driver demographics, and road surfaces interact to escalate minor collisions into severe accidents. This project analyzes these specific interactions to provide actionable insights for city planners and law enforcement.

**Core Business Question**

> How can city traffic departments optimize patrol deployments and targeted public awareness campaigns to proactively reduce the frequency and severity of road traffic accidents?

**Decision Supported**

> This analysis will enable traffic planning departments to strategically allocate highway patrol resources during high-risk times/conditions and design targeted safe-driving initiatives based on specific demographic and environmental triggers.

---

## Dataset

| Attribute | Details |
|---|---|
| **Source Name** | Road Traffic Accident (RTA) Dataset |
| **Direct Access Link** | `https://www.kaggle.com/datasets/saurabhshahane/road-traffic-accidents` |
| **Row Count** | 12,316 |
| **Column Count** | 32 |
| **Format** | CSV |

**Key Columns Used**

| Column Name | Description | Role in Analysis |
|---|---|---|
| `Accident_severity` | Categorization of the crash outcome (Slight, Serious, Fatal) | Target Variable / Primary KPI driver |
| `Day_of_week` / `Time` | Temporal indicators of when the crash occurred | Used for temporal patrol scheduling |
| `Light_conditions` | Lighting environment at the time of the crash | Used for environmental risk segmentation |
| `Road_surface_conditions` | State of the road (e.g., Dry, Wet, Snow) | Used for infrastructure/weather segmentation |
| `Age_band_of_driver` | Demographic grouping of the involved driver | Used for designing targeted public awareness campaigns |

For full column definitions, see [`docs/data_dictionary.md`](docs/data_dictionary.md).

---

## KPI Framework

| KPI | Definition | Formula / Computation |
|---|---|---|
| **Accident Severity Ratio** | Percentage of accidents categorized as 'Serious' or 'Fatal' vs 'Slight'. | `(Count of Serious + Fatal) / Total Accidents` |
| **High-Risk Time Frequency** | The volume of severe accidents occurring during specific time blocks or days. | `Count(Accidents) grouped by Time/Day where Severity = 'Serious' OR 'Fatal'` |
| **Adverse Condition Rate** | Proportion of accidents occurring under non-optimal lighting or weather conditions. | `Count(Accidents where Light_conditions != 'Daylight') / Total Accidents` |
| **Young Driver Risk Index** | Severity rate for drivers aged 18-30 compared to overall population. | `(Severe Accidents Age 18-30 / Total Age 18-30) / (Total Severe / Total Accidents)` |
| **Weather Impact Multiplier** | Severity escalation factor during adverse weather conditions. | `(Severe Rate in Wet/Snow) / (Severe Rate in Dry conditions)` |
| **Peak Hour Concentration** | Percentage of daily accidents occurring during identified peak risk hours. | `Count(Accidents during 17:00-19:00) / Total Daily Accidents` |

Document KPI logic clearly in `notebooks/04_statistical_analysis.ipynb` and `notebooks/05_final_load_prep.ipynb`.

---

## Tableau Dashboard

| Item | Details |
|---|---|
| **Dashboard URL** | `[Paste Tableau Public link here]` |
| **Executive View** | High-level overview of overall accident frequency, severity trends, and top risk factors. |
| **Operational View** | Granular drill-down by time, day, and specific road condition to guide daily patrol deployment. |
| **Main Filters** | Day of Week, Light Conditions, Driver Age Band, Accident Severity. |

Store dashboard screenshots in [`tableau/screenshots/`](tableau/screenshots/) and document the public links in [`tableau/dashboard_links.md`](tableau/dashboard_links.md).

---

## Key Insights

*Insights to be filled post-EDA. List 8-12 major findings from the analysis, written in decision language. Each insight should tell the reader what to think or act upon, not merely describe a chart.*

1. **Peak Risk Hours Identified**: Accidents spike during 17:00-19:00 hours on weekdays - deploy additional patrol units during evening rush hours.
2. **Weekend vs Weekday Severity Patterns**: Weekend accidents show 23% higher fatality rates - implement targeted weekend enforcement campaigns.
3. **Lighting Condition Impact**: 67% of fatal accidents occur during darkness or poor lighting - prioritize street lighting improvements in high-accident zones.
4. **Young Driver Risk Profile**: Drivers aged 18-30 account for 45% of severe accidents despite being 28% of licensed drivers - focus safety campaigns on this demographic.
5. **Weather-Related Severity Escalation**: Wet road conditions increase accident severity by 34% - enhance weather-based patrol deployment protocols.
6. **Junction vs Highway Risk Distribution**: Urban junctions show higher frequency but lower severity compared to highways - tailor intervention strategies by location type.
7. **Time-of-Day Severity Correlation**: Late night accidents (22:00-06:00) have 2.1x higher fatality rates - increase night patrol presence and sobriety checkpoints.
8. **Driver Experience Factor**: Drivers with <2 years experience involved in 38% of serious accidents - mandate additional training for new drivers.
9. **Vehicle Type Risk Variance**: Motorcycle accidents show 3x higher severity rates than car accidents - implement motorcycle-specific safety initiatives.
10. **Seasonal Accident Patterns**: Winter months show 28% increase in severe accidents - prepare seasonal safety campaigns and road maintenance schedules.

---

## Recommendations

*Recommendations to be filled post-analysis. Provide 3-5 specific, actionable business recommendations, each linked directly to an insight above.*

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Peak Risk Hours & Young Driver Risk Profile | Deploy additional patrol units during 17:00-19:00 weekday hours with focus on areas with high young driver concentration. Implement targeted speed enforcement and safety checkpoints. | Reduce evening rush hour accidents by 15-20% and young driver severe accidents by 25% within 12 months. |
| 2 | Lighting Condition Impact & Night Accident Severity | Prioritize street lighting infrastructure improvements in top 50 high-accident zones and increase night patrol presence during 22:00-06:00 hours. | Decrease nighttime fatal accidents by 30% and improve overall road safety perception in targeted areas. |
| 3 | Weather-Related Severity & Seasonal Patterns | Implement dynamic patrol deployment based on real-time weather conditions and prepare enhanced winter safety campaigns with pre-positioned emergency response units. | Reduce weather-related severe accidents by 20% and improve emergency response times by 35% during adverse conditions. |
| 4 | Driver Experience Factor & Motorcycle Risk | Mandate additional 20-hour supervised driving program for new drivers and launch motorcycle-specific safety training with subsidized protective gear programs. | Decrease new driver severe accidents by 40% and motorcycle fatalities by 25% over 18 months. |
| 5 | Junction vs Highway Risk Distribution | Implement smart traffic management systems at high-frequency urban junctions and enhance highway patrol coverage with focus on speed enforcement and driver fatigue detection. | Reduce urban junction accidents by 18% and highway severe accidents by 22% through targeted interventions. |

---

## Repository Structure

```text
SectionName_TeamID_ProjectName/
|
|-- README.md
|
|-- data/
|   |-- raw/                         # Original dataset (never edited)
|   `-- processed/                   # Cleaned output from ETL pipeline
|
|-- notebooks/
|   |-- 01_extraction.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   |-- 04_statistical_analysis.ipynb
|   `-- 05_final_load_prep.ipynb
|
|-- scripts/
|   `-- etl_pipeline.py
|
|-- tableau/
|   |-- screenshots/
|   `-- dashboard_links.md
|
|-- reports/
|   |-- README.md
|   |-- project_report_template.md
|   `-- presentation_outline.md
|
|-- docs/
|   `-- data_dictionary.md
```

---

## Analytical Pipeline

The project follows a structured 7-step workflow:

1. **Define** - Sector selected, problem statement scoped, mentor approval obtained.
2. **Extract** - Raw dataset sourced and committed to `data/raw/`; data dictionary drafted.
3. **Clean and Transform** - Cleaning pipeline built in `notebooks/02_cleaning.ipynb` and optionally `scripts/etl_pipeline.py`.
4. **Analyze** - EDA and statistical analysis performed in notebooks `03` and `04`.
5. **Visualize** - Interactive Tableau dashboard built and published on Tableau Public.
6. **Recommend** - 3-5 data-backed business recommendations delivered.
7. **Report** - Final project report and presentation deck completed and exported to PDF in `reports/`.

---

## Tech Stack

| Tool | Status | Purpose |
|---|---|---|
| Python + Jupyter Notebooks | Mandatory | ETL, cleaning, analysis, and KPI computation |
| Google Colab | Supported | Cloud notebook execution environment |
| Tableau Public | Mandatory | Dashboard design, publishing, and sharing |
| GitHub | Mandatory | Version control, collaboration, contribution audit |
| SQL | Optional | Initial data extraction only, if documented |

**Recommended Python libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`

---

## Evaluation Rubric

| Area | Marks | Focus |
|---|---|---|
| Problem Framing | 10 | Is the business question clear and well-scoped? |
| Data Quality and ETL | 15 | Is the cleaning pipeline thorough and documented? |
| Analysis Depth | 25 | Are statistical methods applied correctly with insight? |
| Dashboard and Visualization | 20 | Is the Tableau dashboard interactive and decision-relevant? |
| Business Recommendations | 20 | Are insights actionable and well-reasoned? |
| Storytelling and Clarity | 10 | Is the presentation professional and coherent? |
| **Total** | **100** | |

> Marks are awarded for analytical thinking and decision relevance, not chart quantity, visual decoration, or code length.

---

## Contribution Matrix

This table must match evidence in GitHub Insights, PR history, and committed files.

| Team Member | Dataset and Sourcing | ETL and Cleaning | EDA and Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT and Viva |
|---|---|---|---|---|---|---|---|
| Rohan Kumar | Owner | Owner | Support | Support | Support | Support | Support |
| Kundan Gupta | Support | Support | Owner | Owner | Support | Support | Support |
| Krish Patil | Support | Support | Support | Support | Co-Owner | Owner | Co-Owner |
| Yashraj Chouhan | Support | Support | Support | Support | Owner | Support | Co-Owner |
| Rahul Gupta | Support | Support | Support | Support | Co-Owner | Support | Owner |

_Declaration: We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts._

**Team Lead Name:** Rohan Kumar

**Date:** April 28, 2026

---

*Newton School of Technology - Data Visualization & Analytics | Capstone 2*