TOP_5 = 5
TOP_10 = 10


def calcular_total_seguidores(datos):
    """Calcula el total de seguidores de todos los canales."""
    total = datos["SEGUIDORES_TOTALES"].sum()
    return total

def calcular_promedio_viewers(datos):
    """Calcula el promedio de espectadores de los canales."""
    promedio = datos["VIEWERS_PROMEDIO"].mean()
    return promedio

def obtener_top_5_seguidores(datos):
    """Obtiene los 5 canales con mayor cantidad de seguidores."""
    top_5 = datos.nlargest(TOP_5, "SEGUIDORES_TOTALES")
    return top_5[["CANAL", "SEGUIDORES_TOTALES"]]


def obtener_top_5_viewers(datos):
    """Obtiene los 5 canales con mayor promedio de viewers."""
    top_5 = datos.nlargest(TOP_5, "VIEWERS_PROMEDIO")
    return top_5[["CANAL", "VIEWERS_PROMEDIO"]]


def obtener_top_5_pico_viewers(datos):
    """Obtiene los 5 canales con mayor pico de viewers."""
    top_5 = datos.nlargest(TOP_5, "PICO_VIEWERS")
    return top_5[["CANAL", "PICO_VIEWERS"]]


def obtener_top_5_views(datos):
    """Obtiene los 5 canales con mayor cantidad de vistas obtenidas."""
    top_5 = datos.nlargest(TOP_5, "VIEWS_OBTENIDAS")
    return top_5[["CANAL", "VIEWS_OBTENIDAS"]]


def obtener_canales_por_idioma(datos):
    """Cuenta la cantidad de canales registrados por idioma."""
    canales_idioma = datos["IDIOMA"].value_counts()
    return canales_idioma


def obtener_top_5_idiomas_viewers(datos):
    """Obtiene los 5 idiomas con mayor promedio de viewers."""
    promedio = datos.groupby("IDIOMA")["VIEWERS_PROMEDIO"].mean()
    return promedio.sort_values(ascending=False).head(TOP_5)


def obtener_top_5_idiomas_views(datos):
    """Obtiene los 5 idiomas con mayor cantidad de views obtenidas."""
    views = datos.groupby("IDIOMA")["VIEWS_OBTENIDAS"].sum()
    return views.sort_values(ascending=False).head(TOP_5)


def obtener_top_5_idiomas_seguidores(datos):
    """Obtiene los 5 idiomas con mayor cantidad de seguidores."""
    seguidores = datos.groupby("IDIOMA")["SEGUIDORES_TOTALES"].sum()
    return seguidores.sort_values(ascending=False).head(TOP_5)


def obtener_top_5_idiomas_pico_viewers(datos):
    """Obtiene los 5 idiomas con mayor pico de viewers."""
    pico = datos.groupby("IDIOMA")["PICO_VIEWERS"].max()
    return pico.sort_values(ascending=False).head(TOP_5)


def obtener_top_10_seguidores_vs_viewers(datos):
    """Obtiene los 10 canales con más seguidores y su promedio de viewers."""
    top_10 = datos.nlargest(TOP_10, "SEGUIDORES_TOTALES")
    return top_10[["CANAL", "SEGUIDORES_TOTALES", "VIEWERS_PROMEDIO"]]


def calcular_views_por_seguidor(datos):
    """Calcula la cantidad de views obtenidas por cada seguidor."""
    datos = datos.copy()
    datos = datos[datos["SEGUIDORES_TOTALES"] > 0]
    datos["VIEWS_POR_SEGUIDOR"] = (
        datos["VIEWS_OBTENIDAS"] / datos["SEGUIDORES_TOTALES"]
    )
    return datos.nlargest(TOP_10, "VIEWS_POR_SEGUIDOR")[
        ["CANAL", "SEGUIDORES_TOTALES", "VIEWS_OBTENIDAS", "VIEWS_POR_SEGUIDOR"]
    ]


