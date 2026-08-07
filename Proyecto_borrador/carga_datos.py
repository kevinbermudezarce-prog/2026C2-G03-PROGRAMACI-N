from pathlib import Path

import kagglehub
import pandas as pd

dataset = "aayushmishra1512/twitchdata"
def cargar_datos() -> pd.DataFrame:
    """Descarga y carga el dataset de Kaggle de Top Streamers on Twitch."""
    
    try:
    # Descargar el dataset completo
        ruta_descarga = Path(
        kagglehub.dataset_download(
            dataset,
            force_download=True
        )
        )

        print("Dataset descargado en:")
        print(ruta_descarga)

        # Buscar automáticamente todos los CSV
        if ruta_descarga.is_file():
            archivos_csv = [ruta_descarga]
        else:
            archivos_csv = list(ruta_descarga.rglob("*.csv"))

        if not archivos_csv:
            raise FileNotFoundError(
                "El dataset se descargó, pero no contiene archivos CSV."
            )

        print("\nArchivos CSV encontrados:")

        for archivo in archivos_csv:
            print("-", archivo.name)

        # Abrir el primer CSV encontrado
        df = pd.read_csv(archivos_csv[0])

        print("\nDatos cargados correctamente.")
        #return df
        print (df.head())

    except Exception as error:
        print("\nOcurrió un error:")
        print(type(error).__name__)
        print(error)
        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error    

if __name__ == "__main__":
    df = cargar_datos()
    if df.empty:
        print("No se pudo cargar los datos.")
    else:
        print("Datos cargados correctamente:")
        print(df.head())

