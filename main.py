import streamlit as st
from currencies.parse import Currency

st.set_page_config(page_title="Exchange Calculator", page_icon="💸")

st.markdown(
    "### Want know how much you need give to the bank for needed amount of currency?"
)

st.markdown(
    "Calculate this for free! Just select amount, two currencies and that's all."
)

currency = Currency()
supported = currency.get_supported_currencies()

from_currency = st.selectbox("From currency", supported)

to_currency_options = [curr for curr in supported if curr != from_currency]
to_currency = st.selectbox("To currency", to_currency_options)

amount = st.number_input(label="Enter amount", step=0.01, max_value=float(1_000_000))

if st.button("Check amount"):
    clean_amount = abs(amount)
    result = currency.convert(
        from_curr=from_currency, to_curr=to_currency, amount=clean_amount
    )
    if result is not None:
        st.markdown(
            f"### 💰 {clean_amount} {from_currency} = **{result:.2f} {to_currency}**"
        )
    else:
        st.error("Conversion failed.")
