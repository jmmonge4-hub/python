import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Diseño de la página web con Streamlit
st.title("📊 Mi primera Web con Streamlit")
st.write("Esta página web se genera completamente desde Python en tiempo real.")

# 1. Menú desplegable lateral en la web para elegir la función
opcion = st.sidebar.selectbox("Elige una función:", ["Seno", "Coseno"])

# 2. Deslizador web interactivo
frecuencia = st.sidebar.slider("Ajusta la Frecuencia:", min_value=1.0, max_value=10.0, value=1.0, step=0.5)

# 3. Cálculo con NumPy
x = np.linspace(0, 10, 500)
if opcion == "Seno":
    y = np.sin(frecuencia * x)
    color = "blue"
else:
    y = np.cos(frecuencia * x)
    color = "red"

# 4. Creación del gráfico con Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y, color=color, linewidth=2)
ax.grid(True)

# ¡Inyectamos el gráfico en la web con una sola línea!
st.pyplot(fig)
