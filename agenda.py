import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Agenda Telefónica")

# Crear un DataFrame para almacenar los contactos
if 'contacts' not in st.session_state:
    st.session_state['contacts'] = pd.DataFrame(columns=['Nombre', 'Teléfono'])

# Función para agregar un nuevo contacto
def add_contact(nombre, telefono):
    new_contact = pd.DataFrame([[nombre, telefono]], columns=['Nombre', 'Teléfono'])
    st.session_state['contacts'] = pd.concat([st.session_state['contacts'], new_contact], ignore_index=True)

# Entrada de datos para un nuevo contacto
st.header("Agregar Nuevo Contacto")
nombre = st.text_input("Nombre")
telefono = st.text_input("Teléfono")

if st.button("Agregar"):
    if nombre and telefono:
        add_contact(nombre, telefono)
        st.success("Contacto agregado exitosamente")
    else:
        st.error("Por favor, ingresa tanto el nombre como el teléfono")

# Mostrar todos los contactos
st.header("Contactos Guardados")
st.dataframe(st.session_state['contacts'])

# Búsqueda de contactos
st.header("Buscar Contacto")
search_term = st.text_input("Buscar por nombre")

if search_term:
    search_results = st.session_state['contacts'][st.session_state['contacts']['Nombre'].str.contains(search_term, case=False)]
    st.dataframe(search_results)
else:
    st.write("Ingresa un nombre para buscar.")

# Mensaje de despedida
st.write("¡Gracias por usar la agenda telefónica!")

