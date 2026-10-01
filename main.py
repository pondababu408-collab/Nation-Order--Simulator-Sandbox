import streamlit as st
import random
import json

# Force dark mobile frame viewport parameters
st.set_page_config(page_title="World Order Sandbox", page_icon="🌐", layout="centered")

# 🎨 Inject structural dark theme styles matching layout requirements
st.markdown("""
    <style>
    /* Wipe standard Streamlit element borders out of layout boxes */
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
        margin-bottom: 20px;
    }
    .menu-button-node {
        background-color: #0A0A0C;
        border: 1px solid #1A1A1E;
        border-radius: 8px;
        padding: 16px;
        text-align: center;
        cursor: pointer;
    }
    .node-icon { font-size: 20px; margin-bottom: 6px; }
    .node-label { font-size: 12px; color: #94A3B8; font-weight: 500; }
    
    /* Map Vector Card Containers */
    .map-legend-box {
        background-color: #0D0D11;
        border: 1px solid #1A1A24;
        border-radius: 6px;
        padding: 12px;
        margin-top: 10px;
        font-size: 12px;
    }
    
    /* Center Setup Component Cards */
    .setup-frame-card {
        background-color: #0A0A0C;
        border: 1px solid #1A1A1E;
        border-radius: 8px;
        padding: 24px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# SYSTEM STATE REGISTER DEFAULTS
# ----------------------------------------------------
if "game_initialized" not in st.session_state:
    st.session_state.game_initialized = False
if "player_country" not in st.session_state:
    st.session_state.player_country = ""
if "player_party" not in st.session_state:
    st.session_state.player_party = ""
if "active_view" not in st.session_state:
    st.session_state.active_view = "HOME"
if "unrest" not in st.session_state:
    st.session_state.unrest = 22.5

# Seed initial unscripted geopolitical vector color registry parameters (Image 3 Mapping)
if "map_vector_colors" not in st.session_state:
    st.session_state.map_vector_colors = {
        "North_America": "#D6001C", # Capitalist Red Alignment
        "South_America": "#008A4B", # Agrarian Green Alignment
        "Eurasia_Bloc": "#0044FF",  # Planned Economy Blue Bloc
        "Africa_Sectors": "#FFBB00", # Unrest Disturbance Yellow Layer
        "Oceania_Base": "#7C3AED"    # Nationalist Purple Axis
    }

# ----------------------------------------------------
# 🎬 GAME STARTING SETUP GATES INTERFACE
# ----------------------------------------------------
if not st.session_state.game_initialized:
    st.title("🌐 World Order Simulator")
    st.subheader("Initialize Your Sovereign Sandbox State")
    
    st.markdown('<div class="setup-frame-card">', unsafe_allow_html=True)
    
    # Step A: Choose or Create Sovereign Identity Details
    st.markdown("##### 🏛️ Country Creation Strategy Blueprint")
    country_choice = st.selectbox(
        "Choose an existing baseline territory or register your own:",
        ["[Create Custom Nation Definition]", "Madrid, Reino de España", "United States of America", "Eurasia Central Union"]
    )
    
    if country_choice == "[Create Custom Nation Definition]":
        custom_country_name = st.text_input("Enter your custom Country identifier name:", placeholder="e.g., Republic of Arauzita")
        chosen_country = custom_country_name if custom_country_name else "Custom Republic"
    else:
        chosen_country = country_choice

    st.write("---")
    
    # Step B: Political Faction Affiliation Matrix Selection
    st.markdown("##### 🗳️ Political Affiliation Matrix")
    party_action = st.radio(
        "Select your path into the state parliamentary house:",
        ["Create a brand new political party", "Join an existing ideological AI faction"]
    )
    
    if party_action == "Create a brand new political party":
        chosen_party = st.text_input("Enter your unique political faction title name:", placeholder="e.g., Technocratic Freedom Front")
    else:
        chosen_party = st.selectbox("Select target AI political alliance group:", ["Ascendancy Capital Faction (CAPITALIST)", "Workers Syndicate Union (SOCIALIST)", "National Sovereignty League (NATIONALIST)"])
        
    st.write("---")
    
    if st.button("🚀 Launch Sovereign Simulation Engine", use_container_width=True):
        if chosen_country and chosen_party:
            st.session_state.player_country = chosen_country
            st.session_state.player_party = chosen_party
            st.session_state.game_initialized = True
            st.balloons()
            st.rerun()
        else:
            st.error("Validation error: All configuration fields must possess values.")
            
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# 🎮 LIVE SIMULATION GAMEPLAY SUB-ROUTER MODAL FRAMES
# ----------------------------------------------------
else:
    # Render Application Top Header Alerts
    st.markdown(f'<div class="top-notification-banner">🔔 Live Context: {st.session_state.player_country} | Active Party: {st.session_state.player_party}</div>', unsafe_allow_html=True)

    if st.session_state.active_view == "HOME":
        st.subheader("👤 Character Dashboard Profile")
        
        # Display custom profile data variables without external player strings
        col_stat1, col_stat2 = st.columns(2)
        with col_stat1:
            st.metric("Systemic Regional Unrest", f"{st.session_state.unrest:.1f}%")
        with col_stat2:
            st.metric("Sovereign Legal Status", "Active Citizen")
            
        if st.button("Tick Environment Volatility Matrix", use_container_width=True):
            st.session_state.unrest = random.uniform(5.0, 95.0)
            # Volatile color shifts trigger unscripted based on unrest parameters (Image 3)
            if st.session_state.unrest > 60.0:
                st.session_state.map_vector_colors["Eurasia_Bloc"] = "#FFBB00" # Shift to crisis yellow
            else:
                st.session_state.map_vector_colors["Eurasia_Bloc"] = "#0044FF" # Revert to planned blue
            st.rerun()

    elif st.session_state.active_view == "WORLD":
        # Image 3: Interactive Vector Color Properties for the World Map View
        st.subheader("🌍 Interactive Vector World Viewport Map")
        
        # Pull live color strings from system session data memory storage banks
        c_na = st.session_state.map_vector_colors["North_America"]
        c_sa = st.session_state.map_vector_colors["South_America"]
        c_eu = st.session_state.map_vector_colors["Eurasia_Bloc"]
        c_af = st.session_state.map_vector_colors["Africa_Sectors"]
        c_oc = st.session_state.map_vector_colors["Oceania_Base"]
        
        # Inject interactive responsive vector map layer SVG frame (Image 3 exact representation)
        st.markdown(f"""
            <div style="background-color: #060608; border: 1px solid #1A1A24; border-radius: 8px; padding: 16px; text-align: center;">
                <svg viewBox="0 0 800 400" xmlns="http://w3.org" style="width: 100%; height: auto;">
                    <!-- North America Map Vector Shape Node -->
                    <rect x="40" y="30" width="240" height="140" rx="12" fill="{c_na}" opacity="0.85" style="cursor: pointer;"/>
                    <text x="60" y="60" fill="#fff" font-size="12" font-weight="bold">North America (Red Bloc)</text>
                    
                    <!-- South America Map Vector Shape Node -->
                    <rect x="160" y="210" width="140" height="150" rx="12" fill="{c_sa}" opacity="0.85" style="cursor: pointer;"/>
                    <text x="180" y="240" fill="#fff" font-size="12" font-weight="bold">South America (Green)</text>
                    
                    <!-- Eurasia Bloc Map Vector Shape Node -->
                    <rect x="340" y="20" width="420" height="150" rx="12" fill="{c_eu}" opacity="0.85" style="cursor: pointer;"/>
                    <text x="360" y="50" fill="#fff" font-size="12" font-weight="bold">Eurasia Continent (Blue Bloc)</text>
                    
                    <!-- Africa Sectors Map Vector Shape Node -->
                    <rect x="380" y="200" width="150" height="170" rx="12" fill="{c_af}" opacity="0.85" style="cursor: pointer;"/>
                    <text x="400" y="230" fill="#fff" font-size="12" font-weight="bold">Africa Sectors (Yellow)</text>
                    
                    <!-- Oceania Base Map Vector Shape Node -->
                    <rect x="580" y="210" width="180" height="120" rx="12" fill="{c_oc}" opacity="0.85" style="cursor: pointer;"/>
                    <text x="600" y="240" fill="#fff" font-size="12" font-weight="bold">Oceania Grid (Purple)</text>
                </svg>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="map-legend-box">
                <strong>🎨 System Geopolitical Vector Legend:</strong><br>
                🔴 Red: Capitalist Factions | 🔵 Blue: Planned Market Zones | 🟡 Yellow: Civil War Unrest Crises
            </div>
        """, unsafe_allow_html=True)

    elif st.session_state.active_view == "NETWORK":
st.subheader("📱 Volatile Social Feed Stream")
st.markdown("""

Javier Córdoba @javolo12345
Eso es bastante nazi hasta para mi jajaja


P. Antón Rayne @Anton
Como pueden detener la ley si tenemos la mayoría del congreso

""", unsafe_allow_html=True)
elif st.session_state.active_view == "HUB":
st.subheader("🛠️ Operations Menu Hub")
st.markdown('', unsafe_allow_html=True)
hub_modules = ["Economía", "Organizaciones", "Conflicto", "Personal", "Conocimiento", "Universidad", "Ranking", "Ajustes"]
for mod in hub_modules:
st.markdown(f"""

📦
{mod}

""", unsafe_allow_html=True)
st.markdown('', unsafe_allow_html=True)
# ----------------------------------------------------
# FIXED REAL-TIME NAVIGATION MENU BAR
# ----------------------------------------------------
st.markdown('', unsafe_allow_html=True) # Space buffer block
col_nav1, col_nav2, col_nav3, col_nav4 = st.columns(4)
with col_nav1:
if st.button("🏠", help="Profile Dashboard Panel"): st.session_state.active_view = "HOME"; st.rerun()
with col_nav2:
if st.button("🔀", help="Social Feed Matrices"): st.session_state.active_view = "NETWORK"; st.rerun()
with col_nav3:
if st.button("🗺️", help="Vector Viewport Map"): st.session_state.active_view = "WORLD"; st.rerun()
with col_nav4:
if st.button("☰", help="More Menu Hub List"): st.session_state.active_view = "HUB"; st.rerun()
