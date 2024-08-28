import json
import requests
import folium

# Get ISS data from the API
response = requests.get("http://api.open-notify.org/iss-now.json").text

# Parse the JSON data
data = json.loads(response)

# Convert latitude and longitude to float from data
longitude, latitude = data["iss_position"].values()

latitude = float(latitude)
longitude = float(longitude)

# Create a map object
map = folium.Map(location=[latitude, longitude], zoom_start=3)

# Add a marker for the ISS
iss_marker = folium.Marker([latitude, longitude], popup="ISS")
iss_marker.add_to(map)

# Show the map in a browser
map.show_in_browser()
