"""Programa principal del proyecto modular BCCR."""

from lectura_datos import cargar_tabla_bccr, mostrar_top_10
from limpieza_datos import limpiar_datos, resumir_por_tipo_entidad, filtrar_diferencial_alto

def ejecutar ():
    """Cargar los datos y presentar el menú del sistema"""
    datos_crudos = cargar_tabla_bccr()
    datos = limpiar_datos(datos_crudos)

    while True:
        print("\nPROYECTO DE ANÁLISIS BCCR ")
        print ("1. Mostrar primeras 10 entidades limpias.")
        print ("2. Promedio por tipo de entidad.")
        print ("3. Mostrar entidades financieras con diferencial mayor al promedio.")
        print ("4. Mostrar lista entidades y exportar CSV.")
        print ("5. Graficar.")
        print ("6. Salir.")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            print (mostrar_top_10(datos))
        elif opcion == "2":
            promedios = resumir_por_tipo_entidad(datos)
            print (f"El promedio general del diferencial es:, {promedios[0]:.2f}")
            print ("Promedio por tipo de entidad: \n", promedios[1].to_string(index=False))
        elif opcion == "3":
            print("Entidades con diferencial mayor al promedio:")
            entidades_altas = filtrar_diferencial_alto(datos)
            print(mostrar_top_10(entidades_altas))
        elif opcion == "4":
            pass    
        elif opcion == "5":
            print ("Graficando ...")   
        elif opcion == "6":
            print ("Análisis finalizado")
            input("presione enter para salir")
            break
        elif opcion == "7":
            pass
        else:
            print ("Opción inválida \nEscriba un número del 1 al 6.")
        input ("\nPrecione enter para continuar\n")
        
        
if __name__ == "__main__":
    ejecutar()

