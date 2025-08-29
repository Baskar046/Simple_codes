"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:

Function	Description
findall	 :   Returns a list containing all matches
search	 :   Returns a Match object if there is a match anywhere in the string
split	 :   Returns a list where the string has been split at each match
sub	     :   Replaces one or many matches with a string

"""
import re
text="the rain"
x=re.search("^the.*rain$",text) #starts with (^the) and ends with(*rain$)
if x:
    print("yes ,pattern is matching")
else:
    print("no more matches are found")
