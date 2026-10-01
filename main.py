import streamlit as st
import random
import json
import math

# Force strict dark mobile-first viewport parameters
st.set_page_config(page_title="World Order Sandbox", page_icon="🌐", layout="centered")

# 🎨 Inject clean visual styling matching layout screenshots exactly
st.markdown("""
    <style>
    /* Wipe default Streamlit clutter components out of frame */
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
    
    /* Responsive Menu Icon Grid Layout System */
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
    }
    .node-icon { font-size: 20px; margin-bottom: 6px; }
    .node-label { font-size: 12px; color: #94A3B8; font-weight: 500; }
    
    /* Display HUD Card Layout Blocks */
    .tactical-hud-card {
        background-color: #0D0D11;
        border: 1px solid #1A1A24;
        border-radius: 6px;
        padding: 14px;
        margin-bottom: 12px;
    }
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
# 🏛️ COMPREHENSIVE 193 COUNTRIES GEOPOLITICAL MASTER ROSTER
# ----------------------------------------------------
ALL_COUNTRIES = [
    "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", 
    "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", 
    "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", 
    "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States of America",
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", 
    "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela",
    "Afghanistan", "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Bahrain", 
    "Bangladesh", "Belarus", "Belgium", "Bhutan", "Bosnia and Herzegovina", "Brunei", 
    "Bulgaria", "Cambodia", "China", "Croatia", "Cyprus", "Czech Republic", "Denmark", 
    "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland", 
    "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Japan", "Jordan", 
    "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Liechtenstein", 
    "Lithuania", "Luxembourg", "Maldives", "Malta", "Moldova", "Monaco", "Mongolia", 
    "Montenegro", "Myanmar", "Nepal", "Netherlands", "North Korea", "North Macedonia", 
    "Norway", "Oman", "Pakistan", "Palestine", "Philippines", "Poland", "Portugal", "Qatar", 
    "Romania", "Russia", "San Marino", "Saudi Arabia", "Serbia", "Singapore", "Slovakia", 
    "Slovenia", "South Korea", "Spain", "Sri Lanka", "Sweden", "Switzerland", "Syria", 
    "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "UAE", "Ukraine", 
    "United Kingdom", "Uzbekistan", "Vietnam", "Yemen",
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", 
    "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo (Brazzaville)", 
    "Congo (Kinshasa)", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", 
    "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", 
    "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", 
    "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", 
    "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", 
    "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe",
    "Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", 
    "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"
]

# ----------------------------------------------------
# 💾 PERSISTENT ENGINE STATE INITIALIZATION
# ----------------------------------------------------
if "game_initialized" not in st.session_state:
    st.session_state.game_initialized = False
if "player_country" not in st.session_state:
    st.session_state.player_country = ""
if "player_party" not in st.session_state:
    st.session_state.player_party = ""
if "active_view" not in st.session_state:
    st.session_state.active_view = "HOME"
if "sub_hub_view" not in st.session_state:
    st.session_state.sub_hub_view = "MENU"

# NationCraft Function Variables
if "unrest" not in st.session_state: st.session_state.unrest = 20.0
if "treasury_gold" not in st.session_state: st.session_state.treasury_gold = 10000.0
if "raw_iron" not in st.session_state: st.session_state.raw_iron = 1000.0
if "refined_steel" not in st.session_state: st.session_state.refined_steel = 0.0
if "military_aggression" not in st.session_state: st.session_state.military_aggression = 10.0
if "territory_size_km2" not in st.session_state: st.session_state.territory_size_km2 = 505990 # Spain Base Size
if "reserve_interest_slider" not in st.session_state: st.session_state.reserve_interest_slider = 4.0

if "map_colors" not in st.session_state:
    st.session_state.map_colors = {"NA": "#D6001C", "SA": "#008A4B", "EU": "#0044FF", "AF": "#FFBB00", "OC": "#7C3AED"}

# ----------------------------------------------------
# 🎬 SCENE 1: STARTING GEOPOLITICAL ONBOARDING GATES
# ----------------------------------------------------
if not st.session_state.game_initialized:
    st.title("🌐 World Order Simulator")
    st.subheader("Initialize Your Sovereign Sandbox State")
    st.markdown('<div class="setup-frame-card">', unsafe_allow_html=True)
    
    st.markdown("##### 🏛️ Country Creation Strategy Blueprint")
    country_options = ["[Create Custom Nation Definition]"] + ALL_COUNTRIES
    country_choice = st.selectbox("Select or spawn your territory node coordinate:", country_options, index=ALL_COUNTRIES.index("Spain")+1 if "Spain" in ALL_COUNTRIES else 0)
    chosen_country = st.text_input("Custom Nation Title ID:", "Republic of Arauzita") if country_choice == "[Create Custom Nation Definition]" else country_choice

    st.write("---")
    st.markdown("##### 🗳️ Political Affiliation Matrix")
    party_action = st.radio("Select your path into parliament:", ["Create a brand new political party", "Join an existing ideological AI faction"])
    chosen_party = st.text_input("Enter your unique political faction title name:", placeholder="e.g., Technocratic Freedom Front") if party_action == "Create a brand new political party" else st.selectbox("Select target AI alliance:", ["Ascendancy Capital Faction (CAPITALIST)", "Workers Syndicate Union (SOCIALIST)", "National Sovereignty League (NATIONALIST)"])
    
    st.write("---")
    if st.button("🚀 Launch Sovereign Simulation Engine", use_container_width=True):
        if chosen_country and chosen_party:
            st.session_state.player_country = chosen_country
            st.session_state.player_party = chosen_party
            st.session_state.game_initialized = True
            st.balloons()
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# 2. GAME SUBSYSTEM FUNCTIONS
# ----------------------------------------------------
else:
    st.markdown(f'<div class="top-notification-banner">👑 Sovereign Territory: {st.session_state.player_country} | Active Party: {st.session_state.player_party}</div>', unsafe_allow_html=True)

    # --- VIEW RADAR: HOME PROFILE VIEW ---
    if st.session_state.active_view == "HOME":
        st.subheader("📊 National Strategy Status")
        
        st.markdown('<div class="tactical-hud-card">', unsafe_allow_html=True)
        col_char1, col_char2 = st.columns(2)
        with col_char1:
            st.write(f"🪙 Treasury Reserves: **{st.session_state.treasury_gold:,.2f} Gold**")
            st.write(f"🗺️ Total Territory Size: **{st.session_state.territory_size_km2:,.0f} km²**")
        with col_char2:
            st.write(f"⚡ Military Aggression Rating: **{st.session_state.military_aggression:.1f}/100**")
            st.write(f"📉 Domestic Tension Unrest: **{st.session_state.unrest:.1f}%**")
        st.markdown('</div>', unsafe_allow_html=True)

        # NationCraft Function: Territory Expansion Engine
        st.markdown('<div class="tactical-hud-card">', unsafe_allow_html=True)
        st.write("##### 🗺️ Expansion & Conquest Vectors")
        if st.button("Fund Colonial Expansion Shift (-2,500 Gold)", use_container_width=True):
            if st.session_state.treasury_gold >= 2500.0:
                st.session_state.treasury_gold -= 2500.0
                st.session_state.territory_size_km2 += random.randint(5000, 25000)
                st.session_state.military_aggression = min(100.0, st.session_state.military_aggression + 5.0)
                st.success("Territory limits successfully expanded via diplomatic annexation!")
                st.rerun()
            else:
                st.error("Insufficient national gold reserves inside the treasury.")
        st.markdown('</div>', unsafe_allow_html=True)

        # Volatile Engine Loop Ticks
