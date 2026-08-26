# Análisis de Top Streamers en Twitch

## Descripción

Este proyecto realiza un análisis de datos de canales de Twitch utilizando información del dataset "Top Streamers on Twitch" disponible en Kaggle.

El programa permite cargar, limpiar, procesar y analizar los datos para obtener información relacionada con seguidores, viewers, actividad, crecimiento, eficiencia, idiomas y otras características de los canales.

También permite realizar consultas interactivas y visualizar algunos de los resultados mediante gráficos.

## Archivos del proyecto

- `app.py`: ejecuta el programa y presenta los resultados, consultas y gráficos.
- `carga_datos.py`: descarga y carga el dataset utilizado en el proyecto.
- `limpieza_datos.py`: organiza, convierte y limpia los datos.
- `procesamiento.py`: contiene las funciones utilizadas para analizar los datos.

## Requisitos

Para ejecutar el proyecto se requiere Python y las siguientes librerías:

- pandas
- matplotlib
- kagglehub

## Ejecución

Desde la carpeta del proyecto ejecutar:

python app.py

El programa descargará y cargará el dataset automáticamente.

Después mostrará los resultados principales del análisis y permitirá realizar diferentes consultas:

1. Consulta de información de un canal.
2. Consulta de información por idioma.
3. Consulta de rankings.
4. Selección y visualización de gráficos.

## Visualizaciones

El programa incluye gráficos para visualizar:

- Top 5 de canales con mayor cantidad de seguidores.
- Top 5 de canales con mayor promedio de viewers.
- Cantidad de canales Partner y No Partner.

## Fuente de datos

Dataset: Top Streamers on Twitch  
Fuente: Kaggle