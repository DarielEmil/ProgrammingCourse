#WARNING: Keeping time, scheduling tasks, and launching programs


#WARNING: Time module


# print(time.time()) #NOTE: This return the number of seconds since that moment as a float value

# print(time.ctime()) #NOTE: This return a string description of the current time
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

# print(datetime.datetime.fromtimestamp(1)) #NOTE: This converted a Unix epoch to datetime

#WARNING: Timedelta data type 

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8) #NOTE: This represents a duration of time rather than a moment in time.
# print(delta.seconds)

#WARNING: Converting datatime objects into strings

#NOTE: To make this possible use strftime() method display a datetime object as a string

example = datetime.datetime(2022, 4, 14, 10, 1)
# print(example.strftime('%B/%a/%d'))

#WARNING: Converting string into object datetime

# datetime.datetime.strptime('October 21, 2022', '%B %d %Y')

#WARNING: Multihreading
#NOTE: This is like to run multiple programs in one, like to execute one or more instruction to execute in different times 


import threading, time

# print("Start of program")

# def takeANap():
    # time.sleep(5)
    # print("Wake up")

# threadObj = threading.Thread(target=takeANap)
# threadObj.start()

# print("End of program")

#WARNING: Passing arguments to the thread's target function

#TODO: If i want to use a function with multiple arguments use this 

# threadI = threading.Thread(target=print, args=['Cats','Dogs', 'Frogs'], kwargs={'sep': ' & '})

# threadI.start()


