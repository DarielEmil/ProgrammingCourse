
'''

Gestion de archivos

'''
# c = open('Chanchito.txt','w') # R es un permiso includo  o append para modificar el archivo 
#print (c.read())
#print(c.readline())
#print(c.readline()) # Para poder leer cada linea 1 en 1 

 # Write para poder escribir en el archivo o x para crear un nuevo archivo

#for x in c:
    #print(x)

# c.close() #Para cerrar el archivo 

# c.write('\nAgregaremos una nueva linea a nuestro archivo') # \n Para poder agregar una nueva linea

# x = open('chanchito.txt')


# print(x.read())

'''

Para eliminar archivos

'''

import os 

if os.path.exists('chanchito.txt'):
    os.remove('Chanchito.txt')
else:
    print('El archivo no existe')

'''

Para eliminar una carpeta

'''

os.rmdir('') # Ingresar el nombre de la carpeta  