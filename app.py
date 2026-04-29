"""
Strategic Market Research | Injectable Regenerative Therapy for ED Market Preview

This Streamlit application embeds a protected, normalized preview of the
Global Injectable Regenerative Therapy for ED Market (2025–2035).

No Excel workbook is required.
No absolute market values are exposed.
Charts are rendered using HTML/CSS rather than Altair to avoid dependency
and schema issues on Streamlit Cloud.
"""

import streamlit as st
from html import escape


# -----------------------------------------------------------------------------
# Page Configuration
# -----------------------------------------------------------------------------

st.set_page_config(
    page_title="Global Injectable Regenerative Therapy for ED Market Preview",
    page_icon="◼",
    layout="wide",
    initial_sidebar_state="expanded",
)


# -----------------------------------------------------------------------------
# Brand Theme
# -----------------------------------------------------------------------------

BURGUNDY = "#5B0F2E"
BURGUNDY_DARK = "#3A071D"
BURGUNDY_SOFT = "#8A2E4D"
BURGUNDY_LIGHT = "#EFE4EA"
GREY_BG = "#F6F4F5"
TEXT = "#252525"
MUTED = "#6B6267"
WHITE = "#FFFFFF"
BORDER = "#E5D7DE"


# -----------------------------------------------------------------------------
# Embedded Protected Data
# -----------------------------------------------------------------------------
# Values are normalized trend indicators only. They do not represent absolute
# revenue, patient count, market size, price, adoption rate, or country values.

