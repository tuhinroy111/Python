import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

style.use('fivethirtyeight')

conn= sqlite3.connect('PythonTut.db')
c= conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Pysample(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO Pysample VALUES(145322, '2016-05-09', 'Python', 5)")
    conn.commit()
    
def dynamic_data_entry():
    unix=time.time()
    date=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword='Python'
    value=random.randrange(0,10)
    c.execute("INSERT INTO Pysample (unix, datestamp, keyword, value) VALUES (?,?,?,?)",
              (unix, date, keyword, value))
    conn.commit()
    
def read_from_db():
    c.execute('SELECT * FROM Pysample')
    for row in c.fetchall():
        print(row)

def graph_data():
    c.execute('SELECT unix,value FROM Pysample')
    dates=[]
    values=[]
    for row in c.fetchall():
        print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()

def update_del_data():
    c.execute('SELECT * from Pysample')
    [print(row) for row in c.fetchall()]

    c.execute('UPDATE Pysample SET value=99 WHERE value=3')
    conn.commit()
    
    c.execute('SELECT * from Pysample')
    [print(row) for row in c.fetchall()] 

    

create_table()
data_entry()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
    
read_from_db()
graph_data()
update_del_data()

c.close()
conn.close()
