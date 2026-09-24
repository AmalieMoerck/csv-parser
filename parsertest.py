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
        bad_line = 'Tobias,45,Århus"Danmark"'

        with self.assertRaises(ValueError):
            line_parser(bad_line)

    def test_nestedquote_open(self):
        bad_line = 'Tobias,45,"Århus""Danmark"'

        with self.assertRaises(ValueError):
            line_parser(bad_line)


    def test_line_parser_nested_qoutes(self):
        line = 'Tobias,45,"Århus,""Danmark"",Jylland"'
  
        result = line_parser(line)

        self.assertEqual(
            result,
            ['Tobias', '45', '"Århus,"Danmark", Jylland"']
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

    #def test_wrong_number_fields(self):
    #    with open("testnumberfields.csv", "w", encoding="utf-8") as file:
    #        file.write(
    #            "navn,alder,by\n"
    #            "Tobias,45\n"
    #            "Katrine,56,Vejle\n"
    #        )
    #    result, error = csv_parser("testnumberfields.csv")

    #    expected = [
    #        {'navn':'Katrine','alder':'56','by':'Vejle'},
    #        {(1,'Tobias,45','wrong number of fields')}
    #    ]

    #    self.assertEqual(result, expected)
    #    self.assertEqual(error, [])


    #def test_csv_parser_esc_qoutes(self):
    #    with open("test1.csv", "w", encoding="utf-8") as file:
    #       file.write(
    #            'navn,alder,by\n'
    #            'Tobias,45,"Aarhus,""Hej"""\n'
    #            'Katrine,56,Vejle\n'
    #        )
    #    result = csv_parser("test1.csv")

    #    expected = [
    #        {'navn': 'Tobias', 'alder': '45', 'by': 'Aarhus,"Hej"'},
    #        {'navn': 'Katrine', 'alder': '56', 'by': 'Vejle'}
    #    ]

    #    self.assertEqual(result, expected)
   

if __name__ == '__main__':
    unittest.main()



