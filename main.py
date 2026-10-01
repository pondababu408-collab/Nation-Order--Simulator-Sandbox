import streamlit as st
import random

# Enforce strict dark mobile layout settings
st.set_page_config(page_title="World Order Sandbox", page_icon="🌐", layout="centered")

# 🎨 Inject layout styles to completely remove standard text sizes and empty margins
st.markdown("""
    <style>
    /* Wipe default Streamlit margins, padding, and text wrappers out of frame */
    [data-testid="stHeader"], [data-testid="stSidebar"], .stDeployButton, footer {
        display: none !important;
    }
    .stApp {
        background-color: #000000 !important;
        color: #FFFFFF !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .block-container {
        padding-top: 10px !important;
        padding-bottom: 80px !important;
        padding-left: 12px !important;
        padding-right: 12px !important;
        max-width: 480px !important;
    }
    
    /* Top Header Status Banner */
    .top-status-strip {
        border: 1px solid #10B981;
        background: #03150d;
        border-radius: 6px;
        padding: 8px;
        text-align: center;
        font-weight: 600;
        font-size: 11px;
        color: #10B981;
        margin-bottom: 16px;
        letter-spacing: 0.3px;
    }
    
    /* Sleek Game Card Wrapper Grid Container Blocks */
    .game-hud-block {
        background-color: #070709;
        border: 1px solid #141419;
        border-radius: 8px;
        padding: 14px;
        margin-bottom: 12px;
    }
    .hud-title-text {
        font-size: 15px;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 12px;
        letter-spacing: -0.2px;
    }
    
    /* Metrics Flex Grid Rows */
    .metric-data-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 13px;
        padding: 6px 0;
        border-bottom: 1px solid #0d0d12;
    }
    .metric-label-tag { color: #8E9CAE; font-weight: 500; }
    .metric-value-tag { color: #FFFFFF; font-weight: 700; font-family: monospace; }
    
    /* Custom Stylings for Streamlit Buttons to act as sleek cards */
    div.stButton > button {
        background-color: #070709 !important;
        color: #8E9CAE !important;
        border: 1px solid #141419 !important;
        border-radius: 8px !important;
        padding: 14px !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        width: 100% !important;
        text-align: left !important;
    }
    div.stButton > button:hover {
        border-color: #2D3748 !important;
        color: #FFFFFF !important;
    }
    
    /* Grid Submodules Model Matrix */
    .operations-sub-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
        margin-bottom: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 💾 PERSISTENT ENGINE INITIALIZATION
# ----------------------------------------------------
if "game_initialized" not in st.session_state: st.session_state.game_initialized = False
if "player_country" not in st.session_state: st.session_state.player_country = "Spain"
if "player_party" not in st.session_state: st.session_state.player_party = "Dj"
if "active_view_state" not in st.session_state: st.session_state.active_view_state = "HOME"
if "sub_hub_view" not in st.session_state: st.session_state.sub_hub_view = "MENU"

# Engine Parameters
if "gold_balance" not in st.session_state: st.session_state.gold_balance = 25000.0
if "unrest" not in st.session_state: st.session_state.unrest = 20.9
if "sol" not in st.session_state: st.session_state.sol = 52.0
if "price_index" not in st.session_state: st.session_state.price_index = 1.06
if "currency_label" not in st.session_state: st.session_state.currency_label = "Gold"

# Bank Account Parameters
if "bank_transaction_acc" not in st.session_state: st.session_state.bank_transaction_acc = 2989
if "bank_time_deposit" not in st.session_state: st.session_state.bank_time_deposit = 11

# University Parameters
if "business_admin" not in st.session_state: st.session_state.business_admin = 15.0
if "political_science" not in st.session_state: st.session_state.political_science = 10.0
if "economics" not in st.session_state: st.session_state.economics = 5.0

# ----------------------------------------------------
# 🎬 INTERACTIVE SIMULATION VIEWS LAYOUTS
# ----------------------------------------------------
# Displays identical text, layout headers, and colors matching your design images

st.markdown(f'<div class="top-status-strip">👑 Sovereign Territory: {st.session_state.player_country} | Active Party: {st.session_state.player_party}</div>', unsafe_allow_html=True)

# --- PANEL VIEW A: DYNAMIC PROFILE VIEWS ---
if st.session_state.active_view_state == "HOME":
    st.markdown('<div class="game-hud-block">', unsafe_allow_html=True)
    st.markdown('<div class="hud-title-text">👤 Character Dashboard Profile</div>', unsafe_allow_html=True)
    
    # Custom stacked layout lines mimicking the screens
    st.markdown(f"""
        <div class="metric-data-row"><span class="metric-label-tag">🪙 Treasury Balance</span><span class="metric-value-tag">{st.session_state.gold_balance:,.2f} {st.session_state.currency_label}</span></div>
        <div class="metric-data-row"><span class="metric-label-tag">📉 Domestic Unrest</span><span class="metric-value-tag">{st.session_state.unrest:.1f}%</span></div>
        <div class="metric-data-row"><span class="metric-label-tag">📊 Market Price Index</span><span class="metric-value-tag">{st.session_state.price_index:.2f}x</span></div>
        <div class="metric-data-row"><span class="metric-label-tag">🛒 Standard of Living</span><span class="metric-value-tag">{st.session_state.sol:.1f}/100</span></div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="game-hud-block">', unsafe_allow_html=True)
    st.markdown('<div class="hud-title-text">⚡ Volatile Real-Time Ticker Advancements</div>', unsafe_allow_html=True)
    if st.button("Advance Live Simulation Pulse", key="ticker_pulse"):
        st.session_state.unrest = max(1.0, min(100.0, st.session_state.unrest + random.uniform(-6, 9)))
        st.session_state.price_index = max(0.5, st.session_state.price_index + random.uniform(-0.05, 0.15))
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANEL VIEW B: INTERACTIVE GRID MODULES HUB ---
elif st.session_state.active_view_state == "HUB":
    if st.session_state.sub_hub_view == "MENU":
        st.markdown('<div class="hud-title-text" style="padding-left:4px;">🛠️ Operations Hub</div>', unsafe_allow_html=True)
        
        # Grid blocks styled cleanly as navigation nodes
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            if st.button("💵 Economy Matrix"): st.session_state.sub_hub_view = "ECONOMY"; st.rerun()
            if st.button("✨ Knowledge Tree"): st.session_state.sub_hub_view = "KNOWLEDGE"; st.rerun()
        with col_g2:
            if st.button("🏛️ Organizations Desk"): st.session_state.sub_hub_view = "ORGS"; st.rerun()
            if st.button("🎓 University Faculty"): st.session_state.sub_hub_view = "UNIVERSITY"; st.rerun()
            
    elif st.session_state.sub_hub_view == "ECONOMY":
        st.markdown('<div class="hud-title-text">🏛️ Economy Dashboard</div>', unsafe_allow_html=True)
        if st.button("← Back to Operations Hub"): st.session_state.sub_hub_view = "MENU"; st.rerun()
        st.write("---")
        
        col_e1, col_e2 = st.columns(2)
        with col_e1:
            if st.button("🏛️ Online Banking"): st.session_state.sub_hub_view = "BANK_DETAILS"; st.rerun()
            st.button("📜 Bilateral Debt")
        with col_e2:
            st.button("📈 Stocks")
            st.button("🛒 B2C Market")
            
    elif st.session_state.sub_hub_view == "BANK_DETAILS":
        st.markdown('<div class="hud-title-text">🏦 Online Banking Terminal</div>', unsafe_allow_html=True)
        if st.button("← Back to Economy Desk"): st.session_state.sub_hub_view = "ECONOMY"; st.rerun()
        
        st.markdown(f"""
            <div class="game-hud-block">
                <div style="font-weight:bold; font-size:13px; margin-bottom:8px;">🟢 Domestic Capital Bank Node</div>
                <div class="bank-balance-grid">
                    <div>
                        <div class="balance-label">Transaction Account</div>
                        <div class="balance-value">{st.session_state.bank_transaction_acc} {st.session_state.currency_label}</div>
                    </div>
                    <div>
                        <div class="balance-label">Time Deposit</div>
                        <div class="balance-value">{st.session_state.bank_time_deposit} {st.session_state.currency_label}</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        transfer_amt = st.number_input("Amount to transfer to deposit ledger:", min_value=0, max_value=st.session_state.bank_transaction_acc, value=0)
        if st.button("Confirm Investment Loop"):
            if transfer_amt > 0:
                st.session_state.bank_transaction_acc -= transfer_amt
                st.session_state.bank_time_deposit += transfer_amt
                st.success("Transferred capital assets successfully.")
                st.rerun()

    elif st.session_state.sub_hub_view == "UNIVERSITY":
        st.markdown('<div class="hud-title-text">🎓 University Faculty Matrix</div>', unsafe_allow_html=True)
        if st.button("← Back to Operations Hub"): st.session_state.sub_hub_view = "MENU"; st.rerun()
        
        col_u1, col_u2 = st.columns(2)
        with col_u1:
            st.write(f"💼 Business Admin: **{st.session_state.business_admin:.1f} pts**")
