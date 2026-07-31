"""Funciones para limpiar y filtrar los datos cambiarios."""

import pandas as pd


def limpiar_datos(datos):
    """Prepara la tabla de tipos de cambio del BCCR."""
    datos_limpios = datos.copy()

    datos_limpios.ffill(inplace=True)
    datos_limpios.drop_duplicates(inplace=True)

    nombres_columnas = {
        0: "TIPO",
        1: "ENTIDAD",
        2: "COMPRA",
        3: "VENTA",
        4: "DIFERENCIAL",
        5: "FECHA",
    }
    datos_limpios.rename(columns=nombres_columnas, inplace=True)
    datos_limpios.drop(0, inplace=True)

    columnas_numericas = ["COMPRA", "VENTA", "DIFERENCIAL"]
    datos_limpios[columnas_numericas] = datos_limpios[
        columnas_numericas
    ].apply(pd.to_numeric, errors="coerce")
    datos_limpios["FECHA"] = pd.to_datetime(
        datos_limpios["FECHA"],
        dayfirst=True,
        errors="coerce",
    )
    datos_limpios.dropna(
        subset=["ENTIDAD", "COMPRA", "VENTA"],
        inplace=True,
    )

    return datos_limpios


def filtrar_diferencial_alto(datos):
    """Devuelve entidades coherentes con diferencial superior al promedio."""
    promedio_diferencial = datos["DIFERENCIAL"].mean()
    filtro = datos["DIFERENCIAL"] > promedio_diferencial
    return datos[filtro]

def resumir_por_tipo_entidad(datos: pd.DataFrame) -> tuple[float, pd.DataFrame]:
    """Devuelve el promedio general del diferencial y el promedio por tipo de entidad de compra, venta y diferencial."""
    promedio_diferencial = datos["DIFERENCIAL"].mean()
    
    #Agrupa por tipo de entidad y calcula el promedio de compra, venta y diferencial
    columnas = ["COMPRA", "VENTA", "DIFERENCIAL"]
    promedios_por_tipo =(
        datos.groupby("TIPO")[columnas]
            .mean ()
            .round(2)
            .sort_values("DIFERENCIAL", ascending=False)
        )
    return (promedio_diferencial, promedios_por_tipo)
