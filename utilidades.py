import pandas as pd
import streamlit as st
from  PIL import Image
from matplotlib import pyplot as plt
import seaborn as sns


def generarMenu():
    with st.sidebar:
        col1, col2=st.columns(2)
        with col1:
            Imagen=Image.open("Media/dimayor.png")
            st.image(Imagen,use_container_width=False, width=80)
        with col2:
            st.header('Liga Betplay 2024',)
            st.page_link('app.py', label='Home', icon='🏡')
            st.page_link("Pages\informe.py", label="informe", icon="🏷️")


def informeDatos(df, titulo):
    df2=pd.DataFrame(df)
    #configuramos la visualizacion
    col1, col2, col3= st.columns([0.5,5,0.5],
                             vertical_alignment="top")
    with col2:

        st.markdown(titulo)
        df2.set_index("Local",inplace=True)
        st.write(df2, unsafe_allow_html=False)
        st.markdown("Grafico de Barras")

        sns.set_style('whitegrid')
        total=df2.groupby('Local')[['Goles Local',
                                    'goles Visitantes']].sum()

        goles=pd.DataFrame(total)
        goles['Goles Total']=goles['Goles Local'] + goles['goles Visitantes']
        goles=goles.reset_index()

        resultado=goles.groupby(['Local']).sum()
        resultado.plot(kind='bar', figsize=(10,10))
        plt.tight_layout()
        st.pyplot(plt)




   


