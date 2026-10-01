import streamlit as st
import random
import json
import math

# Force dark mobile frame viewport configurations
st.set_page_config(page_title="World Order Sandbox", page_icon="🌐", layout="centered")

# 🎨 Inject structural dark theme stylesheets matching design grids exactly
st.markdown("""
    <style>
    /* Wipe standard Streamlit layout containers */
    [data-testid="stHeader"], [data-testid="stSidebar"], .stDeployButton, footer {
        display: none !important;
    }
    .stApp {
        background-color: #000000 !important;
        color: #E2E8F0 !important;
    }
    
    /* Top Full Width Alert Notification Strip */
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
    
    /* Operations Grid Layout */
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
    
    /* Legend Containers */
    .map-legend-box {
        background-color: #0D0D11;
        border: 1px solid #1A1A24;
        border-radius: 6px;
        padding: 12px;
        margin-top: 10px;
        font-size: 12px;
    }
    
    /* Onboarding Setup Cards */
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
# COMPREHENSIVE GLOBAL COUNTRIES MAP REGISTRY
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
    st.session_state.unrest = 20.0

if "map_vector_colors" not in st.session_state:
    st.session_state.map_vector_colors = {
        "North_America": "#D6001C",
        "South_America": "#008A4B",
        "Eurasia_Bloc": "#0044FF",
        "Africa_Sectors": "#FFBB00",
        "Oceania_Base": "#7C3AED"
    }

# ----------------------------------------------------
# 🎬 GAME INTERFACE ENTRY CONTROLLER
# ----------------------------------------------------
if not st.session_state.game_initialized:
    st.title("🌐 World Order Simulator")
    st.subheader("Initialize Your Sandbox State")
    
    st.markdown('<div class="setup-frame-card">', unsafe_allow_html=True)
    
    st.markdown("##### 🏛️ Country Creation Strategy Blueprint")
    country_options = ["[Create Custom Nation Definition]"] + ALL_COUNTRIES
    country_choice = st.selectbox(
        "Choose an official territory node or register your own:",
        country_options,
        index=ALL_COUNTRIES.index("Spain") + 1 if "Spain" in ALL_COUNTRIES else 0
    )
    
    if country_choice == "[Create Custom Nation Definition]":
        custom_country_name = st.text_input("Enter your custom Country identifier name:", placeholder="e.g., Republic of Arauzita")
        chosen_country = custom_country_name if custom_country_name else "Custom Republic"
    else:
        chosen_country = country_choice

    st.write("---")
    
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

else:
    st.markdown(f'<div class="top-notification-banner">👑 Sovereign Territory: {st.session_state.player_country} | Active Party: {st.session_state.player_party}</div>', unsafe_allow_html=True)

    if st.session_state.active_view == "HOME":
        st.subheader("👤 Character Dashboard Profile")
        col_stat1, col_stat2 = st.columns(2)
        with col_stat1:
            st.metric("Systemic Country Unrest", f"{st.session_state.unrest:.1f}%")
        with col_stat2:
            st.metric("Sovereign Legal Status", "Active Citizen")
            
        if st.button("Tick Environment Volatility Matrix", use_container_width=True):
            st.session_state.unrest = random.uniform(5.0, 95.0)
            if st.session_state.unrest > 60.0:
                st.session_state.map_vector_colors["Eurasia_Bloc"] = "#FFBB00"
            else:
                st.session_state.map_vector_colors["Eurasia_Bloc"] = "#0044FF"
            st.rerun()

    elif st.session_state.active_view == "WORLD":
        st.subheader("🌍 Interactive Vector World Viewport Map")
        c_na = st.session_state.map_vector_colors["North_America"]
        c_sa = st.session_state.map_vector_colors["South_America"]
        c_eu = st.session_state.map_vector_colors["Eurasia_Bloc"]
        c_af = st.session_state.map_vector_colors["Africa_Sectors"]
        c_oc = st.session_state.map_vector_colors["Oceania_Base"]
        
        st.markdown(f"""
            <div style="background-color: #060608; border: 1px solid #1A1A24; border-radius: 8px; padding: 16px; text-align: center;">
                <svg viewBox="0 0 800 400" xmlns="http://w3.org" style="width: 100%; height: auto;">
                    <rect x="40" y="30" width="240" height="140" rx="12" fill="{c_na}" opacity="0.85"/>
                    <text x="60" y="60" fill="#fff" font-size="12" font-weight="bold">North America</text>
                    
                    <rect x="160" y="210" width="140" height="150" rx="12" fill="{c_sa}" opacity="0.85"/>
                    <text x="180" y="240" fill="#fff" font-size="12" font-weight="bold">South America</text>
                    
