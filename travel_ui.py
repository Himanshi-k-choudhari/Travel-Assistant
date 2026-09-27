import streamlit as st
import textwrap
import datetime
from google import genai
from dotenv import load_dotenv
import time

load_dotenv(r"C:\Users\Administrator\Desktop\Travel Assistant\.env")

client = genai.Client()

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
#          Tilte of the page
#------------------------------------------------

# Configure page layout
st.set_page_config(
    page_title="AI Travel Assistant",
    page_icon="✈️",
    layout="centered"
)

# Set full app background outside the header
bg_image_url = "https://media.cntraveler.com/photos/67cb142a5d227df863450e65/master/w_2560%2Cc_limit/1278376286"

header_html = textwrap.dedent(f"""
<style>
/* Full app background */
[data-testid="stAppViewContainer"] {{
    background: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.85)), 
                url('{bg_image_url}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Transparent header bar */
[data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
}}

/* Compact outer card container */
.hero-card {{
    background: linear-gradient(140deg, #182A46 0%, #0D5052 100%);
    border-radius: 20px;
    padding: 24px 20px; /* Reduced vertical padding */
    text-align: center;
    color: #FFFFFF;
    box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.4);
    margin: 0 auto 20px auto;
    max-width: 580px; /* Smaller max-width */
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}}

/* Compact plane Icon */
.hero-icon {{
    font-size: 38px; /* Scaled down */
    line-height: 1;
    margin-bottom: 10px;
}}

/* Compact Header Title */
.hero-title {{
    font-size: 28px; /* Reduced font size */
    font-weight: 800;
    margin-bottom: 6px;
    letter-spacing: -0.5px;
    color: #FFFFFF;
}}

/* Compact Subtitle */
.hero-subtitle {{
    font-size: 14px; /* Reduced font size */
    font-weight: 400;
    color: #D1D5DB;
    margin-bottom: 18px;
}}

/* Compact Inner Features Box */
.features-box {{
    background-color: #161B22;
    border-radius: 12px;
    padding: 14px 18px; /* Smaller inner padding */
    margin: 0 auto;
    max-width: 420px; /* Narrower inner box */
    box-shadow: inset 0px 0px 8px rgba(0, 0, 0, 0.4);
}}

/* Compact code tag text */
.features-code-tag {{
    font-family: "Source Code Pro", Consolas, Monaco, monospace;
    color: #8B949E;
    font-size: 13px; /* Scaled down */
    margin-bottom: 6px;
    text-align: center;
}}

/* Compact Feature List Rows */
.feature-item {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 14px; /* Reduced font size */
    font-weight: 600;
    color: #FFFFFF;
    margin: 4px 0; /* Tighter spacing between items */
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}}

.feature-item span.bullet {{
    color: #8B949E;
    font-size: 12px;
    margin-left: 4px;
}}
</style>

<div class="hero-card">
    <div class="hero-icon">🌎</div>
    <div class="hero-title">AI Travel Assistant</div>
    <div class="hero-subtitle">Your Personal Travel Assistant</div>
</div>
""")

# Render header
st.markdown(header_html, unsafe_allow_html=True)

#------------------------------------------------
#          ain content
#------------------------------------------------

name = st.text_input("Enter Your Name : ")
destination = st.text_input("Enter Your Destination ✈️ : ")
num_days = st.text_input("For how many days you want to plan the trip ?: ")


date_trip = st.date_input("On which date your are planing your trip?", datetime.date.today())

type_trip = st.selectbox("What kind of Trip do you want" , ["Select the trip","Luxury", "Moderate" , "Budget friendly"])
budget = st.selectbox("What is your BUDGET for the trip", ["select your budget","upto ~20,000","upto ~70,000", "upto ~1 lakh", "Unlimited"])
who_travel = st.selectbox("With whom you are travelling" , ["Family" ,"Solo" ,"Couples" , "Friends"])
#st.button("Plan Trip")


prompt = f"""You are a travel planar , user that is {name} wants to go to {destination} , on {date_trip} for {num_days}.
travel type is :{type_trip}
user's budget is :{budget}
user is traveling : {who_travel}
plan a trip and share the answer in bullet form."""



if st.button("Plan Trip"):
    interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt
        )

    with st.spinner("Wait for it...", show_time=True):
        time.sleep(5)

    st.success("Wohh !! Pack your bags, and get ready for the trip.....")
    st.write(interaction.output_text)
    