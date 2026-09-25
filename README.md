# csv-parser

This project is a simple CSV parser written in python. The purpose of the project is to convert a csv file to a suitable data structure in Python. The parser can read a csv file and parse it to a list of dictionaries. The parser takes a csv file, takes the first line as a header, and divides each line into fields by seperating by comma. The parser handles commas in quotations ("") so it is read as one field. It can also handle nested quotes, e.g "Daniel, ""Hej""", will keep the qoutes around "Hej". Empty fields will be saved as NULL. The parser can also handle the following errors:

1. Double quotes is not in nested qouted, which makes sure the quotes can only appear in a field that begins with at qoute
2. It checks that all qoutes are closed 
3. It checks that a line has the same number of fields a the header

The parser will save errors in a seperate list which returns after the result.

The project also contains unittest, that checks wether the paser functions correctly.

## Description
The program consists the functions csv_parser() and line_parser(). The function csv_parser recieves the name of a csv file, opens and reads it. It then divides the file in the lines using the python  splitlines() function. The first line functions as a header, and the remaining lines are put through the line_parser() function. For every data line csv_parser() calls the line_parser() function, which parses each line. The line_parser function goes through each line character by character and divides the lines into fields. The function handles commas, quotes and nested qoutes. The line_parser() function returns a list of fields and the csv_parser checks wether the number of fields corresponds to the header. If the number of fields is incorrect the line is saved in an error list. If the line is correct the csv_parser function creates a dictionary with the header values as keys and the corresponding values from the line as values. Empty fields are changed to "NULL".
The csv_parser() function returns a list with the correctly parsed lines and a list of errors.


## Getting Started

### Dependencies
The project uses the Python standard library
Python 3.14.6

### Installing
The program can be downloaden from https://github.com/AmalieMoerck/csv-parser
To run the program you need to have python installed, and the project files should be in the same folder as the program.

### Executing program

The program can be run from the terminal:

python csvparser.py

You will the be prompted to enter a csv file name:

Indtast csv fil: 

and you enter the name of the csv file you want to parse, e.g

employees.ascii.csv


## Help



## Authors
Amalie Mørck

## Version History


## Acknowledgments
