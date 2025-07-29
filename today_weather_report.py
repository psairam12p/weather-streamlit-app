import requests
import streamlit as st

def get_weather(city):
    api_key = "b4ae4c3e04820a5b91f98926ee833ecb"  # Your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    
    print(response.url)  # Debug: Print the actual URL for the API request
    print(response.status_code)  # Debug: Print the response status code
    
    if response.status_code == 200:
        data = response.json()
        print(data)  # Debug: Print the full API response
        temp = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        weather = data['weather'][0]['description']
        return temp, weather
    else:
        print(response.text)  # Print the error message from the API
        return None, None

st.title("Weather App")
city = st.text_input("Enter city name:")

if city:
    temp, weather = get_weather(city)
    if temp:
        st.write(f"**Weather in {city}:** {weather}")
        st.write(f"**Temperature:** {temp:.2f}°C")
    else:
        st.error("City not found!")
