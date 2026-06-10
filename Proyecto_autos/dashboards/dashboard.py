import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# Configuración de página
st.set_page_config(
    page_title="Dashboard de Vehículos",
    page_icon="🚗",
    layout="wide"
)

# Rutas
BASE_DIR = Path(__file__).resolve().parent.parent

csv_path = (
    BASE_DIR
    / "data"
    / "processed"
    / "dataset_final.csv"
)

# Cargar datos
df = pd.read_csv(csv_path)

# Título
st.title(" Dashboard de Análisis de Vehículos")

st.markdown(
    "Visualización interactiva de ventas y características de vehículos."
)

# Sidebar
st.sidebar.header("Filtros")

marcas = sorted(df["Make"].dropna().unique())

marca_seleccionada = st.sidebar.multiselect(
    "Marca",
    marcas,
    default=marcas
)

combustibles = sorted(
    df["Fuel Type"].dropna().unique()
)

combustible_seleccionado = st.sidebar.multiselect(
    "Tipo de Combustible",
    combustibles,
    default=combustibles
)

# Aplicar filtros
df_filtrado = df[
    (df["Make"].isin(marca_seleccionada))
    &
    (df["Fuel Type"].isin(combustible_seleccionado))
]

vista = st.sidebar.radio(
    "Seleccionar Vista",
    ["Ejecutiva", "Técnica"]
)

if vista == "Ejecutiva":

    st.header("Resumen Ejecutivo")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Vehículos",
        len(df_filtrado)
    )

    col2.metric(
        "Precio Promedio USD",
        round(df_filtrado["precio_usd"].mean(), 2)
    )

    col3.metric(
        "Precio Máximo USD",
        round(df_filtrado["precio_usd"].max(), 2)
    )

if vista == "Técnica":

    st.header("Análisis Técnico")

    st.dataframe(df_filtrado)

    st.write(df_filtrado.describe())

# Métricas
col1, col2, col3 = st.columns(3)

col1.metric(
    "Vehículos",
    len(df_filtrado)
)

col2.metric(
    "Precio promedio USD",
    round(df_filtrado["precio_usd"].mean(), 2)
)

col3.metric(
    "Precio promedio EUR",
    round(df_filtrado["precio_eur"].mean(), 2)
)

# Gráfico 1
st.subheader("Cantidad de Vehículos por Marca")

marca_count = (
    df_filtrado["Make"]
    .value_counts()
    .reset_index()
)

marca_count.columns = [
    "Marca",
    "Cantidad"
]

fig1 = px.bar(
    marca_count,
    x="Marca",
    y="Cantidad"
)

st.plotly_chart(
    fig1,
    width="stretch"
)

# Gráfico 2
st.subheader("Distribución de Precios")

fig2 = px.histogram(
    df_filtrado,
    x="precio_usd",
    nbins=30
)

st.plotly_chart(
    fig2,
    width="stretch"
)

# Gráfico 3
st.subheader("Precio Promedio por Combustible")

fuel_avg = (
    df_filtrado
    .groupby("Fuel Type")["precio_usd"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    fuel_avg,
    x="Fuel Type",
    y="precio_usd"
)

st.plotly_chart(
    fig3,
    width="stretch"
)

# Tabla
st.subheader("Datos Filtrados")

st.dataframe(
    df_filtrado,
    width="stretch"
)

transmision = (
    df_filtrado["Transmission"]
    .value_counts()
    .reset_index()
)

transmision.columns = [
    "Transmisión",
    "Cantidad"
]

fig4 = px.pie(
    transmision,
    names="Transmisión",
    values="Cantidad",
    title="Distribución por Transmisión"
)

st.plotly_chart(
    fig4,
    width="stretch"
)

ubicacion = (
    df_filtrado["Location"]
    .value_counts()
    .head(10)
    .reset_index()
)

ubicacion.columns = [
    "Ubicación",
    "Cantidad"
]

fig5 = px.bar(
    ubicacion,
    x="Ubicación",
    y="Cantidad",
    title="Top 10 Ubicaciones"
)

st.plotly_chart(
    fig5,
    width="stretch"
)