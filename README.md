# App Streamlit · Proyecto de minería de datos (Centro de control)

App del grupo con **tres modelos**, una página por modelo.

| Página | Archivo | Responsable | Estado |
|---|---|---|---|
| Inicio (informativa, contexto por equipo de trabajo) | `app.py` | grupo | Listo |
| 1 · Clustering | `pages/1_Clustering.py` | _(compañero/a)_ | Pendiente |
| 2 · Regresión: duración de llamadas | `pages/2_Regresion_Duracion_Llamadas.py` | _(tu nombre)_ | Listo |
| 3 · Predicción | `pages/3_Prediccion.py` | _(compañero/a)_ | Pendiente |

## Estructura

```
app.py                                   # página de inicio (informativa)
pages/                                   # una página por modelo
modelos/
    modelo_regresion_llamadas.pkl        # [modelo, scaler, variables]
    metricas_regresion_llamadas.json
datos/
    resumen_equipo.csv                   # resúmenes agregados, sin datos personales
    resumen_equipo_franja.csv
requirements.txt
```

## Ejecutar en el computador

```
pip install -r requirements.txt
streamlit run app.py
```

## Publicar (GitHub + Streamlit Community Cloud)

1. Subir esta carpeta a un repositorio de GitHub (`app.py` en la raíz).
2. En share.streamlit.io: *New app* → elegir el repositorio, rama `main` y archivo `app.py`.
3. Tomar el pantallazo de la app publicada para la rúbrica.

## Cómo agregar un modelo nuevo

1. En el notebook: `pickle.dump([modelo, scaler, variables], open("modelos/modelo_xxx.pkl", "wb"))`.
2. Copiar el `.pkl` a `modelos/` y editar solo la página que le corresponde en `pages/`
   (la de regresión sirve de ejemplo: cargar, armar dataframe, `get_dummies` + `reindex` + `scaler.transform`, predecir).
3. Cada integrante edita únicamente su archivo para no generar conflictos en GitHub.

## Importante: versiones

Un `.pkl` solo se carga bien con la **misma versión de scikit-learn** con la que se creó.
El notebook imprime la versión al guardar el modelo. Si lo vuelven a ejecutar en otro entorno (por ejemplo Colab),
actualicen la línea `scikit-learn==...` de `requirements.txt` con esa versión y suban el `.pkl` nuevo.
