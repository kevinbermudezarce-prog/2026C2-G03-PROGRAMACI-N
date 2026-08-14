from carga_datos import cargar_datos
from limpieza_datos import limpiar_datos

from procesamiento import (
    calcular_total_seguidores,
    calcular_promedio_viewers,
    obtener_top_5_seguidores,
    obtener_top_5_viewers,
    obtener_top_5_pico_viewers,
    obtener_top_5_views,
    obtener_canales_por_idioma,
    obtener_top_5_idiomas_viewers
)



def ejecutar():
    df = cargar_datos()

    if df.empty:
        print("No se pudo cargar los datos.")
    else:
        df = limpiar_datos(df)
        
        print("Datos cargados correctamente:")
        print(df.head())

        print("\nCantidad de filas:", len(df))
        print("Cantidad de columnas:", len(df.columns))

        print("\nValores nulos por columna:")
        print(df.isnull().sum())

        print("\nRegistros duplicados:", df.duplicated().sum())

        print("\nTipos de datos:")
        print(df.dtypes)

        # Def trabajadas en procesamiento
        total_seguidores = calcular_total_seguidores(df)
        promedio_viewers = calcular_promedio_viewers(df)
        top_5_seguidores = obtener_top_5_seguidores(df)
        top_5_viewers = obtener_top_5_viewers(df)
        top_5_pico_viewers = obtener_top_5_pico_viewers(df)
        top_5_views = obtener_top_5_views(df)
        canales_por_idioma = obtener_canales_por_idioma(df)
        top_5_idiomas_viewers = obtener_top_5_idiomas_viewers(df)
        

        print("\n========================================")
        print("          RESULTADOS DEL ANÁLISIS")
        print("========================================")

        print(f"\nTotal de seguidores de todos los canales: {total_seguidores:,}")
        print(f"Promedio de viewers entre los canales: {promedio_viewers:,.2f}")


        print("\n--- TOP 5 - SEGUIDORES ---")
        for _, fila in top_5_seguidores.iterrows():
            print(f"{fila['CANAL']:<25} {fila['SEGUIDORES_TOTALES']:>12,}")


        print("\n--- TOP 5 - PROMEDIO DE VIEWERS ---")
        for _, fila in top_5_viewers.iterrows():
            print(f"{fila['CANAL']:<25} {fila['VIEWERS_PROMEDIO']:>12,}")


        print("\n--- TOP 5 - PICO DE VIEWERS ---")
        for _, fila in top_5_pico_viewers.iterrows():
            print(f"{fila['CANAL']:<25} {fila['PICO_VIEWERS']:>12,}")
        
        
        
        print("\n--- TOP 5 - VIEWS OBTENIDAS ---")
        for _, fila in top_5_views.iterrows():
            print(f"{fila['CANAL']:<25} {fila['VIEWS_OBTENIDAS']:>12,}")


        print("\n--- CANALES POR IDIOMA ---")
        for idioma, cantidad in canales_por_idioma.items():
            print(f"{idioma:<20} {cantidad:>5}")


        print("\n--- TOP 5 - IDIOMAS POR PROMEDIO DE VIEWERS ---")
        for idioma, promedio in top_5_idiomas_viewers.items():
            print(f"{idioma:<20} {promedio:>12,.2f}")


if __name__ == "__main__":
    ejecutar()

