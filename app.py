import pandas as pd
import streamlit as st

st.set_page_config(page_title="Minería de datos · Centro de control", page_icon="📊", layout="wide")

st.title("Proyecto de minería de datos · Centro de control")
st.write(
    "Aplicación del grupo con **tres modelos** construidos sobre datos de un centro de control de energía. "
    "Usa el menú de la izquierda para abrir cada modelo. Esta página es solo **informativa**: "
    "describe el contexto de cada equipo de trabajo, que es la variable que conecta las bases de datos del proyecto."
)

# ---------------------------------------------------------------- Modelos
st.subheader("Modelos del proyecto")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**1 · Clustering**")
    st.caption("Agrupa los registros en clusters con comportamientos parecidos.")
    st.page_link("pages/1_Clustering.py", label="Abrir modelo 1")
with c2:
    st.markdown("**2 · Regresión: duración de llamadas**")
    st.caption("Estima la duración esperada de una llamada según equipo, hora, día y dirección.")
    st.page_link("pages/2_Regresion_Duracion_Llamadas.py", label="Abrir modelo 2")
with c3:
    st.markdown("**3 · Predicción**")
    st.caption("Modelo predictivo del segundo integrante del grupo.")
    st.page_link("pages/3_Prediccion.py", label="Abrir modelo 3")

# ---------------------------------------------------------------- Contexto por equipo
st.subheader("Contexto por equipo de trabajo")

resumen = pd.read_csv("datos/resumen_equipo.csv")
por_franja = pd.read_csv("datos/resumen_equipo_franja.csv")

equipo = st.selectbox("Equipo de trabajo", resumen["equipo"])
fila = resumen[resumen["equipo"] == equipo].iloc[0]

m1, m2, m3, m4 = st.columns(4)
m1.metric("Llamadas registradas", f"{int(fila['llamadas']):,}".replace(",", "."))
m2.metric("Llamadas contestadas", f"{fila['pct_contestadas']:.0f} %")
m3.metric("Duración promedio", f"{fila['duracion_media']:.0f} s")
m4.metric("Duración mediana", f"{fila['duracion_mediana']:.0f} s")

st.markdown("**Duración promedio por franja horaria (llamadas contestadas)**")
franja = (por_franja[por_franja["equipo"] == equipo]
          .set_index("franja")["duracion_media"]
          .reindex(["Mañana", "Tarde", "Noche"]))
st.bar_chart(franja)

st.markdown("**Clusters de este equipo**")
st.info(
    "Pendiente: aquí se mostrará la descripción de los clusters asociados a este equipo de trabajo "
    "(la completa el responsable del modelo 1)."
)
