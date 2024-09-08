import streamlit as st
import requests
import folium
from streamlit_folium import folium_static

# Define function to fetch distance data using Google Maps Distance Matrix API
def fetch_distance_data(start_port, end_port, api_key):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={start_port}&destinations={end_port}&key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        distance_data = response.json()
        if distance_data['status'] == 'OK':
            element = distance_data['rows'][0]['elements'][0]
            distance = element['distance']['text']
            duration = element['duration']['text']
            return distance, duration
        else:
            st.error(f"Error in response: {distance_data['status']}. {distance_data.get('error_message', '')}")
            return None, None
    else:
        st.error(f"Error fetching distance data: {response.status_code}. {response.text}")
        return None, None

# Define preprocessing functions
def preprocess_weather_data(raw_data):
    processed_data = {
        'wind_speed': raw_data.get('wind', {}).get('speed', 0),
        'wave_height': raw_data.get('waves', {}).get('height', 0),
    }
    return processed_data

def preprocess_ship_data(ship_data):
    processed_data = {
        'length': ship_data.get('length', 0),
        'width': ship_data.get('width', 0),
        'drift_coefficient': ship_data.get('drift', 0),
    }
    return processed_data

# Title
st.title("Ship Route Optimization Tool")

# Input fields
start_port = st.text_input("Enter Starting Port")
end_port = st.text_input("Enter Destination Port")
ship_type = st.selectbox("Select Ship Type", ["Cargo", "Tanker", "Passenger", "Container"])
optimization_criteria = st.multiselect("Optimization Criteria", ["Fuel Efficiency", "Safety", "Travel Time"])

# Fetch distance data using Google Maps Distance Matrix API
api_key = "AIzaSyBzYc1MD8BfylKYojWrj8eOwno30BnScQw"  # Replace with your Google Maps API key
if start_port and end_port:
    distance, duration = fetch_distance_data(start_port, end_port, api_key)

    if distance and duration:
        st.write(f"Distance between ports: {distance}")
        st.write(f"Estimated travel time: {duration}")

        # Dummy weather and ship data for example
        weather_data = {'wind': {'speed': 5.0}, 'waves': {'height': 1.5}}
        ship_characteristics = {'length': 300, 'width': 50, 'drift': 0.02}

        # Process data
        processed_weather = preprocess_weather_data(weather_data)
        processed_ship = preprocess_ship_data(ship_characteristics)

        # Example optimize_route function
        def optimize_route(weather_data, ship_characteristics):
            # Mock function to return dummy results
            return [[100, 80]], [[start_lat, start_lon], [end_lat, end_lon]]

        # Mock coordinates for the purpose of demonstration
        start_lat, start_lon = 40.7128, -74.0060  # Example: New York
        end_lat, end_lon = 34.0522, -118.2437  # Example: Los Angeles

        # Optimize route
        if st.button("Optimize Route"):
            results_f, results_x = optimize_route(processed_weather, processed_ship)
            st.write("Optimal Route Found:", results_x)
            st.write("Objective Values (Fuel, Safety):", results_f)

            # Display route on a map
            m = folium.Map(location=[start_lat, start_lon], zoom_start=5)
            folium.Marker([start_lat, start_lon], popup="Start").add_to(m)  # Start Port
            folium.Marker([end_lat, end_lon], popup="End").add_to(m)  # End Port
            folium_static(m)
else:
    st.write("Please enter both start and end ports.")
