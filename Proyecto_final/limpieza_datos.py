import pandas as pd


def limpiar_datos(datos):
    """Prepara la tabla de Top Streamers on Twitch."""

    datos_limpios = datos.copy()

    #Renombrar las columnas con nombres más descriptivos
    nombres_columnas = {
        "Channel": "CANAL",
        "Watch time(Minutes)": "TIEMPO_VISUALIZADO",
        "Stream time(minutes)": "TIEMPO_STREAMING",
        "Peak viewers": "PICO_VIEWERS",
        "Average viewers": "VIEWERS_PROMEDIO",
        "Followers": "SEGUIDORES_TOTALES",
        "Followers gained": "SEGUIDORES_NUEVOS",
        "Views gained": "VIEWS_OBTENIDAS",
        "Partnered": "PARTNER",
        "Mature": "CONTENIDO_MADURO",
        "Language": "IDIOMA"
    }

    datos_limpios.rename(columns=nombres_columnas, inplace=True)

    #Conversión de los datos a números
    columnas_numericas = [
        "TIEMPO_VISUALIZADO",
        "TIEMPO_STREAMING",
        "PICO_VIEWERS",
        "VIEWERS_PROMEDIO",
        "SEGUIDORES_TOTALES",
        "SEGUIDORES_NUEVOS",
        "VIEWS_OBTENIDAS"
    ]

    for columna in columnas_numericas:
        datos_limpios[columna] = pd.to_numeric(
            datos_limpios[columna],
            errors="coerce"
        )

    #Eliminación de registros duplicados
    datos_limpios = datos_limpios.drop_duplicates()

    return datos_limpios