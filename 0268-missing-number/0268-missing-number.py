class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) 
        natSum = n*(n+1)//2
        arrSum = sum(nums)
        return (natSum - arrSum)
            