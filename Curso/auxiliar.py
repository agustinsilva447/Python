import unittest

class RomanNumber(object):
    def int_to_roman(self, n):
        return 'I'
class RomanNumberTest(unittest.TestCase):
    def setUp(self):
        self.roman_number = RomanNumber()
    
    def test_one_to_roman(self):
        roman_number = self.roman_number.int_to_roman(1)
        self.assertEqual('I', roman_number)    

if __name__ == '__main__':
    unittest.main()