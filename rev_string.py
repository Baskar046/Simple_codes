#reverse string using indexing
s="hello"
print(s[::-1])

#reverse string using for loop
n="don"
result=""
for ch in n:
    result =ch+result
    print(result)


#reverse strng using recursive
def rev_str(n):
    if not n:
        return n

    return rev_str(n[1:]) +n[0]
print(rev_str("hello world"))

