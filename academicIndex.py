#NOTE: Calculate the academic index

import pyinputplus as pyip
def calculateAcademicIndex():
    subjectsCredit = {}
    subjectsName = {}
    subjectQuantity =  pyip.inputNum(prompt='Ingrese la cantidad de materias que tiene ')
    for count in range(subjectQuantity):
        subjectN = pyip.inputStr(prompt='\nNombre de la asignatura ')
        subjectCredit = pyip.inputMenu(['1','2','3','4'],prompt='\nSeleccione la cantidad de creditos \n',numbered=True)
        subjectsCredit.setdefault(subjectN,int(subjectCredit))
        bool = pyip.inputYesNo(yesVal='Si', noVal='No', prompt='\nQuieres ver en pantalla los creditos en la tabla ?')
        if bool.lower() == 'si': 
            for k, v in subjectsCredit.items(): print(f'{k} {v}')
    for subjectN in subjectsCredit.keys():
        subjectQ = pyip.inputNum(prompt=f'\nIngrese la calificacion de {subjectN} ')
        subjectsName.setdefault(subjectN,subjectQ)
        bool = pyip.inputYesNo(yesVal='Si', noVal='No', prompt='\nQuieres ver la lista en pantalla ? \n')
        if bool.lower() == 'si': 
            for k, v in subjectsName.items(): print(f'{k} {v}')
    equalCredit = [0,2,3,4]
    equalPoint = []
    for quantityPoint in subjectsName.values():
        if quantityPoint <= 100 and quantityPoint >= 90: equalPoint.append(equalCredit[3])
        elif quantityPoint <=89 and quantityPoint >= 80: equalPoint.append(equalCredit[2])
        elif quantityPoint <= 79 and quantityPoint >= 70: equalPoint.append(equalCredit[1])
        else: equalPoint.append(equalCredit[0])
    totalPoint = sum([credit*equalPoint[index] for index, credit in enumerate(subjectsCredit.values())])
    totalCredit = sum([value for value in subjectsCredit.values()])
    academicIndex = totalPoint/totalCredit 
    print(f'Tu indice academico es {academicIndex}')
calculateAcademicIndex()

