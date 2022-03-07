# print("Bienvenido a la su listado de compras digital" + '\n' + '\n' + 'Por favor seleccione que categoria quiere guardar' + '\n' )

# ListadoDeCompras = {
#     "Vegetales": [],
#     "Carnes": [],
#     "Otros": [],
# }

# print('Este es su listado de compras', ListadoDeCompras.keys())
# while(True):
#     Category = input('Seleccione uno de las categorias anteriores ')
#     # if Category != "Vegetales" or Category != "Carnes" or Category != "Otros":
#     #     continue

#     if Category == "Vegetales":
#         ListadoDeCompras["Vegetales"] = input('Inserte los vegetales ')
#         print('Este es su lista de vegetales', ListadoDeCompras['Vegetales'])
#         break

#     if Category == "Carnes" or Category == "Carne":
#         ListadoDeCompras["Carnes"] = input('Inserte las carnes ')
#         print('Este es su lista de Carnes', ListadoDeCompras['Carnes'])
#         break

#     if Category == "Otros":
#         ListadoDeCompras["Otros"] = input('Inserte las otros ')
#         print('Este es su lista de otros', ListadoDeCompras['Otros'])
        
#         break
    
#     else:
#         continue

# def Calculo(num = int(input())):
#     Result = num + 1
#     print(Result)

# Calculo()


# name = 'Alice'
# age = 3000

# if name == 'alicia':
#     print('Welcome alice')
# elif age < 12:
#     print('How are you ?')
    
# elif age > 2000:
#     print('A inmortal vampire')

# elif age > 100:
#     print('Hello grandma')


# while True:
#     print("How are you?")
#     name = input()
#     if name != "Joe":
#         continue
#     print('Hello, ' + name + " What's your password ?")
#     password = input()
#     if password == "Swordfish":
#         break
# print("Access granted")

# Frutas = ["Manzana", "Pera", "Uvas", "Madarina"]
# Carnes = ["Carne de res", "Pollo", "Carne de cerdo", "Salchichas"]
# Liquidos = ["Jugo de Limon", "Leche", "Jugo de tamarindo", "Jugo de chinola"]

# Comestibles = [Frutas[0], Carnes[0], Liquidos[0]]

# Terrestres = ["Tigre", "Leon", "jirafa", "Hipopotamo"]
# Acuaticos = ["Pulpo", "Pez", "Tiburon", "Caballito de mar", "Langosta"]
# Aereos = ["Buitre", "Paloma", 'Gaviota', "Halcon"]

# Animales = [Terrestres[0], Acuaticos[0], Aereos[0]]



# print("Hello world")

# about_me = {
#     "Name": "Dariel Rodriguez",
#     "Age": "18",
#     "Location": "Santo Domingo, DO",
#     "Experience": "Null",
#     "Languagues": "Spanish and English"
# }
# print(about_me)

# list = ["a","e","i", "o", "u"]

# for x in range(len(list)):
#     print("Esta es " + list[x] + " una consonante y es la numero " + str(x))


# Music1_80 = ["Take on Me a-ha", "Losing My Religion", "Smells Like teen Spirit", "What is love"]


# Answer1 = Music1_80
# Answer1 += ["It's my live"]

# print(id(Music1_80))


# --------------- LIST CHAPTER ---------------


# Spam = [2, 4, 6, 8, 10]
# Bacon = [3.14, "cat", 11, "cat", True]


# while True:
#     AllList = []
#     Select = input("What list do you want to use? \n")
#     if Select == "Spam":
#         AllList = Spam
#         ListName = "Spam"

#     elif Select == "Bacon":
#         AllList = Bacon
#         ListName = "Bacon"
#     elif Select == "exit":
#         break
#     else:
#         print("The list named " + Select + " doesn't exist") 

#     while Select == "Spam" or Select == "Bacon":
#         print("What do you want to do with your " + ListName +  " list? \n")
#         print("This is your list ", AllList)
#         ChooseFunctions = input("Select what function do you want to use? \n")

