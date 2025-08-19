n=input("enter the word:")
if n==n[::-1]:
    print("it's a palindrome",n)
else:
    print("it's not a palindrome",n)

#another method to find the palindrome
vanakkam=input("enter the word:")
def palindrome_check(vanakkam):
    return vanakkam == vanakkam[::-1]
if palindrome_check(vanakkam):
    print("it's palindrome")
else:
    print("it's not a palindrome")


#checking the palindrome case
def isPalindrome(s):
    s=s.lower()
    if s[::-1]==s :
        return "True"
    else:
        return "False"
isPalindrome("ram")
