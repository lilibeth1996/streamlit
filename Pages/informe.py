import pandas as pd
import utilidades as util
import streamlit as st
from matplotlib import pyplot as plt
import seaborn as sns

#configuramos encabezados de la pagina
st.set_page_config(
    page_title= "Informe de la liga",
    page_icon="📝",
    initial_sidebar_state="expanded",
    layout= "centered"
)

util.generarMenu()

#visualizacion 
st.title("Datos de la liga colombiana 2024")
ruta="Data\\tctClean.csv"
df = pd.read_csv(ruta)
tex=("Cantidad de Goles Marcados por cada equipo")
util.informeDatos(df,tex)






