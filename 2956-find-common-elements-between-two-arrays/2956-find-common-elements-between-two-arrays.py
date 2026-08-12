class Solution:
    def findIntersectionValues(self, num1,num2):
        ans1=0
        ans2=0
        for x in num1:
            if x in num2:
                ans1+=1
        for x in num2:
            if x in num1:
                ans2+=1
        return [ans1,ans2]

        