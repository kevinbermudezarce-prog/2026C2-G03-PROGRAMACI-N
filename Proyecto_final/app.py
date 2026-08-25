from carga_datos import cargar_datos
from limpieza_datos import limpiar_datos
import matplotlib.pyplot as plt


from procesamiento import (
    calcular_total_seguidores,
    calcular_promedio_viewers,
    obtener_top_5_seguidores,
    obtener_top_5_viewers,
    obtener_top_5_pico_viewers,
    obtener_top_5_views,
    obtener_canales_por_idioma,
    obtener_top_5_idiomas_viewers,
    obtener_top_5_idiomas_views,
    obtener_top_5_idiomas_seguidores,
    obtener_top_5_idiomas_pico_viewers,
    obtener_top_10_seguidores_vs_viewers,
    calcular_views_por_seguidor,
    analizar_partner,
    calcular_viewers_por_seguidor,
    analizar_contenido_maduro,
    obtener_top_10_seguidores_nuevos,
    obtener_top_10_tiempo_streaming,
    obtener_top_10_tiempo_visualizado,
    analizar_eficiencia_canal,
    calcular_views_por_minuto_streaming
)

ANCHO_SECCION = 50

def consultar_canal(datos):
    """Permite al usuario consultar la información de un canal."""
    canal_buscado = input(
        "\nIngrese el nombre del canal que desea consultar: "
    )
    resultado = datos[
        datos["CANAL"].str.lower() == canal_buscado.lower()
    ]
    if resultado.empty:
        print("\nEl canal indicado no se encuentra en los datos.")
    else:
        print("\n" + "=" * ANCHO_SECCION)
        print("              CONSULTA DE CANAL")
        print("=" * ANCHO_SECCION)

        fila = resultado.iloc[0]

        print(f"\nCanal:                    {fila['CANAL']}")
        print(f"Seguidores totales:       {fila['SEGUIDORES_TOTALES']:,.0f}")
        print(f"Seguidores nuevos:        {fila['SEGUIDORES_NUEVOS']:,.0f}")
        print(f"Viewers promedio:          {fila['VIEWERS_PROMEDIO']:,.0f}")
        print(f"Pico de viewers:           {fila['PICO_VIEWERS']:,.0f}")
        print(f"Views obtenidas:           {fila['VIEWS_OBTENIDAS']:,.0f}")
        print(f"Tiempo de streaming:       {fila['TIEMPO_STREAMING']:,.0f} min")
        print(f"Tiempo visualizado:        {fila['TIEMPO_VISUALIZADO']:,.0f} min")
        print(f"Idioma:                    {fila['IDIOMA']}")

        if fila["PARTNER"]:
            print("Partner:                   Sí")
        else:
            print("Partner:                   No")

        if fila["CONTENIDO_MADURO"]:
            print("Contenido maduro:          Sí")
        else:
            print("Contenido maduro:          No")


def consultar_idioma(datos):
    """Permite al usuario consultar un resumen de un idioma."""

    idioma_buscado = input(
        "\nIngrese el idioma que desea consultar: "
    )

    resultado = datos[
        datos["IDIOMA"].str.lower() == idioma_buscado.lower()
    ]

    if resultado.empty:
        print("\nEl idioma indicado no se encuentra en los datos.")
    else:
        cantidad_canales = len(resultado)
        seguidores_totales = resultado["SEGUIDORES_TOTALES"].sum()
        promedio_viewers = resultado["VIEWERS_PROMEDIO"].mean()
        views_obtenidas = resultado["VIEWS_OBTENIDAS"].sum()

        print("\n" + "=" * ANCHO_SECCION)
        print("             CONSULTA POR IDIOMA")
        print("=" * ANCHO_SECCION)

        print(f"\nIdioma:                    {resultado['IDIOMA'].iloc[0]}")
        print(f"Cantidad de canales:       {cantidad_canales:,}")
        print(f"Seguidores totales:        {seguidores_totales:,.0f}")
        print(f"Promedio de viewers:       {promedio_viewers:,.2f}")
        print(f"Views obtenidas:           {views_obtenidas:,.0f}")
        


