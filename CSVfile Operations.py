import csv

with open('csvexample.csv') as csvfile:
    readCSV= csv.reader(csvfile, delimiter=',')

    prefects=[]
    for row in readCSV:
        prefect=row[1]

        prefects.append(prefect)


    print(prefects)
    try:
        whichPrefect= input('Which prefect index do you wantto choose?')
        preindex=prefects.index(' '+whichPrefect)
        print(preindex)
    except Exception as e:
        print(e)

    print('program continued...')
    

