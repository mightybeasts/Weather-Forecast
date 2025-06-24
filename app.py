
import streamlit as st
import pandas as pd
API_KEY = st.secrets["API_KEY"]
from weather_fetcher import fetch_weather_data
from visualize import plot_temperature_chart

st.set_page_config(
    page_title="WeatherNow",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("WeatherNow Dashboard")
city = st.text_input("Enter city name", "Bangalore")

if city:
    data, forecast_df = fetch_weather_data(city, API_KEY)

    if data and forecast_df is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Temperature", f"{data['current']['temp_c']} °C")
            st.metric("Condition", data['current']['condition']['text'])
        with col2:
            st.metric("Humidity", f"{data['current']['humidity']}%")
            st.metric("Wind Speed", f"{data['current']['wind_kph']} kph")

        st.subheader("Temperature Forecast")
        st.plotly_chart(plot_temperature_chart(forecast_df), use_container_width=True)

   

        st.map(pd.DataFrame({
            'lat': [data['location']['lat']],
            'lon': [data['location']['lon']]
        }), zoom=8)

    else:
        st.error("❌ Could not fetch weather data. Please check the city name or API key.")
