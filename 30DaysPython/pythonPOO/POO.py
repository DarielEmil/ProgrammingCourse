
#TODO: Python Programming object class (POO)

#NOTE: To create a class

class FirstClass:
    def __init__(self,firstname='Dariel', lastname='Yetayeh', age=15, country='Finland'): #NOTE: __init__ is a contructor of the created class, having the initial properties, can has parametor or not
        self.__firstname = firstname #PERF: This is how to encapsulate an properties, if a propierties is encapsulate can be change in the future
        self.lastname = lastname
        self.age = age
        self.country = country

    def objectMethods(self): #NOTE: This is a method from the class
        print(f"{self.__firstname}")

Object = FirstClass() #NOTE: This ins an object from the class FirstClass

# Object.__firstname = 'Asabeth'
# Object.objectMethods()

#TODO: Inheritance

#NOTE: Inheritance is to inherita the properties, methods, from the class to another

class father:
    def __init__(self,height=6.4, nationality='American', languague='English'):
        self.height =  height
        self.nationality =nationality 
        self.languague = languague
    def status(self):
        return f"Working like a computer sciences, and i speak {self.languague}"

class son(father): #PERF: This class is inherite from father class and only use __init__ construction
    def __init__(self, sport='Swim', favColor='Red'):
        super().__init__(5.9, 'American', 'Spanish, English') #NOTE: With the super() we can have access to the parent properties
    pass

class daugther(father): #PERF: This clas in inherite from father class and use all the methods from the father
    def __init__(self, sport='Swim', favFood='Pasta'):
        self.sport = sport
        self.favFood = favFood
        super().__init__(5.5,'American',['Spanish','English','French'])
    def status(self):
        return f'I go to the school and i speak {self.languague}'


sonObject = son()
daugtherObject = daugther()
# print(daugtherObject.languague)
# print(daugtherObject.status())


