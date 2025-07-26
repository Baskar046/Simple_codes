class Solution:
    #day =sunday,monday,..
    #n=0,1,2,3,4,...
    def findAnswer(self, d, n):
       days = {0: "sunday", 1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday"}
       print(((d-n)%7))

sol=Solution()
sol.findAnswer(2,18)

#calculation
'''
example: if we give d=2,n=18 means
        formula=(d-n)%7
    solution:
        (2-18)%7  it gives : -16%7 ,so what is next multiple value of 16 in 7 is 3*7=21.
        (5-21) : which number gone be reduce the multiplyed from original value is :5
        output is :5
'''