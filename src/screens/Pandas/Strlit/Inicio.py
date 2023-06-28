import streamlit as st   
import webbrowser
from src.constants.directions import DATA_DIR
import os
import PIL



url = 'https://gitlab.catedras.linti.unlp.edu.ar/python2023/code/grupo12'
st.header("UNLP IMAGE")
st.divider()
tab1 , tab2 = st.tabs(["Inicio", "Nosotros"])
with tab2:
     st.subheader("GRUPO 12")
     st.write("""
        Somos un grupo de la Universidad Nacional de La Plata compuesto por las siguientes personas :\n
            👉 Francisco Jorge\n
            👉 Franco Cirielli\n
            👉 Eveling \n
            👉 Dylan Vallejos\n
     """)
     img = PIL.Image.open(os.path.join(DATA_DIR,"defaults","ofc.jpg"))
     st.image(img)
     st.subheader("")





with tab1:
    st.write("""
            Esta aplicación web se realizó con el proposito de brindar información sobre 
            los datos utilizados en nuestra aplicación de escritorio


    """)

    if st.button("Descarga nuestra app"):
         webbrowser.open_new_tab(url)

