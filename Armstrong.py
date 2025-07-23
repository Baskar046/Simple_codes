value=int(input("enter the value :"))
value_=str(value)
count=len(value_)
total=0
for digit in  value_:
    total+=int(digit)**count
if total==value:
    print("armstrong")
else:
    print("not armstrong")