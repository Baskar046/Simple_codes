try :       #try part main code write below here
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
except Exception as e:      #pervent from the code crush
    print("something ",e)
else:               #else part is check the exception is all clear mean else part will run
    print("the result is",a+b)
finally:                #finall part will run this try ,exception and else are done or not .
    print("all checking is done!")