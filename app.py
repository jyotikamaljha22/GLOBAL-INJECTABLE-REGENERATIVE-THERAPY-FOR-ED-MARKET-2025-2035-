"""
Streamlit application for the global injectable regenerative therapy market model.

This version embeds all of the necessary data directly in the code. The raw Excel
workbook is not distributed with the app to protect proprietary information. Instead,
each sheet is summarised into a normalised series of values along with a short
description. These values capture the relative shape of the data without revealing
absolute figures. Users can navigate through the different sections using the
sidebar and view anonymised charts coloured in a deep burgundy theme.
"""

import json
import streamlit as st
import altair as alt

# -----------------------------------------------------------------------------
# Embedded summary data
#
# The DATA_SUMMARY dictionary contains one entry per sheet from the original
# workbook. For each sheet the 'description' field holds a brief textual
# overview, and 'values' holds a list of normalised numbers between 0 and 1.
# These normalised numbers represent the relative magnitude of each row's
# aggregate without exposing underlying confidential values. Because this data
# resides directly in the code, the original Excel file does not need to be
# distributed or published.
DATA_SUMMARY = json.loads(
    """
{"Read Me & Model Guide": {"description": "Formula-driven model for the PDE5 inadequate-responder opportunity across Taiwan, China, United States and staged global expansion markets.", "values": []}, "Control Panel": {"description": "Scenario controls and central commercial assumptions for injectable regenerative therapy for erectile dysfunction.", "values": []}, "Source Register": {"description": "Audit trail for source-backed assumptions used in the market model.", "values": []}, "Country Demographics": {"description": "Male 40+ population base and age structure used to seed the ED patient funnel.", "values": [1.0, 0.0026, 0.1909, 0.0428, 0.018, 0.0075, 0.0, 0.0117, 0.0097, 0.0098, 0.0094, 0.007, 0.0159, 0.0859]}, "ED Epidemiology": {"description": "ED prevalence, severity and etiology assumptions by country.", "values": [1.0, 0.001, 0.061, 0.0171, 0.0078, 0.0028, 0.0, 0.0046, 0.0037, 0.0037, 0.0038, 0.0027, 0.0056, 0.0257]}, "Treatment Funnel": {"description": "Country-level conversion from ED burden to PDE5 inadequate responders.", "values": [1.0, 0.0004, 0.0133, 0.0086, 0.0033, 0.0011, 0.0001, 0.0021, 0.0018, 0.0016, 0.0016, 0.0011, 0.002, 0.0062, 1.0, 0.0003, 0.0077, 0.0064, 0.0023, 0.0007, 0.0001, 0.0015, 0.0012, 0.0011, 0.0011, 0.0007, 0.0012, 0.0034, 1.0, 0.0002, 0.0061, 0.0054, 0.0019, 0.0006, 0.0, 0.0012, 0.001, 0.0009, 0.0009, 0.0006, 0.001, 0.0027, 1.0, 0.0001, 0.002, 0.0017, 0.0006, 0.0002, 0.0, 0.0004, 0.0003, 0.0003, 0.0003, 0.0002, 0.0003, 0.0009]}, "Regenerative Eligibility": {"description": "Clinically eligible and commercially reachable patient pools for regenerative injection.", "values": [1.0, 0.0, 0.0007, 0.0007, 0.0002, 0.0001, 0.0, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0003, 1.0, 0.0, 0.0001, 0.0002, 0.0001, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, "Regulatory & Launch": {"description": "Launch timing assumptions and regulatory pathway logic by country.", "values": []}, "Pricing & Payment": {"description": "Gross price, net realization, treatment-cycle economics and retreatment logic.", "values": [0.1554, 0.262, 0.0, 1.0, 0.5823, 0.3911, 0.7203, 0.4823, 0.4342, 0.4044, 0.3291, 0.3, 0.543, 0.0]}, "Channel & Adoption": {"description": "Post-launch adoption rate applied to the commercially reachable pool.", "values": [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, "Competitive Benchmarking": {"description": "Alternative therapies, substitute competition and EliteCell Bio positioning.", "values": []}, "Country Forecast": {"description": "Revenue forecast for Taiwan, China and United States, with formulas linked to patient funnel, adoption and pricing.", "values": [0.4037, 0.0, 0.0, 0.0001, 0.4037, 0.0, 0.0, 0.0, 0.4037, 0.0, 0.0, 0.0, 0.4037, 0.4724, 0.2851, 1.0, 0.4037, 0.0004, 0.0009, 0.0067, 0.4037, 0.0002, 0.0002, 0.0013]}, "Regional Global Expansion": {"description": "Selective expansion-market opportunity beyond Taiwan, China and the United States.", "values": [1.0, 0.0002, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0001, 0.0, 1.0, 0.0004, 0.0039]}, "EliteCell Bio Opportunity": {"description": "Company-specific revenue, country mix, segment logic and strategic milestones.", "values": [1.0, 0.0001, 0.0001, 0.0027, 0.0, 0.0042]}, "Scenario & Sensitivity": {"description": "Revenue sensitivity to the key commercial and clinical variables.", "values": [0.0, 0.3353, 1.0]}, "Dashboard Summary": {"description": "Executive summary of corrected non-zero market forecast outputs.", "values": []}}
    """
)


