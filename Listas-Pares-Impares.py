# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 09:33:26 2021

@author: DavidAlcázarSánchez
"""

#1. Crear una lista con N numeros enteros.
#2. Mostrar los elementos de la lista ([, , ,]->NO).
#3. Crear "listapares" con los elementos pasres de la lista inicial. Mostrarla.
#4. Exactamente lo mismo con "listaimpares"
#5. Crear una lista ordenada de menor a mayor a partir de la lista inicial.

#Creamos una variable auxiliar que usaremos después.
#La lista vacía la llenaremos más tarde.
contador = 1
lista_numeros = []

#Preguntamos a través de un input cuántos números vamos a utilizar. 
cantidad_de_numeros = int(input("¿Con cuántos números quieres operar?: "))

#A través de un bucle while, pedimos los números.
#Para ello usaremos nuestro contador como limitador, poniendo de máximo la cifra del primer input.
while contador <= cantidad_de_numeros:
    numero = int(input("Elige un número para añadir a la lista: "))
    lista_numeros += [numero]
    contador = contador + 1

print()

#A través de un for, imprimimos cada campo de la lista, en vez de la lista completa.
print("\nEsta es la lista de números elegidos:\n")
for num in lista_numeros:
    print("-", num)
    
#Volvemos a usar for para pintar solo los pares.
print("\nEsta es la lista de números pares entre los que has elegido:\n")
for num in lista_numeros:
    if num %2 == 0:
        print("-", num)

#El mismo método para los impares.        
print("\nEsta es la lista de números impares entre los que has elegido:\n")
for num in lista_numeros:
    if num %2 != 0:
        print("-", num)
        
#Para poder ordenar la lista hemos utilizado el método de orden en burbuja.
#Como el hecho de que la lista se ordene de menor a mayor o viceversa, he añadido un input y dos if para dar la elección. 
#Con el primer for recorremos toda la lista.
#Con el segundo for, recorremos toda la lista de nuevo en cada movimiento de num.
#Dentro del segundo for, hemos creado un if para intercambiar las posiciones de los campos que lo requieran.
#Y una variable auxiliar, para guardar uno de los cambios y no perderlo en el intercambio.        
orden = input('\nIntroduce el comando "<" o el comando ">" si quieres ver la lista ordenada de mayor a menor o viceversa: ')

if orden == "<":
    for num in range(len(lista_numeros)-1, -1, -1):
        for recorrido in range(num):
            if lista_numeros[recorrido] < lista_numeros[recorrido + 1]:
                auxiliar = lista_numeros[recorrido]
                lista_numeros[recorrido] = lista_numeros [recorrido + 1]
                lista_numeros[recorrido +1] = auxiliar
        print ("-", lista_numeros[num])  
    
elif orden == ">":
    for num in range(len(lista_numeros)-1, -1, -1):
        for recorrido in range(num):
            if lista_numeros[recorrido] > lista_numeros[recorrido + 1]:
                auxiliar = lista_numeros[recorrido]
                lista_numeros[recorrido] = lista_numeros [recorrido + 1]
                lista_numeros[recorrido +1] = auxiliar
        print ("-", lista_numeros[num])         
        
#Ponemos los print a la altura del primer for para que se pinten todos los campos una única vez.