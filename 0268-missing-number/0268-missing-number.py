class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_val = sum(nums)
        l = len(nums)
        natural_sum = l*(l+1)//2
        return natural_sum - sum_val
            