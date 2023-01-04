class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -float('inf')
        currsum = 0
        
        for num in nums:
            currsum += num
            if currsum > maxsum:
                maxsum = currsum
            if currsum < 0 :
                currsum = 0
                
        return maxsum
                