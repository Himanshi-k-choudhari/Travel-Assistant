#------------------------------------------------
#          Tools required
#------------------------------------------------

import streamlit as st
import textwrap
import datetime
import google.generativeai as genai
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
    page_title="Himanshi's App",
    page_icon="✈️",
    layout="wide"
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
#          Decor of the page
#------------------------------------------------

import streamlit as st

# Direct image URLs corresponding to your 6 destinations
images = [
    "https://images.unsplash.com/photo-1548013146-72479768bada",  # Snow / Mountains
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",  # Nature
    "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9",  # Desert
    "https://images.unsplash.com/photo-1519046904884-53103b34b206",  # Beach
    "https://images.unsplash.com/photo-1512453979798-5ea266f8880c",  # Dubai
    "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e",  # Japan
]

# Set fixed thumbnail height so all 6 images look uniform
st.markdown(
    """
    <style>
    div[data-testid="stImage"] img {
        height: 110px;          /* Adjust height for 6 smaller thumbnails */
        object-fit: cover;      /* Prevents image stretching */
        border-radius: 8px;     /* Rounded corners */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Expand the center area slightly to accommodate 6 thumbnails nicely
left_spacer, center_content, right_spacer = st.columns([1, 4, 1])

with center_content:
    # Create 6 equal columns in one row
    thumbnail_columns = st.columns(6, gap="small")
    
    # Loop through columns and images together
    for column, image in zip(thumbnail_columns, images):
        column.image(image, use_container_width=True)

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
    