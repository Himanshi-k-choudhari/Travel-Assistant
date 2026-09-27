#------------------------------------------------
#          Tools required
#------------------------------------------------

import streamlit as st
import textwrap
import datetime
from google import genai
from dotenv import load_dotenv
import time
load_dotenv()
client = genai.Client()




#load_dotenv(r"C:\Users\Administrator\Desktop\Travel Assistant\.env")


#------------------------------------------------
#          setting up the background
#------------------------------------------------

def set_bg_from_url(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


image_url = "https://media.cntraveler.com/photos/67cb142a5d227df863450e65/master/w_2560%2Cc_limit/1278376286"


set_bg_from_url(image_url)

#------------------------------------------------
#          Side header
#------------------------------------------------
with st.sidebar:
    st.markdown("🌎  ✈️  🧗")
    st.header("About App")
    st.write("Plan A Trip")
    st.write("🗺️ Discover the new possibilities to travel")
    st.write("🍹 Plan according to your vibe")
    st.write("🏨 Hotel Suggestions")
    st.write("📅 Pick the date from Calender")
    st.write("👤 Expert Travel planer")
    st.write("✨ Google Gemini Suggestins")
    st.write("💸Plan According to your Budget")
    st.divider()
    st.caption("© 2026 Milky Way AI by Himanshi. All rights reserved.")

#------------------------------------------------
#          Tilte of the page
#------------------------------------------------

# Configure page layout
st.set_page_config(
    page_title="AI TRAVEL ASSISTANT",
    page_icon="✈️",
    layout="wide"
)

# Set full app background outside the header
bg_image_url = "https://media.cntraveler.com/photos/67cb142a5d227df863450e65/master/w_2560%2Cc_limit/1278376286"

import textwrap
import streamlit as st

# (Ensure bg_image_url is defined above this block)

header_html = textwrap.dedent(f"""
<style>
/* Full app background */
[data-testid="stAppViewContainer"] {{
    background: linear-gradient(135deg, rgba(10, 15, 29, 0.88), rgba(15, 23, 42, 0.88)), 
                url('{bg_image_url}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Transparent header bar */
[data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
}}

/* Floating Hero Card with Glassmorphism */
.hero-card {{
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 24px;
    padding: 28px 24px;
    text-align: center;
    color: #FFFFFF;
    box-shadow: 0 12px 32px 0 rgba(0, 0, 0, 0.37);
    margin: 10px auto 28px auto;
    max-width: 600px;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}}

.hero-card:hover {{
    transform: translateY(-2px);
    box-shadow: 0 16px 40px 0 rgba(0, 198, 255, 0.15);
}}

/* Animated Floating Icon */
.hero-icon {{
    font-size: 42px;
    line-height: 1;
    margin-bottom: 12px;
    display: inline-block;
    filter: drop-shadow(0 0 12px rgba(56, 189, 248, 0.6));
    animation: float 3s ease-in-out infinite;
}}

@keyframes float {{
    0% {{ transform: translateY(0px) rotate(0deg); }}
    50% {{ transform: translateY(-8px) rotate(4deg); }}
    100% {{ transform: translateY(0px) rotate(0deg); }}
}}

/* Gradient Header Title */
.hero-title {{
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 6px;
    letter-spacing: -0.8px;
    background: linear-gradient(135deg, #FFFFFF 30%, #38BDF8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

/* Subtitle with Accent Pulse */
.hero-subtitle {{
    font-size: 15px;
    font-weight: 400;
    color: #94A3B8;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}}

.live-dot {{
    width: 8px;
    height: 8px;
    background-color: #10B981;
    border-radius: 50%;
    box-shadow: 0 0 8px #10B981;
    animation: pulse 2s infinite;
}}

@keyframes pulse {{
    0% {{ transform: scale(0.95); opacity: 0.8; }}
    50% {{ transform: scale(1.2); opacity: 1; }}
    100% {{ transform: scale(0.95); opacity: 0.8; }}
}}

/* Feature Badges Container */
.features-container {{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-top: 16px;
}}

/* Glass Pill Badges */
.feature-badge {{
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 13px;
    font-weight: 500;
    color: #E2E8F0;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s ease;
}}

.feature-badge:hover {{
    background: rgba(56, 189, 248, 0.2);
    border-color: rgba(56, 189, 248, 0.5);
    color: #FFFFFF;
    transform: scale(1.03);
}}
</style>

<div class="hero-card">
    <div class="hero-icon">✈️</div>
    <div class="hero-title">AI Travel Assistant</div>
    <div class="hero-subtitle">
        <span class="live-dot"></span> Smart Itineraries & Personal Travel Agent
    </div>
    <div class="features-container">
        <div class="feature-badge">🗺️ Custom Plans</div>
        <div class="feature-badge">⚡ Instant Recommendations</div>
        <div class="feature-badge">💰 Budget Optimizer</div>
    </div>
</div>
""")

# Render header
st.markdown(header_html, unsafe_allow_html=True)
#------------------------------------------------
#          Decor of the page
#------------------------------------------------


#------------------------------------------------
#          main content
#------------------------------------------------

name = st.text_input("Enter Your Name : ")

st.subheader("Destination 🗺️")
destination = st.text_input("Enter Your Destination ✈️ : ")

st.subheader("Date & Days 📅")
num_trip, date_trip = st.columns(2)
with num_trip:
    num_days = st.number_input("For how many days you want to plan the trip ?: " , min_value = 1 , max_value = 30)
with date_trip:
    date_trip = st.date_input("On which date your are planing your trip?", datetime.date.today())

st.subheader("Budget 💸")
type_trip, budget = st.columns(2)
with type_trip:
    type_trip = st.selectbox("What kind of Experience do you want" , ["Select the Experience","Luxury", "Moderate" , "Budget friendly"])
 
with budget:
    budget = st.selectbox("What is your BUDGET for the trip", ["select your budget","upto ~20,000","upto ~70,000", "upto ~1 lakh", "Unlimited"])
hotel_sug = st.radio("Do you want hotel suggestions ?🏨" , ["Yes" , "No" ,"Only give a idea"])

st.subheader("Travel Information 👤")
who_travel, number_travelers = st.columns(2)
with who_travel:
    who_travel = st.selectbox("With whom you are travelling" , ["Family" ,"Solo" ,"Couples" , "Friends"])
with number_travelers:
    num_travelers = st.number_input("Number of Travelers" , min_value = 1, max_value = 50)

st.subheader("Vibe of Travel 🍹")
vibe_trip, region = st.columns(2)
with vibe_trip:
    vibe_trip = st.multiselect("Choose your vibe" , ["Nature 🌲", "Cultural ⛩️" , "Adventure 🧗" , "Food and vibe 🍔", "Shoppong 🛍️ and  Souvenirs 🧸" , "All in One"])
with region:
    region = st.multiselect("Which Region or Weather you would prefer ?" , ["Beach 🏖️" , "Mountains 🏔️" , "Snow 🏂" , "Desert 🏜️" ,"Star gazing🌌", "Not Sure Yet"])


#------------------------------------------------
#          Prompt
#------------------------------------------------

prompt = f"""You are a travel planar , user that is {name} wants to go to {destination} , on {date_trip} for {num_days} days.
travel type is :{type_trip}
user's budget is :{budget}
user is traveling : {who_travel} with total {num_travelers} travelers
hotel suggestion required : {hotel_sug}
vibe of trip : {", ".join(vibe_trip) if isinstance(vibe_trip, list) else vibe_trip}
preferred region/weather : {", ".join(region) if isinstance(region, list) else region}
plan a trip and share the answer in bullet form."""

#------------------------------------------------
#          connecting to the model
#------------------------------------------------

if st.button("Plan Trip"):
    interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt
        )

    with st.spinner("Wait for it...", show_time=True):
        time.sleep(3)

    st.success("Wohh !! Pack your bags, and get ready for the trip.....")
    st.write(interaction.output_text)
    st.success("🎉 Trip planned Successfuly !! 🎉")
    st.divider()
    st.caption("AI can make mistakes o please double check")
    