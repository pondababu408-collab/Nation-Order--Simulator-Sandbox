
import streamlit as st
import random

st.set_page_config(page_title="World Order Sandbox", page_icon="🌐", layout="compact")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .metric-card { background-color: #0d0d0d; border: 1px solid #1a1a1a; padding: 15px; border-radius: 6px; margin-bottom: 10px; }
    .status-alert { background-color: rgba(0, 255, 102, 0.05); border: 1px solid #00ff66; padding: 10px; border-radius: 4px; text-align: center; font-weight: bold; color: #00ff66; }
    </style>
""", unsafe_allow_html=True)

st.title("🌐 World Order Sandbox")
st.markdown('<div class="status-alert">🔔 Live Parliamentary Action Session Open: Adjust Minimum Wage Matrix</div>', unsafe_allow_html=True)
st.write("---")

if "unrest" not in st.session_state:
    st.session_state.unrest = 35.0
    st.session_state.steel = 2500.0
    st.session_state.tanks = 0

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.subheader("🏛️ Parliamentary Floor")
    st.write(f"Systemic Population Unrest: **{st.session_state.unrest:.1f}%**")
    if st.button("Propose Planned Economy Act"):
        if st.session_state.unrest > 45.0:
            st.success("CBA Majority Stance Met: Bill passed cleanly!")
        else:
            st.error("Bill Blocked by Opposition Filibuster Obstructions.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.subheader("💼 Industrial Vault")
    st.write(f"Steel Inventory Stockpiles: **{st.session_state.steel:.1f} tons**")
    st.write(f"Arsenal Combat Tanks: **{st.session_state.tanks} Units**")
    if st.button("Run Manufacturing Cycle"):
        if st.session_state.steel >= 500:
            st.session_state.steel -= 500
            st.session_state.tanks += 1
            st.balloons()
        else:
            st.warning("Production halted: insufficient intermediate resource stocks.")
    st.markdown('</div>', unsafe_allow_html=True)

if st.button("Tick Environment Heartbeat"):
    st.session_state.unrest = max(1.0, min(100.0, st.session_state.unrest + random.uniform(-10, 15)))
    st.rerun()
  
