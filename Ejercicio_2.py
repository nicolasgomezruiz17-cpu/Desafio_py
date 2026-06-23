#libreria numpy
import numpy as np

#carga del archivo .csv
array = np.loadtxt("alcohol_cerveza.csv", delimiter=',', skiprows=1)

print("Array: ")
print(array)
print("---------------------------------------------")

print("Media: ")

media = array.mean()
print(media)
print("-------------------")

print("Desviación: ")

desviacion = array.std()

print(desviacion)

print("----------------------------")

print("Límite inferior:")

lic = media - (3*desviacion)

print(lic)

print("-------------------------")

print("Límite superior:")

lsc = media + (3*desviacion)

print(lsc)

print("----------------------------")

array_filtrado = np.logical_or(array<lic, array>lsc)

fuera_de_control = array[array_filtrado]
print(f"Valores fuera de control: {fuera_de_control}")
print(f"Cantidad: {len(fuera_de_control)}")