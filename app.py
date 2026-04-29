import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Global Injectable Regenerative Therapy for ED Market | EliteCell Bio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------------------------------------------------------
# Lightweight Login Gate
# -----------------------------------------------------------------------------
# Keep this password aligned with your earlier dashboard code. If that password
# was different, update only this line before deployment.
APP_PASSWORD = "SMR@2026"


def render_login() -> None:
    """Render a polished login page before the dashboard is loaded."""
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top right, rgba(91,15,46,0.18), transparent 28%),
                linear-gradient(135deg, #3A071D 0%, #5B0F2E 48%, #8A2E4D 100%);
        }
        [data-testid="stHeader"] { background: transparent; }
        [data-testid="stToolbar"] { display: none; }
        .login-shell {
            min-height: 78vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 32px 16px;
        }
        .login-card {
            width: min(760px, 100%);
            background: rgba(255,255,255,0.96);
            border: 1px solid rgba(255,255,255,0.35);
            border-radius: 30px;
            box-shadow: 0 28px 80px rgba(20, 5, 13, 0.32);
            overflow: hidden;
        }
        .login-hero {
            background:
                radial-gradient(circle at top right, rgba(255,255,255,0.20), transparent 35%),
                linear-gradient(135deg, #340719 0%, #5B0F2E 65%, #8A2E4D 100%);
            color: #fff;
            padding: 34px 38px;
        }
        .login-eyebrow {
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.16em;
            color: rgba(255,255,255,0.74);
            font-weight: 800;
            margin-bottom: 12px;
        }
        .login-title {
            font-size: 32px;
            line-height: 1.12;
            font-weight: 900;
            margin: 0 0 12px 0;
        }
        .login-subtitle {
            font-size: 15px;
            line-height: 1.58;
            color: rgba(255,255,255,0.86);
            max-width: 620px;
        }
        .login-body {
            padding: 30px 38px 34px 38px;
        }
        .login-footer {
            margin-top: 18px;
            color: #64748B;
            font-size: 12px;
            line-height: 1.55;
        }
        div[data-testid="stForm"] { border: 0; padding: 0; }
        .stTextInput label {
            color: #5B0F2E !important;
            font-weight: 800 !important;
        }
        .stButton > button {
            width: 100%;
            background: linear-gradient(135deg, #3A071D 0%, #5B0F2E 100%);
            color: #fff;
            border: 0;
            border-radius: 14px;
            padding: 0.75rem 1rem;
            font-weight: 850;
            letter-spacing: 0.02em;
        }
        .stButton > button:hover {
            color: #fff;
            border: 0;
            box-shadow: 0 12px 28px rgba(91,15,46,0.25);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="login-shell">
            <div class="login-card">
                <div class="login-hero">
                    <div class="login-eyebrow">Strategic Market Research | Controlled Dashboard Access</div>
                    <div class="login-title">Global Injectable Regenerative Therapy for ED Market</div>
                    <div class="login-subtitle">
                        Secure preview cockpit for EliteCell Bio covering market size, patient funnel, pricing economics,
                        adoption pathways, regulatory roadmap, competitive positioning, and 2025–2035 revenue outlook.
                    </div>
                </div>
                <div class="login-body">
        """,
        unsafe_allow_html=True,
    )

    with st.form("dashboard_login", clear_on_submit=False):
        name = st.text_input("Name", placeholder="Enter your name")
        password = st.text_input("Password", type="password", placeholder="Enter password")
        submitted = st.form_submit_button("Access Dashboard")

    st.markdown(
        """
                    <div class="login-footer">
                        Access is intended for controlled client preview only. Data shown in the dashboard is drawn from the
                        prepared market model and summarized for executive review.
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if submitted:
        if name.strip() and password == APP_PASSWORD:
            st.session_state["dashboard_authenticated"] = True
            st.session_state["dashboard_user_name"] = name.strip()
            st.rerun()
        else:
            st.error("Invalid name or password. Please try again.")


if not st.session_state.get("dashboard_authenticated", False):
    render_login()
    st.stop()

with st.sidebar:
    st.markdown("### EliteCell Bio Dashboard")
    st.caption(f"Logged in as {st.session_state.get('dashboard_user_name', 'User')}")
    if st.button("Log out"):
        st.session_state["dashboard_authenticated"] = False
        st.rerun()

DASHBOARD_HTML = r'''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Global Injectable Regenerative Therapy for ED Market (2025–2035)</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
:root{
  --burgundy-dark:#340719;--burgundy:#5B0F2E;--burgundy-soft:#8A2E4D;--burgundy-mid:#A94D6A;
  --rose:#D9A8BC;--rose-dark:#B56B87;--rose-soft:#F8EEF3;--rose-light:#F3E7ED;
  --ink:#1E293B;--muted:#64748B;--line:#E2E8F0;--page:#F8FAFC;--white:#FFFFFF;
  --green:#1F7A53;--amber:#A16207;--red:#A8324A;--bluegrey:#475569;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--page);color:var(--ink);overflow:hidden}
body{height:100vh;display:flex;flex-direction:row}
.sidebar{width:300px;min-width:300px;height:100vh;background:linear-gradient(180deg,var(--burgundy-dark) 0%,var(--burgundy) 100%);color:white;display:flex;flex-direction:column;box-shadow:14px 0 34px rgba(58,7,29,.25);z-index:20}
.brand{padding:26px 24px 22px;border-bottom:1px solid rgba(255,255,255,.13)}
.brand h1{font-size:21px;line-height:1.14;margin:0;font-weight:880}.brand p{margin:10px 0 0;font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:rgba(255,255,255,.72);font-weight:780}
.nav{padding:12px 0;overflow-y:auto}.nav button{width:100%;text-align:left;border:0;background:transparent;color:rgba(255,255,255,.76);padding:11.5px 22px;font-size:13.25px;cursor:pointer;border-left:5px solid transparent;transition:.2s ease}.nav button:hover{background:rgba(255,255,255,.08);color:white}.nav button.nav-active{background:rgba(255,255,255,.145);color:white;border-left-color:#F6D6E5;font-weight:780}
.sidebar-footer{margin-top:auto;padding:17px 22px 23px;border-top:1px solid rgba(255,255,255,.12);font-size:12px;line-height:1.45;color:rgba(255,255,255,.70)}
.dashboard-footer{position:fixed;left:300px;right:0;bottom:0;z-index:60;background:rgba(255,255,255,.94);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-top:1px solid var(--line);box-shadow:0 -12px 30px rgba(15,23,42,.06);padding:10px 30px;display:flex;gap:16px;align-items:center;justify-content:space-between;color:var(--muted);font-size:12px;line-height:1.35}.dashboard-footer strong{color:var(--burgundy);font-weight:850}.dashboard-footer .right{white-space:nowrap;color:var(--burgundy-soft);font-weight:800}.dashboard-footer .dot{width:7px;height:7px;background:var(--burgundy);border-radius:999px;display:inline-block;margin-right:7px}
main{flex:1;height:100vh;overflow-y:auto;background:radial-gradient(circle at top right,rgba(91,15,46,.10),transparent 28%),linear-gradient(180deg,#fff 0%,#F8FAFC 44%,#F3F5F8 100%)}
.page{max-width:1240px;margin:0 auto;padding:34px 36px 95px}.content-section{display:none;animation:fadeIn .25s ease-in-out}.content-section.active{display:block}@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.hero{background:radial-gradient(circle at top right,rgba(255,255,255,.18),transparent 30%),linear-gradient(135deg,var(--burgundy-dark) 0%,var(--burgundy) 62%,var(--burgundy-soft) 100%);color:white;padding:34px 36px;border-radius:26px;box-shadow:0 18px 48px rgba(91,15,46,.22);margin-bottom:28px}.eyebrow{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.78);font-weight:820;margin-bottom:12px}.hero h2{margin:0;font-size:38px;line-height:1.08;font-weight:900;max-width:1020px}.hero p{max-width:1020px;margin:16px 0 0;color:rgba(255,255,255,.88);font-size:17px;line-height:1.58}.hero .pills{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}.pill{border:1px solid rgba(255,255,255,.28);background:rgba(255,255,255,.10);border-radius:999px;padding:8px 12px;color:#fff;font-size:12px;font-weight:750}
.header{margin-bottom:24px}.header h2{margin:0 0 8px;color:var(--burgundy);font-size:32px;line-height:1.15;font-weight:880}.header p{margin:0;color:var(--muted);font-size:17px;line-height:1.55;max-width:1040px}
.card{background:white;border:1px solid var(--line);border-radius:20px;box-shadow:0 12px 34px rgba(15,23,42,.06);padding:24px;margin-bottom:24px}.card.compact{padding:20px}.card p{color:#334155;line-height:1.72;margin:0;font-size:15px}.section-note{background:var(--rose-soft);border-left:5px solid var(--burgundy);border-radius:16px;padding:16px 18px;color:#334155;line-height:1.6;font-size:14.5px;margin-bottom:24px}
.kpi-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-bottom:24px}.kpi-grid.four{grid-template-columns:repeat(4,minmax(0,1fr))}.kpi-grid.two{grid-template-columns:repeat(2,minmax(0,1fr))}.kpi{background:white;border:1px solid var(--line);border-radius:20px;padding:23px;box-shadow:0 12px 34px rgba(15,23,42,.06);min-height:140px}.kpi.primary{background:linear-gradient(135deg,var(--burgundy-dark) 0%,var(--burgundy) 100%);color:white;border:0}.kpi.secondary{background:linear-gradient(135deg,#fff 0%,var(--rose-soft) 100%);border-color:#EBD1DC}.kpi-label{font-size:11.5px;text-transform:uppercase;letter-spacing:.10em;color:var(--burgundy-soft);font-weight:840;margin-bottom:8px}.kpi.primary .kpi-label{color:rgba(255,255,255,.68)}.kpi-value{font-size:34px;line-height:1.05;font-weight:900;color:var(--burgundy);margin-bottom:10px}.kpi.primary .kpi-value{color:white}.kpi-note{color:#64748B;font-size:13px;line-height:1.45}.kpi.primary .kpi-note{color:rgba(255,255,255,.78)}
.list-title{font-size:20px;font-weight:850;color:var(--burgundy);margin:0 0 16px}.imperatives{list-style:none;margin:0;padding:0}.imperatives li{display:flex;gap:12px;margin-bottom:16px;color:#334155;line-height:1.58;font-size:14.5px}.imperatives li:last-child{margin-bottom:0}.arrow{color:var(--burgundy);font-weight:900;margin-top:1px}.two-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}.three-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}.four-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}
.chart-container{position:relative;width:100%;height:420px;max-height:520px}.chart-container.small{height:350px}.chart-container.tall{height:500px}.note{text-align:center;color:var(--muted);font-size:12px;margin-top:12px}.table-wrap{overflow-x:auto}table{width:100%;border-collapse:collapse;font-size:14px}thead tr{background:var(--rose-light);color:var(--burgundy);border-bottom:1px solid var(--line)}th,td{padding:14px 13px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}th{font-weight:860}tbody tr:hover{background:#FBF7F9}td:first-child{font-weight:800;color:var(--burgundy)}
.funnel-panel{background:linear-gradient(135deg,var(--burgundy-dark),var(--burgundy));padding:28px;border-radius:22px;box-shadow:0 18px 46px rgba(91,15,46,.22);margin-bottom:24px}.funnel-panel h3{color:white;margin:0 0 22px;padding-bottom:13px;border-bottom:1px solid rgba(255,255,255,.18);font-size:20px}.funnel-steps{display:flex;flex-direction:column;gap:12px}.funnel-step{color:white;border-radius:14px;padding:16px 18px;display:flex;justify-content:space-between;align-items:center;border-left:5px solid rgba(255,255,255,.45);transition:.25s ease;box-shadow:0 12px 24px rgba(0,0,0,.10)}.funnel-step:hover{transform:translateX(8px)}.funnel-step h4{margin:0 0 4px;font-size:15px;font-weight:850}.funnel-step p{margin:0;font-size:12px;color:rgba(255,255,255,.78)}.funnel-value{font-size:19px;font-weight:880;white-space:nowrap;padding-left:18px}.funnel-1{width:100%;background:rgba(255,255,255,.17)}.funnel-2{width:91%;margin-left:auto;background:rgba(255,255,255,.22)}.funnel-3{width:76%;margin-left:auto;background:rgba(255,255,255,.28)}.funnel-4{width:59%;margin-left:auto;background:var(--burgundy-soft)}.funnel-5{width:43%;margin-left:auto;background:#A43A5D}
.geo-card,.scenario-card,.endpoint-card,.step-card{background:white;border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:0 12px 34px rgba(15,23,42,.06);display:flex;flex-direction:column}.geo-head{padding:18px 20px;background:var(--rose-light);border-bottom:1px solid var(--line)}.geo-head.premium{background:linear-gradient(135deg,var(--burgundy-dark),var(--burgundy));color:white}.geo-head h3{margin:0;font-size:21px;font-weight:870}.geo-head p{margin:6px 0 0;color:var(--burgundy);font-size:12px;text-transform:uppercase;letter-spacing:.10em;font-weight:850}.geo-head.premium p{color:rgba(255,255,255,.78)}.geo-body{padding:22px}.geo-block{margin-bottom:18px}.geo-block:last-child{margin-bottom:0}.geo-label{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.10em;font-weight:840;margin-bottom:5px}.geo-value{font-size:20px;color:var(--burgundy);font-weight:880}.geo-text{font-size:14px;line-height:1.6;color:#475569}
.timeline{position:relative;padding-left:18px}.timeline:before{content:"";position:absolute;top:8px;bottom:8px;left:8px;width:3px;background:linear-gradient(180deg,var(--burgundy),var(--rose));border-radius:999px}.timeline-item{position:relative;padding:0 0 18px 28px}.timeline-dot{position:absolute;left:-17px;top:4px;width:16px;height:16px;background:var(--burgundy);border:3px solid white;box-shadow:0 0 0 3px var(--rose);border-radius:50%}.timeline-card{background:white;border:1px solid var(--line);border-radius:16px;padding:16px 18px;box-shadow:0 10px 26px rgba(15,23,42,.05)}.timeline-date{color:var(--burgundy-soft);font-size:12px;text-transform:uppercase;letter-spacing:.09em;font-weight:850;margin-bottom:5px}.timeline-title{color:var(--burgundy);font-size:17px;font-weight:850;margin-bottom:5px}.timeline-text{color:#475569;font-size:14px;line-height:1.55}.scenario-card{padding:22px}.scenario-title{font-size:19px;color:var(--burgundy);font-weight:870;margin-bottom:8px}.scenario-value{font-size:34px;color:var(--burgundy);font-weight:900;margin-bottom:8px}.scenario-text{color:#475569;line-height:1.55;font-size:14px}.endpoint-card,.step-card{padding:20px}.endpoint-title,.step-title{color:var(--burgundy);font-weight:870;font-size:17px;margin-bottom:9px}.endpoint-text,.step-text{color:#475569;font-size:14px;line-height:1.58}.step-number{width:34px;height:34px;border-radius:50%;background:var(--burgundy);color:white;display:flex;align-items:center;justify-content:center;font-weight:900;margin-bottom:12px}.heat{display:inline-block;border-radius:999px;padding:5px 9px;font-size:12px;font-weight:800}.heat-high{background:#F3E7ED;color:var(--burgundy)}.heat-med{background:#F8EEF3;color:var(--burgundy-soft)}.heat-low{background:#F7F7F8;color:#64748B}.footer-note{margin-top:24px;padding:18px 20px;background:white;border:1px solid var(--line);border-radius:18px;color:var(--muted);font-size:13px;line-height:1.6}
@media(max-width:980px){body{flex-direction:column;overflow:auto;height:auto}.sidebar{width:100%;min-width:100%;height:auto}.brand{padding:20px 20px 16px}.nav{display:flex;overflow-x:auto;padding:8px}.nav button{white-space:nowrap;border-left:0;border-bottom:4px solid transparent;padding:12px 14px;font-size:13px}.nav button.nav-active{border-left:0;border-bottom-color:#F6D6E5}.sidebar-footer{display:none}.dashboard-footer{left:0;position:fixed;padding:9px 14px;font-size:11px;align-items:flex-start}.dashboard-footer .right{display:none}main{height:auto;overflow:visible}.page{padding:22px 18px 60px}.hero h2{font-size:28px}.hero{padding:26px 24px}.kpi-grid,.kpi-grid.four,.kpi-grid.two,.three-grid,.two-grid,.four-grid{grid-template-columns:1fr}.funnel-step{width:100%!important;margin-left:0!important}.chart-container{height:340px}}
</style>
</head>
<body>
<aside class="sidebar">
  <div class="brand"><h1>EliteCell Bio<br>Market Cockpit</h1><p>Strategic Market Report</p></div>
  <nav class="nav">
    <button onclick="navigate('executive')" id="nav-executive" class="nav-active">Executive Outlook</button>
    <button onclick="navigate('snapshot')" id="nav-snapshot">Market Size & Capture</button>
    <button onclick="navigate('demand')" id="nav-demand">Demand Foundation</button>
    <button onclick="navigate('funnel')" id="nav-funnel">Patient Funnel</button>
    <button onclick="navigate('country')" id="nav-country">Country Funnel Deep Dive</button>
    <button onclick="navigate('eligibility')" id="nav-eligibility">Eligibility & Reachable Pool</button>
    <button onclick="navigate('geography')" id="nav-geography">Geographic Strategy</button>
    <button onclick="navigate('pricing')" id="nav-pricing">Pricing & Net Realization</button>
    <button onclick="navigate('adoption')" id="nav-adoption">Adoption & Channel Strategy</button>
    <button onclick="navigate('forecast')" id="nav-forecast">Revenue Forecast</button>
    <button onclick="navigate('clinical')" id="nav-clinical">Clinical Endpoint Strategy</button>
    <button onclick="navigate('competition')" id="nav-competition">Competitive Landscape</button>
    <button onclick="navigate('roadmap')" id="nav-roadmap">Roadmap, Scenario & Risk</button>
  </nav>
  <div class="sidebar-footer">Controlled boardroom cockpit. Full study contains complete formulas, source register, country outputs, and strategic recommendations.</div>
</aside>
<main><div class="page">

<section id="executive" class="content-section active">
  <div class="hero"><div class="eyebrow">Global Injectable Regenerative Therapy for ED Market | 2025–2035</div><h2>Executive Outlook: The Next Opportunity in Erectile Dysfunction</h2><p>The injectable regenerative therapy opportunity is defined by targeting PDE5 inadequate responders, validating commercially in Taiwan, scaling selectively in China, and capturing premium value in the United States.</p><div class="pills"><span class="pill">PDE5 non-responder focus</span><span class="pill">Taiwan → China → U.S. rollout</span><span class="pill">Procedure-led premium economics</span></div></div>
  <div class="card"><p>EliteCell Bio should not compete with commoditized generic PDE5 inhibitors. The more defensible opportunity sits downstream, where moderate-to-severe organic ED patients remain underserved after oral therapy. Injectable regenerative medicine can occupy a 2.5-line position between symptomatic drug failure and irreversible surgical implants, provided adoption is anchored in specialist channels, evidence quality, and regulatory credibility.</p></div>
  <div class="kpi-grid"><div class="kpi primary"><div class="kpi-label">EliteCell 2035 Revenue</div><div class="kpi-value">$25.75 Mn</div><div class="kpi-note">Base-case realized revenue across priority and expansion markets.</div></div><div class="kpi"><div class="kpi-label">Target Patient Segment</div><div class="kpi-value">30–35%</div><div class="kpi-note">Estimated share of treated ED patients who are PDE5 inadequate responders.</div></div><div class="kpi"><div class="kpi-label">U.S. Revenue Mix</div><div class="kpi-value">71.1%</div><div class="kpi-note">U.S. premium pricing and commercial reach dominate the 2035 value case.</div></div></div>
  <div class="card"><h3 class="list-title">Strategic Imperatives</h3><ul class="imperatives"><li><span class="arrow">►</span><span><strong>Target the PDE5 failure pool:</strong> focus on organic moderate-to-severe ED, especially diabetic, vasculogenic, and post-prostatectomy segments.</span></li><li><span class="arrow">►</span><span><strong>Use Taiwan as validation, not only revenue:</strong> first-market evidence and workflow credibility enable later scale-up.</span></li><li><span class="arrow">►</span><span><strong>Build an evidence moat:</strong> separate EliteCell Bio from PRP/stem-cell clinic noise through endpoints, registry data, CMC quality, and regulated positioning.</span></li></ul></div>
</section>

<section id="snapshot" class="content-section">
  <div class="header"><h2>Market Size & Capture Snapshot</h2><p>The broader regenerative ED category grows rapidly by 2035, while EliteCell Bio captures a focused specialist-channel share.</p></div>
  <div class="kpi-grid four"><div class="kpi primary"><div class="kpi-label">Total Market 2035</div><div class="kpi-value">$137.65 Mn</div><div class="kpi-note">Total modeled regenerative ED therapy revenue before EliteCell capture.</div></div><div class="kpi secondary"><div class="kpi-label">EliteCell Revenue 2035</div><div class="kpi-value">$25.75 Mn</div><div class="kpi-note">Base-case company opportunity after adoption and capture filters.</div></div><div class="kpi"><div class="kpi-label">Capture Share</div><div class="kpi-value">18.7%</div><div class="kpi-note">Weighted average capture across markets.</div></div><div class="kpi"><div class="kpi-label">Expansion Revenue</div><div class="kpi-value">$3.14 Mn</div><div class="kpi-note">Selective next-wave optionality after core-market proof.</div></div></div>
  <div class="two-grid"><div class="card"><h3 class="list-title">2035 EliteCell Revenue Mix</h3><div class="chart-container small"><canvas id="mixChart"></canvas></div><div class="note">Revenue mix by geography.</div></div><div class="card"><h3 class="list-title">Total Market vs EliteCell Capture</h3><div class="chart-container small"><canvas id="marketCaptureChart"></canvas></div><div class="note">Total category revenue compared with EliteCell realized revenue.</div></div></div>
  <div class="card"><h3 class="list-title">2035 Market Snapshot</h3><div class="table-wrap"><table><thead><tr><th>Metric</th><th>Value</th><th>Interpretation</th></tr></thead><tbody><tr><td>Total Regenerative ED Market</td><td>$137.65 Mn</td><td>Broader category opportunity across all regenerative ED participants.</td></tr><tr><td>EliteCell Bio Revenue</td><td>$25.75 Mn</td><td>Company-specific capture after launch, adoption, price, and share filters.</td></tr><tr><td>U.S. Contribution</td><td>71.1%</td><td>Premium market with strongest valuation impact.</td></tr><tr><td>China Contribution</td><td>9.4%</td><td>Scale market, but heavily filtered by diagnosis, reach, and partner execution.</td></tr></tbody></table></div></div>
</section>

<section id="demand" class="content-section">
  <div class="header"><h2>Demand Foundation: Male 40+ Population and ED Burden</h2><p>The demographic base shows why the category exists, but also why the model must apply commercial filters before sizing revenue.</p></div>
  <div class="kpi-grid four"><div class="kpi primary"><div class="kpi-label">China ED Burden 2035</div><div class="kpi-value">125.8 Mn</div><div class="kpi-note">Largest disease burden in the priority set.</div></div><div class="kpi"><div class="kpi-label">U.S. ED Burden 2035</div><div class="kpi-value">36.0 Mn</div><div class="kpi-note">High diagnosis and treatment conversion.</div></div><div class="kpi"><div class="kpi-label">Taiwan ED Burden 2035</div><div class="kpi-value">2.66 Mn</div><div class="kpi-note">Compact validation market with aging population.</div></div><div class="kpi"><div class="kpi-label">Global ED Patients 2025</div><div class="kpi-value">322 Mn</div><div class="kpi-note">Broad global context, not directly addressable revenue.</div></div></div>
  <div class="two-grid"><div class="card"><h3 class="list-title">2035 ED Burden by Market</h3><div class="chart-container"><canvas id="demandChart"></canvas></div><div class="note">Patients in Mn; shows disease burden before commercial filtering.</div></div><div class="card"><h3 class="list-title">Male 40+ Population Base</h3><div class="chart-container"><canvas id="male40Chart"></canvas></div><div class="note">Male 40+ population in Mn, 2025 vs 2035.</div></div></div>
  <div class="section-note"><strong>Strategic implication:</strong> China has the largest epidemiology pool, but the U.S. has the stronger diagnosis, treatment, affordability, and premium-channel conversion. Taiwan is important because it can prove the model before larger-market expansion.</div>
</section>

<section id="funnel" class="content-section">
  <div class="header"><h2>Patient Funnel: Defining the Reachable Market</h2><p>Why headline ED prevalence materially overstates the realistic commercial opportunity.</p></div>
  <div class="card"><p>The market must be sized through a disciplined patient funnel. Total male 40+ population is reduced by ED prevalence, diagnosis, treatment-seeking, PDE5 usage, inadequate response, clinical eligibility, and commercial reach.</p></div>
  <div class="funnel-panel"><h3>Global Aggregate Funnel Logic | Illustrative 2035 Proportions</h3><div class="funnel-steps"><div class="funnel-step funnel-1"><div><h4>1. Male Population Age 40+</h4><p>Base demographic pool across target regions.</p></div><div class="funnel-value">100%</div></div><div class="funnel-step funnel-2"><div><h4>2. Total ED Prevalence</h4><p>Men with any degree of ED.</p></div><div class="funnel-value">~40%</div></div><div class="funnel-step funnel-3"><div><h4>3. Diagnosed & Treated ED</h4><p>Men actively seeking intervention.</p></div><div class="funnel-value">~15%</div></div><div class="funnel-step funnel-4"><div><h4>4. PDE5 Inadequate Responders</h4><p>The core target after oral therapy failure.</p></div><div class="funnel-value">~4%</div></div><div class="funnel-step funnel-5"><div><h4>5. Commercially Reachable</h4><p>Clinically eligible patients with access and payment capacity.</p></div><div class="funnel-value">&lt;1%</div></div></div></div>
  <div class="two-grid"><div class="card"><h3 class="list-title">Priority Clinical Segments</h3><table><tbody><tr><td>Diabetic ED</td><td>Endothelial and vascular damage</td></tr><tr><td>Vasculogenic ED</td><td>Blood-flow restoration rationale</td></tr><tr><td>Post-prostatectomy ED</td><td>Nerve and tissue rehabilitation pathway</td></tr></tbody></table></div><div class="card"><h3 class="list-title">Funnel Conversion Risk</h3><p>Without specialist urology channels and proven durability, drop-off between PDE5 non-response and actual treatment remains high. Evidence, physician confidence, and payment willingness determine conversion.</p></div></div>
</section>

<section id="country" class="content-section">
  <div class="header"><h2>Country Funnel Deep Dive</h2><p>China has the largest pool; the United States converts more effectively into premium revenue.</p></div>
  <div class="card"><h3 class="list-title">2035 Patient Funnel by Country | Mn Patients</h3><div class="chart-container"><canvas id="countryFunnelChart"></canvas></div><div class="note">Values shown in Mn patients.</div></div>
  <div class="card"><div class="table-wrap"><table><thead><tr><th>Funnel Metric | 2035</th><th>Taiwan</th><th>China</th><th>United States</th><th>Strategic Meaning</th></tr></thead><tbody><tr><td>Total ED Burden</td><td>2.66</td><td>125.80</td><td>35.95</td><td>China dominates gross demand.</td></tr><tr><td>Diagnosed ED Patients</td><td>0.93</td><td>28.93</td><td>17.98</td><td>U.S. diagnosis conversion is structurally stronger.</td></tr><tr><td>Treated ED Patients</td><td>0.63</td><td>16.78</td><td>13.48</td><td>Treatment activity matters more than prevalence alone.</td></tr><tr><td>PDE5-Treated Patients</td><td>0.52</td><td>13.43</td><td>11.33</td><td>PDE5 exposure creates the failure pool.</td></tr><tr><td>PDE5 Inadequate Responders</td><td>0.166</td><td>4.30</td><td>3.62</td><td>Core theoretical target before eligibility and reach filters.</td></tr></tbody></table></div></div>
</section>

<section id="eligibility" class="content-section">
  <div class="header"><h2>Eligibility & Reachable Pool</h2><p>The real opportunity is smaller than the PDE5 non-responder pool, but higher quality and more commercially actionable.</p></div>
  <div class="kpi-grid three"><div class="kpi primary"><div class="kpi-label">U.S. Reachable Pool 2035</div><div class="kpi-value">0.551 Mn</div><div class="kpi-note">Strongest commercial conversion among priority markets.</div></div><div class="kpi"><div class="kpi-label">China Reachable Pool 2035</div><div class="kpi-value">0.195 Mn</div><div class="kpi-note">Large source pool, but heavily filtered by affordability and channel reach.</div></div><div class="kpi"><div class="kpi-label">Taiwan Reachable Pool 2035</div><div class="kpi-value">0.023 Mn</div><div class="kpi-note">Small but high-value launch-validation pool.</div></div></div>
  <div class="two-grid"><div class="card"><h3 class="list-title">PDE5 Non-Responder → Eligible → Reachable</h3><div class="chart-container"><canvas id="eligibilityChart"></canvas></div><div class="note">Compression from target pool to realistic commercial pool.</div></div><div class="card"><h3 class="list-title">Etiology Fit & Clinical Priority</h3><div class="chart-container"><canvas id="etiologyChart"></canvas></div><div class="note">Eligibility weight reflects biological fit and commercial priority.</div></div></div>
  <div class="card"><div class="table-wrap"><table><thead><tr><th>Etiology Segment</th><th>Clinical Fit</th><th>Commercial Priority</th><th>Eligibility Weight</th><th>Strategic Meaning</th></tr></thead><tbody><tr><td>Diabetic ED</td><td><span class="heat heat-high">High</span></td><td><span class="heat heat-high">High</span></td><td>0.45</td><td>Strong endothelial / vascular repair rationale.</td></tr><tr><td>Vasculogenic ED</td><td><span class="heat heat-high">High</span></td><td><span class="heat heat-high">High</span></td><td>0.42</td><td>Strong fit with restorative positioning.</td></tr><tr><td>Post-prostatectomy ED</td><td><span class="heat heat-med">Medium-high</span></td><td><span class="heat heat-high">High</span></td><td>0.35</td><td>Clear, definable trial population.</td></tr><tr><td>Age-related mixed ED</td><td><span class="heat heat-med">Medium</span></td><td><span class="heat heat-med">Medium</span></td><td>0.25</td><td>Large but heterogeneous response.</td></tr><tr><td>Psychogenic ED</td><td><span class="heat heat-low">Low</span></td><td><span class="heat heat-low">Low</span></td><td>0.05</td><td>Not a priority target for invasive regenerative intervention.</td></tr></tbody></table></div></div>
</section>

<section id="geography" class="content-section">
  <div class="header"><h2>Geographic Strategy: Sequencing Launch and Scale</h2><p>A deliberate progression from controlled validation to scale-market expansion and premium commercialization.</p></div>
  <div class="card"><p>Geographic expansion should be sequenced rather than broad-based. Taiwan serves as the validation market, China offers scale through partnership, and the United States provides the highest-value premium market if evidence and regulatory execution are strong.</p></div>
  <div class="three-grid"><div class="geo-card"><div class="geo-head"><h3>Taiwan</h3><p>Launch Validation</p></div><div class="geo-body"><div class="geo-block"><div class="geo-label">Launch</div><div class="geo-value">2027</div></div><div class="geo-block"><div class="geo-label">Role</div><div class="geo-text">Controlled commercialization to generate real-world evidence, refine workflow, and build KOL credibility.</div></div><div class="geo-block"><div class="geo-label">2035 Net Price / Cycle</div><div class="geo-value">~$2,545</div></div></div></div><div class="geo-card"><div class="geo-head"><h3>China</h3><p>Scale Market</p></div><div class="geo-body"><div class="geo-block"><div class="geo-label">Launch</div><div class="geo-value">2029</div></div><div class="geo-block"><div class="geo-label">Role</div><div class="geo-text">Large diabetic and aging male pool, concentrated in premium Tier-1 and Tier-2 urban centers.</div></div><div class="geo-block"><div class="geo-label">2035 Net Price / Cycle</div><div class="geo-value">~$1,536</div></div></div></div><div class="geo-card"><div class="geo-head premium"><h3>United States</h3><p>Premium Evidence Market</p></div><div class="geo-body"><div class="geo-block"><div class="geo-label">Launch</div><div class="geo-value">2031</div></div><div class="geo-block"><div class="geo-label">Role</div><div class="geo-text">Highest-value market requiring stronger evidence, regulatory clarity, and specialist-channel execution.</div></div><div class="geo-block"><div class="geo-label">2035 Net Price / Cycle</div><div class="geo-value">~$5,388</div></div></div></div></div>
  <div class="card" style="margin-top:24px"><h3 class="list-title">Expansion Optionality | 2035 EliteCell Revenue</h3><div class="chart-container"><canvas id="expansionChart"></canvas></div><div class="note">Selective expansion markets after Taiwan / China / U.S. proof.</div></div>
</section>

<section id="pricing" class="content-section">
  <div class="header"><h2>Pricing & Net Realization</h2><p>Premium procedure economics, not commodity oral-drug pricing, drive the revenue case.</p></div>
  <div class="kpi-grid four"><div class="kpi primary"><div class="kpi-label">U.S. Net Cycle Revenue 2035</div><div class="kpi-value">$5,388</div><div class="kpi-note">Highest monetization per new treatment cycle.</div></div><div class="kpi"><div class="kpi-label">Taiwan Net Cycle Revenue 2035</div><div class="kpi-value">$2,545</div><div class="kpi-note">Launch-market pricing supports validation economics.</div></div><div class="kpi"><div class="kpi-label">China Net Cycle Revenue 2035</div><div class="kpi-value">$1,536</div><div class="kpi-note">Scale market with lower net realization.</div></div><div class="kpi"><div class="kpi-label">Retreatment Add-on</div><div class="kpi-value">28%</div><div class="kpi-note">Base-case annual revenue uplift from repeat cycles.</div></div></div>
  <div class="two-grid"><div class="card"><h3 class="list-title">Gross-to-Net Treatment Economics</h3><div class="chart-container"><canvas id="pricingChart"></canvas></div><div class="note">Illustrative 2035 gross / net cycle economics by market.</div></div><div class="card"><h3 class="list-title">Net Revenue per Cycle | 2025 vs 2035</h3><div class="chart-container"><canvas id="netCycleChart"></canvas></div><div class="note">Net cycle revenue grows at ~2% annually in the model.</div></div></div>
  <div class="section-note"><strong>Strategic implication:</strong> the U.S. does not need the largest patient pool to dominate revenue. Pricing power, private-pay depth, specialist access, and confidence in durability create the valuation case.</div>
</section>

<section id="adoption" class="content-section">
  <div class="header"><h2>Adoption & Channel Strategy</h2><p>The forecast is not immediate uptake; it is a specialist-channel ramp after launch timing, evidence, and access constraints.</p></div>
  <div class="card"><h3 class="list-title">Adoption Rate of Commercially Reachable Pool</h3><div class="chart-container"><canvas id="adoptionChart"></canvas></div><div class="note">Adoption rates by year after country launch.</div></div>
  <div class="card"><h3 class="list-title">Channel Mapping</h3><div class="table-wrap"><table><thead><tr><th>Channel</th><th>Role</th><th>Taiwan</th><th>China</th><th>U.S.</th><th>Adoption Constraint</th></tr></thead><tbody><tr><td>Hospital urology departments</td><td>Evidence generation and credibility</td><td><span class="heat heat-high">High</span></td><td><span class="heat heat-high">High</span></td><td><span class="heat heat-high">High</span></td><td>Clinical proof and workflow</td></tr><tr><td>Private urology clinics</td><td>Procedure delivery</td><td><span class="heat heat-med">Med-high</span></td><td><span class="heat heat-med">Medium</span></td><td><span class="heat heat-high">High</span></td><td>Physician confidence and pricing</td></tr><tr><td>Men’s health clinics</td><td>Private-pay conversion</td><td><span class="heat heat-med">Medium</span></td><td><span class="heat heat-high">High urban</span></td><td><span class="heat heat-high">High</span></td><td>Reputation and claims compliance</td></tr><tr><td>Regenerative medicine centers</td><td>Early procedure infrastructure</td><td><span class="heat heat-high">High</span></td><td><span class="heat heat-med">Medium</span></td><td><span class="heat heat-med">Medium</span></td><td>Regulatory quality perception</td></tr><tr><td>Telehealth ED platforms</td><td>Referral source for PDE5 failures</td><td><span class="heat heat-low">Low-med</span></td><td><span class="heat heat-med">Medium</span></td><td><span class="heat heat-high">High</span></td><td>Procedure handoff</td></tr></tbody></table></div></div>
</section>

<section id="forecast" class="content-section">
  <div class="header"><h2>Revenue Forecast | 2025–2035</h2><p>Base-case EliteCell Bio revenue capture build-up by geography.</p></div>
  <div class="card"><p style="margin-bottom:18px">Pre-launch revenue is zero by design. The largest inflection occurs after U.S. entry, where higher net realization per cycle materially changes the global revenue trajectory.</p><div class="chart-container"><canvas id="revenueChart"></canvas></div><div class="note">Revenue shown in US$ Mn.</div></div>
  <div class="two-grid"><div class="card"><h3 class="list-title">EliteCell Revenue | US$ Mn</h3><table><thead><tr><th>Geography</th><th>2027</th><th>2030</th><th>2035</th></tr></thead><tbody><tr><td>Taiwan</td><td>0.14</td><td>0.73</td><td>1.87</td></tr><tr><td>China</td><td>0.00</td><td>0.42</td><td>2.42</td></tr><tr><td>United States</td><td>0.00</td><td>0.00</td><td>18.32</td></tr><tr><td>Expansion Markets</td><td>0.00</td><td>0.00</td><td>3.14</td></tr><tr><td>Global EliteCell Total</td><td>0.14</td><td>1.14</td><td>25.75</td></tr></tbody></table></div><div class="card"><h3 class="list-title">Patient Segment Revenue Mix | 2035</h3><div class="chart-container small"><canvas id="segmentMixChart"></canvas></div><div class="note">Revenue mix by patient segment.</div></div></div>
</section>

<section id="clinical" class="content-section">
  <div class="header"><h2>Clinical Evidence & Endpoint Strategy</h2><p>Premium pricing and adoption depend on functional evidence, objective vascular support, and durability beyond early response.</p></div>
  <div class="card"><p>EliteCell Bio’s position should be built around tissue restoration rather than transient vasodilation. The strongest commercial argument comes from validated erectile-function endpoints, objective vascular measures, and 12-month durability that supports a premium procedure-led intervention.</p></div>
  <div class="three-grid"><div class="endpoint-card"><div class="endpoint-title">IIEF-EF Score</div><div class="endpoint-text">Core erectile-function benchmark and primary regulatory-facing measure.</div></div><div class="endpoint-card"><div class="endpoint-title">Erection Hardness Score</div><div class="endpoint-text">Patient-centric rigidity measure that translates into physician and patient communication.</div></div><div class="endpoint-card"><div class="endpoint-title">SEP-2 / SEP-3</div><div class="endpoint-text">Real-world utility measures linked to penetration and completion outcomes.</div></div><div class="endpoint-card"><div class="endpoint-title">Penile Doppler PSV</div><div class="endpoint-text">Objective vascular-flow evidence supporting a restorative mechanism claim.</div></div><div class="endpoint-card"><div class="endpoint-title">12-Month Durability</div><div class="endpoint-text">Critical bridge between clinical proof, pricing power, and retreatment logic.</div></div><div class="endpoint-card"><div class="endpoint-title">Potency / CMC Assays</div><div class="endpoint-text">Lot-to-lot consistency and potency assurance for FDA, TFDA, and premium-market confidence.</div></div></div>
  <div class="card" style="margin-top:24px"><h3 class="list-title">Endpoint-to-Commercial Implication</h3><div class="table-wrap"><table><thead><tr><th>Outcome Measure</th><th>Significance</th><th>Commercial Implication</th></tr></thead><tbody><tr><td>IIEF-EF</td><td>Core erectile capacity</td><td>Primary regulatory benchmark.</td></tr><tr><td>EHS</td><td>Functional rigidity</td><td>Patient-centric marketing metric.</td></tr><tr><td>SEP-2 / SEP-3</td><td>Successful penetration / completion</td><td>Measures real-world utility.</td></tr><tr><td>Penile Doppler PSV</td><td>Objective vascular flow</td><td>Supports restorative claim.</td></tr><tr><td>12-Month Durability</td><td>Functional persistence</td><td>Justifies procedural premium and retreatment model.</td></tr></tbody></table></div></div>
</section>

<section id="competition" class="content-section">
  <div class="header"><h2>Competitive Landscape & Positioning</h2><p>EliteCell Bio must differentiate across the ED treatment escalation pathway.</p></div>
  <div class="card"><p style="margin-bottom:22px">The central challenge is not defeating generic sildenafil or tadalafil. The real competitive battle is against second-line injections, shockwave therapy, unregulated regenerative clinics, and surgical implants.</p><div class="table-wrap"><table><thead><tr><th>Therapy Category</th><th>Current Positioning</th><th>Invasiveness</th><th>Threat to EliteCell Bio</th></tr></thead><tbody><tr><td>PDE5 Inhibitors</td><td>First-line symptomatic therapy.</td><td>Low</td><td>Low. Defines the failure pool.</td></tr><tr><td>Alprostadil / Trimix</td><td>Second-line on-demand injection.</td><td>Medium–High</td><td>High. Functional injection comparator.</td></tr><tr><td>Shockwave Therapy</td><td>Regenerative-adjacent private-pay procedure.</td><td>Low–Medium</td><td>Very high. Closest cash-pay substitute.</td></tr><tr><td>Unregulated PRP / Stem Cell</td><td>Wellness-clinic offerings.</td><td>Medium</td><td>High. Creates reputational risk.</td></tr><tr><td>Penile Implants</td><td>Third-line irreversible intervention.</td><td>Very High</td><td>Medium. EliteCell can position pre-implant.</td></tr></tbody></table></div></div>
  <div class="card"><h3 class="list-title">Competitive Scoring Matrix</h3><div class="chart-container small"><canvas id="competitiveChart"></canvas></div><div class="note">Directional score: 1 = low, 5 = high.</div></div>
</section>

<section id="roadmap" class="content-section">
  <div class="header"><h2>Roadmap, Scenario & Risk</h2><p>Execution depends on sequencing market entry, regulatory engagement, CMC readiness, evidence generation, and downside-risk mitigation.</p></div>
  <div class="two-grid"><div class="card"><h3 class="list-title">Tactical Milestone Roadmap</h3><div class="timeline"><div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-card"><div class="timeline-date">2025–2026</div><div class="timeline-title">Taiwan Dual Acts Registration</div><div class="timeline-text">Secure first-market regulatory path and validation hub.</div></div></div><div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-card"><div class="timeline-date">2026–2027</div><div class="timeline-title">Texas Facility DMF Expansion</div><div class="timeline-text">Support CMC comparability and potency assurance.</div></div></div><div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-card"><div class="timeline-date">2027–2029</div><div class="timeline-title">Boao Lecheng Entry</div><div class="timeline-text">Accelerate China translation with pilot-zone access.</div></div></div><div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-card"><div class="timeline-date">2028–2030</div><div class="timeline-title">U.S. Pre-IND Meeting</div><div class="timeline-text">Align with FDA CBER on endpoint, CMC, and RMAT logic.</div></div></div><div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-card"><div class="timeline-date">2029–2032</div><div class="timeline-title">12-Month Durability Data</div><div class="timeline-text">Support premium pricing and retreatment assumptions.</div></div></div><div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-card"><div class="timeline-date">2032–2035</div><div class="timeline-title">Expansion Activation</div><div class="timeline-text">Launch in Japan, Korea, Europe, and Middle East premium channels.</div></div></div></div></div><div><div class="three-grid" style="grid-template-columns:1fr;gap:18px"><div class="scenario-card"><div class="scenario-title">Conservative Scenario</div><div class="scenario-value">$10.81 Mn</div><div class="scenario-text">Lower eligibility, reach, price, adoption, and capture; one-year launch delay.</div></div><div class="scenario-card"><div class="scenario-title">Base Case</div><div class="scenario-value">$25.75 Mn</div><div class="scenario-text">Measured specialist uptake, staged launches, and premium U.S. entry.</div></div><div class="scenario-card"><div class="scenario-title">Upside Scenario</div><div class="scenario-value">$55.36 Mn</div><div class="scenario-text">Higher reach, faster adoption, stronger capture, and one-year launch acceleration.</div></div></div></div></div>
  <div class="card"><h3 class="list-title">Sensitivity Drivers</h3><div class="chart-container small"><canvas id="sensitivityChart"></canvas></div><div class="note">Directional sensitivity score: 1 = low, 5 = very high.</div></div>
  <div class="card"><h3 class="list-title">Forecast Logic Bridge</h3><div class="four-grid"><div class="step-card"><div class="step-number">1</div><div class="step-title">Male 40+</div><div class="step-text">Demographic starting base.</div></div><div class="step-card"><div class="step-number">2</div><div class="step-title">ED Burden</div><div class="step-text">Prevalence converts demographics to disease pool.</div></div><div class="step-card"><div class="step-number">3</div><div class="step-title">Treated PDE5 Pool</div><div class="step-text">Diagnosis, treatment, and PDE5 usage define active demand.</div></div><div class="step-card"><div class="step-number">4</div><div class="step-title">PDE5 Non-Responders</div><div class="step-text">The target pool for regenerative intervention.</div></div><div class="step-card"><div class="step-number">5</div><div class="step-title">Eligible + Reachable</div><div class="step-text">Clinical fit and commercial reach narrow opportunity.</div></div><div class="step-card"><div class="step-number">6</div><div class="step-title">Adoption</div><div class="step-text">Post-launch specialist uptake converts reachable pool.</div></div><div class="step-card"><div class="step-number">7</div><div class="step-title">Price + Capture</div><div class="step-text">Net cycle revenue and share convert patients into company revenue.</div></div><div class="step-card"><div class="step-number">8</div><div class="step-title">Scenario Risk</div><div class="step-text">Sensitivity explains downside and upside boundaries.</div></div></div></div>
  <div class="footer-note">This cockpit is designed for client-facing preview use. The full study extends these outputs into detailed source-backed assumptions, country forecasts, regulatory strategy, competitive benchmarking, and commercialization recommendations.</div>
</section>

</div></main>

<div class="dashboard-footer">
  <div><span class="dot"></span><strong>Strategic Market Research</strong> | EliteCell Bio market preview dashboard | Global Injectable Regenerative Therapy for ED Market (2025–2035)</div>
  <div class="right">Confidential client preview · April 2026</div>
</div>
<script>
const BURGUNDY="#5B0F2E", BURGUNDY_DARK="#3A071D", BURGUNDY_SOFT="#8A2E4D", BURGUNDY_MID="#A94D6A", ROSE="#D9A8BC", ROSE_DARK="#B56B87", TEXT="#334155", GRID="rgba(148,163,184,.25)";
const chartInstances={};
function destroyChart(id){if(chartInstances[id]){chartInstances[id].destroy();delete chartInstances[id];}}
function getCtx(id){const c=document.getElementById(id);if(!c||typeof Chart==="undefined")return null;return c.getContext("2d");}
function moneyTick(v){return "$"+v+"M"}
function defaultOptions(yTitle){return{responsive:true,maintainAspectRatio:false,scales:{x:{grid:{display:false},ticks:{color:"#475569",font:{size:12}}},y:{beginAtZero:true,title:{display:!!yTitle,text:yTitle||"",color:BURGUNDY,font:{weight:"bold"}},grid:{color:GRID},ticks:{color:"#475569"}}},plugins:{legend:{position:"bottom",labels:{color:TEXT,boxWidth:14,padding:18}},tooltip:{mode:"index",intersect:false}}};}
function initMixChart(){const id="mixChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"doughnut",data:{labels:["United States","China","Taiwan","Expansion Markets"],datasets:[{data:[71.1,9.4,7.2,12.2],backgroundColor:[BURGUNDY,BURGUNDY_SOFT,ROSE_DARK,ROSE],borderColor:"#fff",borderWidth:3}]},options:{responsive:true,maintainAspectRatio:false,cutout:"62%",plugins:{legend:{position:"bottom",labels:{color:TEXT,boxWidth:14,padding:18}},tooltip:{callbacks:{label:c=>c.label+": "+c.parsed.toFixed(1)+"%"}}}}});}
function initMarketCaptureChart(){const id="marketCaptureChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"bar",data:{labels:["2030","2035"],datasets:[{label:"Total Regenerative ED Market",data:[3.17,137.65],backgroundColor:ROSE,borderColor:ROSE_DARK,borderWidth:1},{label:"EliteCell Revenue",data:[1.14,25.75],backgroundColor:BURGUNDY,borderColor:BURGUNDY_DARK,borderWidth:1}]},options:defaultOptions("Revenue (US$ Mn)")});}
function initDemandChart(){const id="demandChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"bar",data:{labels:["China","United States","Japan","Middle East Premium","Taiwan"],datasets:[{label:"2035 ED Burden (Mn)",data:[125.8,35.95,16.35,12.19,2.66],backgroundColor:[BURGUNDY,BURGUNDY_SOFT,BURGUNDY_MID,ROSE_DARK,ROSE],borderColor:BURGUNDY_DARK,borderWidth:1}]},options:{indexAxis:"y",...defaultOptions("Patients (Mn)"),plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>c.parsed.x.toFixed(2)+" Mn"}}}}});}
function initMale40Chart(){const id="male40Chart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"bar",data:{labels:["Taiwan","China","United States","Japan","Middle East Premium"],datasets:[{label:"2025",data:[6.4,374,83,38.8,30],backgroundColor:ROSE,borderColor:ROSE_DARK,borderWidth:1},{label:"2035",data:[7.0,393.13,89.88,38.03,34.82],backgroundColor:BURGUNDY,borderColor:BURGUNDY_DARK,borderWidth:1}]},options:defaultOptions("Male 40+ population (Mn)")});}
function initCountryFunnelChart(){const id="countryFunnelChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"bar",data:{labels:["ED Burden","Diagnosed","Treated","PDE5 Users","PDE5 Inadequate"],datasets:[{label:"Taiwan",data:[2.66,.93,.63,.52,.166],backgroundColor:ROSE,borderColor:ROSE_DARK,borderWidth:1},{label:"China",data:[125.8,28.93,16.78,13.43,4.30],backgroundColor:BURGUNDY_SOFT,borderColor:BURGUNDY_DARK,borderWidth:1},{label:"United States",data:[35.95,17.98,13.48,11.33,3.62],backgroundColor:BURGUNDY,borderColor:BURGUNDY_DARK,borderWidth:1}]},options:defaultOptions("Patients (Mn)")});}
function initEligibilityChart(){const id="eligibilityChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"bar",data:{labels:["Taiwan","China","United States"],datasets:[{label:"PDE5 inadequate responders",data:[.166,4.30,3.62],backgroundColor:ROSE,borderColor:ROSE_DARK,borderWidth:1},{label:"Clinically eligible",data:[.063,1.504,1.450],backgroundColor:BURGUNDY_MID,borderColor:BURGUNDY_SOFT,borderWidth:1},{label:"Commercially reachable",data:[.023,.195,.551],backgroundColor:BURGUNDY,borderColor:BURGUNDY_DARK,borderWidth:1}]},options:defaultOptions("Patients (Mn)")});}
function initEtiologyChart(){const id="etiologyChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"bar",data:{labels:["Diabetic ED","Vasculogenic ED","Post-prostatectomy","Age-related mixed","Neurogenic/mixed","Psychogenic"],datasets:[{label:"Eligibility weight",data:[.45,.42,.35,.25,.22,.05],backgroundColor:[BURGUNDY,BURGUNDY_SOFT,BURGUNDY_MID,ROSE_DARK,ROSE,"#CBD5E1"],borderColor:BURGUNDY_DARK,borderWidth:1}]},options:{indexAxis:"y",...defaultOptions("Eligibility weight"),plugins:{legend:{display:false}}}});}
function initExpansionChart(){const id="expansionChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"bar",data:{labels:["Japan","Middle East Premium","Germany","South Korea","United Kingdom","France","Italy","Singapore","Spain","RoW Premium"],datasets:[{label:"2035 EliteCell revenue",data:[1.33,.43,.33,.30,.24,.17,.13,.08,.08,.04],backgroundColor:[BURGUNDY,BURGUNDY_SOFT,BURGUNDY_MID,ROSE_DARK,ROSE,ROSE,ROSE,ROSE,ROSE,"#CBD5E1"],borderColor:BURGUNDY_DARK,borderWidth:1}]},options:{indexAxis:"y",...defaultOptions("Revenue (US$ Mn)"),plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>"$"+c.parsed.x.toFixed(2)+" Mn"}}}}});}
function initPricingChart(){const id="pricingChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"bar",data:{labels:["Taiwan","China","United States","Japan","Singapore","Middle East"],datasets:[{label:"Gross price / cycle",data:[3600,2800,8500,6200,6800,6200],backgroundColor:ROSE,borderColor:ROSE_DARK,borderWidth:1},{label:"Net revenue / cycle 2035",data:[2545,1536,5388,3779,4310,3628],backgroundColor:BURGUNDY,borderColor:BURGUNDY_DARK,borderWidth:1}]},options:defaultOptions("US$ per cycle")});}
function initNetCycleChart(){const id="netCycleChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"bar",data:{labels:["Taiwan","China","United States","Japan","Singapore","Germany"],datasets:[{label:"2025",data:[2088,1260,4420,3100,3536,2784],backgroundColor:ROSE,borderColor:ROSE_DARK,borderWidth:1},{label:"2035",data:[2545,1536,5388,3779,4310,3394],backgroundColor:BURGUNDY,borderColor:BURGUNDY_DARK,borderWidth:1}]},options:defaultOptions("Net revenue / cycle (US$)")});}
function initAdoptionChart(){const id="adoptionChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"line",data:{labels:["2025","2026","2027","2028","2029","2030","2031","2032","2033","2034","2035"],datasets:[{label:"Taiwan",data:[0,0,.86,1.71,2.57,3.43,4.29,5.14,6,6,6],borderColor:BURGUNDY,backgroundColor:"rgba(91,15,46,.12)",tension:.35,fill:false},{label:"China",data:[0,0,0,0,.5,1,1.5,2,2.5,3,3.5],borderColor:BURGUNDY_SOFT,backgroundColor:"rgba(138,46,77,.12)",tension:.35,fill:false},{label:"United States",data:[0,0,0,0,0,0,.64,1.29,1.93,2.57,3.21],borderColor:ROSE_DARK,backgroundColor:"rgba(181,107,135,.12)",tension:.35,fill:false},{label:"Japan",data:[0,0,0,0,0,0,0,.5,1,1.5,2],borderColor:"#64748B",backgroundColor:"rgba(100,116,139,.12)",tension:.35,fill:false}]},options:defaultOptions("Adoption rate (%)")});}
function initRevenueChart(){const id="revenueChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"bar",data:{labels:["2025","2026","2027","2028","2029","2030","2031","2032","2033","2034","2035"],datasets:[{label:"Taiwan",data:[0,0,.14,.31,.50,.73,.98,1.28,1.61,1.73,1.87],backgroundColor:ROSE,borderColor:ROSE_DARK,borderWidth:1},{label:"China",data:[0,0,0,0,.19,.42,.70,1.03,1.43,1.89,2.42],backgroundColor:BURGUNDY_SOFT,borderColor:BURGUNDY_DARK,borderWidth:1},{label:"Expansion Markets",data:[0,0,0,0,0,0,0,.47,1.28,2.18,3.14],backgroundColor:BURGUNDY_MID,borderColor:BURGUNDY_SOFT,borderWidth:1},{label:"United States",data:[0,0,0,0,0,0,3.02,6.34,9.99,13.97,18.32],backgroundColor:BURGUNDY,borderColor:BURGUNDY_DARK,borderWidth:1}]},options:{responsive:true,maintainAspectRatio:false,scales:{x:{stacked:true,grid:{display:false},ticks:{color:"#475569",font:{size:12}}},y:{stacked:true,beginAtZero:true,title:{display:true,text:"Revenue (US$ Mn)",color:BURGUNDY,font:{weight:"bold"}},grid:{color:GRID},ticks:{color:"#475569",callback:moneyTick}}},plugins:{tooltip:{mode:"index",intersect:false,callbacks:{label:function(c){return c.dataset.label+": $"+c.parsed.y.toFixed(2)+" Mn"}}},legend:{position:"bottom",labels:{color:TEXT,boxWidth:14,padding:18}}}}});}
function initSegmentMixChart(){const id="segmentMixChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"doughnut",data:{labels:["Diabetic / vascular","Severe age-related organic","Post-prostatectomy","Neurogenic / mixed","Other"],datasets:[{data:[46,22,18,10,4],backgroundColor:[BURGUNDY,BURGUNDY_SOFT,BURGUNDY_MID,ROSE_DARK,ROSE],borderColor:"#fff",borderWidth:3}]},options:{responsive:true,maintainAspectRatio:false,cutout:"60%",plugins:{legend:{position:"bottom",labels:{color:TEXT,boxWidth:14,padding:14}},tooltip:{callbacks:{label:c=>c.label+": "+c.parsed+"%"}}}}});}
function initCompetitiveChart(){const id="competitiveChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"radar",data:{labels:["Efficacy Evidence","Familiarity","Differentiation"],datasets:[{label:"PDE5 Inhibitors",data:[5,5,2],borderColor:"#94A3B8",backgroundColor:"rgba(148,163,184,.16)"},{label:"Shockwave",data:[3,3,4],borderColor:ROSE_DARK,backgroundColor:"rgba(181,107,135,.16)"},{label:"PRP Clinics",data:[2,3,4],borderColor:BURGUNDY_MID,backgroundColor:"rgba(169,77,106,.16)"},{label:"EliteCell Injectable",data:[3,2,5],borderColor:BURGUNDY,backgroundColor:"rgba(91,15,46,.18)"}]},options:{responsive:true,maintainAspectRatio:false,scales:{r:{min:0,max:5,ticks:{stepSize:1,color:"#64748B"},pointLabels:{color:TEXT,font:{size:13,weight:"bold"}},grid:{color:GRID},angleLines:{color:GRID}}},plugins:{legend:{position:"bottom",labels:{color:TEXT,boxWidth:14,padding:18}}}}});}
function initSensitivityChart(){const id="sensitivityChart",ctx=getCtx(id);if(!ctx)return;destroyChart(id);chartInstances[id]=new Chart(ctx,{type:"bar",data:{labels:["Adoption rate","Commercial reach","PDE5 inadequate response","Clinical eligibility","Price per treatment","Capture share","Launch timing","Retreatment add-on"],datasets:[{label:"Base 2035 Revenue",data:[25.75,25.75,25.75,25.75,25.75,25.75,25.75,25.75],backgroundColor:ROSE,borderColor:ROSE_DARK,borderWidth:1},{label:"Downside 2035 Revenue",data:[16.74,19.31,20.12,20.60,21.89,20.60,22.66,23.74],backgroundColor:BURGUNDY,borderColor:BURGUNDY_DARK,borderWidth:1},{label:"Upside 2035 Revenue",data:[37.34,32.19,32.19,30.90,29.61,30.90,28.84,28.56],backgroundColor:BURGUNDY_MID,borderColor:BURGUNDY_SOFT,borderWidth:1}]},options:{indexAxis:"y",...defaultOptions("2035 Revenue (US$ Mn)")}});}
function initChartsForSection(sectionId){setTimeout(()=>{if(sectionId==="snapshot"){initMixChart();initMarketCaptureChart();}if(sectionId==="demand"){initDemandChart();initMale40Chart();}if(sectionId==="country"){initCountryFunnelChart();}if(sectionId==="eligibility"){initEligibilityChart();initEtiologyChart();}if(sectionId==="geography"){initExpansionChart();}if(sectionId==="pricing"){initPricingChart();initNetCycleChart();}if(sectionId==="adoption"){initAdoptionChart();}if(sectionId==="forecast"){initRevenueChart();initSegmentMixChart();}if(sectionId==="competition"){initCompetitiveChart();}if(sectionId==="roadmap"){initSensitivityChart();}},120);}
function navigate(sectionId){document.querySelectorAll(".nav button").forEach(btn=>btn.classList.remove("nav-active"));const activeButton=document.getElementById("nav-"+sectionId);if(activeButton)activeButton.classList.add("nav-active");document.querySelectorAll(".content-section").forEach(section=>section.classList.remove("active"));const activeSection=document.getElementById(sectionId);if(activeSection)activeSection.classList.add("active");initChartsForSection(sectionId);}
window.addEventListener("load",()=>initChartsForSection("executive"));
</script>
</body>
</html>
'''

components.html(DASHBOARD_HTML, height=1220, scrolling=True)
