#Missing quotes in qoutes, and empty space exceptions

#function that takes a line from a csv file as input and saves in a list

def line_parser(line):
    values = []
    current_field = ""   
    nested_quotes = False

    i = 0
    
    while i < len(line):
        char = line[i]
        if char == '"':
            if not nested_quotes and current_field == "":
                nested_quotes = True
            elif nested_quotes and i+1 < len(line) and line[i+1] == '"':
                current_field += '"'
                i+=1
            elif not nested_quotes: 
                if current_field != "":
                    raise ValueError("Double quotes can not be in an unquoted field")
                
            else: 
                nested_quotes = False

        elif char == ',' and not nested_quotes:
                values.append(current_field)
                current_field = ""
                
        else:
            current_field += char
        i+=1

    if nested_quotes:
        raise ValueError("Nested qoutes not closed")
    
    values.append(current_field)

    return values

#Takes filename as input, opens file, reads it into a text string and splits lines by commas
def csv_parser(file):
    with open(file, "r", encoding="utf-8-sig") as csv_file:
        text = csv_file.read()


    lines = text.splitlines()

    if not lines:
        return[], [] 
        

#saves the first line as header
    header = line_parser(lines[0])

#empty lists to save result
    result = []
    errors = []

#goes through all remaining lines, calls parse_line function 
    for line_number, line in enumerate(lines[1:], start=2):

        try:
            values = line_parser(line)

            if len(values) != len(header):
                errors.append(
                    (
                        line_number,
                        line,
                        "wrong number of fields"
                    )
                )
                continue

#saves into dictionary that take header and corresponding value
            row = {}

            for i in range(len(header)):
                if values[i] == "":
                    row[header[i]] = "NULL"
                else:   
                    row[header[i]] = values[i]

            result.append(row)

        except ValueError as error:
            errors.append(
                (
                    line_number,
                    line,
                    str(error),
                )
            )
            #continue   

    return result, errors

#run parser and read csv file

file = input("Indtast csv fil: ")
data = csv_parser(file)
print(data)


