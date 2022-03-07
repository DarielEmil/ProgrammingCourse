
'''

Utilizacion de input y primeros juegos

'''

#dato = input('ingrese dato: ')

lista = ['Hola','Mundo','Chanchito','Feliz','Dragones']

# if lista.count(dato) > 0:
#     print ('el dato existe ', dato)
# else:
#     print ('el dato no exise :( ', dato)

# primero = input ('ingrese primer numero ')
# segundo = input ('ingrese segundo numero ')

# primernumero = int (primero)
# segundonumero = int (segundo)

#print (primernumero + segundonumero)

'''

Usando try y except y otra forma de cambiar de valor int

'''

# tercero = input ('Ingrese la primera cantidad ')

# try: 
#     tercero = int(tercero)
# except: 
#     tercero = 'Chanchito feliz'

# cuarto = input('Ingrese la segunda cantidad ')

# try:
#     cuarto = int(cuarto)
# except:
#     cuarto = 'chanchito triste'

# if tercero == 'Chanchito feliz' or cuarto == 'chanchito triste':
    #print('ingresaste mal un dato, prueba de nuevo solo con numeros')
#else:
    #print (tercero + cuarto)

'''

Validacion 

'''
primero =  input ('Ingrese datos ')

try:
    primero = int(primero)
except:
    primero = 'Chanchito enojado'

if primero == 'Chanchito enojado':
    print('el valor no es valido')
    exit()

segundo = input ('ingrese datos ')

try:
    segundo = int(segundo)
except:
     segundo = 'Chanchito triste'

if segundo == 'Chanchito triste':
    print('el valor no es valido')
    exit()

#print (primero + segundo)
'''

Haciendo una calculadora (simple) +, -, *, /

'''
simbolo = input('ingrese operacion ')

if simbolo == '+':
    print ('suma ', primero + segundo)

elif simbolo == '-':
    print ('resta ', primero - segundo)

elif simbolo == '*':
    print ('Multiplicacion ', primero * segundo)

elif simbolo == '/':
    print ('division ', primero / segundo)

else:
    print('El simbolo agregado no es valido')