def consultar_ranking(datos):
    """Permite al usuario seleccionar y visualizar un ranking."""

    print("\nSeleccione el ranking que desea consultar:")
    print("1. Seguidores")
    print("2. Promedio de viewers")
    print("3. Pico de viewers")
    print("4. Views obtenidas")

    opcion = input("\nIngrese una opción del 1 al 4: ")

    if opcion == "1":
        ranking = obtener_top_5_seguidores(datos)
        columna = "SEGUIDORES_TOTALES"
        titulo = "TOP 5 - SEGUIDORES"
        encabezado = "Seguidores"

    elif opcion == "2":
        ranking = obtener_top_5_viewers(datos)
        columna = "VIEWERS_PROMEDIO"
        titulo = "TOP 5 - PROMEDIO DE VIEWERS"
        encabezado = "Viewers promedio"

    elif opcion == "3":
        ranking = obtener_top_5_pico_viewers(datos)
        columna = "PICO_VIEWERS"
        titulo = "TOP 5 - PICO DE VIEWERS"
        encabezado = "Pico de viewers"

    elif opcion == "4":
        ranking = obtener_top_5_views(datos)
        columna = "VIEWS_OBTENIDAS"
        titulo = "TOP 5 - VIEWS OBTENIDAS"
        encabezado = "Views obtenidas"

    else:
        print("\nLa opción seleccionada no es válida.")
        return

    print("\n" + "=" * ANCHO_SECCION)
    print("              CONSULTA DE RANKING")
    print("=" * ANCHO_SECCION)
    print("\n" + "-" * ANCHO_SECCION)
    print(titulo)
    print("-" * ANCHO_SECCION)
    print(
        f"{'Canal':<25}"
        f"{encabezado:>25}"
    )

    for _, fila in ranking.iterrows():
        print(
            f"{fila['CANAL']:<25}"
            f"{fila[columna]:>25,.0f}"
        )


def mostrar_grafico(datos):
    """Permite al usuario seleccionar y visualizar un gráfico."""

    print("\n¿Desea visualizar un gráfico?")
    respuesta = input("Ingrese Sí o No: ")

    if respuesta.lower() == "si" or respuesta.lower() == "sí":

        print("\nSeleccione el gráfico que desea visualizar:")
        print("1. Top 5 - Seguidores")
        print("2. Top 5 - Promedio de viewers")
        print("3. Canales Partner y No Partner")

        opcion = input("\nIngrese una opción del 1 al 3: ")

        if opcion == "1":
            ranking = obtener_top_5_seguidores(datos)

            plt.bar(
                ranking["CANAL"],
                ranking["SEGUIDORES_TOTALES"]
            )

            plt.title("Top 5 - Canales con más seguidores")
            plt.xlabel("Canal")
            plt.ylabel("Seguidores")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.grid(axis="y", linestyle="--", alpha=0.5)
            for indice, valor in enumerate(ranking["SEGUIDORES_TOTALES"]):
                plt.text(
                    indice,
                    valor,
                    f"{valor:,}",
                    ha="center",
                    va="bottom"
                )
            plt.show()

        elif opcion == "2":
            ranking = obtener_top_5_viewers(datos)

            plt.bar(
                ranking["CANAL"],
                ranking["VIEWERS_PROMEDIO"]
            )

            plt.title("Top 5 - Promedio de viewers")
            plt.xlabel("Canal")
            plt.ylabel("Viewers promedio")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.grid(axis="y", linestyle="--", alpha=0.5)
            for indice, valor in enumerate(ranking["VIEWERS_PROMEDIO"]):
                plt.text(
                    indice,
                    valor,
                    f"{valor:,.0f}",
                    ha="center",
                    va="bottom"
                )
            plt.show()

        elif opcion == "3":
            resumen = analizar_partner(datos)

            etiquetas = []

            for estado in resumen.index:
                if estado:
                    etiquetas.append("Partner")
                else:
                    etiquetas.append("No Partner")

            plt.bar(
                etiquetas,
                resumen["CANAL"]
            )

            plt.title("Cantidad de canales Partner y No Partner")
            plt.xlabel("Tipo de canal")
            plt.ylabel("Cantidad de canales")
            plt.tight_layout()
            plt.grid(axis="y", linestyle="--", alpha=0.5)
            for indice, valor in enumerate(resumen["CANAL"]):
                plt.text(
                    indice,
                    valor,
                    f"{valor:,.0f}",
                    ha="center",
                    va="bottom"
                )
            plt.show()

        else:
            print("\nLa opción seleccionada no es válida.")

    elif respuesta.lower() == "no":
        print("\nNo se mostrará ningún gráfico.")

    else:
        print("\nLa respuesta indicada no es válida.")