#         while ChooseFunctions == "Append":
#             AppendValue = input("Enter your new item ")
#             AllList.append(AppendValue)
#             print("You enter " + AppendValue + " Successful")
#             break

#         while ChooseFunctions == "Remove":
#             print("Your items is a number , string or float? ")
#             RemoveType = input()
#             try:
#                 if RemoveType == "String":
#                     RemoveValue = input("What do you want to remove from your list? \n")
#                     AllList.remove(str(RemoveValue))
#                     print("You remove your item " + RemoveValue + " , your list looks like \n", AllList)
#                     break

#                 elif RemoveType == "Number":
#                     RemoveValue = input("What do you want to remove from your list? \n")
#                     AllList.remove(int(RemoveValue))
#                     print("You remove your item " + RemoveValue + " , your list looks like \n", AllList)
#                     break

#                 elif RemoveType == "Float":
#                     RemoveValue = input("What do you want to remove from your list? \n")
#                     AllList.remove(float(RemoveValue))
#                     print("You remove your item " + RemoveValue + " , your list looks like \n", AllList)
#                     break
#                 else:
#                     print('Need to be a number or string')
#                     continue
#             except ValueError:
#                 print("Your item is not in the list")
#             continue

        
#         while ChooseFunctions == "Contactenation":
#             if AllList == Spam:
#                 AllList += Bacon

#             elif  AllList == Bacon:
#                 AllList += Spam

#             print("Your list looks like this ", AllList)
#             break
        
#         while ChooseFunctions == 'Replicate':
#             print("How many times do you want to replicate yor list? ")
#             x = int(input())
#             print(AllList*x)
#             break

#         while ChooseFunctions == "Insert":  
#             print("What item do you want to add and in which index of your list? ")
#             y = int(input())
#             NewValue = input()
#             AllList.insert(y,NewValue)
#             print(AllList)
#             break
        
#         while ChooseFunctions == "Index":
#             print("What index do you want to know? " + "Must be in your list, this is your list now  \n", AllList )
#             ValueType = input("What index type is your index? " + "String of Integer ")
#             try:
#                 if ValueType == "Integer" or ValueType == "Int":
#                     print(AllList.index(int(input())))
#                     break
#                 elif ValueType == "String" or ValueType == "Str":
#                     print(AllList.index(str(input())))
#                     break
#             except ValueError:
#                 print("That item doesn't exist")
#             else:
#                 print("Need to be a String or Integer ")
        
#         while ChooseFunctions == "Del":
#             print("Please enter a number ")
#             try:
#                 z = int(input("Enter what index do you want to remove from your list \n"))
#             except ValueError:
#                 print("You enter a string need to be a number")
#                 continue
#             else:
#                 try:
#                     del AllList[z]
#                     print("You remove the item from index ", z )
#                     break
#                 except IndexError:
#                     print('Your index is out of range')

#         if ChooseFunctions == "exit":
#             break


# --------------- ---------------

#spam = ["apples", 'bananas', 'tofu', 'cats', "rice", "Beans", "Lion", "Elephant", "Octopus","Train" ]


# def ListToString(converter):
#     for i in range(len(converter) - 1):
#         converter[i] += ', '

#     z = converter[-1]
#     converter[-1] = 'and '
#     converter.append(z)
#     NewString = ""

#     for x in converter:
#         NewString += x
#     return NewString

# print(ListToString(spam))


def Suma(Sum=1):
    Sum += 1
    print(Sum)
#Suma()

#a = [3, 4, 5, 20, 5, 25]
# --------------- DICTIONARY CHAPTER ---------------

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

from typing import Text

# print("ALice" in birthdays.values())



# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break

#     if name in birthdays:
#         print( birthdays[name] + " is the birthday of " + name)
#     else:
#         print("I do not have this birthday " + name)
#         print("What is your birthday? ")
#         bday = input()
#         birthdays[name] = bday
#         print(birthdays)


