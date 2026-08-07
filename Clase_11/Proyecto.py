#import os
#print (os.getcwd())




#import math
#print(math.sqrt(25))


#import numpy as np
#numeros = np.array([10, 20, 30, 40])
#print(numeros.mean())

#import pandas as pd

#datos = {
#    "Nombre": ["Ana", "Luis", "Carlos"],
#    "Edad": [20, 25, 22]
#}

#df = pd.DataFrame(datos)
#print(df)


#import matplotlib.pyplot as plt

#ventas = [15, 20, 18, 25]

#plt.plot(ventas)

#plt.show()


import matplotlib.pyplot as plt

meses = ["Enero", "Febrero", "Marzo", "Abril"]
ventas = [120, 150, 180, 200]

plt.bar(meses, ventas)
plt.title("Ventas por mes")
plt.xlabel("Meses")
plt.ylabel("Cantidad de ventas")

plt.show()