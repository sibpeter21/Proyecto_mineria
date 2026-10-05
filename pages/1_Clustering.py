import streamlit as st

st.set_page_config(page_title="Modelo 1 · Clustering", layout="wide")
st.title("Modelo 1 · Clustering")
st.info("Esta página está reservada para el modelo de clustering. Pendiente: integrante responsable.")

st.markdown(
    """
**Cómo completarla**
1. Entrenar el modelo en su notebook y guardarlo con la misma estructura del profesor:
   `pickle.dump([modelo, scaler, variables], open("modelos/modelo_clustering.pkl", "wb"))`
2. Reemplazar el contenido de este archivo por el formulario y la predicción (plantilla abajo).
3. Si el modelo usa `equipo de trabajo`, usar los mismos nombres de equipo de la base de llamadas
   (Gestión Daños, Operación Distribución, Operación Transmisión) para poder conectar las dos bases.
"""
)

PLANTILLA = '''
import pickle
import pandas as pd
import streamlit as st

modelo, scaler, variables = pickle.load(open("modelos/modelo_clustering.pkl", "rb"))

# 1. Formulario (un widget por variable)
# edad = st.slider("Edad", 14, 52, 20)
# ...

# 2. Dataframe con los mismos nombres de variables del notebook
# data = pd.DataFrame([[edad, ...]], columns=["edad", ...])

# 3. Preparación: get_dummies con drop_first=False, reindex y scaler.transform (sin fit)
# data_preparada = pd.get_dummies(data, columns=[...], drop_first=False, dtype=int)
# data_preparada = data_preparada.reindex(columns=variables, fill_value=0)
# data_preparada[[...]] = scaler.transform(data_preparada[[...]])

# 4. Resultado
# cluster = modelo.predict(data_preparada)[0]
# st.metric("Cluster asignado", cluster)
'''
st.code(PLANTILLA, language="python")
