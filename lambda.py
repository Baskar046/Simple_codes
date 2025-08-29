"""
A lambda expression in Python is a small, anonymous (nameless) function defined with the lambda keyword.
They are used for short, simple, one-line operations and are often passed as arguments to higher-order functions like map(), filter(), and sorted().
"""


var= lambda a,b : a+b  #lambda expression 
print(var(1,2))     #pass value 

cal= lambda a: a**2
print(cal(4))

lst=[1,2,3,4,5]
square_num=list(map(lambda lst:lst**2,lst)) 
print(square_num)
