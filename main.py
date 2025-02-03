import os
import json
import requests
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles

# Load environment variables
load_dotenv()

# Initialize FastAPI application
app = FastAPI()

# Add homepage route
@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Gemini
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# Configure OpenWeather API
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

# Weather icon mapping
WEATHER_ICONS = {
    'clear sky': '☀️',
    'few clouds': '🌤️',
    'scattered clouds': '☁️',
    'broken clouds': '☁️',
    'shower rain': '🌧️',
    'rain': '🌧️',
    'thunderstorm': '⛈️',
    'snow': '🌨️',
    'mist': '🌫️'
}

class Query(BaseModel):
    message: str

def get_weather(city):
    try:
        params = {
            'q': city,
            'appid': WEATHER_API_KEY,
            'units': 'metric',
            'lang': 'en'
        }
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
async def chat(query: Query):
    try:
        # Use Gemini to analyze user input and extract city information
        prompt = f"""You are a weather query assistant. Please analyze the following user input:
        1. If the user is asking about weather information for a city (including temperature, weather conditions, etc.), please return only the city name.
        2. If it's not a weather query, please return 'NOT_WEATHER_QUERY'.
        3. Please ensure the returned city name is accurate and contains no other text.

        Examples:
        Input: "How's the weather in London today?" -> Return: "London"
        Input: "Hello, how are you doing?" -> Return: "NOT_WEATHER_QUERY"

        User input: {query.message}"""
        
        print(f"User input: {query.message}")
        response = model.generate_content(prompt)
        city = response.text.strip()
        print(f"Identified city: {city}")


        if city == 'NOT_WEATHER_QUERY':
            # If not a weather query, let AI respond normally
            response = model.generate_content(query.message)
            return {"type": "chat", "content": response.text}

        # Get weather data
        weather_data = get_weather(city)

        # Generate weather response
        weather_description = weather_data['weather'][0]['description']
        weather_icon = WEATHER_ICONS.get(weather_description, '')
        return {
            "type": "weather",
            "data": {
                "city": weather_data['name'],
                "temperature": round(weather_data['main']['temp']),
                "description": weather_description,
                "icon": weather_icon,
                "humidity": weather_data['main']['humidity']
            }
        }

    except Exception as e:
        error_message = str(e)
        print(f"Error message: {error_message}")
        if "city not found" in error_message.lower():
            return {"response": "Sorry, I couldn't find weather information for this city. Please verify the city name."}
        return {"response": "Sorry, there was a problem getting the weather information. Please try again later."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)