import streamlit as st

st.title("Crediplano")

valor = st.number_input("Valor em dívida")
meses = st.slider("Quantos meses faltam?", 1, 480)
spread = st.slider("Qual o spread?", 0.0, 5.0)/100
juros = st.slider("Qual a taxa de juro?", 0.0, 10.0)/100

def monthly_fee(annual_fee, debt):
	return debt*annual_fee/12

def monthly_payment(debt, periods, spread, fee):
	rate = (fee+spread)/12
	return rate*debt/(1-(1+rate)**(-periods))

mfee = monthly_fee(spread+juros, valor)
mpay = monthly_payment(valor, meses, spread, juros)

st.write("Prestação: ", mpay)
st.write("Juros: ", mfee)
st.write("Amortização: ", mpay-mfee)