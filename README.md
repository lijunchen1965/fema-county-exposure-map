# FEMA County-Month Disaster Exposure Map

An interactive Streamlit application showing monthly county-level exposure to COVID-19 and qualifying nonbiological major-disaster declarations from October 2014 through September 2024.

## Live application

The public Streamlit application link will be added after deployment.

## Exposure categories

The map displays four mutually exclusive categories:

- Not exposed
- COVID-19 only
- Qualifying nonbiological disaster only
- COVID-19 and qualifying nonbiological disaster

Use the time slider or Play/Pause controls to examine changes in county exposure across the 120-month study period.

## Data

The application is based on publicly available FEMA disaster-declaration data:

[FEMA OpenFEMA Disaster Declarations Summaries](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2)

Qualifying nonbiological disasters are major-disaster declarations retained under the project's IA/IH assistance criteria. COVID-19 exposure is analyzed separately.

County geography accommodates changes in Connecticut county definitions during the study period.

## Repository contents

- `streamlit_app.py` — Streamlit application
- `assets/county_month_exposure_slider.json` — prepared Plotly figure
- `requirements.txt` — Python package requirements

## Run locally

Install the required packages:

```powershell
python -m pip install -r requirements.txt