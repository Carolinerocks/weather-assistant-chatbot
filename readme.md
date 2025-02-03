# Weather Assistant Chatbot 🌤️

A **FastAPI-based chatbot** that provides **real-time weather updates** using **Google Gemini AI** and **OpenWeather API**. Users can ask about the weather in different cities, and the chatbot will respond with temperature, conditions, and an emoji-based weather icon. If the input is not a weather-related query, the chatbot will generate a normal AI response.

## 🌟 Features

- 🌍 **Real-time Weather Queries**: Supports weather data retrieval for global cities, including temperature, humidity, and more.
- 🤖 **Intelligent Conversations**: Integrated with Google Gemini AI for natural language interaction.
- ⚡ **High-Performance Backend**: Built with FastAPI for asynchronous processing.
- 🎨 **User-Friendly Interface**: Simple and clean chat interface design.
- 🌈 **Weather Icons**: Uses emojis to visually represent weather conditions.

## 🔧 Tech Stack

| **Component**       | **Technology**               |
|---------------------|-----------------------------|
| **Backend**        | FastAPI (Python)            |
| **AI Model**       | Google Gemini 2.0 Flash      |
| **Frontend**       | HTML + TailwindCSS       |
| **Data Service**    | OpenWeather API          |
| **Containerization** | Docker + Docker Compose          |

## 📋 Prerequisites

Before running this project, ensure you have the following installed:

- **Docker**
- **Google Gemini API key**
- **OpenWeather API key**

## 🚀 Getting Started

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/weather-chatbot.git
cd weather-chatbot
```

### Step 2: Create a `.env` file and configure the following environment variables:

```env
OPENWEATHER_API_KEY=your_openweather_api_key
GOOGLE_API_KEY=your_google_api_key
```

### Step 3: Run the container

```bash
# Build and start the service
docker-compose up -d

# Access the service
open http://localhost:8000
```

## 🔍 Future Improvements

- 🏙️ Support for Multiple Weather Sources (e.g., WeatherAPI, AccuWeather)
- 🎙️ Voice Input Support
- 📍 Location-Based Weather Using IP Geolocation
- 📱 Build a Frontend UI for Better User Experience

## 📜 License

This project is open-source under the MIT License. Feel free to use and contribute! 🚀