def analizar_partner(datos):
    """Analiza los canales según si son Partner o no."""
    datos = datos.copy()
    datos = datos[datos["SEGUIDORES_TOTALES"] > 0]
    datos["VIEWERS_POR_SEGUIDOR"] = (
        datos["VIEWERS_PROMEDIO"] / datos["SEGUIDORES_TOTALES"]
    )
    datos["VIEWS_POR_SEGUIDOR"] = (
        datos["VIEWS_OBTENIDAS"] / datos["SEGUIDORES_TOTALES"]
    )
    resumen = datos.groupby("PARTNER").agg({
        "CANAL": "count",
        "SEGUIDORES_TOTALES": "mean",
        "VIEWERS_PROMEDIO": "mean",
        "VIEWS_OBTENIDAS": "mean",
        "VIEWERS_POR_SEGUIDOR": "mean",
        "VIEWS_POR_SEGUIDOR": "mean"
    })

    return resumen


def calcular_viewers_por_seguidor(datos):
    """Calcula la relación entre viewers promedio y seguidores."""
    datos = datos.copy()
    datos = datos[datos["SEGUIDORES_TOTALES"] > 0]
    datos["VIEWERS_POR_SEGUIDOR"] = (
        datos["VIEWERS_PROMEDIO"] / datos["SEGUIDORES_TOTALES"]
    )
    top_10 = datos.nlargest(TOP_10, "VIEWERS_POR_SEGUIDOR")
    return top_10[
        ["CANAL", "SEGUIDORES_TOTALES", "VIEWERS_PROMEDIO", "VIEWERS_POR_SEGUIDOR"]
    ]


def analizar_contenido_maduro(datos):
    """Analiza el rendimiento de los canales según contenido maduro."""
    resumen = datos.groupby("CONTENIDO_MADURO").agg(
        CANALES=("CANAL", "count"),
        SEGUIDORES_PROMEDIO=("SEGUIDORES_TOTALES", "mean"),
        VIEWERS_PROMEDIO=("VIEWERS_PROMEDIO", "mean"),
        VIEWS_PROMEDIO=("VIEWS_OBTENIDAS", "mean"),
        PICO_VIEWERS_PROMEDIO=("PICO_VIEWERS", "mean")
    )
    return resumen


def obtener_top_10_seguidores_nuevos(datos):
    """Obtiene los 10 canales con mayor cantidad de seguidores nuevos."""
    top_10 = datos.nlargest(TOP_10, "SEGUIDORES_NUEVOS")
    return top_10[["CANAL", "SEGUIDORES_NUEVOS"]]


def obtener_top_10_tiempo_streaming(datos):
    """Obtiene los 10 canales con mayor tiempo de streaming."""
    top_10 = datos.nlargest(TOP_10, "TIEMPO_STREAMING")
    return top_10[["CANAL", "TIEMPO_STREAMING"]]


def obtener_top_10_tiempo_visualizado(datos):
    """Obtiene los 10 canales con mayor tiempo visualizado."""
    top_10 = datos.nlargest(TOP_10, "TIEMPO_VISUALIZADO")
    return top_10[["CANAL", "TIEMPO_VISUALIZADO"]]


    
def analizar_eficiencia_canal(datos):
    """Analiza el crecimiento de los canales según su tiempo de streaming."""
    datos = datos.copy()
    datos = datos[datos["TIEMPO_STREAMING"] > 0]
    datos["SEGUIDORES_NUEVOS_POR_MINUTO"] = (
        datos["SEGUIDORES_NUEVOS"] / datos["TIEMPO_STREAMING"]
    )
    top_10 = datos.nlargest(
        TOP_10,
        "SEGUIDORES_NUEVOS_POR_MINUTO"
    )

    return top_10[
        [
            "CANAL",
            "SEGUIDORES_NUEVOS",
            "TIEMPO_STREAMING",
            "SEGUIDORES_NUEVOS_POR_MINUTO"
        ]
    ]

def calcular_views_por_minuto_streaming(datos):
    """Calcula las views obtenidas por cada minuto de streaming."""
    datos = datos.copy()
    datos = datos[datos["TIEMPO_STREAMING"] > 0]
    datos["VIEWS_POR_MINUTO"] = (
        datos["VIEWS_OBTENIDAS"] / datos["TIEMPO_STREAMING"]
    )
    top_10 = datos.nlargest(TOP_10, "VIEWS_POR_MINUTO")
    return top_10[
        ["CANAL", "VIEWS_OBTENIDAS", "TIEMPO_STREAMING", "VIEWS_POR_MINUTO"]
    ]