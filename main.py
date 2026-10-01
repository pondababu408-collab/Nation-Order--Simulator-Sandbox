import streamlit as st
import random

# Force strict dark mobile frame viewport configurations
st.set_page_config(page_title="World Order Sandbox", page_icon="🌐", layout="centered")

# 🎨 Inject core application CSS stylesheet matching layout requirements exactly
st.markdown("""
    <style>
    /* Wipe standard Streamlit element structures out of layout boxes */
    [data-testid="stHeader"], [data-testid="stSidebar"], .stDeployButton, footer {
        display: none !important;
    }
    .stApp {
        background-color: #000000 !important;
        color: #E2E8F0 !important;
    }
    
    /* Top Full Width Alert Banner */
    .top-notification-banner {
        border: 1px solid #10B981;
        background-color: rgba(16, 185, 129, 0.04);
        border-radius: 8px;
        padding: 12px;
        text-align: center;
        font-weight: 600;
        font-size: 14px;
        color: #10B981;
        margin-bottom: 20px;
    }
    
    /* Grid Layout Matrix Systems */
    .more-hub-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
        margin-bottom: 80px;
    }
    .menu-button-node {
        background-color: #0A0A0C;
        border: 1px solid #1A1A1E;
        border-radius: 8px;
        padding: 16px;
        text-align: center;
        cursor: pointer;
        transition: border 0.2s ease;
    }
    .menu-button-node:hover {
        border-color: #33333A;
    }
    .node-icon {
        font-size: 20px;
        margin-bottom: 6px;
    }
    .node-label {
        font-size: 12px;
        color: #94A3B8;
        font-weight: 500;
    }
    
    /* Fixed Bottom Application Bar (Image Navigation Matrix) */
    .app-bottom-navbar {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        height: 64px;
        background-color: #050507;
        border-top: 1px solid #1A1A1E;
        display: flex;
        justify-content: space-around;
        align-items: center;
        z-index: 99999;
        padding-bottom: env(safe-area-inset-bottom);
    }
    .nav-item-anchor {
        text-align: center;
        color: #64748B;
        font-size: 18px;
        cursor: pointer;
        flex-grow: 1;
        padding: 10px 0;
    }
    .nav-item-anchor.active {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# STATE REGISTRY ROUTING MANAGEMENT ENGINE
# ----------------------------------------------------
if "active_view" not in st.session_state:
    st.session_state.active_view = "HUB"  # VIEWS: HOME, SEARCH, NETWORK, WORLD, HUB
if "unrest" not in st.session_state:
    st.session_state.unrest = 35.0
    st.session_state.steel = 2500.0
    st.session_state.tanks = 0

# --- SCREEN CONTROLLER VIEW TARGET RENDER LINES ---

if st.session_state.active_view == "HUB":
    # Image 1 & 2: Main Grid Matrix View Model
    st.markdown('<div class="top-notification-banner">🔔 Notificaciones Active Loop: Checking Operational State Ledgers</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="more-hub-grid">', unsafe_allow_html=True)
    
    menu_items = [
        {"icon": "💰", "label": "Economía"},
        {"icon": "🏛️", "label": "Organizaciones"},
        {"icon": "🔥", "label": "Conflicto"},
        {"icon": "👤", "label": "Personal"},
        {"icon": "✨", "label": "Conocimiento"},
        {"icon": "🎓", "label": "Universidad"},
        {"icon": "🏆", "label": "Ranking"},
        {"icon": "🌍", "label": "Organismos Supranacionales"},
        {"icon": "✉️", "label": "Mensajes"},
        {"icon": "👑", "label": "Premium (Golden)"},
        {"icon": "🏪", "label": "Tienda"},
        {"icon": "⚙️", "label": "Ajustes"}
    ]
    
    for item in menu_items:
        st.markdown(f"""
            <div class="menu-button-node">
                <div class="node-icon">{item['icon']}</div>
                <div class="node-label">{item['label']}</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.active_view == "WORLD":
    # Image 3: World Map Interface Engine View
    st.subheader("🌍 Dynamic World Map Viewport")
    st.markdown("""
        <div style="text-align: center; background-color: #111115; border-radius: 8px; padding: 20px; border: 1px solid #1A1A1E;">
            <span style="font-size: 80px;">🗺️</span>
            <div style="color: #777; font-size: 12px; margin-top: 10px;">Unscripted Geopolitical Borders Loaded. Tap sectors to interact.</div>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.active_view == "NETWORK":
    # Image 5: Volatile Feed Network Stream Loop
    st.subheader("📱 Volatile Social Feed")
    st.markdown("""
        <div style="background-color: #0A0A0C; padding: 15px; border-radius: 6px; border: 1px solid #1A1A1E; margin-bottom: 12px;">
            <div style="font-weight: bold; font-size: 13px; color: #00FF66;">Javier Córdoba @javolo12345</div>
            <div style="font-size: 12px; color: #E2E8F0; margin-top: 4px;">Eso es bastante nazi hasta para mi jajaja</div>
        </div>
        <div style="background-color: #0A0A0C; padding: 15px; border-radius: 6px; border: 1px solid #1A1A1E;">
            <div style="font-weight: bold; font-size: 13px; color: #0088FF;">P. Antón Rayne @Anton</div>
            <div style="font-size: 12px; color: #E2E8F0; margin-top: 4px;">Como pueden detener la ley si tenemos la mayoría del congreso</div>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.active_view == "HOME":
    # Clean Player Dashboard Skeleton Frame Layout
    st.subheader("👤 Character Dashboard Profile")
    st.write(f"System Population Unrest Core: **{st.session_state.unrest:.1f}%**")
    st.write(f"National Treasury Steel Stocks: **{st.session_state.steel:.1f} tons**")
    if st.button("Trigger Core Simulation Loop Tick"):
        st.session_state.unrest = random.uniform(10.0, 95.0)
        st.session_state.steel += 250.0
        st.rerun()

elif st.session_state.active_view == "SEARCH":
    # Image 6: Explorer / Search Panel
    st.subheader("🔍 Explore Global Rankings")
    st.text_input("Buscar Jugadores o Publicaciones...", placeholder="Type query parameter...")

# ----------------------------------------------------
# FIXED REAL-TIME BAR NAVIGATION CONTROLS (Image Anchors)
# ----------------------------------------------------
st.markdown('<div style="height: 80px;"></div>', unsafe_allow_html=True) # Space buffer block

# Use functional Streamlit button elements styled horizontally to control views
col_nav1, col_nav2, col_nav3, col_nav4, col_nav5 = st.columns(5)
with col_nav1:
    if st.button("🏠", help="Home dashboard view"): st.session_state.active_view = "HOME"; st.rerun()
with col_nav2:
    if st.button("🔍", help="Explore global registers"): st.session_state.active_view = "SEARCH"; st.rerun()
with col_nav3:
    if st.button("🔀", help="Social network matrix loops"): st.session_state.active_view = "NETWORK"; st.rerun()
with col_nav4:
    if st.button("🗺️", help="World geographic sector map"): st.session_state.active_view = "WORLD"; st.rerun()
with col_nav5:
    if st.button("☰", help="More hub tools menu list"): st.session_state.active_view = "HUB"; st.rerun()
