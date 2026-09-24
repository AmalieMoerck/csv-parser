import unittest

from csvparser import line_parser, csv_parser

class TestStringMethods(unittest.TestCase):

    def test_line_parser(self):
        line = "Tobias,45,Århus"

        result = line_parser(line)

        self.assertEqual(
            result,
            ["Tobias", "45", "Århus"]
        )

    def test_line_parser_qoutes(self):
        line = 'Tobias,45,"Århus, Danmark"'
  
        result = line_parser(line)

        self.assertEqual(
            result,
            ["Tobias", "45", "Århus, Danmark"]
        )

    def test_unquoted_field(self):
        line = 'Tobias,45,Århus"Danmark"'

        with self.assertRaises(ValueError):
            line_parser(line)

    def test_nestedquote_open(self):
        line = 'Tobias,45,"Århus, ""Danmark""'

        with self.assertRaises(ValueError):
            line_parser(line)


    def test_line_parser_nested_qoutes(self):
        line = 'Tobias,45,"Århus,""Danmark"", Jylland"'
  
        result = line_parser(line)

        self.assertEqual(
            result,
            ["Tobias", "45", 'Århus,"Danmark", Jylland']
        )


    def test_csv_parser(self):
        with open("testparser.csv", "w", encoding="utf-8") as file:
           file.write(
                "navn,alder,by\n"
                "Tobias,45,Aarhus\n"
                "Katrine,56,Vejle\n"
            )
        result, error = csv_parser("testparser.csv")

        expected = [
            {"navn": "Tobias", "alder": "45", "by": "Aarhus"},
            {"navn": "Katrine", "alder": "56", "by": "Vejle"}
        ]

        self.assertEqual(result, expected)
        self.assertEqual(error, [])

    def test_parser_quotes(self):
        with open("testparserquotes.csv", "w", encoding="utf-8") as file:
           file.write(
                'navn,alder,by\n'
                'Tobias,45,Aarhus\n'
                'Katrine,56,"Vejle, Danmark"\n'
            )
        result, error = csv_parser("testparserquotes.csv")

        expected = [
            {'navn': 'Tobias', 'alder': '45', 'by': 'Aarhus'},
            {'navn': 'Katrine', 'alder': '56', 'by': "Vejle, Danmark"}
        ]

        self.assertEqual(result, expected)
        self.assertEqual(error, [])

    def test_file_empty(self):
        with open("testempty.csv", "w", encoding="utf-8") as file:
            pass
        result = csv_parser("testempty.csv") 
        expected = ([],[])
                   
        self.assertEqual(result, expected)

    def test_wrong_number_fields(self):
        with open("testnumberoffields.csv", "w", encoding="utf-8") as file:
            file.write(
                "navn,alder,by\n"
                "Tobias,45\n"
                "Katrine,56,Vejle\n"
            )
        result, error = csv_parser("testnumberfields.csv")

        self.assertEqual(result, [
            {"navn": "Katrine", "alder": "56", "by": "Vejle"}
        ])
        self.assertEqual(error, 
                         [
                             (2,"Tobias,45","wrong number of fields")
                         ])

    def test_null_values(self):
        with open("testnull.csv", "w", encoding="utf-8") as file:
                   file.write(
                        'navn,alder,by\n'
                        'Tobias,,Aarhus\n'
                        'Katrine,56,Vejle\n'
                    )
        result, error = csv_parser("testnull.csv")
        expected = [{"navn": "Tobias", "alder": "NULL", "by": "Aarhus"},
                    {"navn": "Katrine", "alder": "56", "by": "Vejle"}]
        self.assertEqual(result, expected)
        self.assertEqual(error, [])

    def test_csv_parser_nested_qoutes(self):
        with open("test1.csv", "w", encoding="utf-8") as file:
           file.write(
                'navn,alder,by\n'
                'Tobias,45,"Aarhus,""Hej"""\n'
                'Katrine,56,Vejle\n'
            )
        result, error = csv_parser("test1.csv")

        expected = [
            {'navn': 'Tobias', 'alder': '45', 'by': 'Aarhus,"Hej"'},
            {'navn': 'Katrine', 'alder': '56', 'by': 'Vejle'}
        ]

        self.assertEqual(result, expected)
        self.assertEqual(error, [])

    def test_value_error(self):
        with open("test_value_error.csv", "w", encoding="utf-8") as file:
            file.write(
                "navn,alder,by\n"
                'Katrine,56,Vej"le\n'
            )

        result,error = csv_parser("test_value_error.csv")

        self.assertEqual(result, [])

        self.assertEqual(error,
                         [
                             (2,'Katrine,56,Vej"le',"Double quotes can not be in an unquoted field")
                         ]
                         )


   

if __name__ == '__main__':
    unittest.main()



