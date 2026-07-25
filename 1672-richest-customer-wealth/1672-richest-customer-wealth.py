class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=0
        for account in accounts:
            total=0
            for money in account:
                total+=money
            ans= max(ans,total)
        return ans