TheBoard = {
    "Top-L": " ","Top-M": " ", "Top-R": " ",
    "Mid-L": " ", "Mid-M": " ", "Mid-R": "",
    "Low-L": " ", "Low-M": " ", "Low-R": " "
}

def PrintBoard(Board):
    print(Board["Top-L"] + '|' + Board["Top-M"] + "|" + Board["Top-R"]) 
    print(" ___ " + "\n")
    print(Board["Mid-L"] + '|' + Board["Mid-M"] + "|" + Board["Mid-R"]) 
    print(" ___ " + "\n")
    print(Board["Low-L"] + '|' + Board["Low-M"] + "|" + Board["Low-R"] ) 

#turn = "X"

#for x in range(9):
#    PrintBoard(TheBoard)
#    move = input('Make your move ')
#    TheBoard[move] = turn
#    if turn == "X":
#        turn = "0"
#    else:
#        turn = "X"

Allguest = {
    'Alice': {"Apples": 5, "Pretzels": 12 },
    'Bob': {"Ham Sandwiches": 3, "Apples":2 },
    "Carol": {"Cups": 3, "Apple Pies":  1  } 
}

def TotalBrought(Guest,Items):
    TotalItems = 0
    for x,i in Guest.items():
        # Get only one value, inside of the key
        TotalItems = Guest[x].get(Items,0) 
#       #TotalItems += i.get(Items,0)
    print(TotalItems)

#TotalBrought(Allguest,'Apples')

FantasyInventory = {
    "Arrow": 12,
    "Gold Coin": 42,
    "Rope": 1,
    "Torch": 6,
    "Dagger": 1
}

#def DisplayInventory(Inventory):
#    TotalItems = 0 
#    for x,y in Inventory.items():
       # print(y,x)
#        TotalItems += y
#    print("Your total items are " + str(TotalItems))
    
#DisplayInventory(FantasyInventory)

DragonLoot = ["Gold Coin", "Dagger", "Gold Coin", "Gold Coin", "Ruby"]
Inv = {
    "Gold Coin": 42,
    "Rope": 1
}
def AddNewInventory(NewInv,NewdragonLoot):
    NewItemsTotal = 0
    for i in NewdragonLoot:
        NewInv.setdefault(i,0)
        NewInv[i] += 1
    for k,v in NewInv.items():
        NewItemsTotal += v
        print(k.ljust(10,'.') + '%s'.rjust(10) % (v))
    print('Your total items are ' + '%s' % (NewItemsTotal))

# def AddNewInventory(NewInv, NewDragonLoot):
#     TotalNewItems = 0
#     for z in NewDragonLoot:
#         NewInv.setdefault(z,0)
#         NewInv[z] += 1
    
#     for x,i in NewInv.items():
#         print(i,x)
#         TotalNewItems += i
    
#     print("Your total items are " + str(TotalNewItems))

#AddNewInventory(Inv,DragonLoot)

        
def Spam():
    """ This is a multiline comment to help 
    explain what the spam() function does 
    """
    print("Hello")


Name = "Ka'el "
Age = 114

"""
print('My name is %s. I am %s years old ' % (Name,Age))
print(f"My name is {Name}. Next years i will be {Age + 1}") 

"""



# print("How are you " )
# feeling = input()

# if feeling.lower() == "great":
#     print("I feel great too ")
# else:
#     print("I hope the rest of your day is good ")


# while True:
#     print("Enter your age ")
#     age = input()
#     if age.isalnum():    
#         break
#     print("Please enter a number for your age ")

a = "hello, world! " 

# b, c, d = a.partition(' ')



#print(a.center(30,'-'))

def PrintPicnic(ItemsDict, Leftwidth, Rightwidth):
    print(" Picnic items ".center(Leftwidth + Rightwidth, '-'))
    for k,v in ItemsDict.items():
        print(k.ljust(Leftwidth, '.') + "%s".rjust(Rightwidth) % (v))

PicnicItems = {
    "Sandwiches": 4, "Apples": 12,
    "Cups":4, "Cookies": 8000
}

#PrintPicnic(PicnicItems,12, 5)
 
