
exNum1 = -5
exNum2 = 5

print(abs(exNum1))

if abs(exNum1)==exNum2:
    print('Success')

#OS Module
import os

curDir = os.getcwd()
print (curDir)
os.mkdir('NewPython')

#time Module
import time

time.sleep(2)
os.rename('NewPython','NewPythonMod')
time.sleep(2)

os.rmdir('NewPythonMod')
