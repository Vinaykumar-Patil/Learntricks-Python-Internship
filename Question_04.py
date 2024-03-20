'''Currency Converter: Create a currency converter that can convert between different 
currencies based on real-time exchange rates obtained from an API.'''

import streamlit as st
import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangeratesapi.io/latest?base={from_currency}&symbols={to_currency}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        rate = data["rates"][to_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

def main():
    st.title("Currency Converter")

    amount = st.number_input("Enter amount to convert:", min_value=0.01, step=0.01)
    from_currency = st.text_input("Enter currency to convert from (e.g., USD):").upper()
    to_currency = st.text_input("Enter currency to convert to (e.g., EUR):").upper()

    if st.button("Convert"):
        if from_currency and to_currency:
            converted_amount = convert_currency(amount, from_currency, to_currency)
            if converted_amount is not None:
                st.success(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
            else:
                st.error("Conversion failed. Please check your input currencies.")

if __name__ == "__main__":
    main()
