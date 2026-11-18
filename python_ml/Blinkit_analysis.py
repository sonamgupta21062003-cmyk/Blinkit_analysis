from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np


def apply_blinkit_theme():
    st.markdown("""
    <style>

    /* Main application backstreaground */
    .stApp {
        background-color: #F7F9F2;
        color: #243B2A;
    }

    /* Main content text */
    .stApp p,
    .stApp span,
    .stApp label,
    .stApp li,
    .stApp div {
        color: #243B2A;
    }

    /* Headings */
    h1, h2, h3, h4 {
        color: #176B35 !important;
        font-weight: 700;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #FFF2B2;
    }

    [data-testid="stSidebar"] * {
        color: #24452D !important;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #DCE8D4;
        padding: 18px;
        border-radius: 14px;
        box-shadow: 0 2px 8px rgba(30, 80, 40, 0.06);
    }

    [data-testid="stMetricLabel"] {
        color: #52734D !important;
    }

    [data-testid="stMetricValue"] {
        color: #176B35 !important;
        font-weight: 700;
    }

    /* Buttons */
    .stButton > button {
        background-color: #258B45;
        color: #FFFFFF !important;
        border: none;
        border-radius: 9px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #176B35;
        color: #FFFFFF !important;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab"] {
        color: #365C3C !important;
        font-weight: 600;
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #17833B !important;
        border-bottom-color: #F7D34A !important;
    }

    /* Input fields */
    .stTextInput input,
    .stNumberInput input,
    .stDateInput input,
    .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF;
        color: #243B2A !important;
    }

    /* Dataframes and tables */
    [data-testid="stDataFrame"],
    [data-testid="stTable"] {
        background-color: #FFFFFF;
    }

    /* Links */
    .stApp a {
        color: #16833B !important;
    }

    </style>
    """, unsafe_allow_html=True)



st.set_page_config(
    page_title="Blinkit Analytics & ML",
    page_icon="🛒",
    layout="wide",
)

apply_blinkit_theme()

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "Outputs"


@st.cache_data
def load_csv(filename):
    path = OUTPUT_DIR / filename
    if not path.exists():
        return None
    return pd.read_csv(path)


def show_missing_file(filename):
    st.warning(
        f"Could not find `{filename}`. Place this file inside the "
        f"`Outputs` folder next to `app.py`."
    )


st.title("Blinkit | Business Analytics & Machine Learning")
st.caption(
    "Interactive portfolio application presenting the completed "
    "customer segmentation, delivery-model evaluation, and demand-forecasting work."
)

# Load the saved analysis outputs. This app reads the existing reports;
# it does not rerun model training.
ml_report = load_csv("blinkit_ml_model_comparison.csv")
customer_report = load_csv("blinkit_customer_segment_report.csv")
demand_importance = load_csv("blinkit_demand_feature_importance.csv")
customer_segments = load_csv("blinkit_customer_segments.csv")
delivery_report = load_csv("blinkit_delivery_model_comparison.csv")
demand_report = load_csv("blinkit_demand_model_comparison.csv")
demand_predictions = load_csv("blinkit_demand_predictions.csv")

tab_overview, tab_customers, tab_models, tab_forecast = st.tabs(
    ["Project Overview", "Customer Segmentation", "Model Evaluation", "Demand Forecasting"]
)

with tab_overview:
    st.subheader("Project outputs")
    c1, c2, c3 = st.columns(3)
    c1.metric("Customer segmentation", "Completed")
    c2.metric("Delivery classification", "Evaluated")
    c3.metric("Demand forecasting", "Evaluated")

    st.markdown(
        """
        This application brings together the saved outputs from the Blinkit
        analytics project. It presents historical customer segments, compares
        machine-learning experiments, and displays demand-forecasting results.

        **Interpretation note:** model scores are experimental results on the
        available dataset. They should not be treated as proof of production
        readiness or as guaranteed future performance.
        """
    )

    if ml_report is not None:
        st.markdown("#### Saved ML summary")
        st.dataframe(ml_report, use_container_width=True, hide_index=True)
    else:
        show_missing_file("blinkit_ml_model_comparison.csv")

