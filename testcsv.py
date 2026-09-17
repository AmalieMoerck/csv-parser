import os
import csv

with open('employees.ascii.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['email'])
print (row)
