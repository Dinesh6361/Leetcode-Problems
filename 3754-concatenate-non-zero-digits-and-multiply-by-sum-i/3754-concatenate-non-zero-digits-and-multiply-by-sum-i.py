class Solution:
    def sumAndMultiply(self, n: int) -> int:
       x=""
       for digits in str(n):
            if digits!='0':
                x+=digits
       if x=="":
            return 0
       sum=0
       for digits in x:
            sum+=int(digits)
       return int(x)*sum