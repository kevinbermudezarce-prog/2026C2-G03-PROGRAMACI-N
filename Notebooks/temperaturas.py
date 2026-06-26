temperaturas = []
cantidad_registrada = 0

# Complete aquí el ciclo while.
while True:
    print (" --- REGISTRO DE TEMPERATURAS --- ")
    print ("1. Registrar temperatura")
    print ("2. Reporte temperaturas")
    print ("3. Salir del sistema")
    
    opcion = input ("Ingrese una opción del menú:  ")
    
    if opcion == "1":
        temp = float( input ("Ingrese la temperatura del día: "))
        temperaturas.append(temp)
        print("Registro agregado exitosamente")
        
    elif opcion == "2":
        print("Reporte de temperaturas")
        cantidad = len(temperaturas)
        print (f"Cantidad temperaturas registradas {cantidad}")
        print(f"Temperatura maxima {max(temperaturas):,.2}")
        print(f"Temperatura minima {min(temperaturas):,.2}")
        print(f"Temperatura promedio {sum(temperaturas) / cantidad:,.2}")
        
        
        
    elif opcion == "3":
        print ("Cerrando aplicación")
        break
        
    else:
        print ("Opción invalida, ingrese otra opción")
        
        
        
        
        