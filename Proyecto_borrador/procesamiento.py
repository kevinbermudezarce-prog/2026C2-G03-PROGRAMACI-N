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
    top_5 = datos.nlargest(5, "SEGUIDORES_TOTALES")
    return top_5[["CANAL", "SEGUIDORES_TOTALES"]]


def obtener_top_5_viewers(datos):
    """Obtiene los 5 canales con mayor promedio de viewers."""
    top_5 = datos.nlargest(5, "VIEWERS_PROMEDIO")
    return top_5[["CANAL", "VIEWERS_PROMEDIO"]]


def obtener_top_5_pico_viewers(datos):
    """Obtiene los 5 canales con mayor pico de viewers."""
    top_5 = datos.nlargest(5, "PICO_VIEWERS")
    return top_5[["CANAL", "PICO_VIEWERS"]]


def obtener_top_5_views(datos):
    """Obtiene los 5 canales con mayor cantidad de vistas obtenidas."""
    top_5 = datos.nlargest(5, "VIEWS_OBTENIDAS")
    return top_5[["CANAL", "VIEWS_OBTENIDAS"]]


def obtener_canales_por_idioma(datos):
    """Cuenta la cantidad de canales registrados por idioma."""
    canales_idioma = datos["IDIOMA"].value_counts()
    return canales_idioma


def promedio_viewers_por_idioma(datos):
    """Calcula el promedio de viewers según el idioma."""
    promedio = datos.groupby("IDIOMA")["VIEWERS_PROMEDIO"].mean()
    return promedio.sort_values(ascending=False)


def obtener_top_5_idiomas_viewers(datos):
    """Obtiene los 5 idiomas con mayor promedio de viewers."""
    promedio = datos.groupby("IDIOMA")["VIEWERS_PROMEDIO"].mean()
    return promedio.sort_values(ascending=False).head(5)