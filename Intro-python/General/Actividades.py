
# Multiplicar dos numeros sin usar el simbolo de multiplicacion
a = 4
b = 8 
resultado = 0

for x in range(a):
    resultado += b 

#sprint(resultado)

# Ingresar nombre y apellido e imprimirlo al reves

Nombre = 'Dariel'
Apellido = 'Feliz'

concatenacion = Nombre + ' ' + Apellido

#print(concatenacion[::-1]) # [::-1] para dar vuelta a un string 

# Escribir una funcion que encuentre el elemto menor de una lista

lista = [1, 2, 5, 3, 55, -24, -13]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor 

#print('menor', menor)

# Escribir una funcion que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3

def calcularvolumen(r):
    return 4 / 3 *3.14 * r ** 3 
resultado = calcularvolumen(6)
#print (resultado)

# Escribir una funcion que indique si el usuario es mayor de edad

def esMayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self,edad):
        self.edad = edad 

usuario = Usuario(15)
usuario2 = Usuario(21)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

#print (resultado1,resultado2)

# Escribir una funcion que indique si un numero es par o impar 

def esPara(n):
    return n % 2 == 0 

resultado = esPara(10)
#print(resultado)

# Escribir una funcion que indique cuantas vocales tiene una palabra 

palabra = 'ChanchitoFeliz'
vocales = 0 

for x in palabra:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0
#print(vocales)

# Escribir una aplicacion que recibe una cantidad infinita de numeros hasta 
# decir basta, luego que devuelva la suma de los numeros ingresados 

# lista = []
# print('ingrese numeros y para salir escriba "basta"')
# while True:
#     valor = input('Ingrese valor:')
#     if valor == 'basta':
#         break
#     else:
#         try:
#             valor = int(valor)
#             lista.append(valor)
#         except:
#             print('Dato invalido')
#             exit()

# resultado = 0 
# for x in lista:
#     resultado += x 
# print(resultado)

#Escribit una funcion que recibe nombre y apellido y los vaya agregando
# a un archivo 

def agregaNombrArchivo(Nombre,apellido):
    c = open('nombrecompleto.txt','a')
    c.write(Nombre + ' ' + apellido + '\n')
    c.close
agregaNombrArchivo('Dariel','Rodriguez')

import os

os.remove('nombrecompleto.txt')