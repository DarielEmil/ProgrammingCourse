#WARNING: Keeping time, scheduling tasks, and launching programs

#WARNING: Time module

import time

# print(time.time()) #NOTE: This return the number of seconds since that moment as a float value

# time.ctime() #NOTE: This return a string description of the current time
# def calcProd():
    # product = 1 
    # for i in range(1,100000):
        # product*=i
    # return product

# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print("The result is %s digits long" % len(str(prod)))
# print(f"Took {endTime-startTime} seconds to calculate")

#WARNING: Time.sleep function

# time.sleep(1)#NOTE: This function stay paused the program
# for x in range(3):
    # print("tick")
    # time.sleep(1)
    # print('tock')
    # time.sleep(1)

#WARNING: Round function

# round()#NOTE: This will round the digits after the decimal
# print(round(time.time()))

import datetime

# print(datetime.datetime.now())
dt = datetime.datetime(2020,6,21,10,5,0)#NOTE: This retrieve a datetime for a specific moment
# print(dt.day) #NOTE: This can return by .year, .day, .minute, .second

print(datetime.datetime.fromtimestamp(1)) #NOTE: This converted a Unix epoch to datetime
