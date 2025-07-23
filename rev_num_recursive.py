def case(n):
    if n==1:
        return 1        #both two lines are base case

    return n+ case(n-1)  #this line is recursive case
print(case(51))