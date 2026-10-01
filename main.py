import streamlit as st
import random

# Enforce strict dark mobile viewport settings
st.set_page_config(page_title="World Order Sandbox", page_icon="🌐", layout="centered")

# 🎨 Custom high-fidelity CSS engine to match your exact dark matrix layouts
st.markdown("""
    <style>
    /* Completely eliminate standard Streamlit layout padding and clutter elements */
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
        padding-bottom: 40px !important;
        padding-left: 14px !important;
        padding-right: 14px !important;
        max-width: 460px !important;
    }
    
    /* Top Context Banner Strip */
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
    }
    
    /* Dynamic Notification Pill Wrapper */
    .notifications-pill-box {
        border: 1px solid #1A1A24;
        background-color: #050507;
        border-radius: 6px;
        padding: 10px;
        text-align: center;
        font-size: 12px;
        color: #00FF66;
        font-weight: bold;
        margin-bottom: 14px;
    }
    
    /* Section Separation Titles */
    .section-header-title {
        font-size: 14px;
        font-weight: bold;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-top: 22px;
        margin-bottom: 10px;
        border-left: 3px solid #00FF66;
        padding-left: 8px;
    }
    
    /* Complete 16-Option Operational Hub Grid Layout System */
    .master-hub-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 8px;
        margin-bottom: 16px;
    }
    .grid-node-item {
        background-color: #070709;
        border: 1px solid #141419;
        border-radius: 6px;
        padding: 10px 4px;
        text-align: center;
    }
    .grid-node-icon { font-size: 18px; margin-bottom: 2px; }
    .grid-node-label { font-size: 9px; color: #A0AEC0; font-weight: 500; }
    
    /* Container Display Blocks */
    .hud-display-card {
        background-color: #070709;
        border: 1px solid #141419;
        border-radius: 8px;
        padding: 14px;
        margin-bottom: 12px;
    }
    .hud-sub-title {
        font-size: 13px;
        font-weight: bold;
        color: #FFFFFF;
        margin-bottom: 8px;
    }
    .quote-box {
        text-align: center;
        font-size: 10px;
        color: #718096;
        font-style: italic;
        margin-bottom: 12px;
    }
    
    /* Metrics Flex Layout Rows */
    .metric-data-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 12px;
        padding: 5px 0;
        border-bottom: 1px solid #0d0d12;
    }
    .metric-label-tag { color: #8E9CAE; }
    .metric-value-tag { color: #FFFFFF; font-weight: bold; }
    
    /* Custom Stylings for Interactive Buttons */
    div.stButton > button {
        background-color: #0F0F14 !important;
        color: #FFFFFF !important;
        border: 1px solid #1A1A24 !important;
        border-radius: 6px !important;
        padding: 10px !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        width: 100% !important;
    }
    div.stButton > button:hover {
        border-color: #00FF66 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 💾 RUNTIME DATA MEMORY REGISTERS
# ----------------------------------------------------
if "gold" not in st.session_state: st.session_state.gold = 25000.0
if "unrest" not in st.session_state: st.session_state.unrest = 20.9
if "sol" not in st.session_state: st.session_state.sol = 52.0
if "price_index" not in st.session_state: st.session_state.price_index = 1.09
if "bank_tx" not in st.session_state: st.session_state.bank_tx = 2989
if "bank_dep" not in st.session_state: st.session_state.bank_dep = 11
if "atk_progress" not in st.session_state: st.session_state.atk_progress = 29
if "def_progress" not in st.session_state: st.session_state.def_progress = 71

# ----------------------------------------------------
# 📱 UNIFIED ALL-IN-ONE STRATEGY SCREEN
# ----------------------------------------------------

# Top Context Banner & Notifications Pill
st.markdown('<div class="top-status-strip">👑 Sovereign Territory: Spain | Active Party: Dj</div>', unsafe_allow_html=True)
st.markdown('<div class="notifications-pill-box">🔔 Notifications Area Enabled</div>', unsafe_allow_html=True)

# --- 1. CORE CHARACTER STATUS LAYER ---
st.markdown('<div class="game-hud-block hud-display-card">', unsafe_allow_html=True)
st.markdown('<div class="hud-sub-title">👤 Character Dashboard Stats</div>', unsafe_allow_html=True)
st.markdown(f"""
    <div class="metric-data-row"><span class="metric-label-tag">🪙 Treasury Balance</span><span class="metric-value-tag">{st.session_state.gold:,.2f} Gold</span></div>
    <div class="metric-data-row"><span class="metric-label-tag">📉 Domestic Unrest</span><span class="metric-value-tag">{st.session_state.unrest:.1f}%</span></div>
    <div class="metric-data-row"><span class="metric-label-tag">📊 Market Price Index</span><span class="metric-value-tag">{st.session_state.price_index:.2f}x</span></div>
    <div class="metric-data-row"><span class="metric-label-tag">🛒 Standard of Living</span><span class="metric-value-tag">{st.session_state.sol:.1f}/100</span></div>
""", unsafe_allow_html=True)
if st.button("⚡ Advance Real-Time Simulation Heartbeat", key="pulse_tick"):
    st.session_state.unrest = max(1.0, min(100.0, st.session_state.unrest + random.uniform(-5, 8)))
    st.session_state.price_index = max(0.5, st.session_state.price_index + random.uniform(-0.04, 0.12))
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# --- 2. COMPLETE 16-OPTION NAVIGATION HUB GRID (From your layout screenshots) ---
st.markdown('<div class="section-header-title">🛠️ Master Operations Hub</div>', unsafe_allow_html=True)

st.markdown("""
<div class="master-hub-grid">
    <div class="grid-node-item"><div class="grid-node-icon">💵</div><div class="grid-node-label">Economy</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">🏛️</div><div class="grid-node-label">Organizations</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">🔥</div><div class="grid-node-label">Conflict</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">👤</div><div class="grid-node-label">Personal</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">✨</div><div class="grid-node-label">Knowledge</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">🎓</div><div class="grid-node-label">University</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">🏆</div><div class="grid-node-label">Ranking</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">🌍</div><div class="grid-node-label">Supranational</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">✉️</div><div class="grid-node-label">Messages</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">👑</div><div class="grid-node-label">Premium</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">🏪</div><div class="grid-node-label">Store</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">📺</div><div class="grid-node-label">Ads</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">ℹ️</div><div class="grid-node-label">Tutorial</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">📜</div><div class="grid-node-label">Rules</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">👥</div><div class="grid-node-label">Society</div></div>
    <div class="grid-node-item"><div class="grid-node-icon">⚙️</div><div class="grid-node-label">Settings</div></div>
</div>
""", unsafe_allow_html=True)

# --- 3. HIGH-FIDELITY ONLINE BANK MANAGEMENT DESK ---
st.markdown('<div class="section-header-title">🏦 Online Banking Module</div>', unsafe_allow_html=True)
st.markdown('<div class="quote-box">"I believe that banking institutions are more dangerous than standing armies."<br>— Thomas Jefferson —</div>', unsafe_allow_html=True)

st.markdown(f"""
    <div class="hud-display-card">
        <div class="hud-sub-title">💼 Domestic Capital Bank (Active Branch)</div>
        <div class="metric-data-row"><span class="metric-label-tag">Account Holder Profile</span><span class="metric-value-tag">Master Sandbox Ruler</span></div>
        <div class="metric-data-row"><span class="metric-label-tag">Jurisdiction Status</span><span class="metric-value-tag" style="color:#00FF66;">ACTIVE LEGAL</span></div>
        <div class="bank-balance-grid">
            <div>
                <div class="balance-label">Transaction Acc</div>
                <div class="balance-value" style="font-size:12px;">{st.session_state.bank_tx} PTS</div>
            </div>
            <div>
                <div class="balance-label">Time Deposit</div>
                <div class="balance-value" style="font-size:12px;">{st.session_state.bank_dep} PTS</div>
            </div>
        </div>
        <div style="font-size: 9px; color: #4A5568; text-align: center; font-family: monospace;">ES51 1030 6000 0050 0060 9069</div>
    </div>
""", unsafe_allow_html=True)

col_tx1, col_tx2 = st.columns(2)
with col_tx1:
