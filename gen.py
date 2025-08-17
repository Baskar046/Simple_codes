#generator 
""" a special type of iterable 
    genrate values one at a time using the yield keyword
    memory-efficient :no need to store all values at once 
    it's use cases are get the thousand of data into 100 and 100
    it's have two way to implement 
        1.using the yield
        2.parathesies """

#genrator function
def gen():
    yield "first yield"
    print("after printing the first yield")
    yield "second yield"
    print("after printing thw second yield")

gen_obj=gen()
try:
    print(next(gen_obj))
    print(next(gen_obj))
    print(next(gen_obj))
    print(next(gen_obj))
except: StopIteration
print('no more data is there')

#genrator experssion
#this is a second way 
get_item=(num for num in range(1,10))
print(next(get_item))   #alternative way is list
print(list(get_item))   #it's trigger the next keyword and get elements when loop is over sliently throw the error 

import sys
get_normal_function=[num for num in range(1,100000)]    #it's take the more space in memory
get_genrator_function=(num for num in range(1,10000000))    #it's take the less space in memory

print("normal function memory size",sys.getsizeof(get_normal_function)) #get the size of allocation using sys.getsizeof()
print("genrator function memory size",sys.getsizeof(get_genrator_function))
