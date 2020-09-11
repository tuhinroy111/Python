import urllib.request
import urllib.parse

#gives the  source code of the link
#x = urllib.request.urlopen('https://www.google.com')
#print(x.read())


url='https://www.pythonprogramming.net/search'
values={'q':'basic'}
data= urllib.parse.urlencode(values)
data= data.encode('utf-8')#utf-8 is a type of encoding
req= urllib.request.Request(url,data)
resp=urllib.request.urlopen(req)
respData=resp.read()

print(respData)

'''
#this piece of code will not allow to visit google as google has restrictions for python

try:
    x=urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())
    
except Exception as e:
    print(str(e))


#this piece of code will allow accessing the url as we have specigied headers with the request

try:
    url=urllib.request.urlopen('https://www.google.com/search?q=test')
    headers= {} #headers are info that you sen iin everytime you visit a website
    headers['User-Agent']= #your info like browser details goes in here
    req= urllib.request.Request(url,headers=headers)
    resp=urllib.request.urlopen(req)
    respData= resp.read()

.    saveFile= open('withHeaders.txt','w')
     saveFile.write(str(respData))
     saveFile.close()
''' 
