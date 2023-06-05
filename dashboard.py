import streamlit as st
import pandas as pd
import pymongo
import plotly.express as px

# Conexión a la base de datos MongoDB
mongo_url = "mongodb+srv://mabel:12345@data.jfzuc3o.mongodb.net/?retryWrites=true&w=majority"  # Reemplaza con tu URL de MongoDB
client = pymongo.MongoClient(mongo_url)
db = client['bdnosql']

# Obtener datos desde la primera colección
collection1 = db["bdnosql_reactions"]  # Reemplaza con el nombre de tu primera colección
data1 = list(collection1.find())  # Obtener todos los documentos de la colección

# Convertir los datos en un DataFrame de Pandas
df1 = pd.DataFrame(data1)

# Obtener datos desde la segunda colección (comentarios)
collection2 = db["bdnosql_comments"]  # Reemplaza con el nombre de tu segunda colección (comentarios)
data2 = list(collection2.find())  # Obtener todos los documentos de la colección (comentarios)

# Convertir los datos en un DataFrame de Pandas
df2 = pd.DataFrame(data2)

# Configuración de estilo
st.set_page_config(page_title="Dashboard de Fotoart", layout="wide")

# Título principal
st.title("Dashboard de Fotoart")

# Subtítulo y descripción
st.markdown("Este es un dashboard interactivo para visualizar datos de MongoDB.")

# Título del menú
st.sidebar.title("Opciones del Menú")

# Crear menú
menu_options = ["Gráfico de Pastel", "Gráfico de Barras", "Comentarios","Gráfico de Línea",
"Gráfico de Área","Resumen Estadístico de Reacciones","Resumen Estadístico de Comentarios"]  # Opciones de menú
selected_option = st.sidebar.selectbox("Selecciona una opción", menu_options)

# Mostrar contenido según la opción seleccionada
if selected_option == "Gráfico de Pastel":
    # Código para generar el Gráfico de Pastel
    fig = px.pie(df1, names="reactionId")
    st.plotly_chart(fig)

elif selected_option == "Gráfico de Barras":
    # Código para generar el Gráfico de Barras
    fig = px.bar(df1, x="reactionId", y="objectId")
    st.plotly_chart(fig)

elif selected_option == "Gráfico de Línea":
    # Título de la sección
    st.subheader("Gráfico de Línea")

    # Código para generar el Gráfico de Línea
    fig = px.line(df1, x="reactionId", y="objectId")
    st.plotly_chart(fig)

elif selected_option == "Gráfico de Área":
    # Título de la sección
    st.subheader("Gráfico de Área")

    # Código para generar el Gráfico de Área
    fig = px.area(df1, x="reactionId", y="objectId")
    st.plotly_chart(fig)

elif selected_option == "Comentarios":
    # Mostrar tabla con los comentarios obtenidos
    st.table(df2["comment"])

elif selected_option == "Resumen Estadístico de Reacciones":
    # Título de la sección
    st.subheader("Resumen Estadístico de Reacciones")

    # Mostrar resumen estadístico de los datos
    st.write(df1.describe())

elif selected_option == "Resumen Estadístico de Comentarios":
    # Título de la sección
    st.subheader("Resumen Estadístico de comentarios")

    # Mostrar resumen estadístico de los datos
    st.write(df2.describe())

