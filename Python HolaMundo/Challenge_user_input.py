
while True:
    a = input('Would you like to continue? ')
    if a == ('No' or 'no' or 'N' or 'n'):
        print('Exiting')
        break
    if a == ('Yes' or 'yes' or 'Y' or 'y'):
        print('Continuing...')
        print('Complete!')
        break
    if a != ('Yes' or 'yes' or 'Y' or 'y' or 'No' or 'no' or 'N' or 'n'):
        print('Please try again and respomd with yes or no') 
        continue



    # a = input('Would you like to continue? ')
    # if a == 'No':
    #     print('Exiting')
    #     break
    # if a == 'Yes':
    #     print('Continuing...')
    #     print('Complete!')    
    #     break
    # if a != ('No' or 'Yes'):
    #     print('Please try again and respomd with yes or no') 

# c = input()

# if c == 'Hello' or c == 'Hola':
#     print('True')

# if c == 'Welcome' or c == 'World':
#     print('False')
