
#WARNING: Debugging

# raise Exception('This is an error.') #NOTE: Create a raise Exception()

# def boxPrint(symbol,width,height):
    # if len(symbol) != 1:
        # raise Exception('Symbol must be a single character string')
    # elif width <= 2 : 
        # raise Exception('Width must be greater than 2.')
    # elif height <= 2 : 
        # raise Exception('Height must be greater than 2.')

    # print(symbol*width)
    # for i in range(height-2):
        # print(symbol +(""*(width-2)) + symbol)
    # print(symbol*width)
    
# for sym,w,h in (("*",4,4),('O',20,5),('x',1,3),('ZZ',3,3)):
    # try:
        # boxPrint(sym,w,h)
    # except Exception as err:
        # print(f"An exception happened {err}")

#WARNING: Traceback module 

# import traceback #NOTE: With the format_exc() function to write the error

# try:
    # raise Exception("This is the error message")
# except:
    # errorFile = open('errorFile.txt','w')
    # errorFile.write(traceback.format_exc())
    # errorFile.close()
    # print('The traceback info was written to errorFile.txt')

#WARNING: Assertions

# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.sort()
# assert ages[0] <= ages[-1]

#WARNING: Logging module

import logging

# logging.basicConfig(level=logging.INFO,format='%(asctime)s- %(levelname)s- %(message)s ') 
# #NOTE: logging.DEBUG the lowest level, logging.INFO record information on general events, logging.WARNING indicate a potential problem, logging.ERROR record an error that caused the program to fail to do something, logging.critical THE highest level indicate a fatal error that has caused or is about to cause the program to stop runnin
# logging.debug('Start of program')


# def factorial(n):
    # logging.debug('Start of factorial(%s%%)' % (n))
    # total = 1
    # for i in range(1, n + 1):
        # total *=i
        # logging.debug(f'i is {i}, total is {total}')
    # logging.debug('End of factorial(%s%%)' % (n))
    # return total

# print(factorial(5))
# logging.debug('End of program')

#WARNING: disable logging 

#NOTE: Can be disable with logging.disable(The level of logging)

#WARNING: Logging to a file

#NOTE: with the argument filename='' can be pass into the logging.basicConfig()

import pyinputplus as pyi

# a = pyi.inputNum(prompt='Enter ')
# b = pyi.inputNum(prompt='Enter ')

# assert a >= 10 

#WARNING: Practice 

# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s- %(levelname)s- %(message)s ') 
# logging.debug("Start of program")
# import random
# guess = ''; answer = ['heads', 'tails']
# while guess not in answer:
    # print('Guess the coin toss! Enter heads or tails:')
    # guess = input()
    # toss = random.randint(0, 1) # 0 is tails, 1 is heads
    # if answer[toss].lower() == guess.lower():
        # print('You got it!')
    # else:
        # print('Nope! Guess again!')
        # guess = input()
        # if answer[toss] == guess:
            # print('You got it!')
        # else:
            # print('Nope. You are really bad at this game.')


