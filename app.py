import streamlit as st
import matplotlib.pyplot as plt

# Define emission factors
EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,
        "Electricity": 0.82,
        "Diet": {"Vegan": 1.0, "Vegetarian": 1.5, "Omnivore": 2.5, "Heavy Meat": 3.5},
        "Waste": 0.1,
        "Flights": {"Short-haul": 0.2, "Long-haul": 1.0},
        "Clothing": 30,
        "Electronics": 150,
        "Plastic Usage": 0.02,
    }
}

# Set layout
st.set_page_config(layout="wide", page_title="AI-Powered Carbon Footprint Tracker")
st.title("AI-Powered Carbon Footprint Tracker 🌍")

# User inputs
st.subheader("🌍 Your Country")
country = st.selectbox("Select", ["India"])

col1, col2 = st.columns(2)
with col1:
    distance = st.slider("🚗 Daily commute distance (km)", 0.0, 100.0)
    electricity = st.slider("💡 Monthly electricity consumption (kWh)", 0.0, 1000.0)
    short_flights = st.number_input("✈️ Short-haul flights per year", 0)
    long_flights = st.number_input("✈️ Long-haul flights per year", 0)
    clothing_items = st.number_input("🛍️ New clothing items per year", 0)

with col2:
    waste = st.slider("🗑️ Waste generated per week (kg)", 0.0, 100.0)
    meals = st.number_input("🍽️ Meals per day", 0)
    diet_type = st.selectbox("🥦 Diet Type", ["Vegan", "Vegetarian", "Omnivore", "Heavy Meat"])
    electronics_items = st.number_input("📱 New electronic devices per year", 0)
    plastic_usage = st.slider("🛒 Single-use plastic items per week", 0, 100)

# Normalize inputs
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance * 365 / 1000
energy_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity * 12 / 1000
diet_emissions = EMISSION_FACTORS[country]["Diet"][diet_type] * meals * 365 / 1000
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste * 52 / 1000
flight_emissions = (
    EMISSION_FACTORS[country]["Flights"]["Short-haul"] * short_flights +
    EMISSION_FACTORS[country]["Flights"]["Long-haul"] * long_flights
)
clothing_emissions = EMISSION_FACTORS[country]["Clothing"] * clothing_items / 1000
electronics_emissions = EMISSION_FACTORS[country]["Electronics"] * electronics_items / 1000
plastic_emissions = EMISSION_FACTORS[country]["Plastic Usage"] * plastic_usage * 52 / 1000

total_emissions = round(
    transportation_emissions + energy_emissions + diet_emissions + waste_emissions +
    flight_emissions + clothing_emissions + electronics_emissions + plastic_emissions, 2
)

# Carbon credit rewards system
avg_emission_per_capita = 1.9  # Tons CO2 per year (India)
reduction_ratio = max(0, (avg_emission_per_capita - total_emissions) / avg_emission_per_capita)
green_points = round(reduction_ratio * 1000)

if st.button("Calculate & Track CO2 Emissions"):
    st.header("Results")
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {energy_emissions} tonnes CO2 per year")
        st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")
        st.info(f"✈️ Flights: {flight_emissions} tonnes CO2 per year")
        st.info(f"🛍️ Clothing: {clothing_emissions} tonnes CO2 per year")
        st.info(f"📱 Electronics: {electronics_emissions} tonnes CO2 per year")
        st.info(f"🛒 Plastic: {plastic_emissions} tonnes CO2 per year")
    
    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        st.warning(f"India's per capita emissions (2021) were 1.9 tonnes CO2 per year.")
        st.success(f"🎉 You earned {green_points} Green Points for sustainability!")

    # Bar chart for emissions breakdown
    categories = ["Transport", "Electricity", "Diet", "Waste", "Flights", "Clothing", "Electronics", "Plastic"]
    values = [
        transportation_emissions, energy_emissions, diet_emissions, waste_emissions,
        flight_emissions, clothing_emissions, electronics_emissions, plastic_emissions
    ]
    fig, ax = plt.subplots()
    ax.barh(categories, values, color="green")
    ax.set_xlabel("CO2 Emissions (tonnes per year)")
    ax.set_title("Your Carbon Footprint Breakdown")
    st.pyplot(fig)

    # Suggestions for reducing emissions
    st.subheader("AI-Powered Sustainability Tips")
    suggestions = []
    if transportation_emissions > 0.5:
        suggestions.append("🚲 Consider biking or carpooling to reduce transport emissions.")
    if energy_emissions > 1:
        suggestions.append("💡 Switch to energy-efficient appliances or solar power.")
    if diet_emissions > 1:
        suggestions.append("🥗 Try plant-based meals to lower food emissions.")
    if waste_emissions > 0.5:
        suggestions.append("♻️ Reduce, reuse, and recycle more to minimize waste impact.")
    if plastic_emissions > 0.1:
        suggestions.append("🛍️ Use reusable bags, bottles, and containers to cut plastic waste.")
    for tip in suggestions:
        st.info(tip)
    if not suggestions:
        st.success("🎉 You are already making great sustainable choices!")
