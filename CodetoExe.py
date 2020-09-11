#in python 2.7 there is  module called pytoexe but not supported in python 3
#cx_freeze is used instead
#download cx_freeze and install

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
