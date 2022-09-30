
#TODO: Documentation of the requests module
import requests


r = requests.get('https://pokeapi.co/api/v2/') #NOTE: This return a response of the status code HTTP


#NOTE: To make HTTP request like POST, GET, PUT,#DELETE, etc

# r = requests.post('https://httpbin.org/post', data={'key': 'value'}) #NOTE: This is the HTTP POST Request
# r = requests.put('https://httpbin.org/put', data={'key': 'value'}) #NOTE: This is the HTTP Put request
# r = requests.delete('https://httpbin.org/delete') #NOTE: This is the HTTP delete request
# r = requests.head('https://httpbin.org/get') #NOTE: This is the HTTP head request
# r = requests.options('https://httpbin.org/get') #NOTE: This is the HTTP options

#TODO: Passing Parameters in URLs

arguments = {'key1':'value1','key2':'value2'}
a = requests.get('https://httpbin.org/get', params=arguments) #NOTE: Using the keyword params we can put the arguments
# print(a.url) #PERF: Using the atribute .url we can see the url of the APi

#TODO: Response Content

# githbTime = requests.get('https://api.github.com/events')
# print(githbTime.text) #PERF: Using the atribute .text we can read the content

#HACK: To see what encoding is the requests is used, when we user .text

# githbTime.encoding = 'ISO-8859-1' #NOTE: To change encoding depending the situation
# print(githbTime.encoding)

#TODO: Binary Response Content

# print(githbTime.content)

#TODO: JSON Response Content

jsonAPI = requests.get('https://api.github.com/events')

# print(jsonAPI.json()) #NOTE: This show the content in json file

#TODO: Custom Headers

url = "https://api.github.com/some/endpoint"
Headers = {'user-agent': 'my-app/0.0.1'}
newAPi = requests.get(url,headers=Headers)
# print(newAPi.headers)

#TODO: More Complicated POST request

#NOTE: To send some form encoded data - much like an HTML form, simply pass a dictionary to the data argument, The dictionary of data will automatically be form-encoded when the request is made

#PERF: The Params and data are different, the first one is to pass to the URL, example: https:myproyect/paramsInfo, but in the case of the data is used to send informationthat in the url couldn't see, is used to the html form
newData = [('key1','value1'),('key1', 'value2' )]
anApi = requests.post('https://httpbin.org/post', data=newData)
anotherData = {'key1':['value1', 'value2']}
anApi1 = requests.post('https://httpbin.org/post', data=anotherData)
# print(anApi.text == anApi1.text)

#NOTE: Send data that is not for-encoded

import json

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
jsoAPi = requests.post(url, data=json.dumps(payload)) #NOTE: If we want to pass a json string 

#PERF: In case we want the header set and don't want to encode the dict yourself

jsonEncoded = requests.post(url, json=payload)

#TODO: POST a MultiPart-Encoded file

url = 'https://httpblin.org/post'
# files = {'file': open('text.txt', 'rb')}

# multipart = requests.post(url, files=files)
# print(multipart.text)

#TODO: Response Status Codes

# r = requests.get(url)
# print(r.status_code) #NOTE: To see the status_code
# print(r.status_code == requests.codes.ok) #PERF: To check if the status_code is ok
# print(r.raise_for_status())

#TODO: Response Headers

# print(r.headers) #NOTE: This allow to view the headers of the response, 
# print(r.headers['date'])#NOTE: if we want to specify what we want to see... use this

#TODO: Cookies

# url = 'http://example.com/some/cookie/setting/url'
# r = requests.get(url)
# print(r.cookies)

#PERF: To send our own cookies to the server, we can use the cookies parameter

# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r= requests.get(url, cookies=cookies)
# print(r.text)

#TODO: Timeouts

#NOTE: We can stop the request waiting for a response after a given number of seconds with the timeout parameter

# requests.get(url, timeout=0.001)


url = 'https://httpbin.org/get'
info = {'name':'dark'}
test = requests.get(url)
# print(test.text)
