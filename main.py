import streamlit as st
import pandas as pd

st.title("Crediplano")

valor = st.sidebar.number_input("Valor em dívida", value=200000)
meses = st.sidebar.number_input("Quantos meses faltam?", value=480)
spread = st.sidebar.number_input("Qual o spread?", value=1.0)/100
juros = st.sidebar.number_input("Qual a taxa de juro?", value=1.0, step=0.001, format="%5.3f")/100

def monthly_fee(annual_fee, debt):
	return debt*annual_fee/12

def monthly_payment(debt, periods, spread, fee):
	rate = (fee+spread)/12
	return rate*debt/(1-(1+rate)**(-periods))

mfee = monthly_fee(spread+juros, valor)
mpay = monthly_payment(valor, meses, spread, juros)

st.write("Prestação: {:.2f}".format(mpay))
st.write("Juros: {:.2f}".format(mfee))
st.write("Amortização: {:.2f}".format(mpay-mfee))

months = [i for i in range(1, meses+1)]

m_fee = []
m_pay = []
m_debt = []

for m in range(1, meses+1):
	mfee = monthly_fee(spread+juros, valor)
	m_amort = mpay-mfee
	valor = valor - m_amort
	m_debt.append(valor)
	m_fee.append(mfee)
	m_pay.append(mpay)

dict_df = {"Mês": months, "Prestação": m_pay, "Juros": m_fee, "Dívida": m_debt}
df = pd.DataFrame(dict_df)

df["Amortização"] = df["Prestação"] - df["Juros"]
df = df[["Mês", "Prestação", "Juros", "Amortização", "Dívida"]]

st.dataframe(df.round(2))