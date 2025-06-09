import streamlit as st
from currencies.parse import Currency


st.set_page_config(page_title='Excange Calculator', page_icon='💸')

st.markdown("**Want know how much you need give to the bank for needed amount of currency?** Calculate this on my Currency-Calculator! Just select amount, two currencies and thats all!")


# Choise the currency
from_currency = st.selectbox("From currency", ['USD', 'UAH', 'RUB'])

to_currency_options = [curr for curr in ['USD', 'UAH', 'RUB'] if curr != from_currency]

to_currency = st.selectbox("To currency", to_currency_options)

amount = st.number_input(
    label="Enter amount", 
    step=0.01, 
    max_value=float(9_007_199_254_740_991)
)
if st.button("Check amount"):
    currency = Currency()
    clean_amount = abs(amount)
    result = currency.convert(
        to_curr=to_currency, 
        from_curr=from_currency,
        amount=clean_amount
    )
    print("DEBUG amount: ", clean_amount)
    if result is not None:
        st.markdown(f"### 💰 {clean_amount} {from_currency} = **{result:.2f} {to_currency}**")
    else:
        st.error("Conversion failed.")
