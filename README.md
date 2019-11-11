
# Palindrome Project
​
## What is a Palindrome?
​
A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as taco cat or madam or racecar or the number 10801. Sentence-length palindromes may be written when allowances are made for adjustments to capital letters, punctuation, and word dividers, such as "A man, a plan, a canal, Panama!", "Was it a car or a cat I saw?" or "No 'x' in Nixon" (Wikipedia)
​
​
## Project

The variable input used for this project and function is 'inString' the function title is 'palindrome_check'.

```python
inString = input("enter text.")


def palindrome_check(inString):
```

​
Built with python, this project consists of the file PalindromeChecker.py that allows a user to input characters into the console box and will return a checker on whether or not the value is a Palindrome or not... If the characters enter is a palindrome, then the program would return an output:
​
```python
print(f'this string {inString} is a palindrome.')
```
​
else if the phrase is not a palindrome then it will return:
​
```python
print(f'this string {inString} is not palindrome.')
```
​
This project removes all special characters, spacing and returns the values in lower cases within the function 
```python
    inString = re.sub('[^A-Za-z0-9]+', '', inString) # regex solution matches characters and numbers, replaces symbols
    inString = inString.lower() # lowercase string characters
    inString = inString.replace(" ","") # removes whitespacing
 ``` 
additional formating or string manipulation can be implemented in the function before it checks the string. 
​
​
## Testfile
​
In order to run a testfile, the user must run the PalindromeUnitTest.py file that contains all the positive and negative testing of the program. The file will initiate once the user has pressed the 'enter' key in the console box OR removed the replaced the following line of code in PalindromeCheck.py:
​
​
```python
inString = input("enter text.")
```
with the following code:
```python
inString = ""
```
so that the program could remove the input box and allow the user to run the program from the test file alone, though this is not recommended however would result with convenience of running the test file. 
​
## Contributing
​
The following websites have helped with the creation of the Palindrome project:
https://docs.python.org/3/library/unittest.html
https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
https://www.tutorialspoint.com/python/python_reg_expressions.htm
​
​
##Authors and acknowledgment
​
Created by Riley Powell and assisted by Kumail Anis
