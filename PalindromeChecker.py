import re
# string variable to enter the palindrome function
inString=input("enter text:")

def palindrome_check(inString):
    # string manipulation to aid in unittests
    inString = re.sub('[^A-Za-z0-9]+', '', inString) # regex solution matches characters and numbers, replaces symbols
    inString = inString.lower() # lowercase string characters
    inString = inString.replace(" ","") # removes whitespacing

    #revstring is the variable created when reversing the input string
    revString = inString[::-1]

    # check if the reversed string matches for a palindrome
    if (revString == inString):
        print(f'this string {inString} is a palindrome.')
        return True
    else:
        print(f'this string {inString} is not palindrome.')
        return False

    print(inString)
# calls the function
palindrome_check(inString)
