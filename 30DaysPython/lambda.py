
#TODO: Lambda function

#NOTE: This works like a functin how takes parametor and arguments


concatenateLambda = lambda param1, param2: param1 + " "+  param2
# print(concatenateLambda("Hello", "World"))

#TODO: Selft invoking lambda function

involkinLambda = (lambda a,b: a+b)(2,3)
# print(involkinLambda)

#TODO: Lambda function inside another function

def lambdaFunction(x):
    return lambda n :x - n

lambdaVariable = lambdaFunction(5)(3)
# print(lambdaVariable)


#WARNING: Exercise

#NOTE: Filter only negative and zero in the list using list comprehension, number = [-4,-3,-2.-1,0,1,2,4,6]

numbers = [i for i in range(-4,6) if i <= 0]

#NOTE: Flatten the following list of lists of lists to a one dimensional list list_of_lists [[[1,2,3]], [[4,5,6]], [[7,8,9]]]

list_of_lists = [[[1,2,3]], [[4,5,6]],[[7,8,9]]]
list = [a for x in list_of_lists for i in x for a in i]

#NOTE: Flatten the following list to a new list

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countriesList = [a for x in countries for i in x for a in i]
# print(countriesList)

#NOTE: Change the following list to a list of dictionaries

countrie = [[('Finland', 'Helsinki')], [('Swden', 'Stockholm')], [('Norway', 'Oslo')]]
countrieDict = [] 
for x in countrie:
    for value in x:
        countrieDict.append({value[0]:value[1]})
# print(countrieDict)

#NOTE: Change the following list of list to a lsit of concatenated string

name = [[('Asambeneh', 'Yetaeyeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names = []
# for x in name:
    # for i in x:
        # names.append(' '.join(i))
# print(names)
