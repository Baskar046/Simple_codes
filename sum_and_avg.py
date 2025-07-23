n=int(input('enter the number:'))
first_num=0
second_num=1
for i in range(1,n+1):
    third_num=first_num+second_num
    first_num=second_num
    second_num=third_num
    print("final result",third_num)
