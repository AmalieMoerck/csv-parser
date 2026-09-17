import unittest

from csvparser import line_parser#, csv_parser

class TestStringMethods(unittest.TestCase):

    def test_line_parser(self):
        line = "Tobias,45,Århus"

        result = line_parser(line)

        self.assertEqual(
            result,
            ["Tobias", "45", "Århus"]
        )



if __name__ == '__main__':
    unittest.main()
