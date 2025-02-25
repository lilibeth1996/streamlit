import pandas as pd
import utilidades as util
import streamlit as st
from PIL import Image




#pagina de presentacion 
st.set_page_config(
    page_title="Info Liga Colombiana",
    initial_sidebar_state="expanded",
    layout="wide",
    page_icon="🦚"
)

#llamamos la funcion
util.generarMenu()

#estructura de presentacion
left_col, center_col, right_col= st.columns([1,4,1], vertical_alignment= "center")

#edito columna central
with center_col: 
    st.title("Informe de la Liga Colombiana 2024 - 2")
    st.write( """
             En este espacio ponemos mostrar el desempeño de los equipos durante la liga BetPlay 2024-2
             en la pagina informes se puede observar los datos y sus analisis.
             """)
    imagen2= Image.open("Media\\balon.jpg")
    st.image(imagen2,use_container_width=True, width=500,
             caption="Selección Colombia")
