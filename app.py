import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Global Injectable Regenerative Therapy for ED Market | EliteCell Bio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

DASHBOARD_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Global Injectable Regenerative Therapy for ED Market (2025–2035)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
        :root {
            --burgundy-dark: #3A071D;
            --burgundy: #5B0F2E;
            --burgundy-soft: #8A2E4D;
            --burgundy-light: #F3E7ED;
            --ink: #1E293B;
            --muted: #64748B;
            --line: #E2E8F0;
            --page: #F8FAFC;
            --white: #FFFFFF;
        }

        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: var(--page);
            color: var(--ink);
            overflow: hidden;
        }

        body {
            height: 100vh;
            display: flex;
            flex-direction: row;
        }

        .sidebar {
            width: 275px;
            min-width: 275px;
            height: 100vh;
            background: linear-gradient(180deg, var(--burgundy-dark) 0%, var(--burgundy) 100%);
            color: white;
            display: flex;
            flex-direction: column;
            box-shadow: 14px 0 34px rgba(58, 7, 29, 0.25);
            z-index: 20;
        }

        .brand {
            padding: 28px 24px 24px 24px;
            border-bottom: 1px solid rgba(255,255,255,0.12);
        }

        .brand h1 {
            font-size: 21px;
            line-height: 1.15;
            margin: 0;
            font-weight: 800;
        }

        .brand p {
            margin: 10px 0 0 0;
            font-size: 11px;
            letter-spacing: 0.13em;
            text-transform: uppercase;
            color: rgba(255,255,255,0.72);
            font-weight: 700;
        }

        .nav {
            padding: 16px 0;
            overflow-y: auto;
        }

        .nav button {
            width: 100%;
            text-align: left;
            border: 0;
            background: transparent;
            color: rgba(255,255,255,0.75);
            padding: 15px 22px;
            font-size: 14px;
            cursor: pointer;
            border-left: 5px solid transparent;
            transition: 0.2s ease;
        }

        .nav button:hover {
            background: rgba(255,255,255,0.08);
            color: white;
        }

        .nav button.nav-active {
            background: rgba(255,255,255,0.14);
            color: white;
            border-left-color: #F6D6E5;
            font-weight: 750;
        }

        .sidebar-footer {
            margin-top: auto;
            padding: 18px 22px 24px 22px;
            border-top: 1px solid rgba(255,255,255,0.12);
            font-size: 12px;
            line-height: 1.45;
            color: rgba(255,255,255,0.70);
        }

        main {
            flex: 1;
            height: 100vh;
            overflow-y: auto;
            background:
                radial-gradient(circle at top right, rgba(91,15,46,0.10), transparent 28%),
                linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 42%, #F3F5F8 100%);
        }

        .page {
            max-width: 1180px;
            margin: 0 auto;
            padding: 34px 36px 80px 36px;
        }

        .content-section {
            display: none;
            animation: fadeIn 0.25s ease-in-out;
        }

        .content-section.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .hero {
            background:
                radial-gradient(circle at top right, rgba(255,255,255,0.18), transparent 30%),
                linear-gradient(135deg, var(--burgundy-dark) 0%, var(--burgundy) 62%, var(--burgundy-soft) 100%);
            color: white;
            padding: 34px 36px;
            border-radius: 26px;
            box-shadow: 0 18px 48px rgba(91,15,46,0.22);
            margin-bottom: 28px;
        }

        .eyebrow {
            font-size: 12px;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            color: rgba(255,255,255,0.78);
            font-weight: 800;
            margin-bottom: 12px;
        }

        .hero h2 {
            margin: 0;
            font-size: 38px;
            line-height: 1.08;
            font-weight: 850;
            max-width: 980px;
        }

        .hero p {
            max-width: 980px;
            margin: 16px 0 0 0;
            color: rgba(255,255,255,0.88);
            font-size: 17px;
            line-height: 1.58;
        }

        .header {
            margin-bottom: 24px;
        }

        .header h2 {
            margin: 0 0 8px 0;
            color: var(--burgundy);
            font-size: 32px;
            line-height: 1.15;
            font-weight: 850;
        }

        .header p {
            margin: 0;
            color: var(--muted);
            font-size: 17px;
            line-height: 1.55;
            max-width: 980px;
        }

        .card {
            background: white;
            border: 1px solid var(--line);
            border-radius: 20px;
            box-shadow: 0 12px 34px rgba(15, 23, 42, 0.06);
            padding: 24px;
            margin-bottom: 24px;
        }

        .card p {
            color: #334155;
            line-height: 1.72;
            margin: 0;
            font-size: 15px;
        }

        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 18px;
            margin-bottom: 24px;
        }

        .kpi {
            background: white;
            border: 1px solid var(--line);
            border-radius: 20px;
            padding: 23px;
            box-shadow: 0 12px 34px rgba(15, 23, 42, 0.06);
            min-height: 145px;
        }

        .kpi.primary {
            background: linear-gradient(135deg, var(--burgundy-dark) 0%, var(--burgundy) 100%);
            color: white;
            border: 0;
        }

        .kpi-label {
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.10em;
            color: var(--burgundy-soft);
            font-weight: 800;
            margin-bottom: 8px;
        }

        .kpi.primary .kpi-label {
            color: rgba(255,255,255,0.68);
        }

        .kpi-value {
            font-size: 36px;
            line-height: 1.05;
            font-weight: 850;
            color: var(--burgundy);
            margin-bottom: 10px;
        }

        .kpi.primary .kpi-value {
            color: white;
        }

        .kpi-note {
            color: #64748B;
            font-size: 13px;
            line-height: 1.45;
        }

        .kpi.primary .kpi-note {
            color: rgba(255,255,255,0.78);
        }

        .list-title {
            font-size: 20px;
            font-weight: 820;
            color: var(--burgundy);
            margin: 0 0 16px 0;
        }

        .imperatives {
            list-style: none;
            margin: 0;
            padding: 0;
        }

        .imperatives li {
            display: flex;
            gap: 12px;
            margin-bottom: 16px;
            color: #334155;
            line-height: 1.58;
        }

        .imperatives li:last-child {
            margin-bottom: 0;
        }

        .arrow {
            color: var(--burgundy);
            font-weight: 900;
            margin-top: 1px;
        }

        .funnel-panel {
            background: linear-gradient(135deg, var(--burgundy-dark), var(--burgundy));
            padding: 28px;
            border-radius: 22px;
            box-shadow: 0 18px 46px rgba(91,15,46,0.22);
            margin-bottom: 24px;
        }

        .funnel-panel h3 {
            color: white;
            margin: 0 0 22px 0;
            padding-bottom: 13px;
            border-bottom: 1px solid rgba(255,255,255,0.18);
            font-size: 20px;
        }

        .funnel-steps {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .funnel-step {
            color: white;
            border-radius: 14px;
            padding: 16px 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-left: 5px solid rgba(255,255,255,0.45);
            transition: 0.25s ease;
            box-shadow: 0 12px 24px rgba(0,0,0,0.10);
        }

        .funnel-step:hover {
            transform: translateX(8px);
        }

        .funnel-step h4 {
            margin: 0 0 4px 0;
            font-size: 15px;
            font-weight: 800;
        }

        .funnel-step p {
            margin: 0;
            font-size: 12px;
            color: rgba(255,255,255,0.78);
        }

        .funnel-value {
            font-size: 19px;
            font-weight: 850;
            white-space: nowrap;
            padding-left: 18px;
        }

        .funnel-1 { width: 100%; background: rgba(255,255,255,0.17); }
        .funnel-2 { width: 91%; margin-left: auto; background: rgba(255,255,255,0.22); }
        .funnel-3 { width: 76%; margin-left: auto; background: rgba(255,255,255,0.28); }
        .funnel-4 { width: 59%; margin-left: auto; background: var(--burgundy-soft); }
        .funnel-5 { width: 43%; margin-left: auto; background: #A43A5D; }

        .two-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 18px;
        }

        .three-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 18px;
        }

        .geo-card {
            background: white;
            border: 1px solid var(--line);
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 12px 34px rgba(15, 23, 42, 0.06);
            display: flex;
            flex-direction: column;
        }

        .geo-head {
            padding: 18px 20px;
            background: var(--burgundy-light);
            border-bottom: 1px solid var(--line);
        }

        .geo-head.premium {
            background: linear-gradient(135deg, var(--burgundy-dark), var(--burgundy));
            color: white;
        }

        .geo-head h3 {
            margin: 0;
            font-size: 21px;
            font-weight: 850;
        }

        .geo-head p {
            margin: 6px 0 0 0;
            color: var(--burgundy);
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.10em;
            font-weight: 850;
        }

        .geo-head.premium p {
            color: rgba(255,255,255,0.78);
        }

        .geo-body {
            padding: 22px;
        }

        .geo-block {
            margin-bottom: 18px;
        }

        .geo-block:last-child {
            margin-bottom: 0;
        }

        .geo-label {
            font-size: 11px;
            color: var(--muted);
            text-transform: uppercase;
            letter-spacing: 0.10em;
            font-weight: 800;
            margin-bottom: 5px;
        }

        .geo-value {
            font-size: 20px;
            color: var(--burgundy);
            font-weight: 850;
        }

        .geo-text {
            font-size: 14px;
            line-height: 1.6;
            color: #475569;
        }

        .chart-container {
            position: relative;
            width: 100%;
            height: 420px;
            max-height: 520px;
        }

        .note {
            text-align: center;
            color: var(--muted);
            font-size: 12px;
            margin-top: 12px;
        }

        .table-wrap {
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }

        thead tr {
            background: var(--burgundy-light);
            color: var(--burgundy);
            border-bottom: 1px solid var(--line);
        }

        th, td {
            padding: 15px 14px;
            text-align: left;
            vertical-align: top;
            border-bottom: 1px solid var(--line);
        }

        th {
            font-weight: 850;
        }

        tbody tr:hover {
            background: #FBF7F9;
        }

        td:first-child {
            font-weight: 800;
            color: var(--burgundy);
        }

        .footer-note {
            margin-top: 24px;
            padding: 18px 20px;
            background: white;
            border: 1px solid var(--line);
            border-radius: 18px;
            color: var(--muted);
            font-size: 13px;
            line-height: 1.6;
        }

        @media (max-width: 900px) {
            body {
                flex-direction: column;
                overflow: auto;
                height: auto;
            }

            .sidebar {
                width: 100%;
                min-width: 100%;
                height: auto;
            }

            .nav {
                display: flex;
                overflow-x: auto;
                padding: 8px;
            }

            .nav button {
                white-space: nowrap;
                border-left: 0;
                border-bottom: 4px solid transparent;
                padding: 12px 16px;
            }

            .nav button.nav-active {
                border-left: 0;
                border-bottom-color: #F6D6E5;
            }

            .sidebar-footer {
                display: none;
            }

            main {
                height: auto;
                overflow: visible;
            }

            .page {
                padding: 22px 18px 60px 18px;
            }

            .hero h2 {
                font-size: 28px;
            }

            .hero {
                padding: 26px 24px;
            }

            .kpi-grid, .three-grid, .two-grid {
                grid-template-columns: 1fr;
            }

            .funnel-step {
                width: 100% !important;
                margin-left: 0 !important;
            }

            .chart-container {
                height: 330px;
            }
        }
    </style>
