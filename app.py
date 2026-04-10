import streamlit as st
import pandas as pd

# API response (your data)
api_response = {
    "train_name": "Rajdhani Express",
    "train_number": "12301",
    "route": [
        {"station": "New Delhi",      "arrival": "Source",      "departure": "07:05"},
        {"station": "Kanpur Central", "arrival": "10:10",       "departure": "10:15"},
        {"station": "Allahabad Jn",   "arrival": "12:00",       "departure": "12:10"},
        {"station": "Patna Jn",       "arrival": "16:30",       "departure": "16:40"},
        {"station": "Howrah Jn",      "arrival": "21:30",       "departure": "Destination"}
    ]
}

# Title
st.title("🚆 Train Route Dashboard")

# Train Info
st.subheader("Train Information")
st.write(f"**Train Name:** {api_response['train_name']}")
st.write(f"**Train Number:** {api_response['train_number']}")

# Convert route to DataFrame
df = pd.DataFrame(api_response["route"])

# Show Table
st.subheader("📍 Route Details")
st.dataframe(df)

# Station Selector
st.subheader("🔍 Search Station")
station = st.selectbox("Select Station", df["station"])

# Display Selected Station Info
selected = df[df["station"] == station].iloc[0]

st.write("### Station Details")
st.write(f"📍 Station: {selected['station']}")
st.write(f"⏰ Arrival: {selected['arrival']}")
st.write(f"🚆 Departure: {selected['departure']}")

# Timeline view
st.subheader("🛤️ Journey Timeline")
for i, row in df.iterrows():
    st.write(f"{i+1}. {row['station']} | Arrival: {row['arrival']} | Departure: {row['departure']}")
