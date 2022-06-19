from importlib.resources import path
from pathlib import Path
import os
from posixpath import abspath

#! Join Two Path
myFiles = ['index.py']

# for filename in myFiles:
#   print(Path('/home') / 'dariel' /'Workstation' / filename)

# homeFolder= Path('/home/dariel')
# subFolder= Path('WorkStation')
homeFolder = Path(r'home/dariel')
subFolder = Path('WorkStation')
# print(Path(homeFolder) / subFolder) #TODO concatenate an Path
# print(str(homeFolder / subFolder))


# print(os.chdir(Path('/home/dariel'))) #TODO change the current working directory
# print(Path.home()) #TODO To know the root path or home directory

# os.makedirs('/home/dariel/Workstation/ProgrammingCourse/automateDirectory') #TODO Make folders one or more 

# Path(r'Prueba').mkdir() #TODO Make just one folder per time 

# print(Path.home() / Path('index.py')) #TODO to use another path besides the current directory, i can use path.home()

# print(os.path.abspath('.')) #TODO return string of the absolute path. Way to converte relative to absolute

# print(os.path.isabs('')) #TODO return True if is relative otherwise false if is false

# print(os.path.relpath('/home/dariel/WorkStation', '/home'))


#! Getting a Parts of a file path

# print(Path('/home/dariel/WorkStation/ProgrammingCourse/index.py').parents[1]) #TODO .name with extension, .stem without it, .suffix return extensions, .anchor blacklashes

# pat = os.path.abspath(Path('/home/dariel/WorkStation'))
#* os.path.basename and os.path.dirname its like .parents and .name or .stem

# print(os.path.basename(pat)) #TODO Return a list of each part of part

#! Finding files sizes and folder contents

# print(os.path.getsize('/home/dariel/Workstation/ProgrammingCourse/index.py')) #TODO return the bytes of the directory o file

# print(os.listdir('/home/dariel/Workstation/ProgrammingCourse')) #TODO Return a list of filename

# totalSize = 0
# for filename in os.listdir('/home/dariel/Workstation/ProgrammingCourse'):
#   totalSize += os.path.getsize(os.path.join('/home/dariel/Workstation/ProgrammingCourse', filename))
#   totalSize += os.path.getsize(filename) #TODO easer way 
# print(totalSize)

#WARNING: Modifying a list of files using glob patterns

# pth = Path('/home/dariel/Workstation/ProgrammingCourse')
# print(list(pth.glob('*.?'))) #TODO Return a specify o all Path of an directory with * or like regular expression

# print999(type(os.path.abspath(os.listdir('/home/dariel/Workstation/ProgrammingCourse'))))

#! Cheking Path validity

# print(pth.is_file()) #TODO Check if the file, directory or path exist with is_dir(), is_file() or exists()



# Path() #NOTE: Crea un path
# Path.cdw() #NOTE: Devuelve el path actual
# Path.glob() #NOTE: Es especificar un path o como regular expression
# Path() #NOTE: .name,.suffix,.paterns,.stem,.anchor
# os.listdir() #* Retorna una lista del contenido del path
# os.chdir #* Cambia el nombre del path conjunto al cwd()
# os.makedirs() #* Crear multiple directorios y subdirectorios
# Path().mkdir() #* Crea un solo directorio por vez
# os.path.abspath() #* Retorna el path en string
# os.path.isabs()#* Devuelve True si es absoluto sino falso
# os.path.relpath() #* Devuelve el inicio y donde empieza
# os.path.getsize() #* Devuelve la cantidad de bytes
# os.path.dirname() #* forma anterior de devolver el /home
# os.path.basename() #* Forma anterior de devolver los /home/dariel/workstation
# os.path.exists() #* Comprueba si existe el path
# pth.is_dir() #* Comprueba si el directorio existe 
# pth.is_file() #* Comprueba si el archivo existe

#WARNING: The file reading/ writing process

writingText = Path('/home/dariel/Workstation/ProgrammingCourse/creatingFileText.txt')
writingText.write_text('''
  When, in disgrace with fortune and men's eyes
  i all alone beweep my outcast state,
  and trouble deaf heaven with my bootles cries,
  and look upon 
''') #TODO create and file with path and content 

# print(writingText.read_text()) #TODO: Read the file
#TODO NOTE open() method open the file, and read() method work passing and variable with open() method. readLines() return a list of large string value and read() return the string
# openFile = open(writingText); readinFile = openFile.read() 
# print(readinFile)

#WARNING: Writing files

# test = open(writingText, 'w'); test.write('New String \n') ; test.close() #TODO 'w' is write mode, to the create a eliminate the last content and add new one

# test1 = open(writingText, 'a'); test1.write('I like chocolate') ; test1.close() #TODO 'a' it's like append from list, append to the last in the file

# o = open(writingText) ; read = o.read() ; print(read)

#! Saving variables with the shelve module

o = open('ProgrammingCourse', 'w'); o.write('Remenber'); o.close()
o = open('ProgrammingCourse'); r = o.read()
print(r)

import shelve 

# shel = shelve.open('ProgrammingCourse') #TODO module to create binary file, where i can store my data, config, etc
# config = ['Hello', 'World']
# shel['config'] = config
# shel.close()

# data = [132, 456]
# shel['data'] = data
# shel.close()
# print(list(shel['data']))



