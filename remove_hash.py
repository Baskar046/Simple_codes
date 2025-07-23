s=input()
def remove(s):
    re=s.count("#")
    s=s.replace("#","")
    return ("#"*re+s)
print(remove(s))