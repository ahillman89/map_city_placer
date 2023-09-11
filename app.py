import folium
from geopy.geocoders import Nominatim
import webbrowser
import os




# List of US cities
us_cities = [
    'Reno, NV',
    'Detroit, MI',
    'San Francisco, CA',
    'Austin, TX',
    'Miami, FL',
    'Seattle, WA',
    'Denver, CO',
    'Chicago, IL',
    'Boston, MA',
    'Nashville, TN'
]

# Function to get latitude and longitude of a city
def get_lat_lon(city):
    geolocator = Nominatim(user_agent="test_app")
    location = geolocator.geocode(city)
    return (location.latitude, location.longitude)

# Create a base map
us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)  # Using the approximate lat-long for the center of US

# Add cities to the map
for city in us_cities:
    lat, lon = get_lat_lon(city)
    tooltip = folium.Tooltip(city)
    folium.Marker([lat, lon], tooltip=tooltip).add_to(us_map)

# Save the map to an HTML file
us_map.save("us_cities_map.html")

# Specify the path to your HTML file
file_path = "us_cities_map.html"  # replace with your path

# Convert it to a URL
url = "file://" + os.path.abspath(file_path)

# Open in default web browser
webbrowser.open(url)
