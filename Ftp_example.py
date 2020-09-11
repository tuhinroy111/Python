from ftplib import FTP

ftp= FTP('domainname.com')
ftp.login(user='username',passwd='password')
ftp.cwd('//specific domain or location')

#receiving a file

def grabFile():
    filename='filename.txt'
    localfile= open(filename,'wb')
    ftp.retrbinary('RETR '+ filename, localfile.write, 1024)
    ftp.quit()
    locafile.close()

def sendFile():
    filename='filename.txt'
    ftp.storbinary('STOR '+filename, open(filename,'rb'))
    ftp.quit()
    
