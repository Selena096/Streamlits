import streamlit as st
import pandas as pd

df = pd.read_csv('titanic_data.csv')

def main():
 st.title("Curso de Streamlit")
 st.header("Dataframe:")
 st.dataframe(df)
             
 st.header("Esto es un encabezado")
 st.header("Esto es un sub encabezado")
 st.text("Hola, esto es un texto")



 Nombre = "Talentotech"
 st.text(f"Saludos desde {Nombre}, esto es un texto")
 st.markdown("### Esto es un makdown")

 st.success ("Éxito")
 st.warning("Esto es una advertencia")
 st.info("Esto es información")
 st.error("Esto es un error")
 st.exception("Esto es una excepción")



if __name__ == '__main__':
 main()