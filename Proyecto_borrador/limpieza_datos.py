def limpiar_datos(datos):
    """Prepara la tabla de Top Streamers on Twitch."""
    datos_limpios = datos.copy()


    nombres_columnas = {
        0: "CANAL",
        1: "TIEMPO_VISUALIZADO",
        2: "TIEMPO_STEAMING",
        3: "PICO_VIEWERS",
        4: "VIEWERS_PROMEDIO",
        5: "SEGUIDORES_TOTAL",
        6: "SEGUIDORES_NUEVOS",
    }
    datos_limpios.rename(columns=nombres_columnas, inplace=True)


    return datos_limpios