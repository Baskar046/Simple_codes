"""
Anagram means (rearranging words) in Python. It's a method to check if two words or phrases are anagrams of each other.
This is done by seeing if they have the same characters, with the same count for each character, but in a different order. 
For example, the words "listen" and "silent" are anagrams.
"""
def palindrome(s,s1):
    return sorted(s)==sorted(s1)
print(palindrome("listen","silent"))