def ejecutar():
    df = cargar_datos()

    if df.empty:
        print("No se pudo cargar los datos.")
    else:
        df = limpiar_datos(df)
        
        print("\nPrimeros registros del dataset:")
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
        top_10_seguidores_vs_viewers = obtener_top_10_seguidores_vs_viewers(df)
        top_5_viewers = obtener_top_5_viewers(df)
        top_5_pico_viewers = obtener_top_5_pico_viewers(df)
        top_5_views = obtener_top_5_views(df)
        canales_por_idioma = obtener_canales_por_idioma(df)
        top_5_idiomas_viewers = obtener_top_5_idiomas_viewers(df)
        top_10_views_por_seguidor = calcular_views_por_seguidor(df)
        resumen_partner = analizar_partner(df)
        resumen_maduro = analizar_contenido_maduro(df)
        top_10_viewers_por_seguidor = calcular_viewers_por_seguidor(df)
        top_10_views_por_minuto = calcular_views_por_minuto_streaming(df)
        top_10_seguidores_nuevos = obtener_top_10_seguidores_nuevos(df)
        top_10_tiempo_streaming = obtener_top_10_tiempo_streaming(df)
        top_10_tiempo_visualizado = obtener_top_10_tiempo_visualizado(df)
        eficiencia_canal = analizar_eficiencia_canal(df)
        
        

        print("\n" + "=" * ANCHO_SECCION)
        print("             RESULTADOS DEL ANÁLISIS")
        print("=" * ANCHO_SECCION)

        print(f"\n{'Total de seguidores:':<30}{total_seguidores:>20,}")
        print(f"{'Promedio de viewers:':<30}{promedio_viewers:>20,.2f}")


        print("\n" + "-" * ANCHO_SECCION)
        print("TOP 5 - SEGUIDORES")
        print("-" * ANCHO_SECCION)
        print(f"{'Canal':<30}{'Seguidores':>20}")

        for _, fila in top_5_seguidores.iterrows():
            print(
                f"{fila['CANAL']:<30}"
                f"{fila['SEGUIDORES_TOTALES']:>20,}"
            )


        print("\n" + "-" * ANCHO_SECCION)
        print("TOP 5 - PROMEDIO DE VIEWERS")
        print("-" * ANCHO_SECCION)
        print(f"{'Canal':<30}{'Viewers promedio':>20}")

        for _, fila in top_5_viewers.iterrows():
            print(
                f"{fila['CANAL']:<30}"
                f"{fila['VIEWERS_PROMEDIO']:>20,}"
            )


        print("\n" + "-" * ANCHO_SECCION)
        print("TOP 5 - PICO DE VIEWERS")
        print("-" * ANCHO_SECCION)
        print(f"{'Canal':<30}{'Pico de viewers':>20}")

        for _, fila in top_5_pico_viewers.iterrows():
            print(
                f"{fila['CANAL']:<30}"
                f"{fila['PICO_VIEWERS']:>20,}"
            )


        print("\n" + "-" * ANCHO_SECCION)
        print("TOP 5 - VIEWS OBTENIDAS")
        print("-" * ANCHO_SECCION)
        print(f"{'Canal':<30}{'Views obtenidas':>20}")

        for _, fila in top_5_views.iterrows():
            print(
                f"{fila['CANAL']:<30}"
                f"{fila['VIEWS_OBTENIDAS']:>20,}"
            )


        print("\n" + "-" * 70)
        print("TOP 10 - SEGUIDORES Y VIEWERS")
        print("-" * 70)
        print(
            f"{'Canal':<25}"
            f"{'Seguidores':>20}"
            f"{'Viewers promedio':>25}"
        )

        for _, fila in top_10_seguidores_vs_viewers.iterrows():
            print(
                f"{fila['CANAL']:<25}"
                f"{fila['SEGUIDORES_TOTALES']:>20,}"
                f"{fila['VIEWERS_PROMEDIO']:>25,.0f}"
            )


        print("\n" + "-" * 85)
        print("TOP 10 - VIEWS POR SEGUIDOR")
        print("-" * 85)
        print(
            f"{'Canal':<25}"
            f"{'Seguidores':>18}"
            f"{'Views':>20}"
            f"{'Views/seguidor':>20}"
        )

        for _, fila in top_10_views_por_seguidor.iterrows():
            print(
                f"{fila['CANAL']:<25}"
                f"{fila['SEGUIDORES_TOTALES']:>18,}"
                f"{fila['VIEWS_OBTENIDAS']:>20,}"
                f"{fila['VIEWS_POR_SEGUIDOR']:>20.2f}"
            )
        
        
        print("\n" + "=" * ANCHO_SECCION)
        print("              ANÁLISIS DE IDIOMAS")
        print("=" * ANCHO_SECCION)


        print("\n" + "-" * ANCHO_SECCION)
        print("CANALES POR IDIOMA")
        print("-" * ANCHO_SECCION)
        print(f"{'Idioma':<20}{'Canales':>10}")

        for idioma, cantidad in canales_por_idioma.items():
            print(
                f"{idioma:<20}"
                f"{cantidad:>10}"
            )


        print("\n" + "-" * ANCHO_SECCION)
        print("TOP 5 - VIEWS OBTENIDAS POR IDIOMA")
        print("-" * ANCHO_SECCION)
        print(f"{'Idioma':<20}{'Views obtenidas':>25}")

        top_idiomas_views = obtener_top_5_idiomas_views(df)

        for idioma, views in top_idiomas_views.items():
            print(
                f"{idioma:<20}"
                f"{views:>25,.0f}"
            )

        print("\n" + "-" * ANCHO_SECCION)
        print("TOP 5 - PROMEDIO DE VIEWERS POR IDIOMA")
        print("-" * ANCHO_SECCION)
        print(f"{'Idioma':<20}{'Viewers promedio':>25}")

        for idioma, promedio in top_5_idiomas_viewers.items():
            print(
                f"{idioma:<20}"
                f"{promedio:>25,.2f}"
            )

        print("\n" + "-" * ANCHO_SECCION)
        print("TOP 5 - SEGUIDORES POR IDIOMA")
        print("-" * ANCHO_SECCION)
        print(f"{'Idioma':<20}{'Seguidores':>25}")

        top_idiomas_seguidores = obtener_top_5_idiomas_seguidores(df)
        for idioma, seguidores in top_idiomas_seguidores.items():
            print(
                f"{idioma:<20}"
                f"{seguidores:>25,.0f}"
            )

        print("\n" + "-" * ANCHO_SECCION)
        print("TOP 5 - PICO DE VIEWERS POR IDIOMA")
        print("-" * ANCHO_SECCION)
        print(f"{'Idioma':<20}{'Pico de viewers':>25}")

        top_idiomas_pico = obtener_top_5_idiomas_pico_viewers(df)
        for idioma, pico in top_idiomas_pico.items():
            print(
                f"{idioma:<20}"
                f"{pico:>25,.0f}"
            )
            
            
            
        print("\n" + "=" * ANCHO_SECCION)
        print("              ANÁLISIS DE PARTNER")
        print("=" * ANCHO_SECCION)

        for estado, datos_partner in resumen_partner.iterrows():
            if estado:
                tipo = "ES PARTNER"
            else:
                tipo = "NO ES PARTNER"
            print("\n" + "-" * ANCHO_SECCION)
            print(tipo)
            print("-" * ANCHO_SECCION)
            print(
                f"{'Cantidad de canales:':<30}"
                f"{datos_partner['CANAL']:>20,.0f}"
            )
            print(
                f"{'Promedio de seguidores:':<30}"
                f"{datos_partner['SEGUIDORES_TOTALES']:>20,.0f}"
            )
            print(
                f"{'Promedio de viewers:':<30}"
                f"{datos_partner['VIEWERS_PROMEDIO']:>20,.0f}"
            )
            print(
                f"{'Promedio de views:':<30}"
                f"{datos_partner['VIEWS_OBTENIDAS']:>20,.0f}"
            )
            print(
                f"{'Viewers por seguidor:':<30}"
                f"{datos_partner['VIEWERS_POR_SEGUIDOR']:>20.4f}"
            )
            print(
                f"{'Views por seguidor:':<30}"
                f"{datos_partner['VIEWS_POR_SEGUIDOR']:>20,.2f}"
            )
            
        print("\n" + "=" * ANCHO_SECCION)
        print("         ANÁLISIS DE CONTENIDO MADURO")
        print("=" * ANCHO_SECCION)

        for estado, datos_maduro in resumen_maduro.iterrows():
            if estado:
                tipo = "CANAL CON CONTENIDO MADURO"
            else:
                tipo = "CANAL SIN CONTENIDO MADURO"
            print("\n" + "-" * ANCHO_SECCION)
            print(tipo)
            print("-" * ANCHO_SECCION)
            print(
                f"{'Cantidad de canales:':<30}"
                f"{datos_maduro['CANALES']:>20,.0f}"
            )
            print(
                f"{'Promedio de seguidores:':<30}"
                f"{datos_maduro['SEGUIDORES_PROMEDIO']:>20,.0f}"
            )
            print(
                f"{'Promedio de viewers:':<30}"
                f"{datos_maduro['VIEWERS_PROMEDIO']:>20,.0f}"
            )
            print(
                f"{'Promedio de views:':<30}"
                f"{datos_maduro['VIEWS_PROMEDIO']:>20,.0f}"
            )
            print(
                f"{'Pico promedio de viewers:':<30}"
                f"{datos_maduro['PICO_VIEWERS_PROMEDIO']:>20,.0f}"
            )
        
        print("\n" + "=" * ANCHO_SECCION)
        print("            ANÁLISIS DE RENDIMIENTO")
        print("=" * ANCHO_SECCION)

        print("\n" + "-" * 75)
        print("TOP 10 - VIEWERS POR SEGUIDOR")
        print("-" * 75)

        print(
            f"{'Canal':<25}"
            f"{'Seguidores':>15}"
            f"{'Viewers':>15}"
            f"{'Viewers/seguidor':>20}"
        )

        for _, fila in top_10_viewers_por_seguidor.iterrows():
            print(
                f"{fila['CANAL']:<25}"
                f"{fila['SEGUIDORES_TOTALES']:>15,}"
                f"{fila['VIEWERS_PROMEDIO']:>15,.0f}"
                f"{fila['VIEWERS_POR_SEGUIDOR']:>20.4f}"
            )
        
        
        print("\n" + "=" * ANCHO_SECCION)
        print("            ANÁLISIS DE CRECIMIENTO")
        print("=" * ANCHO_SECCION)
        print("\n" + "-" * ANCHO_SECCION)
        print("TOP 10 - SEGUIDORES NUEVOS")
        print("-" * ANCHO_SECCION)
        print(
            f"{'Canal':<25}"
            f"{'Seguidores nuevos':>25}"
        )
        for _, fila in top_10_seguidores_nuevos.iterrows():
            print(
                f"{fila['CANAL']:<25}"
                f"{fila['SEGUIDORES_NUEVOS']:>25,}"
            )
        
        
        print("\n" + "=" * ANCHO_SECCION)
        print("              ANÁLISIS DE ACTIVIDAD")
        print("=" * ANCHO_SECCION)
        print("\n" + "-" * ANCHO_SECCION)
        print("TOP 10 - TIEMPO DE STREAMING")
        print("-" * ANCHO_SECCION)
        print(
            f"{'Canal':<25}"
            f"{'Tiempo de streaming':>25}"
        )

        for _, fila in top_10_tiempo_streaming.iterrows():
            print(
                f"{fila['CANAL']:<25}"
                f"{fila['TIEMPO_STREAMING']:>21,.0f} min"
            )
        
        print("\n" + "-" * ANCHO_SECCION)
        print("TOP 10 - TIEMPO VISUALIZADO")
        print("-" * ANCHO_SECCION)
        print(
            f"{'Canal':<25}"
            f"{'Tiempo visualizado':>25}"
        )

        for _, fila in top_10_tiempo_visualizado.iterrows():
            print(
                f"{fila['CANAL']:<25}"
                f"{fila['TIEMPO_VISUALIZADO']:>21,.0f} min"
            )



        print("\n" + "=" * ANCHO_SECCION)
        print("             ANÁLISIS DE EFICIENCIA")
        print("=" * ANCHO_SECCION)

        print("\n" + "-" * 85)
        print("TOP 10 - CRECIMIENTO POR MINUTO DE STREAMING")
        print("-" * 85)
        print(
            f"{'Canal':<25}"
            f"{'Seguidores nuevos':>20}"
            f"{'Streaming':>18}"
            f"{'Seguidores/min':>22}"
        )

        for _, fila in eficiencia_canal.iterrows():
            print(
                f"{fila['CANAL']:<25}"
                f"{fila['SEGUIDORES_NUEVOS']:>20,}"
                f"{fila['TIEMPO_STREAMING']:>14,.0f} min"
                f"{fila['SEGUIDORES_NUEVOS_POR_MINUTO']:>22.2f}"
            )

        print("\n" + "-" * 75)
        print("TOP 10 - VIEWS POR MINUTO DE STREAMING")
        print("-" * 75)
        print(
            f"{'Canal':<25}"
            f"{'Views':>18}"
            f"{'Streaming':>17}"
            f"{'Views/min':>15}"
        )

        for _, fila in top_10_views_por_minuto.iterrows():
            print(
                f"{fila['CANAL']:<25}"
                f"{fila['VIEWS_OBTENIDAS']:>18,}"
                f"{fila['TIEMPO_STREAMING']:>13,.0f} min"
                f"{fila['VIEWS_POR_MINUTO']:>15,.2f}"
            )

        consultar_canal(df)
        consultar_idioma(df)
        consultar_ranking(df)
        mostrar_grafico(df)


if __name__ == "__main__":
    ejecutar()

