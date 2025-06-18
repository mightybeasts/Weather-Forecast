# weather_fetcher.py
import requests
import pandas as pd

def fetch_weather_data(city, api_key):
    try:
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1&aqi=no&alerts=no"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        forecast_data = data['forecast']['forecastday'][0]['hour']
        df = pd.DataFrame(forecast_data)
        df = df[['time', 'temp_c', 'humidity', 'wind_kph']].rename(columns={
            'temp_c': 'temperature',
            'humidity': 'humidity',
            'wind_kph': 'wind_speed'
        })

        return data, df

    except Exception as e:
        print("Error fetching weather data:", e)
        return None, None