''' A = 'Hello, World'
A.rstrip, lstrip
A = A.strip('hello')
print(A)
'''

#print(ord(chr(65)))
 
#pyperclip.copyt("Hello, world! ")
#print(pyperclip.paste())

#! Python3
# mclip.py PROYECT

# Text = {
#     "Agree": """ Yes, I agree. That sounds fine to me """,
#     "Busy": """ Sorry, can we do this later this week or next week? """,
#     "Upsell": """ Would you consider making this a monthly donation? """
# }
import pyperclip, sys

''' if len(sys.argv) < 2:
    print('Usage: python myclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in Text:
    pyperclip.copy(Text[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.') 
else:
    print('There is no text for ' + keyphrase) '''


#! PYTHON3
# BULLET_POINT_ADDER.PY 
# OF EACH LINE OF TEXT ON THE CLIPBOARD

# text = pyperclip.paste()
# lines = text.split('\n')

# for i in range(len(lines)):
#     lines[i] = '* ' + lines[i]

# text = '\n'.join(lines)

# # TODO: SEPARATE LINES AND ADD STARS 

#pyperclip.copy(text)

#ENGLISH TO PIG LATIN

''' print('Enter the English message to translate into pig Latin: ')
message = input()

VOWELS = ('a', 'e', 'i', 'u', 'y' )

PigLatin = []

for word in message.split():
    PrefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        PrefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        PigLatin.append(PrefixNonLetters)
        continue
    
    SuffixNonLetters = ''
    while not word[-1].isalpha():
        SuffixNonLetters += word[-1]
        word = word[:-1]

    Wasupper = word.isupper()
    WasTitle = word.istitle()

    word = word.lower()

    PrefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        PrefixConsonants += word[0]
        word = word[:1]

    if PrefixConsonants != '':
        word += PrefixConsonants + 'ay'

    else:
        word += 'yay'

    if Wasupper:
        word = word.upper()        

    if WasTitle:
        word = word.title()
    
    PigLatin.append(PrefixNonLetters + word + SuffixNonLetters)

print(''.join(PigLatin))

'''
 
TableData = [['Apples', 'Oranges', 'Cherries','Bananas'],   
    ['Alice', 'Bob', 'Carol', 'David'],
    ['Dogs','Cats', 'Moose','Goose']
]


def PrintTable():
    Colwidth = [] * len(TableData)
    for x in TableData:
        Colwidth.append(x[0])
    Colwidth.append('\n')

    for i in TableData:
        Colwidth.append(i[1])
    Colwidth.append('\n')
    
    for z in TableData:
        Colwidth.append(z[2])
    Colwidth.append('\n')
    
    for y in TableData:
        Colwidth.append(y[3])
    Colwidth.append('\n')

    Colwidth = ' '.join(Colwidth)
    print(Colwidth)    

#PrintTable()

import zombiedice


# class MyZombie:
#     def __init__(self,name):
#         self.name = name

#     def turn(self,gameState):
#         DiceRollResults = zombiedice.roll()

#         Brains = 0
#         while DiceRollResults is not None:
#             Brains += DiceRollResults['brains']

#             if Brains < 2:
#                 DiceRollResults = zombiedice.roll()
#             else:
#                 break   
#         zombies = (
#             zombiedice.examples.RandomCoinFlipZombie(name='Random'),
#             zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
#             zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2Shotguns', minShotguns=2),
#             zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1Shotgun', minShotguns=1),
#             MyZombie(name='My Zombie Bot'),
#     # Add any other zombie players here.
# )


def IsPhoneNumber(text):
    if len(text) != 12:
        return False
    
    for i in range(0,3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4,7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False
    
    for i in range(8,12):
        if not text[i].isdecimal():
            return False

    return True

#print(IsPhoneNumber('405-555-4242'))

Message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

# for i in range(len(Message)):
#     Chunk = Message[i:i+12]

#     if IsPhoneNumber(Chunk):
#         print('Phone number found: ' + Chunk)
#print('Done')