def create_chart(values: list[float]) -> alt.Chart:
    """Generate an Altair bar chart from a list of normalised values.

    Bars use a deep burgundy colour palette. Axis labels and tick marks are
    intentionally hidden to avoid exposing underlying scales. When the list
    contains no data, a placeholder chart is returned.

    Args:
        values: A list of floats between 0 and 1 representing normalised data.

    Returns:
        An Altair chart object.
    """
    # If no values exist for this sheet, return a single empty bar
    if not values:
        dummy = [{'index': 0, 'value': 0.0}]
        chart = alt.Chart(dummy).mark_bar(color='#581845').encode(
            x=alt.X('index:O', axis=alt.Axis(title='', labels=False, ticks=False)),
            y=alt.Y('value:Q', axis=alt.Axis(title='', labels=False, ticks=False))
        ).properties(width=700, height=450)
        return chart

    # Build a DataFrame-like structure for Altair (Altair accepts list of dicts)
    data = [{'index': str(i + 1), 'value': v} for i, v in enumerate(values)]

    chart = alt.Chart(data).mark_bar(color='#581845').encode(
        x=alt.X('index:O', axis=alt.Axis(title='', labels=False, ticks=False)),
        y=alt.Y('value:Q', axis=alt.Axis(title='', labels=False, ticks=False)),
        tooltip=[]  # disable tooltips to prevent value disclosure
    ).properties(width=700, height=450)
    return chart


def main() -> None:
    """Render the Streamlit app."""
    st.set_page_config(
        page_title="Global Injectable Regenerative Therapy Market Model",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Apply basic styling to incorporate the deep burgundy palette
    st.markdown(
        """
        <style>
        :root {
            --primary-color: #581845;
            --background-color: #ffffff;
            --text-color: #333333;
        }
        .sidebar .sidebar-content {
            background-color: #f7f2f5;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Global Injectable Regenerative Therapy for ED Market Model (2025–2035)")
    st.markdown(
        """
        Explore an anonymised view of the injectable regenerative therapy market model. Each section of the
        original workbook has been distilled into a set of normalised values that describe the relative
        shape of the data without exposing proprietary numbers. Use the sidebar to navigate through the
        different sheets and inspect their high‑level trends.
        """
    )

    # Sidebar navigation
    sheet_names = list(DATA_SUMMARY.keys())
    selected_sheet = st.sidebar.selectbox("Select Section", sheet_names, index=0)

    # Retrieve the summary for the selected sheet
    summary = DATA_SUMMARY.get(selected_sheet, {})
    description = summary.get('description')
    values = summary.get('values', [])

    # Display sheet title
    st.header(selected_sheet)

    # Show the description if available
    if description:
        st.info(description)

    # Render the chart and display it
    chart = create_chart(values)
    st.altair_chart(chart, use_container_width=True)

    # Explain that the values are normalised
    st.caption(
        "Charts display normalised trends only. Absolute magnitudes and detailed data are intentionally omitted to protect proprietary market information."
    )


if __name__ == "__main__":
    main()