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

    #def test_line_parser_nested_qoutes(self):
    #    line = 'Tobias,45,"Århus,""Danmark"""'
  
    #    result = line_parser(line)

    #    self.assertEqual(
    #        result,
    #        ['Tobias', '45', '"Århus,"Danmark""']
    #    )

    def test_csv_parser(self):
        with open("test.csv", "w", encoding="utf-8") as file:
           file.write(
                "navn,alder,by\n"
                "Tobias,45,Aarhus\n"
                "Katrine,56,Vejle\n"
            )
        result = csv_parser("test.csv")

        expected = [
            {"navn": "Tobias", "alder": "45", "by": "Aarhus"},
            {"navn": "Katrine", "alder": "56", "by": "Vejle"}
        ]

        self.assertEqual(result, expected)

    def test_csv_parser_esc_qoutes(self):
        with open("test1.csv", "w", encoding="utf-8") as file:
           file.write(
                'navn,alder,by\n'
                'Tobias,45,"Aarhus,""Hej"""\n'
                'Katrine,56,Vejle\n'
            )
        result = csv_parser("test1.csv")

        expected = [
            {'navn': 'Tobias', 'alder': '45', 'by': 'Aarhus,"Hej"'},
            {'navn': 'Katrine', 'alder': '56', 'by': 'Vejle'}
        ]

        self.assertEqual(result, expected)
   

if __name__ == '__main__':
    unittest.main()



