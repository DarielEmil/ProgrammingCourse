#WARNING: Project web scraping
import webbrowser, sys, pyperclip 
# if len(sys.argv) > 1:
    # address = ''.join(sys.argv[1:])
# else:
    # address = pyperclip.paste()

# webbrowser.open('https://docs.python.org/3/library/%s' % (address))
#NOTE: request.code.ok its a way to determinate if the URL is 200 HTTPS status

#WARNING: Using request function

import requests

# res = requests.get('https://www.google.com/webhp?hl=es-419&sa=X&ved=0ahUKEwj-x7aqibf3AhWuQjABHRMSC1MQPAgI')
# print(len(res.text))

#WARNING: Checking errors

#NOTE: A good way to checked is using the methods raise_for_status()

#WARNING: Saving into the hard drive

save = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#PERF: requests.get call download the file 
save.raise_for_status()
playFile = open('googleExample.txt', 'wb') #NOTE: wb is text in binary when call a .txt in the web is needed to mantein unicode encoding in text

for chunk in save.iter_content(100000): #NOTE: 10,000 its a normal quantity bytes, but sometimes can be needed more than 10,000
    playFile.write(chunk)

playFile.close()

#WARNING: bs4 module

#TODO: This module make easer to find code in HTML extensions 

#NOTE: There are some function to get some of the content in a website with HTML extension 

#NOTE: firsta bs4.BeautifulSoup() function return a BeautifulSoup object, once we have a BeautifulSoup object we can use its methods to locate specific parts of an HTML documento 

#TODO: We have the select() method wich match the tags, like soup.select('div'), soup.select('.notice'), soup.select('#author'), once we find the tag we want to use with soup.select('') we can use variableName.getText() return the first string in the list.

#WARNING: Getting Data from an Element's Attributes

#TODO: With variableName.get() return the name of the atribute

