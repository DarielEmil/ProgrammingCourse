
# name = ''
import time

# number = 0

# for number in range(10):
#     if number == 5:
#         break    # break here    

#     print('Number is ' + str(number))

# print('Out of loop')

# while True:
#     print('Please type your name')
#     name = input()
#     if name == 'Your name':
#         break
#     print("Try again")
    
# print ("Thank you")

# print('Sin tiempo de respuesta')
# time.sleep(5)
# print('Tiempo de espera')

from Modulo_1 import Quantity

def Quiz():
    
    # quantity = input('Cantidad ')

    pregunte1 = input('respuesta ')
    pregunte2 = input('respuesta ')
    pregunte3 = input('respuesta ')

    if pregunte1 == '1':
        point1 = 1
    else:
        point1 = 0

    if pregunte2 == '1':
        point2 = 1
    else:
        point2 = 0

    if pregunte3 == '1':
        point3 = 1
    else:
        point3 = 0

    Score = point1 + point2 + point3 

    while int(Quantity) == 6:
        pregunte4 = input('respuesta ')
        pregunte5 = input('respuesta ')
        pregunte6 = input('respuesta ')

        if pregunte4 == '1':
            point4 = 1
        else:
            point4 = 0

        if pregunte5 == '1':
            point5 = 1
        else:
            point5 = 0

        if pregunte6 == '1':
            point6 = 1
        else:
            point6 = 0
        
        Score = point1 + point2 + point3 + point4 + point5 + point6

        return print(Score)

    print(Score)


Quiz()