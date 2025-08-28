import streamlit as st

# Gravity constants
GRAVITY = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Earth": 1.0,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14,
}

# Streamlit UI
st.title("🌍 Planetary Weight Calculator")

# Input from user
earth_weight = st.number_input("Enter your weight on Earth (lbs):", min_value=0.0, step=1.0)

# Planet selector
planet = st.selectbox("Select a planet:", list(GRAVITY.keys()))

# Calculate weight
if st.button("Calculate Weight"):
    gravity_constant = GRAVITY[planet]
    planet_weight = round(earth_weight * gravity_constant, 2)
    st.success(f"Your weight on **{planet}** is **{planet_weight} lbs**.")
