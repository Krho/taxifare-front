import streamlit as st
import folium as fl
from streamlit_folium import st_folium

import requests

from datetime import datetime

def get_pos(lat,lng):
    return lat,lng

st.set_page_config(
    page_icon="🚕",
    page_title="Taxifare"
)

HEIGHT = 350
WIDTH = 700

"# 🚕 Our beautiful front"


"## Trajectory"

start_lat = st.number_input("Lattitude start", -73.950655)
start_long = st.number_input("Longitude start", 40.783282)


end_lat = st.number_input("Lattitude end", -73.984365)
end_long = st.number_input("Longitude end", 40.769802)


# m = fl.Map(location=[48.859, 2.378], zoom_start=13)

# m.add_child(fl.LatLngPopup())

# out = st_folium(m, width=WIDTH, height=HEIGHT, key="map")

# st.session_state.current='start'
# st.session_state.start = "?"
# st.session_state.destination = "?"

# st.write(f"going from {st.session_state["start"]} to {st.session_state["destination"]}")

# st.session_state.click = out.get("last_clicked")
# if st.session_state.click:
#     st.write("Hello")
#     coords = (st.session_state.click["lat"], st.session_state.click["lng"])
#     if st.session_state.current == "start":
#         st.write("Darkness")
#         st.session_state.start = coords
#         st.session_state.current = "destination"
#         st.session_state.click = None
#     else:
#         st.write("My old friend")
#         st.session_state.destination = coords
#         st.session_state.current = "start"
#         st.session_state.click = None
#     st.rerun()

# st.write(st.session_state.current)


"## Additionnal info"

input_time = st.datetime_input(
    "Pickup time",
    datetime(2025, 11, 19, 16, 45),
)
passenger_count = st.slider("Number of passengers", 1, 8, 1)

"# Prediction"


api = st.secrets["URL"]
params = {
    'pickup_datetime': str(input_time),
    'pickup_longitude': start_long,
    'pickup_latitude':  start_lat,
    'dropoff_longitude': end_long,
    'dropoff_latitude': end_lat,
    'passenger_count': str(passenger_count)
    }


if st.button('Get Prediction'):

    response = requests.get(api, params)

    if response.status_code != 200:
        st.write('Something went wrong during request ', response.status_code, response.text)
    else:
        prediction = response.json()["fare"]
        st.write(f'The current prediction is **{str(prediction)}**.')

else:
    st.write("You don't have a prediction yet...")
