#Missing quotes in qoutes, and empty space exceptions

#function that takes a line from a csv file as input and saves in a list
def line_parser(line):
    values = []
    current_field = ""
    esc_qoutes = False

#goes through all characters, and checks for "" and , 
    for char in line:
        if char == '"':
            esc_qoutes = not esc_qoutes
        elif char == ',' and not esc_qoutes:
            values.append(current_field)
            current_field = ""
        else:
            current_field += char

    values.append(current_field)
    return values

#test = 'Thomas, 23, "vejle, Danmark"'
#print(parse_line(test))

#def csv_parser(filename)
#   with open(filename, "r", encoding="utf-8") as csv_file:
#       text = file.read()

#Takes filename as input, opens file, reads it into a text string and splits lines by commas
def csv_parser(file):
    with open(file, "r", encoding="utf-8") as csv_file:
        text = csv_file.read()
    lines = text.splitlines()

#checks for empty file
    if not lines:
         return[]

#saves the first line in header
    header = line_parser(lines[0])

#empty list to save result
    data = []

#goes through all remaining lines, calls parse_line function 
    for line in lines[1:]:
        values = line_parser(line)

#saves into dictionary that take header and corresponding value
        row = {}

        for i in range(len(header)):
            row[header[i]] = values[i]

        data.append(row)

    return data

#run parser and read csv file
data = csv_parser("employees.ascii.csv")
#data = csv_parser("testcsv.csv")
#data = csv_parser("sogne.dawa.csv")

#filename = input("indtast csv fil:")

#data = csv_parser(filename)

print(data)


