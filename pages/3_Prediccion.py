import streamlit as st

st.set_page_config(page_title="Modelo 3 · Predicción", layout="wide")
st.title("Modelo 3 · Predicción")
st.info("Esta página está reservada para el modelo predictivo del segundo integrante. Pendiente: integrante responsable.")

st.markdown(
    """
**Cómo completarla**
1. Guardar el modelo con la misma estructura del profesor:
   `pickle.dump([modelo, scaler, variables], open("modelos/modelo_prediccion.pkl", "wb"))`
2. Reemplazar el contenido de este archivo por el formulario y la predicción.
   Se puede copiar la estructura de `pages/2_Regresion_Duracion_Llamadas.py`:
   cargar el modelo, armar el dataframe, preparar con `get_dummies` + `reindex` + `scaler.transform` y mostrar el resultado.
3. Mantener los mismos nombres de variables y categorías que se usaron al entrenar.
"""
)
