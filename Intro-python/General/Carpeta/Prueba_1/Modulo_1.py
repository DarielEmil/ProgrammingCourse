
'''

Utilizacion de modulos

'''

# import Modulos # Para importar el saludo

# print(Modulos.Mascotas)
# Modulos.saludo('Dariel') # Para utilizar una funcion 

# import Modulos as Xs # Para renombrar el modulo

# print(Xs.Comida) 

# from Modulos import saludo,Comida # Para poder importar especificamente un modulo
                    
# print(Comida)
# saludo('Mundo') 

# Numero = ( 5 , 6 , 7, 8 )

# War1 = ['Eventos','Historicos']
# War2 = ['Acontecimientos','Desastrosos']

# from General.Carpeta.Modulos import Quantity


List_Answer1 = ['RayCharles','Sebastian','Raul', 'Benjamin']
List_Answer2 = ['Maria','Sara','Daniela', 'Ana']

Quantity = '10'

# import os 

# path = ('/intro-python/Prueba/Modulos')

# os.chdir(path)

# import Modulos

# Quantity = Modulos.Quantity


# print(List_Answer1[0][1])

# if Quantity == '10':
#     Answer = List_Answer1[0]
#     Answer2 = List_Answer1[1]
#     List = [Answer,Answer2]

def Answer_Variable1(List):
    if Quantity == '10':
        Answer = List_Answer1[0]
        Answer2 = List_Answer1[1]
        List = [Answer,Answer2]
    return print(List=List)
    # elif Quantity == '20':
    #     Answer = List_Answer1[1]

# def Answer_Variable2(Quantity):
#     if Quantity == '10':
#         Answer = List_Answer2[2]
#     elif Quantity == '20':
#         Answer = List_Answer2[1]
#     return print(Answer)

# def Answer_Variable(Quantity):
#     Answer_Variable1(Quantity=Quantity)
#     Answer_Variable2(Quantity=Quantity)

Answer_Variable1([1])