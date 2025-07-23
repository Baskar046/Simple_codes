n=input("enter the value:")
baskar={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
for digit in n:
    check=int(digit)
    print(baskar[check],end=" ")