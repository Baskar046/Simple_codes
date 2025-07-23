n = int(input("enter the number:"))
a = list(map(int, input("enter the range:").split()))
b = set(a)
c = list(b)
c.sort()
if len(a)!=n:
    print("enter the valid number:")
elif len(c)<2:
    print("not found a ruuner_up score")
else:
    print(c[-2])