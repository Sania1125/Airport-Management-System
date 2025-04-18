# Create a basic Streamlit interface for the Airport Management System
streamlit_code = """
import streamlit as st
from airport import Flight, Passenger

st.set_page_config(page_title="Airport Management System", layout="centered")

st.title("✈️ Airport Management System")

# Create a flight
if 'flight' not in st.session_state:
    st.session_state.flight = Flight("PK303", "Karachi", "Lahore", 2)

flight = st.session_state.flight

st.subheader("📄 Flight Info")
st.write(f"**Flight Number**: {flight.flight_number}")
st.write(f"**From**: {flight.origin}")
st.write(f"**To**: {flight.destination}")
st.write(f"**Capacity**: {flight.capacity}")
st.write(f"**Seats Booked**: {len(flight.passengers)}")

st.subheader("🧍 Passenger Booking")

with st.form("booking_form"):
    name = st.text_input("Passenger Name")
    passport = st.text_input("Passport Number")
    submitted = st.form_submit_button("Book Seat")

    if submitted:
        if name and passport:
            passenger = Passenger(name, passport)
            message = flight.book_passenger(passenger)
            st.success(message) if "✔" in message else st.error(message)
        else:
            st.warning("Please enter both name and passport number.")

st.subheader("🧾 Passenger Manifest")
st.write(flight.show_manifest())
"""

# Save the Streamlit script
streamlit_path = "/mnt/data/airport-management-system/streamlit_app.py"
with open(streamlit_path, "w") as f:
    f.write(streamlit_code)

streamlit_path
