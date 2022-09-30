#TODO: Select you own adventure

# import pyinputplus as Pi


pages = [" Al principio pensé que era algún camión pasando a gran velocidad,\n pero el temblor se sostubo... Me desperte de golpe y pensé -ES UN TEMBLOR!...\n What do you want to do? \n1) Esperar a que pase 2)Salir corriendo 3) Pedir ayuda", "Me quede inmóvil, esperando a que el temblor pase...\n De repente se hizo la oscuridad... \nHubo mucho ruido... Sentí que algo se caía...... \n What do you want to do? \n1) ... 2) ... 3) ...", "Once upon a time ... \n What do you want to do? \n1) ... 2) ... 3) ..."]

# def showPage(pageNumber):
    # text = pages[pageNumber] 
    # print(text)
    # response = int(input())
    # showPage(response)
# showPage(0)

#TODO: An program with csv archive and validation 
#WARNING: INCOMPLETE 

import pathlib, os, csv, json

o = open('database.json', 'w')

w = json.dumps({'Name': "John"})
i = o.write(w)
o.close()

# create = open("database.csv", 'w')
# cs = csv.DictWriter(create,['name','age'])
# cs.writerow({'name':'josh', 'age': '14'})
# create.close()

# o = open('database.csv','r')
# re = csv.DictReader(o,['name'])
# for x in re:
    # print(x)
 

# def accountValidation(name, password):
    # database = open('database.csv', 'r')
    # databaseReader = csv.DictReader(database,['userName','password'])
    # for valid in databaseReader:
        # if name == valid['userName'] and password == valid['password']:
            # print(f"Welcome {name}, you logged in with {password}")

# def createNewAccount(user, password):
    # database = open('database.csv', 'a')
    # databaseCursor = csv.DictWriter(database,['userName','password'])
    # databaseCursor.writerow("username:"user,"password:")

# validationDatabase = pathlib.Path('home/dariel/workstation/database.csv')
# if not validationDatabase.is_file():
    # database = open('database.csv', 'w') 
    # databaseCursor = csv.DictWriter(database, ['userName','password'])
    # database.close()

# print("""WELCOME TO VALIDATION DATABASE\n
        # Do you have an account ?""")
# newAccount = input()
# if newAccount.lower() == 'yes':
    # print("Please insert your user name and your password")
    # userName = input()
    # password = input()
    # accountValidation(userName, password)
# else:
    # userName = input('Please enter your user name: ')
    # password = input('Please enter your password: ')

