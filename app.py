import streamlit as st
import pandas as pd
from whr_model import run_whr_model

st.title("🔥 Thermosyphon-Pro FINAL (Structured)")

# -----------------------------
# INPUTS
# -----------------------------
gas_flow = st.sidebar.number_input("Gas Flow (kg/hr)", value=12820.0)
Tg_in = st.sidebar.slider("Gas Inlet Temp (°C)", 50, 400, 140)

air_flow = st.sidebar.number_input("Air Flow (kg/hr)", value=10000.0)
Ta_in = st.sidebar.slider("Air Inlet Temp (°C)", 20, 80, 30)

rows = st.sidebar.slider("Rows", 5, 25, 15)
cols = st.sidebar.slider("Columns", 20, 200, 100)

pipe_dia = st.sidebar.number_input("Pipe Diameter (m)", value=0.03)
pipe_length = st.sidebar.number_input("Pipe Length (m)", value=1.48)

# -----------------------------
# RUN MODEL
# -----------------------------
Q_total, Tg_out, Ta_out, data = run_whr_model(
    gas_flow, air_flow, Tg_in, Ta_in,
    rows, cols, pipe_dia, pipe_length
)

# -----------------------------
# OUTPUT
# -----------------------------
st.header("📊 RESULTS")

st.write(f"Heat Recovery: {int(Q_total)} kW")
st.write(f"Gas Outlet: {int(Tg_out)} °C")
st.write(f"Air Outlet: {int(Ta_out)} °C")

df = pd.DataFrame(data, columns=[
    "Row","Gas Temp","Air Temp","ΔT","Q_pipe (kW)","Heat Flux"
])

st.dataframe(df)

st.line_chart({
    "Gas Temp": df["Gas Temp"],
    "Air Temp": df["Air Temp"]
})