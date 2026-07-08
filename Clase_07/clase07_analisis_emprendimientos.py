"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes


def calcular_total(lista_ventas):
    """Recibo una lista, la sumo y retorno el total."""
    return sum(lista_ventas)


def calcular_promedio(lista_ventas):
    """Retorna el promedio de las ventas de la lista ventas"""
    return sum(lista_ventas) / len(lista_ventas)


def calcular_porcentaje (total_ventas ,meta):
    """Calcula el porcentaje de cumplimiento de la meta"""
    return total_ventas / meta * 100





def imprimir_reporte(reporte):
    """Imprime el reorte final de ventas por emprendimiento"""
    print("\nREPORTE FINAL")
    print("-" * 60)
    for fila in reporte:
        print(f"Empredimiento: {fila["nombre"].upper()}")
        print(f"Provincia: {fila["provincia"]}")
        print(f"Tipo: {fila["tipo"]}")
        
        print(f"Total semanal: ₡{fila["total"]:,.2f}")
        print(f"Promedio diario: ₡{fila["promedio"]:,.2f}")
        print(f"Porcentaje cumplimiento: {fila["porcentaje"]:,.0f}%")
        print(f"Estado: {fila["estado"]}")
        print("-" * 60)
    print(f"Cantidad de emprendimientos: {len(reporte)}")


def calcular_clasificacion(porcentaje_logro):
    """"Clasifica el emprendimiento según porcentaje de cumplimiento de meta de ventas."""
    if porcentaje_logro >= 100:
        clasificacion_emprendimiento = "Meta alcanzada, emprendimiento rentable"
    elif porcentaje_logro >= 80:
        clasificacion_emprendimiento = "Observación, no se logró la meta."
    else:
        clasificacion_emprendimiento = "ADVERTENCIA, problemas de rentabilidad. URGE ATENCIÓN."
    return clasificacion_emprendimiento


reporte = []
provincias = set()
venta_mas_alta = 0
emprendimientos_mas_ingresos = []


#print("Cantidad de sedes: " ,len(sedes))
#print (type (sedes), "vrs", type (sedes[0]))
#print ("Datos por sede: " ,sedes[0].keys())





for emprendimiento in sedes: 
    #emprendimiento = sedes[0]
    ventas = emprendimiento ["ventas"]
    meta = emprendimiento ["meta"]

    total_emprendimiento = calcular_total (ventas)
    promedio_emprendimiento = calcular_porcentaje (total_emprendimiento , meta)
    promedio_diario = calcular_promedio (ventas)
    clasificacion = calcular_clasificacion (promedio_emprendimiento)


    provincias.add(emprendimiento["provincia"])
    
    #print ("\nEmprendimiento: ",emprendimiento ["nombre"])
    #print ("Total de ventas: ", total_emprendimiento)
    #print ("Porcentaje logrado: ", promedio_emprendimiento)
    #print ("Promedio diario: ", promedio_diario)
    #print ("Analisis de emprendimiento: ", clasificacion)
    
    reporte.append(
        {
            "nombre": emprendimiento ["nombre"],
            "provincia": emprendimiento["provincia"],
            "tipo": emprendimiento["tipo"],
            "total": total_emprendimiento,
            "promedio": promedio_diario,
            "porcentaje": promedio_emprendimiento,
            "estado": clasificacion
            
        }
    )
    
    ranking []
    
    imprimir_reporte(reporte)
    
    if total_emprendimiento > venta_mas_alta:
        venta_mas_alta = total_emprendimiento
        emprendimientos_mas_ingresos = [emprendimiento ["nombre"]]
    elif total_emprendimiento == venta_mas_alta:
        emprendimientos_mas_ingresos.append(emprendimiento ["nombre"])
    
    
    
#venta_maxima = max(fila["total"] for fila in reporte)


print ("\n Provincias analizadas: " ,provincias)

#for fila in reporte:
#    if fila["total"] == venta_maxima:
#        print(f"\n Sede con mayor cantidad de ventas: {fila['nombre']} con ₡{fila['total']:,.2f}")

print ("La venta más alta es: ", venta_mas_alta, "El cual corresponde a: " ,emprendimientos_mas_ingresos)



def obtener_total(fila):
    """Se ordena el orden de los emprendimientos para poder generar un ranking de ventas a mostrar"""
    return fila["total"]
reporte.sort(key=obtener_total, reverse=True)


print("\n Ranking de ventas entre los emprendimientos: ")
print("-" * 60)



for posicion, fila in enumerate(reporte, start=1):
    print(f"{posicion}. {fila['nombre']} - ₡{fila['total']:,.2f}")



