

# def numero1():

#     Music_Answer1 = input()

#     if Music_Answer1 == ('Six lines and five space'):
#         Music_Answer1 = False

#     if Music_Answer1 == ('Five lines and five space'):
#         Music_Answer1 = False

#     if Music_Answer1 == ('Five lines and four space'):
#         Music_Answer1 = True

#     if Music_Answer1 == ('Five lines and six space'):
#         Music_Answer1 = False

#     while True:
#         if Music_Answer1 == True:
#             Music_Point1 = 1
#         else:
#             Music_Point1 = 0 
#         return Music_Point1

# def numero2():
#     cantidad2 = 1
#     return cantidad2


# Puntaje = numero1() + numero2()

# print(Puntaje)

# def Question1():

#     a = input('El cantante considerado como el rey del pop es ')

#     while True:
#         if a == 'Elvis Presley':
#             Score = 1

#         else:
#             Score = 0
#         return Score


   # if a == 'respuesta':
   #     Score = 1
   # else:
   #     Score = 0
   # return Score

# def Question2():
#     Quantity2 = 2
#     return Quantity2


# Point = Question1()+ Question2()

# print(Point)

def History_Question1():
        History_Answer1 = input('What started the Second World War ')
        if History_Answer1 == ('Germany invaded Poland'):
            History_Point1 = 1 
        else:
            History_Point1 = 0 
                

        History_Answer2 = input('Where Paleolithic Period Paintings Have Been Found Mainly ')
        if History_Answer2 == ('In caves'): 
            History_Point2 = 1 
        else:
            History_Point2 = 0 


        History_Answer3 = input('How the First World War started ')
        if History_Answer3 == ('With the assassination of Archduke Francisco Fernando'):
            History_Point3 = 1 
        else:
            History_Point3 = 0 
              

        History_Answer4 = input('In what year did Christopher Columbus discover America ')
        if History_Answer4 == ('In 1492'):
            History_Point4 = 1 
        else:
            History_Point4 = 0 
    

        History_Answer5 = input('What nationality was Adolf Hitler ')
        if History_Answer5 == ('Was born in austria'):
            History_Point5 = 1 
        else:
            History_Point5 = 0 


        History_Answer6 = input('In which country did the Industrial Revolution begin ')

        if History_Answer6 == ('Britain'):
            History_Point6 = 1 
        else:
            History_Point6 = 0 
               
        History_Answer7 = input('Which island generated a conflict between the United Kingdom and Argentina ') 
        if History_Answer7 == ('The Falkland Islands'):
            History_Point7 = 1 
        else:
            History_Point7 = 0 
               
        History_Answer8 = input('Where the missile revolution took place ')
        if History_Answer8 == ('Cuba'):
            History_Point8 = 1 
        else:
            History_Point8 = 0 
               
        History_Answer9 = input('Who was the first Roman emperor ')
        if History_Answer9 == ('Cesar Augusto'):
            History_Point9 = 1 
        else:
            History_Point9 = 0 
               
        History_Answer10 = input('What war did Joan of Arc participate in ')
        if History_Answer10 == ('Britain'):
            History_Point10 = 1 
        else:
            History_Point10 = 0 
               

        Point = History_Point1 + History_Point2 + History_Point3 + History_Point4 + History_Point5 + History_Point6 + History_Point7 + History_Point8 + History_Point9 + History_Point10

        return print(Point)
        

# def History_Question2():
#         History_Answer2 = input('Where Paleolithic Period Paintings Have Been Found Mainly ')

#         while True:
#             if History_Answer2 == ('In caves'):
#                 History_Point2 = 1 
#             else:
#                 History_Point2 = 0 
            
#             return History_Point2


# def History_Question3():
#         History_Answer3 = input('How the First World War started ')

#         while True:
#             if History_Answer3 == ('With the assassination of Archduke Francisco Fernando'):
#                 History_Point3 = 1 
#             else:
#                 History_Point3 = 0 
            
#             return History_Point3


# def History_Question4(History_Answer4):
#         History_Answer4 = input('In what year did Christopher Columbus discover America ')
#         while True:
#             if History_Answer4 == ('In 1492'):
#                 History_Point4 = 1 
#             else:
#                 History_Point4 = 0 
            
#             return History_Point4

# def History_Question5(History_Answer5):
#         History_Answer5 = input('What nationality was Adolf Hitler ')

#         while True:
#             if History_Answer5 == ('Was born in austria'):
#                 History_Point5 = 1 
#             else:
#                 History_Point5 = 0 
            
#             return History_Point5

#Point = History_Question1() + History_Question2() + History_Question3() + History_Question4() + History_Question5()

History_Question1()