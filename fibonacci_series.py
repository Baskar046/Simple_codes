n=int(input('enter the number:'))
first_num=0
second_num=1
for i in range(1,n+1):
    third_num=first_num+second_num
    first_num=second_num
    second_num=third_num
    print("final result",third_num)


class fibo:
    def __init__(self):
        self.num=n=int(input("enter the number :"))

    def calculation(self):
        num_1=0
        num_2=1
        print(num_1,num_2,end=" ")
        for i in range(self.num-2):
            num_3=num_1+num_2
            num_1=num_2
            num_2=num_3
            print(num_3,end=" ")

obj=fibo()
obj.calculation()
