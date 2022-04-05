"""
Autor: Gabriela Hilario Acuapan
Fecha: 04/04/2022
Archivo: SumaArr.py
Descripción: Teniendo un arreglo de enteros encuentra el resultado de la suma de los elementos del arreglo.
"""
print("SUMA DE ELEMENTOS DE UN ARREGLO")

arreglo = [1,2,3]
print("\nEl arreglo es: \n" + str(arreglo))

def sum_arr(arreglo):
    suma = 0
    for n in arreglo:
        suma += int(n)
    return suma

print("\nLa suma total de los números es: " + str(sum_arr(arreglo)))