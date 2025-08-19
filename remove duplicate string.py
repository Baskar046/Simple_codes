n="hello"
remove=set()        #used to apprence of string
result=""       #collect the string
for ch in n:        #get the each string from n
    if ch not in remove:        #check the string is already present in remove 
        result+=ch  #append into result
        remove.add(ch)      #add the string for check the remaining string
print(result)
