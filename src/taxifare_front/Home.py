import streamlit as st
import folium as fl
from streamlit_folium import st_folium

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
m = fl.Map(location=[48.859, 2.378], zoom_start=13)

m.add_child(fl.LatLngPopup())

out = st_folium(m, width=WIDTH, height=HEIGHT, key="map")

st.session_state["current"]='start'
st.session_state["start"]= "?"
st.session_state["destination"] = "?"

st.write(f"going from {st.session_state["start"]} to {st.session_state["destination"]}")

last_clicked = out.get("last_clicked")
if last_clicked:
    st.write("Hello")
    coords = (last_clicked["lat"], last_clicked["lng"])
    if st.session_state["current"] == "start":
        st.write("Darkness")
        st.session_state["start"]= coords
        st.session_state["current"] = "destination"
    else:
        st.write("My old friend")
        st.session_state["destination"] = coords
        st.session_state["current"] = "start"
    st.rerun()

st.write(st.session_state["current"])


"## Additionnal info"

input_time = st.datetime_input(
    "Pickup time",
    datetime(2025, 11, 19, 16, 45),
)
passenger_count = st.slider("Number of passengers", 1, 8, 1)
