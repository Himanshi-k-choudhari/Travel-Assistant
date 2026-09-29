# AI Travel Assistant

A smart travel planning app built with Python, Generative AI and Streamlit. It helps users generate travel ideas based on destination, duration, budget, trip type, travel companions, and preferred vibes using Google Gemini.

## Overview

This project provides a user-friendly travel planner interface where users can enter:

- Name
- Destination
- Trip start date
- Number of days
- Budget range
- Type of experience
- Travel companions
- Hotel preference
- Travel vibe and region preferences

Once the form is filled, the app builds a custom trip prompt and sends it to Google Gemini to generate a trip plan.

## Features

- Modern Streamlit UI with a travel-themed background
- Destination and trip planning form
- Budget-based travel suggestions
- Companion-aware trip planning
- Vibe and region selection
- Hotel suggestion toggle
- AI-generated itinerary using Gemini

## Tech Stack

- Python
- Streamlit
- Google GenAI SDK
- python-dotenv

## Project Structure

- `travel_ui.py` – main Streamlit application
- `requirements.text` – Python dependencies
- `.env` – environment variables (API key storage)

## Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd "Travel Assistant"
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - Windows:

     ```bash
     venv\Scripts\activate
     ```

   - macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.text
   ```

5. Add your Google API key in a `.env` file:

   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

## Run the App

Start the Streamlit app:

```bash
streamlit run travel_ui.py
```

The app will open in your browser, where you can enter trip details and generate a customized travel plan.

## Usage

1. Open the app in the browser.
2. Fill in your trip preferences.
3. Click the `Plan Trip` button.
4. Review the AI-generated itinerary, recommendations, and travel suggestions.

## Notes

- The project depends on a valid Google Gemini API key.
- Keep your API key private and do not commit it to version control.
- Some scripts in the repository are experimental and may not be used in the main app flow.

## License

This project is for educational and personal use.
