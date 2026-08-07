from carga_datos import cargar_datos

def ejecutar():
    df = cargar_datos()
    if df.empty:
        print("No se pudo cargar los datos.")
    else:
        print("Datos cargados correctamente:")
        print(df.head())


if __name__ == "__main__":
    ejecutar()






