import unittest

from PalindromeChecker import palindrome_check
class TestPalindromes(unittest.TestCase):
    def test_palindrome_check_with_mirrored_strings(self):
       # simple palindromes that are mirrored strings
       # Call the function you would like to test (which uses input)
       # assert palindrome_check == ('') is True  # base case
       # assert palindrome_check == ('A') is True  # base case
       print("Testing for Palindromes to pass")
       print("")
       assert palindrome_check('BB') is True
       assert palindrome_check('LOL') is True
       assert palindrome_check('noon') is True
       assert palindrome_check('radar') is True
       print("")
    def test_palindrome_check_with_mixed_casing(self):
       # palindromes with mixed letter casing
       print("Testing Palindromes with mixed letter casing")
       print("")
       assert palindrome_check('bB') is True
       assert palindrome_check('NoOn') is True
       assert palindrome_check('Radar') is True
       assert palindrome_check('RaceCar') is True
       print("")
    def test_palindrome_check_with_whitespace(self):
       # palindromes with whitespace
       print("checking for palindromes with whitespaces.")
       print("")
       assert palindrome_check('taco cat') is True
       assert palindrome_check('race car') is True
       assert palindrome_check('race fast safe car') is True
       print("")
    def test_palindrome_check_with_whitespace_and_mixed_casing(self):
       # palindromes with whitespace and mixed letter casing
       print("Testing for whitespace and mix letter casing.")
       print("")
       assert palindrome_check('Taco Cat') is True
       assert palindrome_check('Race Car') is True
       assert palindrome_check('Race Fast Safe Car') is True
       print("")
    def test_palindrome_check_with_whitespace_and_punctuation(self):
       # palindromes with whitespace and punctuation
       print("testing for palindromes with whitespace and punctuation")
       print("")
       assert palindrome_check('taco cat!') is True
       assert palindrome_check('race, car!!') is True
       assert palindrome_check('race fast, safe car.') is True
       print("")
    def test_palindrome_check_with_mixed_casing_and_punctuation(self):
       print("Testing for palindromes with whitespace, punctuation and mixed letter casing")
       print("")
       # palindromes with whitespace, punctuation and mixed letter casing
       assert palindrome_check('Race fast, safe car.') is True
       assert palindrome_check('Was it a car or a cat I saw?') is True
       assert palindrome_check('Go hang a salami, Im a lasagna hog.') is True
       assert palindrome_check('A man, a plan, a canal - Panama!') is True
       print("")
    def test_palindrome_check_with_non_palindromic_strings(self):
       # negative testing for palindromes
       print("Negative testing for palindromes")
       print("")
       assert palindrome_check('AB') is False  # even length
       assert palindrome_check('ABC') is False  # odd length
       assert palindrome_check('doge') is False
       assert palindrome_check('monkey') is False
       assert palindrome_check('chicken, monkey!') is False
       print("")
       print("testing complete")


if __name__ == '__main__':
   unittest.main()
