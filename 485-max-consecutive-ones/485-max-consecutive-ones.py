class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        temp = 0
        for ele in nums:
            if ele == 1:
                temp += 1
            else:
                temp = 0
            maxi = max(maxi,temp)
        return maxi
                