import streamlit as st
from src.screens.Pandas.pandas import *

st.header("Nubes de palabras")
st.balloons()

st.subheader("Nube de palabras de todas las etiquetas")
fig_nube_tags = nube_de_palabras()
fig_nube_tags.savefig('nube_de_palabras_tags.png')
st.image("nube_de_palabras_tags.png")


st.header("Gráficos de torta")
st.balloons()

st.subheader("Gráfico de los tipos de archivos utilizados")
figura_tipos = graf_torta_tipos()
figura_tipos.savefig('grafico_torta_tipo.png')
st.image("grafico_torta_tipo.png")

st.header("Tablas")
st.balloons()

st.subheader("Etiquetas más usadas")
tabla_ranking_tags = ranking_tags()
st.table(tabla_ranking_tags)

st.subheader("Tamaño en MB promedio de las imágenes actualizadas por cada perfil")
tabla_usuarios_imagenes_act = usuarios_imagenes_act()
st.table(tabla_usuarios_imagenes_act)

st.subheader("Gráfico de dispersión")
fig_graf_disp = graf_disp()
fig_graf_disp.savefig('grafico_de_dispercion.png')
st.image("grafico_de_dispercion.png")


st.header("Gráficos de líneas")
st.balloons()


st.subheader("Gráfico de días")
fig_graf_dias = graf_dias()
fig_graf_dias.savefig("GraficoDias.png")
st.image("GraficoDias.png")