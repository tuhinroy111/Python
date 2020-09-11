x = [5,4,6,7,8,5,6,7,6,5,4]
y = ['Janet','Jessy','Kelly','Alice','Joe','Bob']
x.append(2)#appends 2 at the end of the list
print(x)
x.insert(2,99)#inserts 99 at the 2nd index of the list
print(x)
x.remove(4)#removes the first 4 that occurs in the list
print(x)
print(x[4:7])# prints the elements from index 4 to 6
print(x[-1])#prints the last element in the list
print(x[-2])#prints the 2nd last element in the list
print(x.index(6))# prints the index of first occurrence of 6
print(x.count(6))# prints the no. of 6 in the list
x.sort()#sorts the list
print(x)
y.sort()#sort list y in alphabetical order
print(y)
