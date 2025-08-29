# 🌍 AI-Powered Carbon Footprint Tracker

A Streamlit-based web application that helps users estimate and visualize their annual carbon footprint based on various lifestyle choices such as transportation, electricity usage, diet, flights, and more. The app also provides AI-powered tips for reducing emissions and rewards users with **Green Points** for sustainable habits.

---

## 🚀 Features

- **User-Friendly Interface**: Interactive sliders and input fields for easy data entry.
- **Personalized Emission Calculation**: Calculates emissions across multiple categories based on user inputs and country-specific emission factors (currently supports India).
- **Visual Insights**: Horizontal bar chart to visualize carbon emissions breakdown.
- **Green Points System**: Encourages users to reduce their carbon footprint with a gamified point-based reward system.
- **Sustainability Tips**: Smart suggestions for reducing emissions based on the user's lifestyle patterns.

---

## 🧮 Emission Categories & Calculations

The app calculates emissions in **tonnes of CO₂ per year** for the following categories:

| Category        | Input Type                | Calculation Details |
|----------------|---------------------------|---------------------|
| Transportation | Daily commute distance     | `distance * 365 * factor / 1000` |
| Electricity    | Monthly kWh consumption    | `consumption * 12 * factor / 1000` |
| Diet           | Meals per day & diet type | `meals * 365 * diet_factor / 1000` |
| Waste          | Weekly waste generated     | `waste * 52 * factor / 1000` |
| Flights        | Short & long-haul flights  | `flights * flight_factor` |
| Clothing       | Clothing items per year    | `items * factor / 1000` |
| Electronics    | Electronic devices per year| `items * factor / 1000` |
| Plastic Usage  | Weekly single-use items    | `items * 52 * factor / 1000` |

All emission factors are based on average values for India.

---

## 🏆 Green Points

Your annual carbon footprint is compared to the Indian per capita average (1.9 tonnes/year). If your emissions are lower, you earn Green Points:


---

## 📊 Visualization

- A **horizontal bar chart** shows the emissions by category using `matplotlib`.
- Helps users quickly identify their highest-impact habits.

---

## 💡 AI-Powered Sustainability Tips

Based on your input data, the app provides relevant suggestions such as:
- Using public transport or cycling
- Switching to renewable energy
- Adopting a plant-based diet
- Reducing single-use plastic and household waste

---

## 🛠️ How to Run

1. **Install Dependencies**

```bash
pip install streamlit matplotlib



