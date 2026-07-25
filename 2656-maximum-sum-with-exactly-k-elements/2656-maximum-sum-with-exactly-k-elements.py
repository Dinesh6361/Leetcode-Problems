class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ans=0
        num=max(nums)
        for i in range(k):
            ans+=num
            num+=1
        return ans