DATA_SUMMARY = {
    "Executive Preview": {
        "description": "A protected market-intelligence view of the injectable regenerative therapy opportunity for erectile dysfunction, focused on PDE5 inadequate responders and staged geographic expansion.",
        "strategic_lens": "The market is best understood through a treatment-funnel lens rather than a broad ED-drug-market lens. Value creation depends on identifying clinically eligible, commercially reachable, and adoption-ready patients.",
        "values": [0.20, 0.38, 0.54, 0.73, 0.88, 1.00],
        "cards": [
            ("Market Scope", "PDE5 inadequate-responder opportunity"),
            ("Priority Launch Logic", "Taiwan validation → China scale → U.S. premium evidence"),
            ("Data Exposure", "Normalized directional preview only"),
        ],
    },
    "Country Demographics": {
        "description": "Male 40+ population base and age-structure logic used to establish the underlying ED risk pool across priority and expansion markets.",
        "strategic_lens": "Demographic scale creates the outer market boundary, but does not equal commercial opportunity. Only a subset converts through diagnosis, treatment, PDE5 use, inadequate response, clinical eligibility, and reachable adoption.",
        "values": [1.00, 0.0026, 0.1909, 0.0428, 0.0180, 0.0075, 0.0117, 0.0097, 0.0098, 0.0094, 0.0070, 0.0159, 0.0859],
        "cards": [
            ("Coverage", "Priority and expansion geographies"),
            ("Use Case", "Population base for patient funnel"),
            ("Disclosure", "Relative shape only"),
        ],
    },
    "ED Epidemiology": {
        "description": "ED prevalence and severity assumptions by geography, used to convert demographic scale into a clinically relevant disease pool.",
        "strategic_lens": "The epidemiology layer separates headline male population from addressable disease burden. The strongest commercial geographies are not always the largest population markets; affordability, treatment behavior, and specialist access matter materially.",
        "values": [1.00, 0.0010, 0.0610, 0.0171, 0.0078, 0.0028, 0.0046, 0.0037, 0.0037, 0.0038, 0.0027, 0.0056, 0.0257],
        "cards": [
            ("Core Lens", "Prevalence-adjusted ED pool"),
            ("Market Relevance", "Severity and treatment propensity"),
            ("Output Type", "Protected relative index"),
        ],
    },
    "Treatment Funnel": {
        "description": "Country-level conversion from ED burden to diagnosed, treated, PDE5-using, and PDE5 inadequate-responder populations.",
        "strategic_lens": "This is the most important commercial screen. Injectable regenerative therapy should not be sized against all ED patients; it should be sized against patients who are already treatment-active and insufficiently served by PDE5 inhibitors.",
        "values": [1.00, 0.0004, 0.0133, 0.0086, 0.0033, 0.0011, 0.0001, 0.0021, 0.0018, 0.0016, 0.0016, 0.0011, 0.0020, 0.0062, 0.74, 0.54, 0.38, 0.21],
        "cards": [
            ("Funnel Start", "Diagnosed ED population"),
            ("Commercial Filter", "PDE5 inadequate responders"),
            ("Strategic Importance", "Defines realistic addressability"),
        ],
    },
    "Regenerative Eligibility": {
        "description": "Clinical and commercial filters applied to identify patients plausibly eligible for injectable regenerative therapy.",
        "strategic_lens": "Eligibility is narrower than medical need. Realistic demand depends on contraindications, comorbidity profile, disease etiology, specialist evaluation, willingness to pay, and treatment-site availability.",
        "values": [1.00, 0.0007, 0.0007, 0.0002, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0003, 0.55, 0.31, 0.19],
        "cards": [
            ("Clinical Screen", "Regenerative therapy suitability"),
            ("Commercial Screen", "Reachable patient pool"),
            ("Strategic Role", "Narrows headline demand"),
        ],
    },
    "Regulatory & Launch": {
        "description": "Country-by-country launch-pathway logic for Taiwan, China, the United States, and broader expansion markets.",
        "strategic_lens": "The launch pathway is not uniform. Taiwan can support early validation, China offers scale if evidence and channel access are strong, and the United States requires a more evidence-led commercialization route.",
        "values": [0.22, 0.34, 0.48, 0.63, 0.77, 0.91],
        "cards": [
            ("Launch Logic", "Sequenced market entry"),
            ("Evidence Need", "Higher in premium markets"),
            ("Commercial Role", "Timing and risk gating"),
        ],
    },
    "Pricing & Payment": {
        "description": "Relative pricing, payment, net-realization, and retreatment economics across priority geographies.",
        "strategic_lens": "The category is likely to behave more like a premium procedure-led therapy than a conventional chronic prescription market. Pricing power depends on evidence quality, durability, patient selection, and physician confidence.",
        "values": [0.1554, 0.2620, 1.0000, 0.5823, 0.3911, 0.7203, 0.4823, 0.4342, 0.4044, 0.3291, 0.3000, 0.5430],
        "cards": [
            ("Payment Archetype", "Procedure-led / cash-pay hybrid"),
            ("Key Variable", "Net realization"),
            ("Sensitivity", "High impact on revenue outcome"),
        ],
    },
    "Channel & Adoption": {
        "description": "Specialist-channel and post-launch adoption pathway across target markets.",
        "strategic_lens": "Adoption depends less on awareness alone and more on urologist confidence, clinical workflow fit, patient affordability, and proof that outcomes justify an injectable intervention.",
        "values": [0.05, 0.10, 0.18, 0.31, 0.46, 0.64, 0.79, 0.91, 1.00],
        "cards": [
            ("Primary Channel", "Urology / men’s health specialists"),
            ("Adoption Driver", "Evidence and workflow confidence"),
            ("Commercial Pattern", "Gradual ramp, not immediate conversion"),
        ],
    },
    "Competitive Benchmarking": {
        "description": "Competitive positioning versus PDE5 inhibitors, devices, injectables, procedures, and emerging regenerative approaches.",
        "strategic_lens": "The market will not be won by novelty alone. Competitive differentiation must be built around durability, patient selection, physician usability, safety, and economics versus existing treatment pathways.",
        "values": [0.38, 0.52, 0.61, 0.73, 0.84, 0.92],
        "cards": [
            ("Competitive Set", "Drug, device, procedure, regenerative alternatives"),
            ("Differentiator", "Durability and patient selection"),
            ("Risk", "Evidence gaps and substitute inertia"),
        ],
    },
    "Country Forecast": {
        "description": "Protected directional view of Taiwan, China, and United States revenue development through 2035.",
        "strategic_lens": "The forecast structure reflects staged commercialization: Taiwan as launch validation, China as scale expansion, and the United States as premium opportunity contingent on evidence and access readiness.",
        "values": [0.4037, 0.0001, 0.4037, 0.4724, 0.2851, 1.0000, 0.4037, 0.0004, 0.0009, 0.0067, 0.4037, 0.0002, 0.0013],
        "cards": [
            ("Priority Markets", "Taiwan, China, United States"),
            ("Forecast Horizon", "2025–2035"),
            ("Display Mode", "No absolute values disclosed"),
        ],
    },
    "Regional Global Expansion": {
        "description": "Selective expansion-market opportunity beyond the first three launch geographies.",
        "strategic_lens": "Global expansion should be selective rather than broad-based. The most attractive secondary markets combine specialist access, premium self-pay behavior, regulatory clarity, and sufficient ED treatment activity.",
        "values": [1.0000, 0.0002, 0.0001, 0.0004, 0.0039, 0.18, 0.29, 0.41, 0.57],
        "cards": [
            ("Expansion Logic", "Selective, not universal"),
            ("Market Filters", "Access, affordability, channel readiness"),
            ("Strategic Use", "Prioritization of next-wave geographies"),
        ],
    },
    "EliteCell Bio Opportunity": {
        "description": "Company-specific opportunity view covering commercial capture, geographic mix, and strategic milestones.",
        "strategic_lens": "EliteCell Bio’s opportunity depends on converting Taiwan validation into broader geographic credibility while building a differentiated evidence and channel-access position against substitutes.",
        "values": [1.0000, 0.0001, 0.0001, 0.0027, 0.0042, 0.21, 0.39, 0.58, 0.76],
        "cards": [
            ("Strategic Position", "Taiwan-first expansion pathway"),
            ("Commercial Requirement", "Evidence-led conversion"),
            ("Growth Logic", "Validation → scale → premium market entry"),
        ],
    },
    "Scenario & Sensitivity": {
        "description": "Sensitivity view across the commercial and clinical variables most likely to alter the 2035 opportunity.",
        "strategic_lens": "The most sensitive variables are not population size alone. Adoption rate, net price, treatment durability, reachable-patient conversion, and evidence strength can materially change the commercial outcome.",
        "values": [0.0000, 0.3353, 1.0000],
        "cards": [
            ("Downside Case", "Slow adoption / narrower eligibility"),
            ("Base Case", "Measured specialist uptake"),
            ("Upside Case", "Evidence-supported acceleration"),
        ],
    },
    "Dashboard Summary": {
        "description": "Boardroom-style summary of the market opportunity, staged entry logic, and value of the full study.",
        "strategic_lens": "The full study is designed to clarify where the regenerative ED opportunity is real, where it is overstated, and how EliteCell Bio can sequence commercialization without relying on headline ED-market assumptions.",
        "values": [0.17, 0.29, 0.44, 0.63, 0.82, 1.00],
        "cards": [
            ("Purpose", "Commercial strategy preview"),
            ("Core Question", "Where does regenerative ED therapy convert into revenue?"),
            ("Full Study Value", "Market size, evidence, access, competition, and strategy"),
        ],
    },
}


