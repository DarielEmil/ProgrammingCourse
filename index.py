import re

# Regex = re.compile(r'''(
    # \d{1,2}
    # ([,]\d{3})* 
    # )''')
# Found = Regex.search('6,780,129,231')
# print(Found.group())

# regex = re.compile(r'''(^[A-Z]\w+  
# Watanabe$   
# )''')

# found = regex.search('''Haruto 
# Watanabe # ''')

# regex1 = re.compile(r"[Alice|Bob|Carol]+ [eats|pets|throws]+ [apples|cats|baseballs]+", re.I)
# found1 = regex1.search('alice Eats Apples')

# print(found1.group())

# regex2 = re.compile(r'([1-12]+)/([1000-2999]+)')
# found2 = regex2.search('5/1200')
# print(found2.group())

# regex3 = re.compile(r'([0-3]?\d)/([0-2]?\d)/([1-2]\d{3})')
# regex3 = re.compile(r'([0-3]?\d)/([0-1]?\d)/([1-2]+\d{3})')
# found3 = regex3.search('1/14/4333')

# print(found3.group())
# day,month,year = found3.groups()

# def checkDate(D,M):
#     monthList = [4,6,9,11]
#     if not int(M) in monthList and int(D) <= 30:
#         return print('It\'s a valid date')
#     elif int(M) in monthList and int(D) > 30: 
#         return print('It\'s not a valid date')
#     elif int(M) == 2 and int(D) > 28:
#         return print('It\'s not a valid date')
#     elif int(M) > 12 or int(D) > 31:
#         return print('It\'s not a valid date')
#     else:
#         return print('It\'s a valid date')
# checkDate(day,month)

# passWordStrong = re.compile(r'(?=.*[A-Z]+[a-z]+\d).{8,}')

# strongPassword = passWordStrong.search('Helloworld8')
# print(strongPassword.group())

# passwordRegex = re.compile(r'''(
#     ^(?=.*[A-Z].*[A-Z])                # at least two capital letters
#     (?=.*[!@#$&*])                     # at least one of these special characters
#     (?=.*[0-9].*[0-9])                 # at least two numeric digits
#     (?=.*[a-z].*[a-z].*[a-z])          # at least three lower case letters
#     .{10,}                              # at least 10 total digits
#     $
#     )''', re.VERBOSE)
# found = passwordRegex.search('12AE#hello')
# print(found.group())


#! INPUT VALIDATION #8

# while True:
#     print('Enter your age')
#     age = input()
#     try:
#         age = int(age)
#     except:
#         print('Please use numeric digits')
#         continue
#     if age<1:
#         print('Please enter a positive number')
#         continue
#     break

# print('Your age is %s' % (age))

import pyinputplus as  pyip

pyInputPlusConfig = {
    'inputStr()': 'It\'s like input() but with more functions',

    'inputNum()': 'Only numbers or float',

    'inputChoise()': 'Ensures the user enters one of provided choices',

    'inputMenu()': '''Is similar to inputChoise(), but provides a menu with numbered
    or tered options''',

    'inputDatetime()': 'Enters date and time',

    'inputYesNo()': 'Enters a "yes" or "No" ',

    'inputBool()': 'Similiar like inputYesNo() but with "True" or "False"',

    'inputEmail()': 'Enters email',

    'inputFilePath()' : ''' Enters a valid file path and filename, 
    and can optionally ''',

    'inputPassword()': 'Display * characters as the user types so that passwords '''
}

# response = pyip.inputInt(prompt='Insert ',max=20) #TODO: LessThan, MaxThan, Min, Max adittional function 

# response1 = pyip.inputNum(prompt='> ', min=4, lessThan=6)
#response2 = pyip.inputNum(limit=2,default='N/A') #TODO: Limit, Timeout and default arguments  

# regularResponse = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero']) #TODO: user regular expresion an allow them with alloRegexes or block with blockRegexes
# blockRegularResponse = pyip.inputNum(blockRegexes=[r'[02468]$'])

# use2Regex = pyip.inputNum(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])

#! InputCustom
# def addsUpToTen(numbers):
#     numbersList = list(numbers)
#     for x, y in enumerate(numbersList):
#         numbersList[x] = int(y)
#     if sum(numbersList) != 10:
#         raise exception(f'The digits must add up to 10, not {sum(numbersList)}. ')
#     return int(numbers)

# upToResponse = pyip.inputCustom(addsUpToTen, limit=2, defaul='N/A')

#TODO: Project How to keep an Idiot Busy for hours

# while True:
#     prompt='Want to know how to keep an idiot busy for hours?\n'
#     respond = pyip.inputYesNo(prompt) #* yesVal= and noVal= para otros idiomas
#     if respond == 'no':
#         print('Have a nice day!')
#         break

#TODO: Sandwich Maker

# selectBread = pyip.inputMenu(['wheat','white','sourdought'], numbered=True)
# print('\n')
# selectProtein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
# print(f'Your sandwich bread {selectBread} and your protein type {selectProtein}')
# wantCheese =pyip.inputYesNo(prompt='Want cheese ? ')
# if wantCheese == 'yes':
    # print('What type of cheese do you want? ')
    # typeOfCheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'],numbered=True)
# else:
    # typeOfCheese = 0
# wantAdditional =pyip.inputYesNo(prompt='Do you want some additional ?\n')
# if wantAdditional == 'yes':
    # additional = pyip.inputMenu(['mayo','mustard','lettuce', 'tomato'],numbered=True)
# else:
    # additional = 0
# sandwichQuantity = pyip.inputInt(prompt='How many sandwich do you want ?\n')

def priceOfSandwich(breadP,proteinP,cheeseP,additionalP,sandwichP):
    price = {
    'breadPrice': {
        'wheat': 5,
        'white': 8,
        'sourdought': 10
    },
    'proteinPrice': {
        'chicken': 10,
        'turkey': 20,
        'ham': 10,
        'tofu': 15
    },
    'cheesePrice': {
        'cheddar': 8,
        'Swiss' :12,
        'mozzarella': 10
    },
    'additional': {
        'mayo': 4,
        'mustard': 2,
        'lettuce': 4,
        'tomato': 2
    }}
    if cheeseP == 0:
        cheeseP = 0
    else:
        cheeseP = price['cheesePrice'].get(cheeseP)
    if additionalP == 0:
        additionalP = 0
    else:
        additionalP = price['additional'].get(additionalP)
    totalPrice = price['breadPrice'].get(breadP)+price['proteinPrice'].get(proteinP)+cheeseP+additionalP
    totalPrice *= sandwichP
    return totalPrice
# print(priceOfSandwich(selectBread,selectProtein,typeOfCheese,additional,sandwichQuantity))



