import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from weather_fetcher import fetch_weather_data
from visualize import plot_temperature_chart

st.set_page_config(page_title="Weather Dashboard", layout="wide")
st.title("🌍 Weather Forecast")

city = st.text_input("City Name", value="London")

# Trigger search
if st.button("Get Forecast"):
    weather, err = fetch_weather_data(city)
    if err:
        st.error(err)
    else:
        st.session_state.weather = weather

# Only render once weather is stored in state
if "weather" in st.session_state:
    w = st.session_state.weather

    # Show current stats
    st.subheader(f"{w['current']['city']}, {w['current']['country']} — Now: {w['current']['temp_c']}°C")
    cols = st.columns(3)
    cols[0].metric("Humidity", f"{w['current']['humidity']}%")
    cols[1].metric("Wind", f"{w['current']['wind_kph']} km/h")
    cols[2].metric("Condition", w['current']['condition'])

    # Plotly chart
    fig = plot_temperature_chart(w['forecast_df'])
    st.plotly_chart(fig, use_container_width=True)

    # Map
    m = folium.Map(location=[w['lat'], w['lon']], zoom_start=10)
    folium.Marker(
        [w['lat'], w['lon']],
        tooltip=city,
        icon=folium.Icon(color="blue")
    ).add_to(m)
    st.subheader("Location Map")
    st_folium(m, width=700, height=450)
