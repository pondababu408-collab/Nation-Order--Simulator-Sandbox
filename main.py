import streamlit as st
import random
import datetime

# 1. Force strict dark mobile-first viewport parameters
st.set_page_config(page_title="World Order Sandbox", page_icon="🌐", layout="centered")

# 🎨 Inject custom high-fidelity dark matrix styles matching layout screenshots
st.markdown("""
    <style>
    /* Wipe default Streamlit branding layout out of frame */
    [data-testid="stHeader"], [data-testid="stSidebar"], .stDeployButton, footer {
        display: none !important;
    }
    .stApp {
        background-color: #000000 !important;
        color: #E2E8F0 !important;
        font-family: sans-serif;
    }
    
    /* Notification Bar */
    .top-notification-banner {
        border: 1px solid #00FF66;
        background-color: rgba(0, 255, 102, 0.02);
        border-radius: 8px;
        padding: 12px;
        text-align: center;
        font-weight: 600;
        font-size: 13px;
        color: #00FF66;
        margin-bottom: 20px;
    }
    
    /* Operations Menu Grid Layout Systems */
    .game-menu-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
        margin-bottom: 20px;
    }
    .menu-node-card {
        background-color: #050507;
        border: 1px solid #141419;
        border-radius: 8px;
        padding: 18px 10px;
        text-align: center;
    }
    
    /* Sub-Menu Grid Architecture */
    .sub-grid-node-card {
        background-color: #070709;
        border: 1px solid #141419;
        border-radius: 6px;
        padding: 14px;
        text-align: left;
        margin-bottom: 12px;
    }
    .node-header-row {
        font-size: 13px;
        font-weight: 600;
        color: #FFFFFF;
        margin-bottom: 6px;
    }
    .node-body-description {
        font-size: 11px;
        color: #718096;
        line-height: 1.3;
    }
    
    /* banking and conflict HUD component display blocks */
    .hud-display-card {
        background-color: #070709;
        border: 1px solid #141419;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
    }
    .bank-balance-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        background-color: #020204;
        border: 1px solid #101014;
        border-radius: 6px;
        padding: 12px;
        margin-bottom: 12px;
        text-align: center;
    }
    .balance-label { font-size: 10px; color: #718096; text-transform: uppercase; }
    .balance-value { font-size: 14px; font-weight: bold; color: #FFFFFF; }
    
    /* Quote Header Container */
    .quote-box-layout {
        text-align: center;
        font-size: 11px;
        color: #718096;
        font-style: italic;
        line-height: 1.4;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 🏛️ GEOPOLITICAL COMPREHENSIVE REGISTRY (193 NATIONS)
# ----------------------------------------------------
ALL_COUNTRIES = [
    "Canada", "Mexico", "Spain", "France", "Germany", "United Kingdom", "United States of America",
    "Argentina", "Brazil", "Chile", "Colombia", "Venezuela", "China", "Japan", "India", "Russia",
    "Australia", "South Africa", "Egypt", "Italy", "Portugal", "Andorra", "Malta", "Ukraine"
] # Trimmed layout sample wrapper containing core target indicators from your screen logs

# ----------------------------------------------------
# 💾 PERSISTENT ENGINE STATE REGISTERS (CACHE)
# ----------------------------------------------------
if "game_initialized" not in st.session_state: st.session_state.game_initialized = False
if "player_country" not in st.session_state: st.session_state.player_country = ""
if "player_party" not in st.session_state: st.session_state.player_party = ""
if "active_view_state" not in st.session_state: st.session_state.active_view_state = "HOME"
if "sub_hub_view" not in st.session_state: st.session_state.sub_hub_view = "MENU"

# Unscripted Simulation Ticker Variables
if "gold_balance" not in st.session_state: st.session_state.gold_balance = 25000.0
if "unrest" not in st.session_state: st.session_state.unrest = 20.0
if "sol" not in st.session_state: st.session_state.sol = 50.0
if "currency_label" not in st.session_state: st.session_state.currency_label = "PTS"
if "price_index" not in st.session_state: st.session_state.price_index = 1.0

# Bank Account Registers
if "bank_transaction_acc" not in st.session_state: st.session_state.bank_transaction_acc = 2989
if "bank_time_deposit" not in st.session_state: st.session_state.bank_time_deposit = 11

# University Discipline Degrees Scores
if "business_admin" not in st.session_state: st.session_state.business_admin = 15.0
if "political_science" not in st.session_state: st.session_state.political_science = 10.0
if "economics" not in st.session_state: st.session_state.economics = 5.0
if "military_academy" not in st.session_state: st.session_state.military_academy = 45.0

# Learned Knowledge Traits Tree Status Registers
if "traits" not in st.session_state:
    st.session_state.traits = {
        "Young_Entrepreneur": False, "Young_Idealistic": False,
        "Young_Worker": False, "Military_Strategist": False, "Minion_Devil": False
    }

# Dynamic Combat Metrics Registers
if "attacker_progress" not in st.session_state: st.session_state.attacker_progress = 29
if "defender_progress" not in st.session_state: st.session_state.defender_progress = 71
if "casualty_dead" not in st.session_state: st.session_state.casualty_dead = 0
if "casualty_injured" not in st.session_state: st.session_state.casualty_injured = 0

# Joined & Managed Organizations Registry
if "joined_orgs" not in st.session_state:
    st.session_state.joined_orgs = []

# ----------------------------------------------------
# 🎬 SETUP STAGE: COUNTRY & POLITICAL ONBOARDING GATES
# ----------------------------------------------------
if not st.session_state.game_initialized:
    st.title("🌐 World Order Simulator")
    st.subheader("Initialize Your Sovereign Sandbox State")
    st.markdown('<div class="hud-display-card">', unsafe_allow_html=True)
    
    country_choice = st.selectbox("Select your starting geographic country node:", ALL_COUNTRIES, index=ALL_COUNTRIES.index("Spain"))
    party_path = st.radio("Select your path into the state house:", ["Create a brand new political party", "Join an existing ideological AI faction"])
    party_title = st.text_input("Enter your faction name:", placeholder="e.g., Technocratic Freedom Front")
    
    st.write("---")
    if st.button("🚀 Launch Sovereign Simulation Engine", use_container_width=True):
        if country_choice and party_title:
            st.session_state.player_country = country_choice
            st.session_state.player_party = party_title
            st.session_state.game_initialized = True
            st.balloons()
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# 🎮 CORE GAME STAGE: ACTIVE RUNTIME VIEW CONTROLLER
# ----------------------------------------------------
else:
    st.markdown(f'<div class="top-notification-banner">👑 Sovereign Territory: {st.session_state.player_country} | Active Party: {st.session_state.player_party}</div>', unsafe_allow_html=True)

    # --- RADAR TAB A: CHARACTER HOME STATE ---
    if st.session_state.active_view_state == "HOME":
        st.subheader("👤 Character Dashboard Profile")
        
        st.markdown('<div class="hud-display-card">', unsafe_allow_html=True)
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.write(f"🪙 Treasury Balance: **{st.session_state.gold_balance:,.2f} Gold**")
            st.write(f"📉 Domestic Unrest: **{st.session_state.unrest:.1f}%**")
        with col_c2:
            st.write(f"📊 Market Price Index: **{st.session_state.price_index:.2f}x**")
            st.write(f"🛒 Standard of Living: **{st.session_state.sol:.1f}/100**")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="hud-display-card">', unsafe_allow_html=True)
        st.write("##### ⚡ Volatile Real-Time Ticker Advancements")
        if st.button("Advance Live Simulation Pulse", use_container_width=True):
            st.session_state.unrest = max(1.0, min(100.0, st.session_state.unrest + random.uniform(-8, 12)))
            st.session_state.price_index = max(0.5, st.session_state.price_index + random.uniform(-0.1, 0.4))
            
            # --- CRITICAL RE-DENOMINATION LOOP TRIGGER ---
            if st.session_state.price_index >= 2.5:
                st.session_state.currency_label = "NVE1"
                st.session_state.price_index *= 0.01
                st.warning("🚨 Hyperinflation threshold breached! AI Central Bank executed full redenomination.")
            
            # --- MONDAY 2% UNIVERSITY SKILL POINTS DECAY LOOP ---
            st.session_state.business_admin *= 0.98
            st.session_state.political_science *= 0.98
            st.session_state.economics *= 0.98
            st.session_state.military_academy *= 0.98
            
            # --- SUNDAY SOCIAL CAPACITY POP CONSUMPTION Ticks ---
            if st.session_state.unrest > 55.0: st.session_state.sol = max(1.0, st.session_state.sol - 3)
            else: st.session_state.sol = min(100.0, st.session_state.sol + 2)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # --- RADAR TAB B: CONFLICT & THEATER INTERFACE ---
    elif st.session_state.active_view_state == "CONFLICT":
        st.subheader("⚔️ Conflict Standoff Monitor")
        st.markdown('<div class="quote-box-layout">"Mankind must put an end to war before war puts an end to mankind."</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="hud-display-card">', unsafe_allow_html=True)
        st.write("##### Live Battlefront Tactical Alignment")
