import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(160deg, #0F0A1E 0%, #1A1145 40%, #2D1B69 100%) !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background: rgba(255,255,255,0.06) !important;
                    backdrop-filter: blur(16px) !important;
                    -webkit-backdrop-filter: blur(16px) !important;
                    padding: 2.5rem !important;
                    border-radius: 2rem !important;
                    border: 1px solid rgba(255,255,255,0.1) !important;
                    box-shadow: 0 8px 32px rgba(0,0,0,0.3) !important;
                    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
                    }

                .stApp div[data-testid="stColumn"]:hover {
                    transform: translateY(-4px) !important;
                    box-shadow: 0 16px 48px rgba(124,58,237,0.25) !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp,
                [data-testid="stAppViewContainer"],
                [data-testid="stHeader"] {
                    background:
                        radial-gradient(circle at 8% 0%, rgba(242, 127, 89, 0.16), transparent 28rem),
                        radial-gradient(circle at 100% 12%, rgba(24, 143, 143, 0.18), transparent 26rem),
                        linear-gradient(135deg, #11191c 0%, #172326 52%, #0d1417 100%) !important;
                }

                [data-testid="stMainBlockContainer"] {
                    background: transparent !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():

    st.markdown("""
        <style>
        @import url('https://api.fontshare.com/v2/css?f[]=satoshi@400,500,600,700,900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                max-width: 1180px !important;
                padding-top: 2rem !important;
                padding-bottom: 3rem !important;
            }

            h1 {
                font-family: 'Satoshi', sans-serif !important;
                font-weight: 900 !important;
                font-size: clamp(2rem, 4vw, 3.5rem) !important;
                line-height: 1.05 !important;
                letter-spacing: -0.04em !important;
            }
                

            h2 {
                font-family: 'Satoshi', sans-serif !important;
                font-weight: 700 !important;
                font-size: clamp(1.55rem, 3vw, 2.2rem) !important;
                line-height: 1.05 !important;
                letter-spacing: -0.035em !important;
            }
                
            h3, h4 {
                font-family: 'Satoshi', sans-serif !important;
                font-weight: 700 !important;
            }

            p, label, span, li, div {
                font-family: 'Satoshi', sans-serif;
                color: #d7e0df;
            }

            h1, h2, h3, h4 {
                color: #f3f7f5 !important;
            }

            label, [data-testid="stWidgetLabel"] p,
            [data-testid="stWidgetLabel"] label {
                color: #d7e0df !important;
                font-weight: 600 !important;
            }

            [data-baseweb="input"] input,
            [data-baseweb="textarea"] textarea {
                color: #f3f7f5 !important;
                caret-color: #55c6bd !important;
            }

            [data-baseweb="select"] * {
                color: #f3f7f5 !important;
            }

            button {
                border-radius: 10px !important;
                background: #188f8f !important;
                color: white !important;
                min-height: 2.75rem !important;
                border: 1px solid #188f8f !important;
                font-weight: 600 !important;
                box-shadow: 0 5px 14px rgba(24, 143, 143, 0.16) !important;
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
                }

            button[kind="secondary"]{
                background: rgba(255, 255, 255, 0.04) !important;
                color: #d7e0df !important;
                border: 1px solid rgba(215, 224, 223, 0.24) !important;
                box-shadow: none !important;
                }

            button[kind="tertiary"]{
                background: transparent !important;
                color: #aab8b7 !important;
                border: 1px solid rgba(215, 224, 223, 0.2) !important;
                box-shadow: none !important;
                }

            button:hover {
                transform: translateY(-1px) !important;
                box-shadow: 0 8px 18px rgba(24, 143, 143, 0.2) !important;
            }

            button[kind="secondary"]:hover, button[kind="tertiary"]:hover {
                background: rgba(255, 255, 255, 0.10) !important;
                box-shadow: none !important;
            }

            /* ── Dark-theme hover overrides for all Streamlit elements ── */

            /* Selectbox / multiselect dropdown items */
            [data-baseweb="menu"] li:hover,
            [data-baseweb="menu"] [role="option"]:hover,
            [data-baseweb="popover"] li:hover {
                background: rgba(255, 255, 255, 0.10) !important;
            }

            /* Selectbox container hover */
            [data-baseweb="select"] > div:hover {
                border-color: #188f8f !important;
            }

            /* Toolbar that appears on hover over elements */
            [data-testid="stElementToolbar"] {
                background: rgba(23, 35, 38, 0.95) !important;
                border: 1px solid rgba(215, 224, 223, 0.14) !important;
            }

            [data-testid="stElementToolbar"] button {
                background: transparent !important;
                box-shadow: none !important;
                border: none !important;
            }

            [data-testid="stElementToolbar"] button:hover {
                background: rgba(255, 255, 255, 0.10) !important;
            }

            /* Dataframe cells hover */
            [data-testid="stDataFrame"] td:hover,
            [data-testid="stDataFrame"] th:hover {
                background: rgba(255, 255, 255, 0.06) !important;
            }

            /* Expander header hover */
            [data-testid="stExpander"] summary:hover {
                background: rgba(255, 255, 255, 0.06) !important;
            }

            /* Tab hover */
            [data-baseweb="tab"]:hover {
                background: rgba(255, 255, 255, 0.06) !important;
            }

            /* Links */
            a:hover {
                color: #55c6bd !important;
            }

            /* File uploader hover */
            [data-testid="stFileUploader"] section:hover {
                border-color: rgba(85, 198, 189, 0.4) !important;
                background: rgba(255, 255, 255, 0.04) !important;
            }

            /* Camera input hover */
            [data-testid="stCameraInput"] > div:hover {
                border-color: rgba(85, 198, 189, 0.4) !important;
            }

            /* Toast / notification */
            [data-testid="stToast"] {
                background: rgba(23, 35, 38, 0.96) !important;
                border: 1px solid rgba(215, 224, 223, 0.14) !important;
                color: #d7e0df !important;
            }

            /* Dialog / modal backdrop */
            [data-testid="stModal"] > div {
                background: rgba(15, 20, 23, 0.85) !important;
            }

            [data-testid="stModal"] [data-testid="stModalBody"] {
                background: #172326 !important;
            }

            /* Popover menus */
            [data-baseweb="popover"] > div {
                background: #1f3033 !important;
                border: 1px solid rgba(215, 224, 223, 0.14) !important;
            }

            /* Tooltip */
            [data-baseweb="tooltip"] > div {
                background: #1f3033 !important;
                color: #d7e0df !important;
            }

            /* General interactive row hover */
            .stApp tr:hover td {
                background: rgba(255, 255, 255, 0.04) !important;
            }

            input, textarea, [data-baseweb="select"] > div {
                border-radius: 10px !important;
                border-color: rgba(215, 224, 223, 0.2) !important;
                background: rgba(255, 255, 255, 0.06) !important;
                color: #f3f7f5 !important;
                transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
            }

            input:focus, textarea:focus {
                border-color: #188f8f !important;
                box-shadow: 0 0 0 3px rgba(24, 143, 143, 0.12) !important;
            }

            input::placeholder, textarea::placeholder {
                color: #80908f !important;
            }

            .stDivider {
                border-color: rgba(215, 224, 223, 0.16) !important;
            }

            [data-testid="stMetric"] {
                background: rgba(255, 255, 255, 0.055);
                border: 1px solid rgba(215, 224, 223, 0.14);
                border-radius: 12px;
                padding: 1rem 1.1rem;
            }

            [data-testid="stMetricLabel"] {
                color: #91a2a1 !important;
            }

            [data-testid="stMetricValue"] {
                color: #f3f7f5 !important;
            }

            [data-testid="stDataFrame"] {
                border: 1px solid rgba(215, 224, 223, 0.14);
                border-radius: 12px;
                overflow: hidden;
            }

            .portal-kicker, .portal-section-label {
                color: #55c6bd;
                font-size: 0.72rem;
                font-weight: 700;
                letter-spacing: 0.14em;
                margin-bottom: 0.35rem;
                text-transform: uppercase;
            }

            .portal-title {
                color: #f3f7f5 !important;
                font-family: 'Satoshi', sans-serif !important;
                margin: 0 !important;
            }

            .portal-subtitle {
                color: #9aabaa;
                font-size: 0.95rem;
                margin: 0.35rem 0 0;
            }

            .portal-rule {
                border-top: 1px solid rgba(215, 224, 223, 0.14);
                margin: 1.25rem 0;
            }

            [data-testid="stAlert"] {
                background: rgba(255, 255, 255, 0.06) !important;
                border: 1px solid rgba(215, 224, 223, 0.16) !important;
                color: #d7e0df !important;
            }

            @keyframes fadeInUp {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }

            @media (max-width: 700px) {
                .block-container {
                    padding: 1rem 0.9rem 2rem !important;
                }
                button {
                    min-height: 2.6rem !important;
                }
            }

            .block-container > div {
                animation: fadeInUp 0.5s ease-out;
            }

        </style>  

                """
            ,unsafe_allow_html=True)
