import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📊 Mi primera Web con Streamlit")
st.write("Esta página se genera completamente desde Python en tiempo real.")

opcion = st.selectbox("Elige una función matemática:", ["Seno", "Coseno"])
frecuencia = st.slider("Ajusta la Frecuencia:", min_value=1.0, max_value=10.0, value=1.0, step=0.5)

x = np.linspace(0, 10, 500)
if opcion == "Seno":
    y = np.sin(frecuencia * x)
    color = "blue"
else:
    y = np.cos(frecuencia * x)
    color = "red"

fig, ax = plt.subplots()
ax.plot(x, y, color=color, linewidth=2)
ax.grid(True)

st.pyplot(fig)