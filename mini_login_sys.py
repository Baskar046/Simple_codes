#login user_id management
user_id=input("enter the user id:")
while user_id!="venkat":
    print("Invalid user id")
    user_id = input("enter the user id:")
print("login successfully")

#loop condition for password management
number=int(input("enter the number from 1 :"))
total=0
while number!=0:
    total+=number
    number=int(input("enter again one time:"))
print(total)