"""Programa principal del proyecto modular BCCR."""

from lectura_datos import cargar_tabla_bccr
from limpieza_datos import limpiar_datos

def ejecutar ():
    """Cargar los datos y presentar el menú del sistema"""
    datos_crudos = cargar_tabla_bccr()
    datos = limpiar_datos(datos_crudos)
    print(datos.head())

if __name__ == "__main__":
    ejecutar()

