#replace the empty place by string

add="m d m"
ch="a"
result=" "
for i in add:
    if i ==" ":
        i=ch
    result+=i
print(result)
