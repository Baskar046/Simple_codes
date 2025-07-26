#print its characters at even indices (index starts at 0)
class solution:
    def print_even(self,st):
        for i in range( len(st)):
            if i%2==0:
                print(st[i],end="")
st=input()
obj=solution()
obj.print_even(st)