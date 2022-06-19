from pathlib import Path; import os
# validationFile = Path('/home/dariel')
# if validationFile.is_dir():
    # for fileDirectory in os.listdir(validationFile):
        # if fileDirectory == 'Workstation':
            # newPath = Path(validationFile) / fileDirectory
            # Path(newPath / 'newDirectory').mkdir()
            # for file in os.listdir(newPath):
                # if (newPath / file).is_dir() and file == 'newDirectory': 
                    # os.chdir(f'/home/dariel/Workstation/{file}') 
                    # newFile = Path(newPath) / file newFile = open('newText.txt', 'w'); newFile.write('Hello, now i dominate the files and directory with python :D') newFile.close() newFile = open('newText.txt'); readFile = newFile.read() print(readFile) 


#WARNING: ORGANIZING FILES 
# import shutil #NOTE: HAS MODULES LIKE COPY,RENAME, MOVE O DELETE FILES 
# awn = Path('/home/dariel/Workstation/ProgrammingCourse') ewn = Path('/home/dariel/Workstation/ProgrammingCourse/Nvim/index.py') 
# shutil.copy(awn / 'index.html', awn / '../index.html') #NOTE: TO COPY (SOURCE, DESTINATION) JUST COPY A FILE shutil.copytree() 
# #NOTE: COPY AN ENTIRE FOLDER AND EVERY FOLDER AND FILE CONTANINED IN IT 
# shutil.copytree(awn / 'Nvim', awn / '../Nvim') #WARNING: MOVING AND RENAMING FILES AND FOLDERS

# shutil.move('/home/dariel/Workstation/ProgrammingCourse/Nvim/index.py', '/home/dariel/Workstation/ProgrammingCourse') #NOTE: TO MOVE AN FILE OR DIRECTORY, DOESN'T ALLOW VARIABLE WITH PATH, CAN RENAME A FILE OR FOLDER TOO

#WARNING: PERMANENTLY DELETING FILES AND FOLDERS

# os.unlink() #NOTE: WILL DELETE THE FILE AT PATH
# os.rmdir() #NOTE: WILL DELETE THE FOLDER AT PATH, THIS FOLDER MUST BE EMPTY OF ANY FILES OR FOLDERSO
# shutil.rmtree() #NOTE: WILL REMOVE THE FOLDER AT PATH, AND ALL FILES AND FOLDERS IT CONTAINS WILL ALSO BE DELETED

#WARNING: SAFE DELETES WITH THE SEND2TRASH MODULE

#PERF: THIS IS A THIRD PARTY MODULE, WHERE DELETE THE FILE SAFE, SENDING THE FILE TO TRASH, WHERE CAN BE RESTORE


#WARNING: WALKING A DIRECTORY TREE

# for folderName, subFolder, fileNames in os.walk('/home/dariel/Workstation'):
    # print(folderName)

#WARNING: COMPRESSIONG FILES WITH THE ZIPFILES MODULE

#

