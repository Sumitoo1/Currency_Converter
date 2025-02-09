import streamlit as st
import requests

# Function to get exchange rates
def get_exchange_rate(base_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url).json()
    return response.get('rates', {})

# Function to convert currency
def convert_currency(amount, from_currency, to_currencies):
    rates = get_exchange_rate(from_currency)
    results = []
    for currency in to_currencies:
        rate = rates.get(currency)
        if rate:
            converted_amount = round(amount * rate, 2)
            results.append(f"{converted_amount} {currency}")
        else:
            results.append(f"Error fetching rate for {currency}")
    return "\n".join(results)

# Apply new background image and adjust text visibility
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1625225233840-695456021cde?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>select, .stMultiselect>div>div>div, .stButton>button, .stMarkdown, .stText {
        background-color: rgba(255, 255, 255, 0.9) !important;  /* Semi-transparent white background */
        padding: 10px;
        border-radius: 10px;
        color: black !important;  /* Ensure text color is black */
        border: 1px solid #ccc !important;  /* Add border for better visibility */
    }
    .stTitle {
        color: white;
        background-color: rgba(0, 0, 0, 0.8);  /* Semi-transparent black background */
        padding: 10px;
        border-radius: 10px;
    }
    .stMarkdown {
        color: black;  /* Ensure markdown text is black */
    }
    .stButton>button {
        color: white !important;
        background-color: #4CAF50 !important;  /* Green background for buttons */
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049 !important;  /* Darker green on hover */
    }
    .stNumberInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: black !important;
        border: 1px solid #ccc !important;
    }
    .stSelectbox>div>div>select, .stMultiselect>div>div>div {
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: black !important;
        border: 1px solid #ccc !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit App
st.title("💰 Simple Currency Converter")

amount = st.number_input("Enter Amount:", min_value=0.0, value=1.0, step=0.1)
from_currency = st.selectbox("From Currency:", ["USD", "EUR", "CNY", "JPY", "GBP", "INR"])
to_currencies = st.multiselect("To Currencies (You can select multiple options):", ["USD", "EUR", "CNY", "JPY", "GBP", "INR"])

if st.button("Convert"):
    if not to_currencies:
        st.error("Please select at least one currency to convert to!")
    else:
        result = convert_currency(amount, from_currency, to_currencies)
        st.text(f"{amount} {from_currency} converts to:")
        for line in result.split("\n"):
            st.text(line)

st.markdown("---")