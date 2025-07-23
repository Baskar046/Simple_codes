n = int(input())  # get the input user for how many records going to enter
students_records = {}  # stores the students details for checking
if 2 <= n <= 10:  # enter the records range between 2 to 10
    for _ in range(n):  # run until given range
        name, *line = input().split()  # get the name and mark from user on same line
        marks = list(map(float, line))  # line variable use to unpack the mark
        students_records[name] = marks  # store the details into dictionary
    final_student = input()  # get name from user to find average
    marks = students_records[final_student]  # find the user name in student_records
    avg = sum(marks) / len(marks)  # calculate sum and average
    print(f"{avg:.2f}")  # print the average with two decimal points