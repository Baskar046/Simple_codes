
n=int(input(""))
student_marks_info=[]
check_score=[]
if 2<=n<=5:
        for i in range(n):
                name=input("enter the name:")
                score=float(input("enter the score:"))
                student_marks_info.append([name,score])
                check_score.append(score)
        second_score = sorted(set(check_score))[1]
        second_name = [name for name, score in student_marks_info if score == second_score]
        second_name.sort()
        print(*second_name, sep="\n")
        print(second_score)
        print(student_marks_info)
else:
        print("invalid")