# -----------------------------------------------------------------------------
# CSS
# -----------------------------------------------------------------------------

st.markdown(
    f"""
    <style>
    html, body, [class*="css"] {{
        font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        color: {TEXT};
    }}

    .stApp {{
        background: linear-gradient(180deg, #fbfafb 0%, #f6f4f5 100%);
    }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {BURGUNDY_DARK} 0%, {BURGUNDY} 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }}

    section[data-testid="stSidebar"] * {{
        color: #ffffff !important;
    }}

    div[data-baseweb="select"] > div {{
        background-color: rgba(255,255,255,0.10) !important;
        border: 1px solid rgba(255,255,255,0.22) !important;
        border-radius: 12px !important;
    }}

    .hero {{
        background:
            radial-gradient(circle at top right, rgba(138,46,77,0.28), transparent 30%),
            linear-gradient(135deg, {BURGUNDY_DARK} 0%, {BURGUNDY} 58%, #7A2142 100%);
        padding: 34px 36px;
        border-radius: 28px;
        color: white;
        box-shadow: 0 18px 48px rgba(91,15,46,0.22);
        margin-bottom: 24px;
    }}

    .eyebrow {{
        font-size: 12px;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        opacity: 0.82;
        font-weight: 700;
        margin-bottom: 12px;
    }}

    .hero-title {{
        font-size: 38px;
        line-height: 1.08;
        font-weight: 850;
        max-width: 980px;
        margin-bottom: 14px;
    }}

    .hero-subtitle {{
        font-size: 17px;
        line-height: 1.55;
        max-width: 940px;
        opacity: 0.90;
    }}

    .section-card {{
        background: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 22px;
        padding: 24px 26px;
        box-shadow: 0 12px 34px rgba(40, 22, 31, 0.06);
        margin-bottom: 18px;
    }}

    .section-title {{
        font-size: 24px;
        font-weight: 820;
        color: {BURGUNDY};
        margin-bottom: 8px;
    }}

    .section-description {{
        font-size: 15px;
        line-height: 1.65;
        color: {TEXT};
        margin-bottom: 16px;
    }}

    .lens-box {{
        border-left: 5px solid {BURGUNDY};
        background: {BURGUNDY_LIGHT};
        padding: 16px 18px;
        border-radius: 16px;
        color: {TEXT};
        font-size: 15px;
        line-height: 1.6;
        margin-top: 12px;
    }}

    .cards-grid {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 16px;
        margin: 18px 0 6px 0;
    }}

    .metric-card {{
        background: linear-gradient(180deg, #ffffff 0%, #fbf8fa 100%);
        border: 1px solid {BORDER};
        border-radius: 18px;
        padding: 18px 18px;
        min-height: 112px;
    }}

    .metric-label {{
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.09em;
        color: {BURGUNDY_SOFT};
        font-weight: 800;
        margin-bottom: 10px;
    }}

    .metric-value {{
        color: {TEXT};
        font-size: 18px;
        line-height: 1.35;
        font-weight: 760;
    }}

    .chart-wrap {{
        background: #ffffff;
        border: 1px solid {BORDER};
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 12px 34px rgba(40, 22, 31, 0.06);
        margin-top: 18px;
    }}

    .chart-title {{
        color: {BURGUNDY};
        font-size: 19px;
        font-weight: 820;
        margin-bottom: 6px;
    }}

    .chart-note {{
        color: {MUTED};
        font-size: 13px;
        line-height: 1.45;
        margin-bottom: 18px;
    }}

    .bars {{
        height: 360px;
        display: flex;
        align-items: end;
        gap: 9px;
        padding: 18px 8px 4px 8px;
        border-radius: 18px;
        background:
            linear-gradient(180deg, rgba(91,15,46,0.045) 0%, rgba(91,15,46,0.015) 100%);
        overflow: hidden;
    }}

    .bar-shell {{
        flex: 1;
        min-width: 8px;
        height: 100%;
        display: flex;
        align-items: end;
        justify-content: center;
    }}

    .bar {{
        width: 100%;
        max-width: 42px;
        min-height: 8px;
        border-radius: 12px 12px 4px 4px;
        background: linear-gradient(180deg, {BURGUNDY_SOFT} 0%, {BURGUNDY} 82%);
        box-shadow: 0 10px 18px rgba(91,15,46,0.20);
        opacity: 0.94;
    }}

    .skeleton {{
        height: 360px;
        border-radius: 18px;
        background:
            repeating-linear-gradient(
                -45deg,
                rgba(91,15,46,0.06),
                rgba(91,15,46,0.06) 12px,
                rgba(91,15,46,0.025) 12px,
                rgba(91,15,46,0.025) 24px
            );
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: {BURGUNDY};
        font-weight: 800;
        padding: 24px;
    }}

    .pill-row {{
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin-top: 14px;
    }}

    .pill {{
        border: 1px solid rgba(91,15,46,0.18);
        background: #fff;
        color: {BURGUNDY};
        border-radius: 999px;
        padding: 8px 12px;
        font-size: 12px;
        font-weight: 750;
    }}

    .footer-note {{
        margin-top: 20px;
        padding: 16px 18px;
        border-radius: 18px;
        background: #ffffff;
        border: 1px solid {BORDER};
        color: {MUTED};
        font-size: 13px;
        line-height: 1.6;
    }}

    .sidebar-brand {{
        padding: 10px 4px 18px 4px;
    }}

    .sidebar-brand-title {{
        font-size: 18px;
        font-weight: 850;
        line-height: 1.25;
        color: #ffffff;
    }}

    .sidebar-brand-sub {{
        font-size: 12px;
        line-height: 1.45;
        opacity: 0.78;
        margin-top: 8px;
    }}

    .coverage-list {{
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 14px;
        margin-top: 14px;
    }}

    .coverage-item {{
        border: 1px solid {BORDER};
        background: #ffffff;
        border-radius: 16px;
        padding: 14px 15px;
        color: {TEXT};
        font-size: 14px;
        line-height: 1.45;
    }}

    .coverage-item b {{
        color: {BURGUNDY};
    }}

    @media (max-width: 900px) {{
        .cards-grid {{
            grid-template-columns: 1fr;
        }}

        .coverage-list {{
            grid-template-columns: 1fr;
        }}

        .hero-title {{
            font-size: 28px;
        }}

        .hero {{
            padding: 26px 24px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------------------------------------------------------
# Rendering Helpers
# -----------------------------------------------------------------------------

def render_sidebar() -> str:
    st.sidebar.markdown(
        """
        <div class="sidebar-brand">
            <div class="sidebar-brand-title">Strategic Market Research</div>
            <div class="sidebar-brand-sub">
                Protected commercial preview for the Global Injectable Regenerative Therapy for ED Market.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_names = list(DATA_SUMMARY.keys())
    selected = st.sidebar.selectbox(
        "Navigate Preview",
        section_names,
        index=0,
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        **Preview Controls**

        This application displays directional market patterns only.  
        Absolute values, detailed assumptions, and underlying workbook logic are intentionally protected.
        """
    )

    return selected


def render_hero() -> None:
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">Protected Market Intelligence Preview | 2025–2035</div>
            <div class="hero-title">
                Global Injectable Regenerative Therapy for ED Market
            </div>
            <div class="hero-subtitle">
                A professional preview of the PDE5 inadequate-responder opportunity, built around
                patient funnel conversion, Taiwan-to-China-to-U.S. expansion logic, specialist-channel
                adoption, pricing sensitivity, and competitive positioning.
            </div>
            <div class="pill-row">
                <div class="pill">No Excel file required</div>
                <div class="pill">No absolute values exposed</div>
                <div class="pill">Deep burgundy SMR styling</div>
                <div class="pill">Streamlit Cloud compatible</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_cards(cards: list[tuple[str, str]]) -> None:
    html = '<div class="cards-grid">'
    for label, value in cards:
        html += f"""
        <div class="metric-card">
            <div class="metric-label">{escape(label)}</div>
            <div class="metric-value">{escape(value)}</div>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def render_css_chart(values: list[float], title: str) -> None:
    safe_title = escape(title)

    if not values:
        st.markdown(
            f"""
            <div class="chart-wrap">
                <div class="chart-title">{safe_title}</div>
                <div class="chart-note">
                    This section is intentionally shown as a strategic narrative layer. No values are displayed.
                </div>
                <div class="skeleton">
                    Protected section — detailed values available in the full study.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    bars_html = ""
    for raw_value in values:
        try:
            v = float(raw_value)
        except Exception:
            v = 0.0

        v = max(0.0, min(1.0, v))
        height = max(3.0, v * 100.0)

        bars_html += f"""
        <div class="bar-shell">
            <div class="bar" style="height:{height:.2f}%"></div>
        </div>
        """

    st.markdown(
        f"""
        <div class="chart-wrap">
            <div class="chart-title">{safe_title}</div>
            <div class="chart-note">
                Directional normalized pattern only. Axes, labels, tooltips, and absolute magnitudes are intentionally removed.
            </div>
            <div class="bars">
                {bars_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section(selected: str) -> None:
    section = DATA_SUMMARY[selected]

    st.markdown(
        f"""
        <div class="section-card">
            <div class="section-title">{escape(selected)}</div>
            <div class="section-description">{escape(section["description"])}</div>
            <div class="lens-box"><b>Strategic interpretation:</b> {escape(section["strategic_lens"])}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_cards(section.get("cards", []))
    render_css_chart(section.get("values", []), f"{selected} | Protected Directional View")


def render_coverage_panel() -> None:
    st.markdown(
        f"""
        <div class="section-card">
            <div class="section-title">Full Preview Coverage</div>
            <div class="section-description">
                The application is structured to demonstrate the breadth of the underlying market study while protecting proprietary detail.
            </div>
            <div class="coverage-list">
                <div class="coverage-item"><b>Demand Foundation</b><br>Demographics, ED epidemiology, treatment funnel, and PDE5 inadequate-responder logic.</div>
                <div class="coverage-item"><b>Commercial Reach</b><br>Eligibility, channel access, adoption readiness, and specialist conversion pathway.</div>
                <div class="coverage-item"><b>Market Economics</b><br>Pricing, net realization, retreatment behavior, and sensitivity to adoption variables.</div>
                <div class="coverage-item"><b>Expansion Strategy</b><br>Taiwan validation, China scale-up, U.S. premium pathway, and selective global expansion.</div>
                <div class="coverage-item"><b>Competitive Positioning</b><br>Comparison versus existing ED therapies, procedures, devices, and regenerative alternatives.</div>
                <div class="coverage-item"><b>Strategic Outcome</b><br>Directional revenue opportunity, market-share potential, and evidence-led commercialization priorities.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    st.markdown(
        """
        <div class="footer-note">
            This preview is designed for controlled external demonstration. It intentionally uses normalized directional visuals,
            narrative descriptions, and protected section-level summaries. The full study contains the detailed market sizing,
            source-backed assumptions, country forecasts, segmentation outputs, and strategic recommendations.
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------------------------------------------------------
# Main App
# -----------------------------------------------------------------------------

def main() -> None:
    selected = render_sidebar()

    render_hero()

    left, right = st.columns([1.55, 0.85], gap="large")

    with left:
        render_section(selected)

    with right:
        render_coverage_panel()

    render_footer()


if __name__ == "__main__":
    main()
