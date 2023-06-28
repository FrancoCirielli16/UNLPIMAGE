import streamlit as st
from src.screens.Pandas.pandas import *

# Configuración de la página
st.set_page_config(layout="wide", page_title="UNLP Image Stats")

# Título y efectos visuales
st.balloons()
st.title("Estadísticas")
st.divider()

# Encabezados y subtítulos
st.header("Nubes de palabras")
st.balloons()


st.subheader("Nube de palabras de los títulos de los collages")
fig_nube_collages = nube_de_palabras_collages()
fig_nube_collages.savefig('nube_de_palabras_collage.png')
st.image("nube_de_palabras_collage.png")


st.header("Gráficos de torta")
st.balloons()

st.subheader("Operaciones por género")
figura_generos = graf_torta_generos()
figura_generos.savefig('grafico_torta_generos.png')
st.image("grafico_torta_generos.png")

st.subheader("Uso por género")
figura_uso_genero = graf_torta_uso_genero()
figura_uso_genero.savefig('grafico_torta_uso_generos.png')
st.image("grafico_torta_uso_generos.png")

# Gráficos de barras
st.header("Gráficos de barras")
st.balloons()

st.subheader("Cantidad de cada operación realizada")
fig_graf_operaciones = grafico_operaciones()
fig_graf_operaciones.savefig('grafico_operaciones_uso.png')
st.image("grafico_operaciones_uso.png")

st.subheader("Gráfico de barras apilado de operaciones")
fig_graf_operaciones_por_nick = grafico_operaciones_por_nick()
fig_graf_operaciones_por_nick.savefig('grafico_barra_operaciones_uso.png')
st.image("grafico_barra_operaciones_uso.png")

# Tablas
st.header("Tablas")
st.balloons()

st.subheader("Ranking de imágenes más usadas en generador de memes")
tabla_ranking_memes = ranking_memes()
st.table(tabla_ranking_memes)

st.subheader("Ranking de imágenes más usadas en generador de collages")
tabla_ranking_collage = ranking_collage()
st.table(tabla_ranking_collage)



# Gráficos de líneas
st.header("Gráficos de líneas")
st.balloons()

st.subheader("Gráfico lineal")
fig_graf_lineal = graf_lineal()
fig_graf_lineal.savefig("FiguraEst.png")
st.image("FiguraEst.png")

