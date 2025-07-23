n=int(input("enter the range:"))
arr=[]
for _ in range(n):
    user_command=input("enter the commands:").split()
    if  user_command[0]=="insert":
        arr.insert(int(user_command[1]) ,int(user_command[2]))
    elif  user_command[0]=="remove":
        arr.remove(int(user_command[1]))
    elif  user_command[0]=="append":
        arr.append(int(user_command[1]))
    elif user_command[0]=="sort":
        arr.sort()
    elif user_command[0]=="pop":
        arr.pop()
    elif  user_command[0]=="reverse":
        arr.reverse()
    elif  user_command[0]=="print":
        print(arr)
    else:
        print("in-valid command")