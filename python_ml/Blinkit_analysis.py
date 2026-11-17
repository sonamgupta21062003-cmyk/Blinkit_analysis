from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Blinkit Analytics & ML",
    page_icon="🛒",
    layout="wide",
)

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

    if delivery_report is not None:
        st.dataframe(delivery_report, use_container_width=True, hide_index=True)

        if {"Model", "Accuracy", "Macro_F1"}.issubset(delivery_report.columns):
            plot_data = delivery_report.melt(
                id_vars="Model",
                value_vars=["Accuracy", "Macro_F1"],
                var_name="Metric",
                value_name="Score",
            )
            chart = px.bar(
                plot_data,
                x="Model",
                y="Score",
                color="Metric",
                barmode="group",
                title="Delivery model comparison",
                text_auto=".2f",
            )
            st.plotly_chart(chart, use_container_width=True)
    else:
        st.info(
            "The separate delivery comparison report is optional. "
            "The combined ML summary may be shown above instead."
        )

    st.markdown("#### Combined ML summary")
    if ml_report is not None:
        st.dataframe(ml_report, use_container_width=True, hide_index=True)

    st.caption(
        "The delivery classification experiment had weak class-wise performance. "
        "Accuracy alone can be misleading when delayed-order classes are smaller; "
        "review Macro-F1 and the dataset limitations before drawing conclusions."
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
