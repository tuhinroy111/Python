text= 'Writing to a file'
saveFile=open('Writetofile.txt','w')
saveFile.write(text)
saveFile.close()
appendText='appended text'
appendFile=open('WritetoFile.txt','a')
appendFile.write('\n')
appendFile.write(appendText)
appendFile.close()
readFile=open('WritetoFile.txt','r').read()
print(readFile)

"""
this is commented
we can use .readlines instead of .read
to print each line in a single line separated wit commas
this is generally used to read excel sheets

"""
