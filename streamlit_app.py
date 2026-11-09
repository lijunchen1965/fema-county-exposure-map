
# For Streamlit app to visualize FEMA county-month exposure data.


from pathlib import Path

import plotly.io as pio
import streamlit as st


# This file is in ChildMaltreatment/apps/, so parents[1] is the project root.
ROOT = Path(__file__).resolve().parent

FIGURE_PATH = (
    ROOT
    / "assets"
    / "county_month_exposure_slider.json"
)

st.set_page_config(
    page_title="FEMA County-Month Exposure",
    layout="wide",
)

st.title("FEMA County-Month Disaster Exposure")

st.markdown(
    """
    County-month exposure to COVID-19 and qualifying
    nonbiological major-disaster declarations,
    October 2014 through September 2024.
    """
)

st.caption(
    "Exploratory visualization based on publicly available FEMA data. "
    "This application is not an official FEMA product."
)

# validation: check that the figure JSON file exists before trying to read it
if not FIGURE_PATH.exists():
    st.error(
        "The Plotly figure JSON file was not found:\n\n"
        f"{FIGURE_PATH}"
    )
    st.stop()

# fig = pio.read_json(FIGURE_PATH)
@st.cache_resource(show_spinner="Loading the FEMA map...")
def load_figure(figure_path: str, modified_time: int):
    return pio.read_json(figure_path)

fig = load_figure(
    str(FIGURE_PATH),
    FIGURE_PATH.stat().st_mtime_ns,
)


st.plotly_chart(
    fig,
    width="stretch",
    config={
        "displaylogo": False,
        "responsive": True,
    },
)

