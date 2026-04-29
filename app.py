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

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
        :root {
            --burgundy-dark: #3A071D;
            --burgundy: #5B0F2E;
            --burgundy-soft: #8A2E4D;
            --burgundy-mid: #A94D6A;
            --burgundy-light: #F3E7ED;
            --rose: #D9A8BC;
            --rose-soft: #F8EEF3;
            --ink: #1E293B;
            --muted: #64748B;
            --line: #E2E8F0;
            --page: #F8FAFC;
            --white: #FFFFFF;
            --green: #1F7A53;
            --amber: #A16207;
            --red: #A8324A;
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
            width: 292px;
            min-width: 292px;
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
            font-weight: 850;
        }

        .brand p {
            margin: 10px 0 0 0;
            font-size: 11px;
            letter-spacing: 0.13em;
            text-transform: uppercase;
            color: rgba(255,255,255,0.72);
            font-weight: 750;
        }

        .nav {
            padding: 14px 0;
            overflow-y: auto;
        }

        .nav button {
            width: 100%;
            text-align: left;
            border: 0;
            background: transparent;
            color: rgba(255,255,255,0.75);
            padding: 13px 22px;
            font-size: 13.5px;
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
            font-weight: 760;
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
            max-width: 1220px;
            margin: 0 auto;
            padding: 34px 36px 90px 36px;
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
            font-weight: 880;
            max-width: 1000px;
        }

        .hero p {
            max-width: 1000px;
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
            font-weight: 860;
        }

        .header p {
            margin: 0;
            color: var(--muted);
            font-size: 17px;
            line-height: 1.55;
            max-width: 1020px;
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

        .card.compact {
            padding: 20px;
        }

        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 18px;
            margin-bottom: 24px;
        }

        .kpi-grid.four {
            grid-template-columns: repeat(4, minmax(0, 1fr));
        }

        .kpi {
            background: white;
            border: 1px solid var(--line);
            border-radius: 20px;
            padding: 23px;
            box-shadow: 0 12px 34px rgba(15, 23, 42, 0.06);
            min-height: 142px;
        }

        .kpi.primary {
            background: linear-gradient(135deg, var(--burgundy-dark) 0%, var(--burgundy) 100%);
            color: white;
            border: 0;
        }

        .kpi.secondary {
            background: linear-gradient(135deg, #FFFFFF 0%, var(--rose-soft) 100%);
            border-color: #EBD1DC;
        }

        .kpi-label {
            font-size: 11.5px;
            text-transform: uppercase;
            letter-spacing: 0.10em;
            color: var(--burgundy-soft);
            font-weight: 830;
            margin-bottom: 8px;
        }

        .kpi.primary .kpi-label {
            color: rgba(255,255,255,0.68);
        }

        .kpi-value {
            font-size: 34px;
            line-height: 1.05;
            font-weight: 880;
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
            font-weight: 840;
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
            font-size: 14.5px;
        }

        .imperatives li:last-child {
            margin-bottom: 0;
        }

        .arrow {
            color: var(--burgundy);
            font-weight: 900;
            margin-top: 1px;
        }

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
            font-weight: 820;
        }

        .funnel-step p {
            margin: 0;
            font-size: 12px;
            color: rgba(255,255,255,0.78);
        }

        .funnel-value {
            font-size: 19px;
            font-weight: 860;
            white-space: nowrap;
            padding-left: 18px;
        }

        .funnel-1 { width: 100%; background: rgba(255,255,255,0.17); }
        .funnel-2 { width: 91%; margin-left: auto; background: rgba(255,255,255,0.22); }
        .funnel-3 { width: 76%; margin-left: auto; background: rgba(255,255,255,0.28); }
        .funnel-4 { width: 59%; margin-left: auto; background: var(--burgundy-soft); }
        .funnel-5 { width: 43%; margin-left: auto; background: #A43A5D; }

        .geo-card, .scenario-card, .endpoint-card, .roadmap-card {
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
            font-weight: 820;
            margin-bottom: 5px;
        }

        .geo-value {
            font-size: 20px;
            color: var(--burgundy);
            font-weight: 860;
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

        .chart-container.small {
            height: 360px;
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

        .timeline {
            position: relative;
            padding-left: 18px;
        }

        .timeline::before {
            content: "";
            position: absolute;
            top: 8px;
            bottom: 8px;
            left: 8px;
            width: 3px;
            background: linear-gradient(180deg, var(--burgundy), var(--rose));
            border-radius: 999px;
        }

        .timeline-item {
            position: relative;
            padding: 0 0 18px 28px;
        }

        .timeline-dot {
            position: absolute;
            left: -17px;
            top: 4px;
            width: 16px;
            height: 16px;
            background: var(--burgundy);
            border: 3px solid white;
            box-shadow: 0 0 0 3px var(--rose);
            border-radius: 50%;
        }

        .timeline-card {
            background: white;
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 16px 18px;
            box-shadow: 0 10px 26px rgba(15, 23, 42, 0.05);
        }

        .timeline-date {
            color: var(--burgundy-soft);
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.09em;
            font-weight: 850;
            margin-bottom: 5px;
        }

        .timeline-title {
            color: var(--burgundy);
            font-size: 17px;
            font-weight: 850;
            margin-bottom: 5px;
        }

        .timeline-text {
            color: #475569;
            font-size: 14px;
            line-height: 1.55;
        }

        .badge-row {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 16px;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: 8px 12px;
            background: var(--rose-soft);
            color: var(--burgundy);
            border: 1px solid #E7C7D4;
            font-size: 12px;
            font-weight: 800;
        }

        .scenario-card {
            padding: 22px;
        }

        .scenario-title {
            font-size: 19px;
            color: var(--burgundy);
            font-weight: 850;
            margin-bottom: 8px;
        }

        .scenario-value {
            font-size: 34px;
            color: var(--burgundy);
            font-weight: 880;
            margin-bottom: 8px;
        }

        .scenario-text {
            color: #475569;
            line-height: 1.55;
            font-size: 14px;
        }

        .endpoint-card {
            padding: 20px;
        }

        .endpoint-title {
            color: var(--burgundy);
            font-weight: 850;
            font-size: 17px;
            margin-bottom: 9px;
        }

        .endpoint-text {
            color: #475569;
            font-size: 14px;
            line-height: 1.58;
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

        @media (max-width: 980px) {
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

            .brand {
                padding: 20px 20px 16px 20px;
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
                padding: 12px 14px;
                font-size: 13px;
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

            .kpi-grid, .kpi-grid.four, .three-grid, .two-grid {
                grid-template-columns: 1fr;
            }

            .funnel-step {
                width: 100% !important;
                margin-left: 0 !important;
            }

            .chart-container {
                height: 340px;
            }
        }
    </style>
</head>

<body>
    <aside class="sidebar">
        <div class="brand">
            <h1>EliteCell Bio<br>Market Cockpit</h1>
            <p>Strategic Market Report</p>
        </div>

        <nav class="nav">
            <button onclick="navigate('executive')" id="nav-executive" class="nav-active">Executive Outlook</button>
            <button onclick="navigate('snapshot')" id="nav-snapshot">Market Size & Capture</button>
            <button onclick="navigate('funnel')" id="nav-funnel">Patient Funnel</button>
            <button onclick="navigate('country')" id="nav-country">Country Funnel Deep Dive</button>
            <button onclick="navigate('geography')" id="nav-geography">Geographic Strategy</button>
            <button onclick="navigate('forecast')" id="nav-forecast">Revenue Forecast</button>
            <button onclick="navigate('clinical')" id="nav-clinical">Clinical Endpoint Strategy</button>
            <button onclick="navigate('competition')" id="nav-competition">Competitive Landscape</button>
            <button onclick="navigate('roadmap')" id="nav-roadmap">Roadmap & Scenario Risk</button>
        </nav>

        <div class="sidebar-footer">
            Controlled boardroom preview. Full study includes detailed country forecasts, source-backed assumptions, clinical evidence, regulatory mapping, and commercialization strategy.
        </div>
    </aside>

    <main>
        <div class="page">

            <!-- Executive -->
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
                        This dashboard summarizes the strategic thesis for EliteCell Bio. The erectile dysfunction market is entering a second-line innovation phase where the most attractive opportunity is not broad competition with low-cost generic PDE5 inhibitors, but a focused intervention for patients who remain insufficiently served after oral therapy. Injectable regenerative medicine can sit between symptomatic drug failure and end-stage surgical implants, provided it is positioned through specialist channels and supported by formal clinical evidence.
                    </p>
                </div>

                <div class="kpi-grid">
                    <div class="kpi primary">
                        <div class="kpi-label">EliteCell 2035 Revenue</div>
                        <div class="kpi-value">$25.75 Mn</div>
                        <div class="kpi-note">Base-case capture across Taiwan, China, United States, and expansion markets.</div>
                    </div>

                    <div class="kpi">
                        <div class="kpi-label">Target Patient Segment</div>
                        <div class="kpi-value">30–35%</div>
                        <div class="kpi-note">Share of treated ED patients estimated to be PDE5 inadequate responders.</div>
                    </div>

                    <div class="kpi">
                        <div class="kpi-label">2035 U.S. Revenue Mix</div>
                        <div class="kpi-value">71.1%</div>
                        <div class="kpi-note">The United States is the primary valuation and monetization anchor.</div>
                    </div>
                </div>

                <div class="card">
                    <h3 class="list-title">Strategic Imperatives</h3>
                    <ul class="imperatives">
                        <li>
                            <span class="arrow">►</span>
                            <span><strong>Target the PDE5 failure pool:</strong> Avoid broad ED-market inflation. Focus on organic moderate-to-severe ED where oral therapies fail and willingness to escalate is highest.</span>
                        </li>
                        <li>
                            <span class="arrow">►</span>
                            <span><strong>Execute staged geographic rollout:</strong> Use Taiwan for validation, China for scale through partnership, and the United States for premium evidence-led commercialization.</span>
                        </li>
                        <li>
                            <span class="arrow">►</span>
                            <span><strong>Differentiate with regulated evidence:</strong> Anchor adoption in clear clinical endpoints, CMC quality, and formal regulatory positioning to separate EliteCell Bio from unregulated regenerative wellness offerings.</span>
                        </li>
                    </ul>
                </div>
            </section>

            <!-- Market Snapshot -->
            <section id="snapshot" class="content-section">
                <div class="header">
                    <h2>Market Size & Capture Snapshot</h2>
                    <p>The 2035 opportunity is attractive because the total regenerative ED category expands rapidly, while EliteCell Bio can capture a focused, premium, specialist-channel share.</p>
                </div>

                <div class="kpi-grid four">
                    <div class="kpi primary">
                        <div class="kpi-label">Total Market 2035</div>
                        <div class="kpi-value">$137.65 Mn</div>
                        <div class="kpi-note">Global regenerative ED therapy revenue across all players.</div>
                    </div>

                    <div class="kpi secondary">
                        <div class="kpi-label">EliteCell Revenue 2035</div>
                        <div class="kpi-value">$25.75 Mn</div>
                        <div class="kpi-note">Base-case realized revenue from launched markets.</div>
                    </div>

                    <div class="kpi">
                        <div class="kpi-label">Capture Share</div>
                        <div class="kpi-value">18.7%</div>
                        <div class="kpi-note">Weighted average EliteCell capture share across markets.</div>
                    </div>

                    <div class="kpi">
                        <div class="kpi-label">U.S. Contribution</div>
                        <div class="kpi-value">71.1%</div>
                        <div class="kpi-note">The U.S. dominates due to premium pricing and higher commercial reach.</div>
                    </div>
                </div>

                <div class="two-grid">
                    <div class="card">
                        <h3 class="list-title">2035 EliteCell Revenue Mix</h3>
                        <div class="chart-container small">
                            <canvas id="mixChart"></canvas>
                        </div>
                        <div class="note">Revenue mix by geography, based on EliteCell Bio 2035 revenue contribution.</div>
                    </div>

                    <div class="card">
                        <h3 class="list-title">Total Market vs EliteCell Capture</h3>
                        <div class="chart-container small">
                            <canvas id="marketCaptureChart"></canvas>
                        </div>
                        <div class="note">Comparison of total regenerative ED market and EliteCell captured revenue.</div>
                    </div>
                </div>

                <div class="card">
                    <h3 class="list-title">Key Global Forecast Metrics | 2035</h3>
                    <div class="table-wrap">
                        <table>
                            <thead>
                                <tr>
                                    <th>Metric</th>
                                    <th>Value</th>
                                    <th>Strategic Interpretation</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Total Regenerative ED Market Revenue</td>
                                    <td>$137.65 Mn</td>
                                    <td>Represents the broader emerging category, not only EliteCell Bio revenue.</td>
                                </tr>
                                <tr>
                                    <td>EliteCell Bio Global Revenue</td>
                                    <td>$25.75 Mn</td>
                                    <td>Base-case realized opportunity after market launch, capture, and adoption assumptions.</td>
                                </tr>
                                <tr>
                                    <td>EliteCell Weighted Capture Share</td>
                                    <td>~18.7%</td>
                                    <td>Indicates meaningful but not unrealistic penetration in a specialist-led procedure market.</td>
                                </tr>
                                <tr>
                                    <td>U.S. Revenue Contribution</td>
                                    <td>71.1%</td>
                                    <td>Confirms that the United States is the critical premium-value anchor.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- Patient Funnel -->
            <section id="funnel" class="content-section">
                <div class="header">
                    <h2>Patient Funnel: Defining the Reachable Market</h2>
                    <p>Why headline ED prevalence materially overstates the realistic commercial opportunity.</p>
                </div>

                <div class="card">
                    <p>
                        The market must be sized through a disciplined patient funnel. The total male 40+ population is reduced sequentially by ED prevalence, diagnosis, treatment-seeking behavior, PDE5 usage, inadequate response, clinical eligibility, and commercial reach. This prevents unrealistic TAM inflation and isolates the patient pool most relevant for injectable regenerative therapy.
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
                            Without specialist urology channels and proven clinical durability, drop-off between PDE5 inadequate responders and actual treated patients can remain high. The commercial unlock depends on evidence, physician confidence, and willingness to pay for a procedure-led intervention.
                        </p>
                    </div>
                </div>
            </section>

            <!-- Country Funnel -->
            <section id="country" class="content-section">
                <div class="header">
                    <h2>Country Funnel Deep Dive</h2>
                    <p>China has the largest patient pool, but the United States provides the strongest commercial conversion and pricing potential.</p>
                </div>

                <div class="card">
                    <p>
                        The three priority markets have very different demand structures. Taiwan provides a compact validation market, China provides scale, and the United States provides the highest monetization. The critical comparison is not only total ED burden, but how much of that burden converts into diagnosed, treated, PDE5-exposed, and non-responder patients.
                    </p>
                </div>

                <div class="card">
                    <h3 class="list-title">2035 Patient Funnel by Country | Mn Patients</h3>
                    <div class="chart-container">
                        <canvas id="countryFunnelChart"></canvas>
                    </div>
                    <div class="note">Values shown in million patients. Funnel reflects progression from ED burden to PDE5 inadequate responders.</div>
                </div>

                <div class="card">
                    <div class="table-wrap">
                        <table>
                            <thead>
                                <tr>
                                    <th>Funnel Metric | 2035</th>
                                    <th>Taiwan</th>
                                    <th>China</th>
                                    <th>United States</th>
                                    <th>Strategic Meaning</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Total ED Burden</td>
                                    <td>2.66 Mn</td>
                                    <td>125.80 Mn</td>
                                    <td>35.95 Mn</td>
                                    <td>China dominates gross demand, but not necessarily revenue.</td>
                                </tr>
                                <tr>
                                    <td>Diagnosed ED Patients</td>
                                    <td>0.93 Mn</td>
                                    <td>28.93 Mn</td>
                                    <td>17.98 Mn</td>
                                    <td>U.S. diagnosis conversion is structurally stronger.</td>
                                </tr>
                                <tr>
                                    <td>Treated ED Patients</td>
                                    <td>0.63 Mn</td>
                                    <td>16.78 Mn</td>
                                    <td>13.48 Mn</td>
                                    <td>Treatment activity matters more than prevalence alone.</td>
                                </tr>
                                <tr>
                                    <td>PDE5-Treated Patients</td>
                                    <td>0.52 Mn</td>
                                    <td>13.43 Mn</td>
                                    <td>11.33 Mn</td>
                                    <td>PDE5 exposure creates the failure pool for EliteCell Bio.</td>
                                </tr>
                                <tr>
                                    <td>PDE5 Inadequate Responders</td>
                                    <td>0.166 Mn</td>
                                    <td>4.30 Mn</td>
                                    <td>3.62 Mn</td>
                                    <td>Core theoretical target pool before eligibility and commercial reach filters.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- Geography -->
            <section id="geography" class="content-section">
                <div class="header">
                    <h2>Geographic Strategy: Sequencing Launch and Scale</h2>
                    <p>A deliberate progression from controlled validation to scale-market expansion and premium commercialization.</p>
                </div>

                <div class="card">
                    <p>
                        Geographic expansion should be sequenced rather than broad-based. Taiwan serves as the validation market, China offers patient-volume scale through partnership, and the United States provides the highest-value premium market if evidence and regulatory execution are strong.
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

            <!-- Forecast -->
            <section id="forecast" class="content-section">
                <div class="header">
                    <h2>Revenue Forecast | 2025–2035</h2>
                    <p>Base-case EliteCell Bio revenue capture build-up by geography.</p>
                </div>

                <div class="card">
                    <p style="margin-bottom: 18px;">
                        The forecast reflects staged launch sequencing. Pre-launch revenue is zero by design. The largest inflection occurs after anticipated U.S. entry, where higher net realization per cycle materially changes the global revenue trajectory.
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
                        <h3 class="list-title">EliteCell Revenue | US$ Mn</h3>
                        <table>
                            <thead>
                                <tr>
                                    <th>Geography</th>
                                    <th>2027</th>
                                    <th>2030</th>
                                    <th>2035</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Taiwan</td>
                                    <td>0.14</td>
                                    <td>0.73</td>
                                    <td>1.87</td>
                                </tr>
                                <tr>
                                    <td>China</td>
                                    <td>0.00</td>
                                    <td>0.42</td>
                                    <td>2.42</td>
                                </tr>
                                <tr>
                                    <td>United States</td>
                                    <td>0.00</td>
                                    <td>0.00</td>
                                    <td>18.32</td>
                                </tr>
                                <tr>
                                    <td>Expansion Markets</td>
                                    <td>0.00</td>
                                    <td>0.00</td>
                                    <td>3.14</td>
                                </tr>
                                <tr>
                                    <td>Global EliteCell Total</td>
                                    <td>0.14</td>
                                    <td>1.14</td>
                                    <td>25.75</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="card">
                        <h3 class="list-title">Key Revenue Drivers</h3>
                        <ul class="imperatives">
                            <li><span class="arrow">►</span><span><strong>Pricing durability:</strong> Maintaining premium procedure-led economics versus generic oral therapies.</span></li>
                            <li><span class="arrow">►</span><span><strong>Reachable-pool adoption:</strong> Converting specialist-screened PDE5 inadequate responders into treated patients.</span></li>
                            <li><span class="arrow">►</span><span><strong>Retreatment mechanics:</strong> Revenue expansion as early adopters return for subsequent cycles.</span></li>
                        </ul>
                    </div>
                </div>
            </section>

            <!-- Clinical -->
            <section id="clinical" class="content-section">
                <div class="header">
                    <h2>Clinical Evidence & Endpoint Strategy</h2>
                    <p>Premium pricing and physician adoption depend on functional evidence, objective vascular support, and durability beyond early response.</p>
                </div>

                <div class="card">
                    <p>
                        EliteCell Bio’s market position should be built around tissue restoration rather than transient vasodilation. The strongest clinical and commercial argument comes from demonstrating improvement in validated erectile function endpoints, objective vascular measures, and 12-month durability that justifies a premium procedure-led intervention.
                    </p>
                </div>

                <div class="three-grid">
                    <div class="endpoint-card">
                        <div class="endpoint-title">IIEF-EF Score</div>
                        <div class="endpoint-text">Core erectile-function benchmark and the primary regulatory-facing measure for functional improvement.</div>
                    </div>
                    <div class="endpoint-card">
                        <div class="endpoint-title">Erection Hardness Score</div>
                        <div class="endpoint-text">Patient-centric rigidity measure that translates more easily into physician and patient communication.</div>
                    </div>
                    <div class="endpoint-card">
                        <div class="endpoint-title">SEP-2 / SEP-3</div>
                        <div class="endpoint-text">Real-world utility measures linked to successful penetration and completion of intercourse.</div>
                    </div>
                    <div class="endpoint-card">
                        <div class="endpoint-title">Penile Doppler PSV</div>
                        <div class="endpoint-text">Objective vascular-flow evidence supporting the restorative mechanism and premium positioning.</div>
                    </div>
                    <div class="endpoint-card">
                        <div class="endpoint-title">12-Month Durability</div>
                        <div class="endpoint-text">The critical bridge between clinical proof and pricing power; durability supports retreatment logic.</div>
                    </div>
                    <div class="endpoint-card">
                        <div class="endpoint-title">Potency / CMC Assays</div>
                        <div class="endpoint-text">Lot-to-lot consistency and potency assurance are essential for FDA, TFDA, and premium-market confidence.</div>
                    </div>
                </div>

                <div class="card" style="margin-top:24px;">
                    <h3 class="list-title">Endpoint-to-Commercial Implication</h3>
                    <div class="table-wrap">
                        <table>
                            <thead>
                                <tr>
                                    <th>Clinical Outcome Measure</th>
                                    <th>Significance</th>
                                    <th>Commercial Implication</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>IIEF-EF Score</td>
                                    <td>Core erectile capacity</td>
                                    <td>Primary regulatory benchmark</td>
                                </tr>
                                <tr>
                                    <td>Erection Hardness Score</td>
                                    <td>Functional rigidity</td>
                                    <td>Patient-centric marketing metric</td>
                                </tr>
                                <tr>
                                    <td>SEP-2 / SEP-3</td>
                                    <td>Successful penetration / completion</td>
                                    <td>Measures real-world utility</td>
                                </tr>
                                <tr>
                                    <td>Penile Doppler PSV</td>
                                    <td>Objective vascular flow</td>
                                    <td>Supports the restorative claim</td>
                                </tr>
                                <tr>
                                    <td>12-Month Durability</td>
                                    <td>Long-term functional persistence</td>
                                    <td>Justifies procedural premium and retreatment model</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- Competition -->
            <section id="competition" class="content-section">
                <div class="header">
                    <h2>Competitive Landscape & Positioning</h2>
                    <p>Where EliteCell Bio must differentiate across the ED treatment escalation pathway.</p>
                </div>

                <div class="card">
                    <p style="margin-bottom: 22px;">
                        EliteCell Bio’s central challenge is not defeating generic sildenafil or tadalafil. The real competitive battle is against second-line injections, shockwave therapy, unregulated regenerative wellness clinics, and surgical implants. A defensible position requires regulated evidence, durability, specialist acceptance, and clear patient-selection logic.
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

                <div class="card">
                    <h3 class="list-title">Competitive Scoring Matrix</h3>
                    <div class="chart-container small">
                        <canvas id="competitiveChart"></canvas>
                    </div>
                    <div class="note">Directional score: 1 = low, 5 = high. EliteCell differentiation is strongest, but evidence maturity must improve.</div>
                </div>
            </section>

            <!-- Roadmap -->
            <section id="roadmap" class="content-section">
                <div class="header">
                    <h2>Regulatory Roadmap & Scenario Risk</h2>
                    <p>Execution depends on sequencing market entry, regulatory engagement, CMC readiness, evidence generation, and downside-risk mitigation.</p>
                </div>

                <div class="two-grid">
                    <div class="card">
                        <h3 class="list-title">Tactical Milestone Roadmap</h3>
                        <div class="timeline">
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <div class="timeline-card">
                                    <div class="timeline-date">2025–2026</div>
                                    <div class="timeline-title">Taiwan Dual Acts Registration</div>
                                    <div class="timeline-text">Secure first-market regulatory path and position Taiwan as the validation hub.</div>
                                </div>
                            </div>

                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <div class="timeline-card">
                                    <div class="timeline-date">2026–2027</div>
                                    <div class="timeline-title">Texas Facility DMF Expansion</div>
                                    <div class="timeline-text">Support global CMC comparability, potency assurance, and premium-market credibility.</div>
                                </div>
                            </div>

                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <div class="timeline-card">
                                    <div class="timeline-date">2027–2029</div>
                                    <div class="timeline-title">Boao Lecheng Entry</div>
                                    <div class="timeline-text">Accelerate China translation through controlled pilot-zone access and local partnership.</div>
                                </div>
                            </div>

                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <div class="timeline-card">
                                    <div class="timeline-date">2028–2030</div>
                                    <div class="timeline-title">U.S. Pre-IND Meeting</div>
                                    <div class="timeline-text">Align with FDA CBER on endpoint, CMC, and RMAT / serious-condition positioning.</div>
                                </div>
                            </div>

                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <div class="timeline-card">
                                    <div class="timeline-date">2029–2032</div>
                                    <div class="timeline-title">12-Month Durability Data</div>
                                    <div class="timeline-text">Justify premium pricing, retreatment assumptions, and specialist-channel adoption.</div>
                                </div>
                            </div>

                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <div class="timeline-card">
                                    <div class="timeline-date">2032–2035</div>
                                    <div class="timeline-title">Expansion Activation</div>
                                    <div class="timeline-text">Launch in Japan, Korea, EU, and other expansion markets using TFDA / FDA evidence base.</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div>
                        <div class="three-grid" style="grid-template-columns: 1fr; gap:18px;">
                            <div class="scenario-card">
                                <div class="scenario-title">Base Case</div>
                                <div class="scenario-value">$25.75 Mn</div>
                                <div class="scenario-text">Measured specialist uptake, staged country launches, and successful premium U.S. entry.</div>
                            </div>

                            <div class="scenario-card">
                                <div class="scenario-title">Launch Delay Case</div>
                                <div class="scenario-value">$22.7 Mn</div>
                                <div class="scenario-text">One-year delay across markets reduces the 2035 revenue position and slows expansion activation.</div>
                            </div>

                            <div class="scenario-card">
                                <div class="scenario-title">Commercial Reach Constraint</div>
                                <div class="scenario-value">$19.3 Mn</div>
                                <div class="scenario-text">Affordability and channel constraints reduce reachable-patient conversion, especially in scale markets.</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card">
                    <h3 class="list-title">Sensitivity Drivers</h3>
                    <div class="chart-container small">
                        <canvas id="sensitivityChart"></canvas>
                    </div>
                    <div class="note">Directional sensitivity score: 1 = low, 5 = very high.</div>
                </div>

                <div class="card">
                    <h3 class="list-title">Risk-Mitigation Matrix</h3>
                    <div class="table-wrap">
                        <table>
                            <thead>
                                <tr>
                                    <th>Risk Factor</th>
                                    <th>Impact on Forecast</th>
                                    <th>Mitigation Strategy</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Weak Durability</td>
                                    <td>Reduces price realization and retreatment logic.</td>
                                    <td>Prioritize 12- and 24-month clinical follow-up.</td>
                                </tr>
                                <tr>
                                    <td>Physician Skepticism</td>
                                    <td>Slows specialist adoption and referral formation.</td>
                                    <td>KOL-led evidence, registry data, and objective vascular endpoints.</td>
                                </tr>
                                <tr>
                                    <td>Regulatory Delay</td>
                                    <td>Pushes revenue curve and delays U.S. inflection.</td>
                                    <td>Early engagement with TFDA, CBER, and country-specific regulators.</td>
                                </tr>
                                <tr>
                                    <td>China Partner Risk</td>
                                    <td>Limits scale execution and hospital access.</td>
                                    <td>Select partner with urology, cell therapy, and Class 3A hospital experience.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="footer-note">
                    The full report extends this cockpit into detailed country forecasts, source-linked assumptions, treatment funnel calculations, clinical endpoint mapping, competitive benchmarking, regulatory strategy, and commercialization recommendations for EliteCell Bio.
                </div>
            </section>
        </div>
    </main>

    <script>
        const BURGUNDY = "#5B0F2E";
        const BURGUNDY_DARK = "#3A071D";
        const BURGUNDY_SOFT = "#8A2E4D";
        const BURGUNDY_MID = "#A94D6A";
        const ROSE = "#D9A8BC";
        const ROSE_DARK = "#B56B87";
        const TEXT = "#334155";
        const GRID = "rgba(148, 163, 184, 0.25)";

        const chartInstances = {};

        function destroyChart(id) {
            if (chartInstances[id]) {
                chartInstances[id].destroy();
                delete chartInstances[id];
            }
        }

        function getCanvas(id) {
            const canvas = document.getElementById(id);
            if (!canvas || typeof Chart === "undefined") return null;
            return canvas.getContext("2d");
        }

        function defaultOptions(yTitle) {
            return {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        grid: { display: false },
                        ticks: { color: "#475569", font: { size: 12 } }
                    },
                    y: {
                        beginAtZero: true,
                        title: {
                            display: !!yTitle,
                            text: yTitle || "",
                            color: BURGUNDY,
                            font: { weight: "bold" }
                        },
                        grid: { color: GRID },
                        ticks: { color: "#475569" }
                    }
                },
                plugins: {
                    legend: {
                        position: "bottom",
                        labels: { color: TEXT, boxWidth: 14, padding: 18 }
                    },
                    tooltip: {
                        mode: "index",
                        intersect: false
                    }
                }
            };
        }

        function initMixChart() {
            const id = "mixChart";
            const ctx = getCanvas(id);
            if (!ctx) return;
            destroyChart(id);

            chartInstances[id] = new Chart(ctx, {
                type: "doughnut",
                data: {
                    labels: ["United States", "China", "Taiwan", "Expansion Markets"],
                    datasets: [{
                        data: [71.1, 9.4, 7.2, 12.2],
                        backgroundColor: [BURGUNDY, BURGUNDY_SOFT, ROSE_DARK, ROSE],
                        borderColor: "#FFFFFF",
                        borderWidth: 3
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    cutout: "62%",
                    plugins: {
                        legend: {
                            position: "bottom",
                            labels: { color: TEXT, boxWidth: 14, padding: 18 }
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.label + ": " + context.parsed.toFixed(1) + "%";
                                }
                            }
                        }
                    }
                }
            });
        }

        function initMarketCaptureChart() {
            const id = "marketCaptureChart";
            const ctx = getCanvas(id);
            if (!ctx) return;
            destroyChart(id);

            chartInstances[id] = new Chart(ctx, {
                type: "bar",
                data: {
                    labels: ["2030", "2035"],
                    datasets: [
                        {
                            label: "Total Regenerative ED Market",
                            data: [3.17, 137.65],
                            backgroundColor: ROSE,
                            borderColor: ROSE_DARK,
                            borderWidth: 1
                        },
                        {
                            label: "EliteCell Revenue",
                            data: [1.14, 25.75],
                            backgroundColor: BURGUNDY,
                            borderColor: BURGUNDY_DARK,
                            borderWidth: 1
                        }
                    ]
                },
                options: defaultOptions("Revenue (US$ Mn)")
            });
        }

        function initCountryFunnelChart() {
            const id = "countryFunnelChart";
            const ctx = getCanvas(id);
            if (!ctx) return;
            destroyChart(id);

            chartInstances[id] = new Chart(ctx, {
                type: "bar",
                data: {
                    labels: ["ED Burden", "Diagnosed", "Treated", "PDE5 Users", "PDE5 Inadequate Responders"],
                    datasets: [
                        {
                            label: "Taiwan",
                            data: [2.66, 0.93, 0.63, 0.52, 0.166],
                            backgroundColor: ROSE,
                            borderColor: ROSE_DARK,
                            borderWidth: 1
                        },
                        {
                            label: "China",
                            data: [125.80, 28.93, 16.78, 13.43, 4.30],
                            backgroundColor: BURGUNDY_SOFT,
                            borderColor: BURGUNDY_DARK,
                            borderWidth: 1
                        },
                        {
                            label: "United States",
                            data: [35.95, 17.98, 13.48, 11.33, 3.62],
                            backgroundColor: BURGUNDY,
                            borderColor: BURGUNDY_DARK,
                            borderWidth: 1
                        }
                    ]
                },
                options: defaultOptions("Patients (Mn)")
            });
        }

        function initRevenueChart() {
            const id = "revenueChart";
            const ctx = getCanvas(id);
            if (!ctx) return;
            destroyChart(id);

            chartInstances[id] = new Chart(ctx, {
                type: "bar",
                data: {
                    labels: ["2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034", "2035"],
                    datasets: [
                        {
                            label: "Taiwan ($Mn)",
                            data: [0, 0, 0.14, 0.31, 0.50, 0.73, 0.98, 1.28, 1.61, 1.73, 1.87],
                            backgroundColor: ROSE,
                            borderColor: ROSE_DARK,
                            borderWidth: 1
                        },
                        {
                            label: "China ($Mn)",
                            data: [0, 0, 0, 0, 0.19, 0.42, 0.70, 1.03, 1.43, 1.89, 2.42],
                            backgroundColor: BURGUNDY_SOFT,
                            borderColor: BURGUNDY_DARK,
                            borderWidth: 1
                        },
                        {
                            label: "Expansion Markets ($Mn)",
                            data: [0, 0, 0, 0, 0, 0, 0, 0.47, 1.28, 2.18, 3.14],
                            backgroundColor: BURGUNDY_MID,
                            borderColor: BURGUNDY_SOFT,
                            borderWidth: 1
                        },
                        {
                            label: "United States ($Mn)",
                            data: [0, 0, 0, 0, 0, 0, 3.02, 6.34, 9.99, 13.97, 18.32],
                            backgroundColor: BURGUNDY,
                            borderColor: BURGUNDY_DARK,
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        x: {
                            stacked: true,
                            grid: { display: false },
                            ticks: { color: "#475569", font: { size: 12 } }
                        },
                        y: {
                            stacked: true,
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: "Revenue (US$ Mn)",
                                color: BURGUNDY,
                                font: { weight: "bold" }
                            },
                            grid: { color: GRID },
                            ticks: {
                                color: "#475569",
                                callback: function(value) { return "$" + value + "M"; }
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
                            labels: { color: TEXT, boxWidth: 14, padding: 18 }
                        }
                    }
                }
            });
        }

        function initCompetitiveChart() {
            const id = "competitiveChart";
            const ctx = getCanvas(id);
            if (!ctx) return;
            destroyChart(id);

            chartInstances[id] = new Chart(ctx, {
                type: "radar",
                data: {
                    labels: ["Efficacy Evidence", "Familiarity", "Differentiation"],
                    datasets: [
                        {
                            label: "PDE5 Inhibitors",
                            data: [5, 5, 2],
                            borderColor: "#94A3B8",
                            backgroundColor: "rgba(148,163,184,0.16)"
                        },
                        {
                            label: "Shockwave",
                            data: [3, 3, 4],
                            borderColor: ROSE_DARK,
                            backgroundColor: "rgba(181,107,135,0.16)"
                        },
                        {
                            label: "PRP Clinics",
                            data: [2, 3, 4],
                            borderColor: BURGUNDY_MID,
                            backgroundColor: "rgba(169,77,106,0.16)"
                        },
                        {
                            label: "EliteCell Injectable",
                            data: [3, 2, 5],
                            borderColor: BURGUNDY,
                            backgroundColor: "rgba(91,15,46,0.18)"
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        r: {
                            min: 0,
                            max: 5,
                            ticks: { stepSize: 1, color: "#64748B" },
                            pointLabels: { color: TEXT, font: { size: 13, weight: "bold" } },
                            grid: { color: GRID },
                            angleLines: { color: GRID }
                        }
                    },
                    plugins: {
                        legend: {
                            position: "bottom",
                            labels: { color: TEXT, boxWidth: 14, padding: 18 }
                        }
                    }
                }
            });
        }

        function initSensitivityChart() {
            const id = "sensitivityChart";
            const ctx = getCanvas(id);
            if (!ctx) return;
            destroyChart(id);

            chartInstances[id] = new Chart(ctx, {
                type: "bar",
                data: {
                    labels: ["Adoption Rate", "Commercial Reach", "Durability", "Pricing Power", "Launch Timing", "China Partner Risk"],
                    datasets: [{
                        label: "Sensitivity Score",
                        data: [5, 5, 4, 4, 3, 3],
                        backgroundColor: [BURGUNDY, BURGUNDY, BURGUNDY_SOFT, BURGUNDY_SOFT, ROSE_DARK, ROSE_DARK],
                        borderColor: BURGUNDY_DARK,
                        borderWidth: 1
                    }]
                },
                options: {
                    indexAxis: "y",
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        x: {
                            beginAtZero: true,
                            max: 5,
                            grid: { color: GRID },
                            ticks: { color: "#475569", stepSize: 1 }
                        },
                        y: {
                            grid: { display: false },
                            ticks: { color: "#475569" }
                        }
                    },
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return "Sensitivity score: " + context.parsed.x + " / 5";
                                }
                            }
                        }
                    }
                }
            });
        }

        function initChartsForSection(sectionId) {
            setTimeout(function() {
                if (sectionId === "snapshot") {
                    initMixChart();
                    initMarketCaptureChart();
                }
                if (sectionId === "country") {
                    initCountryFunnelChart();
                }
                if (sectionId === "forecast") {
                    initRevenueChart();
                }
                if (sectionId === "competition") {
                    initCompetitiveChart();
                }
                if (sectionId === "roadmap") {
                    initSensitivityChart();
                }
            }, 120);
        }

        function navigate(sectionId) {
            document.querySelectorAll(".nav button").forEach(function(btn) {
                btn.classList.remove("nav-active");
            });

            const activeButton = document.getElementById("nav-" + sectionId);
            if (activeButton) activeButton.classList.add("nav-active");

            document.querySelectorAll(".content-section").forEach(function(section) {
                section.classList.remove("active");
            });

            const activeSection = document.getElementById(sectionId);
            if (activeSection) activeSection.classList.add("active");

            initChartsForSection(sectionId);
        }

        window.addEventListener("load", function() {
            initChartsForSection("executive");
        });
    </script>
</body>
</html>
"""

components.html(DASHBOARD_HTML, height=1100, scrolling=True)
