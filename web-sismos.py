import streamlit as st 
import pandas as pd
import plotly.express as px
import requests

# Realizar la petición GET a la API
def obtener_datos(url):
    try:
        respuesta = requests.get(url)
        df = pd.DataFrame(respuesta.json())
    
        # Cerrar la conexión con la API
        respuesta.close()
        
    except:
        # Mensaje de error si no se puede conectar a la API
        st.error("Error al realizar la petición GET")
        
    return df

# ------------ EJERCICIO 1 ------------
    
def relacion_profundidad_magnitud(datos):
    fig = px.scatter(datos, x='Profundidad', y='Magnitud', title='1. Relación entre Profundidad y Magnitud de sismos')

    # Tamaño de fuente del titulo
    fig.update_layout(title_font=dict(size=30))

    # Color de los puntos
    fig.update_traces(marker=dict(color='blueviolet', size=12))

    # Dimensiones de la grafica
    fig.update_layout(width=800, height=600)

    # Tamaño de fuente de nombres eje x e y 
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_yaxes(title_font=dict(size=20))
     
    return fig

# ------------ EJERCICIO 2 ------------

def profundidad_tiempo(datos):
    fig = px.line(datos, x='Fecha', y='Profundidad', title='2. Profundidad de los sismos a través del tiempo')

    # Tamaño de fuente del titulo
    fig.update_layout(title_font=dict(size=30))

    # Color y tamaño de linea
    fig.update_traces(line=dict(color='blueviolet', width=4))

    # Dimensiones de la grafica
    fig.update_layout(width=800, height=600)

    # Tamaño de fuente de nombres eje x e y 
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_yaxes(title_font=dict(size=20))

    return fig

# ------------ EJERCICIO 3 ------------

def magnitud_tiempo(datos):
    fig = px.line(datos, x='Fecha', y='Magnitud', title='3. Magnitud de los sismos a través del tiempo')
    
    # Tamaño de fuente del titulo
    fig.update_layout(title_font=dict(size=30))
    
    # Color y tamaño barras
    fig.update_traces(line=dict(color='blueviolet', width=4))
        
    # Dimensiones de la grafica
    fig.update_layout(width=800, height=600)
    
    # Tamaño de fuente de nombres eje x e y 
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_yaxes(title_font=dict(size=20))
    
    return fig

# ------------ EJERCICIO 4 ------------

def distribucion_profundidad(datos):
    fig = px.histogram(datos, x='Profundidad', title='4. Distribución de la profundidad de los sismos', color_discrete_sequence=['blueviolet'])
    
    # Tamaño de fuente del titulo
    fig.update_layout(title_font=dict(size=30))
    
    # Dimensiones de la grafica
    fig.update_layout(width=800, height=600)
    fig.update_layout(bargap=0.01)
        
    # Tamaño de fuente de nombres eje x e y 
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_yaxes(title_font=dict(size=20), title_text='frecuencia')
        
    return fig

# ------------ EJERCICIO 5 ------------

def distribucion_magnitud(datos):
    fig = px.histogram(datos, x='Magnitud', title= '5. Distribución de la magnitud de los sismos', color_discrete_sequence=['blueviolet'])
    
    # Tamaño de fuente del titulo
    fig.update_layout(title_font=dict(size=30))
    
    # Dimensiones de la grafica
    fig.update_layout(width=800, height=600)
    
    fig.update_layout(bargap=0.02)
        
    # Tamaño de fuente de nombres eje x e y 
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_yaxes(title_font=dict(size=20), title_text='frecuencia')
    
    return fig

# ------------ EJERCICIO 6 ------------

def resumen_profundidad(datos):
    fig = px.box(datos, x='Profundidad', title='6. Resumen estadístico de la profundidad de los sismos', color_discrete_sequence=['blueviolet'])
    
    # Tamaño de fuente del titulo
    fig.update_layout(title_font=dict(size=30))
    
    # Dimensiones de la grafica
    fig.update_layout(width=800, height=600)
            
    # Tamaño de fuente de nombres eje x e y 
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_yaxes(title_font=dict(size=20))
    
    return fig

# ------------ EJERCICIO 7 ------------

def resumen_magnitud(datos):
    fig = px.box(datos, x='Magnitud', title='7. Resumen estadístico de la magnitud de los sismos', color_discrete_sequence=['blueviolet'])
    
    # Tamaño de fuente del titulo
    fig.update_layout(title_font=dict(size=30))
    
    # Dimensiones de la grafica
    fig.update_layout(width=800, height=600)
            
    # Tamaño de fuente de nombres eje x e y 
    fig.update_xaxes(title_font=dict(size=20))
    fig.update_yaxes(title_font=dict(size=20))
    
    return fig

# ------------ WEB CON STREAMLIT------------

def main():
    # URL de la API
    url = 'https://api.gael.cloud/general/public/sismos'
    
    # Obtener los datos de la API y guardarlos en un DataFrame
    df = obtener_datos(url)
    
    # Titulo de la aplicacion
    st.title('Sismos en Chile')
    st.write('06 dec 2023 - 07 dec 2023')

    # Mostrar los datos del DataFrame en la web al seleccionar el checkbox
    if st.checkbox("Mostrar Datos"):
        st.header('Registro de sismos')
        st.dataframe(df)    
        
    #--------- Mostrar las graficas en la web ---------#
    
    # Mostar la grafica de dispersion relacion_profundidad_magnitud
    st.plotly_chart(relacion_profundidad_magnitud(df))
    
    # Mostrar la grafica de linea profundidad_tiempo
    st.plotly_chart(profundidad_tiempo(df))
    
    # Mostrar la grafica de linea magnitud_tiempo
    st.plotly_chart(magnitud_tiempo(df))
    
    # Mostrar Distribucion de la profundidad de los sismos
    st.plotly_chart(distribucion_profundidad(df))
    
    # Distribucion de la magnitud de los sismos
    st.plotly_chart(distribucion_magnitud(df))
    
    # Resumen estadistico de la profundidad de los sismos
    st.plotly_chart(resumen_profundidad(df))
    
    # Resumen estadistico de la magnitud de los sismos
    st.plotly_chart(resumen_magnitud(df))
    
    # --------------------------------------------------- #
    
if __name__ == "__main__":
    main()