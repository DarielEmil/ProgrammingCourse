#WARNING: CSV module 

import csv
# exampleFile = open('exampleCSV.csv')
# exampleReader = csv.reader(exampleFile) #NOTE: This is used instead read or readerlines because is needed to create an reader object in the CSV file
# exampleList = list(exampleReader)
# print(exampleList)

# for row in exampleReader:
    # print(f"Row {exampleReader.line_num} {row}")

#WARNING: Writer Objects

# outputFile = open('exampleCSV.csv', 'w')
# outputWriter = csv.writer(outputFile)
# outputWriter.writerow(['spam','eggs!','bacon','ham']) #NOTE: This will change all the content of csv file
# outputFile.close()

# exampleFile = open('exampleCSV.csv')
# exampleReader = csv.reader(exampleFile)

# for row in exampleReader :
    # print(f"Row# {row}")

#WARNING: Delimiter and lineterminator Keyword arguments

# delimiter='\t', lineterminator='\n\n' #NOTE: delimiter is the character that appears between cells on a row. The line terminator is the character that comes at the end of a row.

#WARNING: DictReader and DictWriter CSV Objects


# cvs.DictReader() #NOTE: This convert into a dictionary instead of a list, it can pass [key, key, key] to specify the keys of the dictionary

# csv.DictWriter() #NOTE: Tis create a CSV files, include specify the key name
"""
outputDictWriter.writerow({'name': key}), to add content into the dictionary
"""

#WARNING: JSON and APIs


# stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
# import json
# jsonDataAsPythonValue = json.loads(stringOfJsonData) #NOTE: This translate a string containing JSON data into a Python Value
# print(jsonDataAsPythonValue)

#WARNING: Writing Json with dumps() function

pythonValue = {'isCat':True, 'miceCaught': 0,'name':'Zophie','felineIQ':None }
import json
stringOfJsonData = json.dumps(pythonValue) #NOTE: This will translate a Python Value into a string of JSON-formatted Data
print(stringOfJsonData)
