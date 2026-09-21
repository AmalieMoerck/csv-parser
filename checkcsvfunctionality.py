import csv

with open('testcsv.csv', newline='') as csvfile:
    checkreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in checkreader:
        print(', '.join(row))