with tab_customers:
    st.subheader("Customer segmentation")

    if customer_report is not None:
        report = customer_report.copy()

        # The report was saved with its cluster index, so normalize its label.
        if "Unnamed: 0" in report.columns:
            report = report.rename(columns={"Unnamed: 0": "Cluster"})
        elif report.columns[0].lower().startswith("cluster"):
            report = report.rename(columns={report.columns[0]: "Cluster"})

        st.dataframe(report, use_container_width=True, hide_index=True)

        if {"Cluster", "Revenue"}.issubset(report.columns):
            chart = px.bar(
                report,
                x="Cluster",
                y="Revenue",
                title="Revenue contribution by customer cluster",
                text_auto=".2s",
            )
            st.plotly_chart(chart, use_container_width=True)

        if {"Cluster", "Customers"}.issubset(report.columns):
            chart = px.bar(
                report,
                x="Cluster",
                y="Customers",
                title="Customer count by cluster",
                text_auto=True,
            )
            st.plotly_chart(chart, use_container_width=True)
    else:
        show_missing_file("blinkit_customer_segment_report.csv")

    if customer_segments is not None:
        with st.expander("View customer-level cluster assignments"):
            st.dataframe(
                customer_segments,
                use_container_width=True,
                hide_index=True,
            )


with tab_models:
    st.subheader("Delivery classification")

    # Get delivery results from the existing combined ML report
    if ml_report is not None and "Model" in ml_report.columns:

        delivery_summary = ml_report[
            ml_report["Model"].astype(str).str.contains(
                "Delivery", case=False, na=False
            )
        ]

        if not delivery_summary.empty:
           

            st.dataframe(
                delivery_summary,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.warning("Delivery results were not found in the ML summary.")

        st.markdown("#### Combined ML summary")

        st.dataframe(
            ml_report,
            use_container_width=True,
            hide_index=True
        )

    else:
        show_missing_file("blinkit_ml_model_comparison.csv")

    st.caption(
        "The delivery classification experiment had weak class-wise "
        "performance. Accuracy alone can be misleading when delayed-order "
        "classes are smaller. Review Macro-F1 and dataset limitations "
        "before drawing conclusions."
    )


with tab_forecast:
    st.subheader("Demand forecasting")

    if demand_report is not None:
        st.markdown("#### Forecast model comparison")
        st.dataframe(demand_report, use_container_width=True, hide_index=True)

    if demand_predictions is not None:
        st.markdown("#### Actual vs predicted demand")
        if "Date" in demand_predictions.columns:
            demand_predictions["Date"] = pd.to_datetime(
                demand_predictions["Date"], errors="coerce"
            )
            numeric_cols = [
                col for col in demand_predictions.columns
                if col != "Date"
                and pd.api.types.is_numeric_dtype(demand_predictions[col])
            ]
            if numeric_cols:
                chart_data = demand_predictions.melt(
                    id_vars="Date",
                    value_vars=numeric_cols,
                    var_name="Series",
                    value_name="Quantity",
                )
                chart = px.line(
                    chart_data,
                    x="Date",
                    y="Quantity",
                    color="Series",
                    title="Actual and predicted daily quantity",
                )
                st.plotly_chart(chart, use_container_width=True)
        st.dataframe(
            demand_predictions,
            use_container_width=True,
            hide_index=True,
        )

    if demand_importance is not None:
        st.markdown("#### Demand forecasting feature importance")
        st.dataframe(
            demand_importance,
            use_container_width=True,
            hide_index=True,
        )

        feature_col = next(
            (c for c in demand_importance.columns if c.lower() == "feature"),
            None,
        )
        importance_col = next(
            (c for c in demand_importance.columns if c.lower() == "importance"),
            None,
        )
        if feature_col and importance_col:
            chart = px.bar(
                demand_importance.sort_values(importance_col, ascending=True),
                x=importance_col,
                y=feature_col,
                orientation="h",
                title="Features contributing to the Random Forest forecast",
            )
            st.plotly_chart(chart, use_container_width=True)
    else:
        show_missing_file("blinkit_demand_feature_importance.csv")

st.caption(
        "The forecasting experiment showed high WAPE, so present it as an "
        "evaluated baseline/experiment rather than a reliable operational forecast. "
        "Missing dates in the source were treated as zero-demand days."
    )

st.divider()
st.caption("Blinkit Analytics & ML Portfolio Project | Built with Python and Streamlit")
