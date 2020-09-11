
exDict= {'Jack':15, 'Bob':22, 'Alice':12, 'Kevin':17}
print(exDict)
print(exDict['Jack']) # prints the value of Jack

exDict['Tim']=14
print(exDict)

exDict['Tim']=15
print(exDict)

del exDict['Tim']
print(exDict)

exaDict={'Jack':[15,'brown'], 'Bob':[22,'golden'], 'Alice':[12,'black'], 'Kevin':[17,'blonde']}
print(exaDict)
print (exaDict['Alice'][1])