</head>

<body>
    <aside class="sidebar">
        <div class="brand">
            <h1>EliteCell Bio<br>Market Preview</h1>
            <p>Strategic Market Report</p>
        </div>

        <nav class="nav">
            <button onclick="navigate('executive')" id="nav-executive" class="nav-active">Executive Outlook</button>
            <button onclick="navigate('funnel')" id="nav-funnel">Patient Funnel</button>
            <button onclick="navigate('geography')" id="nav-geography">Geographic Strategy</button>
            <button onclick="navigate('forecast')" id="nav-forecast">Revenue Forecast</button>
            <button onclick="navigate('competition')" id="nav-competition">Competitive Landscape</button>
        </nav>

        <div class="sidebar-footer">
            Built as a controlled preview. Full study includes detailed country forecasts, assumptions, evidence mapping, and commercialization strategy.
        </div>
    </aside>

    <main>
        <div class="page">

            <section id="executive" class="content-section active">
                <div class="hero">
                    <div class="eyebrow">Global Injectable Regenerative Therapy for ED Market | 2025–2035</div>
                    <h2>Executive Outlook: The Next Opportunity in Erectile Dysfunction</h2>
                    <p>
                        The injectable regenerative therapy opportunity is defined by targeting PDE5 inadequate responders,
                        validating commercially in Taiwan, scaling selectively in China, and capturing premium value in the United States.
                    </p>
                </div>

                <div class="card">
                    <p>
                        This preview outlines the core strategic thesis for EliteCell Bio. The erectile dysfunction market is entering a
                        second-line innovation phase where the most valuable opportunity is not broad competition with low-cost generic
                        PDE5 inhibitors, but a focused intervention for patients who remain insufficiently served after oral therapy.
                        Injectable regenerative medicine can sit between symptomatic drug failure and end-stage surgical implants,
                        provided it is positioned through specialist channels and supported by formal clinical evidence.
                    </p>
                </div>

                <div class="kpi-grid">
                    <div class="kpi primary">
                        <div class="kpi-label">Global 2035 Revenue</div>
                        <div class="kpi-value">$25.7 Mn</div>
                        <div class="kpi-note">Base-case capture for EliteCell Bio across launched and expansion markets.</div>
                    </div>

                    <div class="kpi">
                        <div class="kpi-label">Target Patient Segment</div>
                        <div class="kpi-value">30–35%</div>
                        <div class="kpi-note">Share of treated ED patients estimated to be PDE5 inadequate responders.</div>
                    </div>

                    <div class="kpi">
                        <div class="kpi-label">U.S. Premium Price</div>
                        <div class="kpi-value">$5,100</div>
                        <div class="kpi-note">Illustrative 2035 net realization per treatment cycle in the premium U.S. setting.</div>
                    </div>
                </div>

                <div class="card">
                    <h3 class="list-title">Strategic Imperatives</h3>
                    <ul class="imperatives">
                        <li>
                            <span class="arrow">►</span>
                            <span><strong>Target the PDE5 failure pool:</strong> Avoid broad ED-market inflation. Focus on organic moderate-to-severe ED where oral drugs fail and willingness to escalate is highest.</span>
                        </li>
                        <li>
                            <span class="arrow">►</span>
                            <span><strong>Execute staged geographic rollout:</strong> Use Taiwan for validation, China for scale through partnership, and the United States for premium evidence-led commercialization.</span>
                        </li>
                        <li>
                            <span class="arrow">►</span>
                            <span><strong>Differentiate with regulated evidence:</strong> Anchor adoption in clear clinical endpoints and formal regulatory positioning to separate EliteCell Bio from unregulated regenerative wellness offerings.</span>
                        </li>
                    </ul>
                </div>
            </section>

            <section id="funnel" class="content-section">
                <div class="header">
                    <h2>Patient Funnel: Defining the Reachable Market</h2>
                    <p>Why headline ED prevalence materially overstates the realistic commercial opportunity.</p>
                </div>

                <div class="card">
                    <p>
                        The market must be sized through a disciplined patient funnel. The total male 40+ population is reduced
                        sequentially by ED prevalence, diagnosis, treatment-seeking behavior, PDE5 usage, inadequate response,
                        clinical eligibility, and commercial reach. This prevents unrealistic TAM inflation and isolates the
                        patient pool most relevant for injectable regenerative therapy.
                    </p>
                </div>

                <div class="funnel-panel">
                    <h3>Global Aggregate Funnel Logic | Illustrative 2035 Proportions</h3>

                    <div class="funnel-steps">
                        <div class="funnel-step funnel-1">
                            <div>
                                <h4>1. Male Population Age 40+</h4>
                                <p>Base demographic pool across target regions.</p>
                            </div>
                            <div class="funnel-value">100%</div>
                        </div>

                        <div class="funnel-step funnel-2">
                            <div>
                                <h4>2. Total ED Prevalence</h4>
                                <p>Men with any degree of erectile dysfunction.</p>
                            </div>
                            <div class="funnel-value">~40%</div>
                        </div>

                        <div class="funnel-step funnel-3">
                            <div>
                                <h4>3. Diagnosed & Treated ED</h4>
                                <p>Men actively seeking medical intervention.</p>
                            </div>
                            <div class="funnel-value">~15%</div>
                        </div>

                        <div class="funnel-step funnel-4">
                            <div>
                                <h4>4. PDE5 Inadequate Responders</h4>
                                <p>The core target market after oral therapy failure.</p>
                            </div>
                            <div class="funnel-value">~4%</div>
                        </div>

                        <div class="funnel-step funnel-5">
                            <div>
                                <h4>5. Commercially Reachable</h4>
                                <p>Clinically eligible patients with access and payment capacity.</p>
                            </div>
                            <div class="funnel-value">&lt;1%</div>
                        </div>
                    </div>
                </div>

                <div class="two-grid">
                    <div class="card">
                        <h3 class="list-title">Priority Clinical Segments</h3>
                        <table>
                            <tbody>
                                <tr>
                                    <td>Diabetic ED</td>
                                    <td>Endothelial and vascular damage</td>
                                </tr>
                                <tr>
                                    <td>Vasculogenic ED</td>
                                    <td>Blood-flow restoration rationale</td>
                                </tr>
                                <tr>
                                    <td>Post-prostatectomy ED</td>
                                    <td>Nerve and tissue rehabilitation pathway</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="card">
                        <h3 class="list-title">Funnel Conversion Risk</h3>
                        <p>
                            Without specialist urology channels and proven clinical durability, drop-off between PDE5 inadequate
                            responders and actual treated patients can remain high. The commercial unlock depends on evidence,
                            physician confidence, and willingness to pay for a procedure-led intervention.
                        </p>
                    </div>
                </div>
            </section>

            <section id="geography" class="content-section">
                <div class="header">
                    <h2>Geographic Strategy: Sequencing Launch and Scale</h2>
                    <p>A deliberate progression from controlled validation to scale-market expansion and premium commercialization.</p>
                </div>

                <div class="card">
                    <p>
                        Geographic expansion should be sequenced rather than broad-based. Taiwan serves as the validation market,
                        China offers patient-volume scale through partnership, and the United States provides the highest-value
                        premium market if evidence and regulatory execution are strong.
                    </p>
                </div>

                <div class="three-grid">
                    <div class="geo-card">
                        <div class="geo-head">
                            <h3>Taiwan</h3>
                            <p>Launch Validation</p>
                        </div>
                        <div class="geo-body">
                            <div class="geo-block">
                                <div class="geo-label">Estimated Launch</div>
                                <div class="geo-value">2027</div>
                            </div>
                            <div class="geo-block">
                                <div class="geo-label">Strategic Role</div>
                                <div class="geo-text">Controlled commercialization to generate real-world evidence, refine workflow, and build regional KOL credibility.</div>
                            </div>
                            <div class="geo-block">
                                <div class="geo-label">Net Price / Cycle 2035</div>
                                <div class="geo-value">~$2,500</div>
                            </div>
                        </div>
                    </div>

                    <div class="geo-card">
                        <div class="geo-head">
                            <h3>China</h3>
                            <p>Scale Market</p>
                        </div>
                        <div class="geo-body">
                            <div class="geo-block">
                                <div class="geo-label">Estimated Launch</div>
                                <div class="geo-value">2029</div>
                            </div>
                            <div class="geo-block">
                                <div class="geo-label">Strategic Role</div>
                                <div class="geo-text">Large diabetic and aging male pool, with commercialization concentrated in premium Tier-1 and Tier-2 urban centers.</div>
                            </div>
                            <div class="geo-block">
                                <div class="geo-label">Net Price / Cycle 2035</div>
                                <div class="geo-value">~$1,500</div>
                            </div>
                        </div>
                    </div>

                    <div class="geo-card">
                        <div class="geo-head premium">
                            <h3>United States</h3>
                            <p>Premium Evidence Market</p>
                        </div>
                        <div class="geo-body">
                            <div class="geo-block">
                                <div class="geo-label">Estimated Launch</div>
                                <div class="geo-value">2031</div>
                            </div>
                            <div class="geo-block">
                                <div class="geo-label">Strategic Role</div>
                                <div class="geo-text">Highest-value market requiring stronger evidence, regulatory clarity, and specialist urology / men’s health channel execution.</div>
                            </div>
                            <div class="geo-block">
                                <div class="geo-label">Net Price / Cycle 2035</div>
                                <div class="geo-value">~$5,100</div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <section id="forecast" class="content-section">
                <div class="header">
                    <h2>Revenue Forecast | 2025–2035</h2>
                    <p>Base-case EliteCell Bio revenue capture build-up by geography.</p>
                </div>

                <div class="card">
                    <p style="margin-bottom: 18px;">
                        The forecast reflects staged launch sequencing. Pre-launch revenue is zero by design. The largest inflection
                        occurs after anticipated U.S. entry, where higher net realization per cycle materially changes the global
                        revenue trajectory.
                    </p>

                    <div class="chart-container">
                        <canvas id="revenueChart"></canvas>
                    </div>

                    <div class="note">
                        Revenue shown in US$ Mn. Illustrative base-case values assume successful clinical endpoints, regulatory clearances, and targeted specialist-channel adoption.
                    </div>
                </div>

                <div class="two-grid">
                    <div class="card">
                        <h3 class="list-title">Key Revenue Drivers</h3>
                        <ul class="imperatives">
                            <li><span class="arrow">►</span><span><strong>Pricing durability:</strong> Maintaining premium procedure-led economics versus generic oral therapies.</span></li>
                            <li><span class="arrow">►</span><span><strong>Reachable-pool adoption:</strong> Converting specialist-screened PDE5 inadequate responders into treated patients.</span></li>
                            <li><span class="arrow">►</span><span><strong>Retreatment mechanics:</strong> Revenue expansion as early adopters return for subsequent cycles.</span></li>
                        </ul>
                    </div>

                    <div class="card">
                        <h3 class="list-title">Sensitivity & Risks</h3>
                        <ul class="imperatives">
                            <li><span class="arrow">►</span><span><strong>Downside case:</strong> Slower adoption, weaker durability, lower pricing, or regulatory delay.</span></li>
                            <li><span class="arrow">►</span><span><strong>Upside case:</strong> Faster evidence acceptance, broader eligibility, stronger private-pay conversion, and faster U.S. uptake.</span></li>
                        </ul>
                    </div>
                </div>
            </section>

            <section id="competition" class="content-section">
                <div class="header">
                    <h2>Competitive Landscape & Positioning</h2>
                    <p>Where EliteCell Bio must differentiate across the ED treatment escalation pathway.</p>
                </div>

                <div class="card">
                    <p style="margin-bottom: 22px;">
                        EliteCell Bio’s central challenge is not defeating generic sildenafil or tadalafil. The real competitive
                        battle is against second-line injections, shockwave therapy, unregulated regenerative wellness clinics, and
                        surgical implants. A defensible position requires regulated evidence, durability, specialist acceptance, and
                        clear patient-selection logic.
                    </p>

                    <div class="table-wrap">
                        <table>
                            <thead>
                                <tr>
                                    <th>Therapy Category</th>
                                    <th>Current Positioning</th>
                                    <th>Invasiveness</th>
                                    <th>Threat to EliteCell Bio</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>PDE5 Inhibitors</td>
                                    <td>First-line symptomatic therapy; low cost and high familiarity.</td>
                                    <td>Low</td>
                                    <td>Low. They define the failure pool rather than the premium regenerative market.</td>
                                </tr>
                                <tr>
                                    <td>Alprostadil / Trimix</td>
                                    <td>Second-line, on-demand injection therapy.</td>
                                    <td>Medium–High</td>
                                    <td>High. Primary functional comparator for injection acceptance.</td>
                                </tr>
                                <tr>
                                    <td>Shockwave Therapy</td>
                                    <td>Regenerative-adjacent private-pay procedure.</td>
                                    <td>Low–Medium</td>
                                    <td>Very high. Closest commercial substitute competing for cash-pay budgets.</td>
                                </tr>
                                <tr>
                                    <td>Unregulated PRP / Stem Cell</td>
                                    <td>Wellness-clinic offerings with uneven evidence quality.</td>
                                    <td>Medium</td>
                                    <td>High. Creates reputational risk; EliteCell Bio must differentiate through formal evidence.</td>
                                </tr>
                                <tr>
                                    <td>Penile Implants</td>
                                    <td>Third-line surgical and irreversible intervention.</td>
                                    <td>Very High</td>
                                    <td>Medium. EliteCell Bio can position as a pre-implant option to delay surgery.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="footer-note">
                    The full report extends this preview into a detailed country forecast, treatment funnel, regulatory pathway,
                    competitive benchmark, sensitivity analysis, and commercialization roadmap for EliteCell Bio.
                </div>
            </section>

        </div>
    </main>

    <script>
        const chartData = {
            labels: ["2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034", "2035"],
            datasets: [
                {
                    label: "Taiwan ($Mn)",
                    data: [0, 0, 0.14, 0.31, 0.50, 0.73, 0.98, 1.28, 1.61, 1.73, 1.87],
                    backgroundColor: "#D9A8BC",
                    borderColor: "#B56B87",
                    borderWidth: 1
                },
                {
                    label: "China ($Mn)",
                    data: [0, 0, 0, 0, 0.19, 0.42, 0.70, 1.03, 1.43, 1.89, 2.42],
                    backgroundColor: "#8A2E4D",
                    borderColor: "#6F1D3B",
                    borderWidth: 1
                },
                {
                    label: "Expansion Markets ($Mn)",
                    data: [0, 0, 0, 0, 0, 0, 0, 0.47, 1.28, 2.18, 3.14],
                    backgroundColor: "#B97991",
                    borderColor: "#8A2E4D",
                    borderWidth: 1
                },
                {
                    label: "United States ($Mn)",
                    data: [0, 0, 0, 0, 0, 0, 3.02, 6.34, 9.99, 13.97, 18.32],
                    backgroundColor: "#5B0F2E",
                    borderColor: "#3A071D",
                    borderWidth: 1
                }
            ]
        };

        let revenueChartInstance = null;

        function initChart() {
            const canvas = document.getElementById("revenueChart");
            if (!canvas || typeof Chart === "undefined") {
                return;
            }

            const ctx = canvas.getContext("2d");

            if (revenueChartInstance) {
                revenueChartInstance.destroy();
            }

            revenueChartInstance = new Chart(ctx, {
                type: "bar",
                data: chartData,
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        x: {
                            stacked: true,
                            grid: { display: false },
                            ticks: {
                                color: "#475569",
                                font: { size: 12 }
                            }
                        },
                        y: {
                            stacked: true,
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: "Revenue (US$ Mn)",
                                color: "#5B0F2E",
                                font: { weight: "bold" }
                            },
                            grid: {
                                color: "rgba(148, 163, 184, 0.25)"
                            },
                            ticks: {
                                color: "#475569",
                                callback: function(value) {
                                    return "$" + value + "M";
                                }
                            }
                        }
                    },
                    plugins: {
                        tooltip: {
                            mode: "index",
                            intersect: false,
                            callbacks: {
                                label: function(context) {
                                    let label = context.dataset.label || "";
                                    if (label) label += ": ";
                                    if (context.parsed.y !== null) {
                                        label += "$" + context.parsed.y.toFixed(2) + " Mn";
                                    }
                                    return label;
                                }
                            }
                        },
                        legend: {
                            position: "bottom",
                            labels: {
                                color: "#334155",
                                boxWidth: 14,
                                padding: 18
                            }
                        }
                    }
                }
            });
        }

        function navigate(sectionId) {
            document.querySelectorAll(".nav button").forEach(function(btn) {
                btn.classList.remove("nav-active");
            });

            const activeButton = document.getElementById("nav-" + sectionId);
            if (activeButton) {
                activeButton.classList.add("nav-active");
            }

            document.querySelectorAll(".content-section").forEach(function(section) {
                section.classList.remove("active");
            });

            const activeSection = document.getElementById(sectionId);
            if (activeSection) {
                activeSection.classList.add("active");
            }

            if (sectionId === "forecast") {
                setTimeout(initChart, 80);
            }
        }

        window.addEventListener("load", function() {
            setTimeout(function() {
                if (document.getElementById("forecast").classList.contains("active")) {
                    initChart();
                }
            }, 120);
        });
    </script>
</body>
</html>
"""

components.html(DASHBOARD_HTML, height=980, scrolling=True)
