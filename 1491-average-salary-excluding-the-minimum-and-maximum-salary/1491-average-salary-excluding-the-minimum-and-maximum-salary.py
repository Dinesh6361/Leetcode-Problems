class Solution:
    def average(self, salary: List[int]) -> float:
        avg= (sum(salary)-(min(salary)+max(salary)))/(len(salary)-2)
        return avg
        