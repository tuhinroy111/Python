'''
Identifiers:

\d-any number
\D- anything but a number
\s- space
\S- anything but a space
\w- any character
\W- anything but a character
. - any character except a new line
\b- the whitespace around words
\.- a period

Modifiers:

{1,3}- we're expecting 1-3
+ - Match 1 or more
? - Match 0 or 1
* - Match 0 or more
$ - Match the end of a string
^ - Mstch at the beginning of a string
| - Either or
[]- range or variance
{x}- expecting 'x' amount


White Space Characters:

\n - new Line
\s - space
\t - Tab
\e - escape
\f - form feed
\r - return

'''


import re

str= '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}',str)
names = re.findall(r'[A-Z][a-z]*',str)

print(ages)
print(names)

ageDict={}

x=0
for eachName in names:
    ageDict[eachName]=ages[x]
    x+=1

print(ageDict)
