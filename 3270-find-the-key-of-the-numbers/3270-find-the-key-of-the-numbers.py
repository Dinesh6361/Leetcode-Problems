class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ans=0
        place=1
        for _ in range(4):
            d1=num1 %10
            d2=num2 %10
            d3=num3 %10
            ans+=min(d1,d2,d3)*place
            
            num1//=10
            num2//=10
            num3//=10
            place *=10
        return ans