
'''

funciones

'''


#def Mi_funcion():
 #   print('Mi primera funcion!')

#Mi_funcion()

#def imprimeDato(nombre): # Esto es un argumento
 #   print ('EL nombre completo es:', nombre)

#imprimeDato('Chanchito') # Esto es un parametro

#def imprimeDato1(Nacionalidad, pais): # Utilizando 2 argumentos y 2 parametros
#   print ('La nacionalidad y pais son ',Nacionalidad, pais)
#imprimeDato1('Canadiense', 'canada')

#def imprimeDato2(*Nombres): # Utilizando * para tener 1 argumento y varios parametros
#    print ('Los nombres son ', Nombres)
#imprimeDato2('Chanchito', 'Emil','pablo')

#def imprimeDato3(*Comida): # Para seleccionar un parametro de la lista  
#    print ('Las comidas son', Comida[2])
#imprimeDato3('Pizza','sopa', 'arroz', 'pan')

#def nombre_completo(apellido, nombre): # Asignarle un parametro junto al argumento
#    print(nombre, apellido)
#nombre_completo(nombre='chanchito', apellido='feliz')

#def nombre_completo2(**kwargs): # Otra forma de asignarle a un argumento un parametro usando **kwargs
#    print (kwargs['nombre'], kwargs['apellido'])
#nombre_completo2(nombre='chanchito', apellido='Feliz')

'''

Mas funciones

'''
#def Mi_funcion2 (argument = 'Chanchito'): # Para asignar un valor por defecto
    #print(argument)
# Mi_funcion2('batman')
# Mi_funcion2()

#def Mi_funcionLista(lista): # para poder asignarle una lista como argumento
    #for el in lista:
        #print (el)
#Mi_funcionLista(['chanchito', 'Feliz'])


#def concatena_nombres(lista): # para retonar un valor para volverlo a usar
    #i = ''
    #for el in lista:
        #i = i + ' ' + el
    #return i 
#Nombres = concatena_nombres(['chanchito', 'feliz'])

#print(Nombres)

'''

Recursividad

''' 

def recursion(i):
    if (i < 1):
        return i
    print(i)
    recursion(i - 1)
recursion(6)


