class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        count = 1
        temp = 1
        prev = nums[0]
        for i in range(1,len(nums)):
            
            if nums[i] == prev + 1:
                temp += 1
            elif nums[i] != prev :
                temp = 1
            prev = nums[i]
            count = max(count,temp)
                
            
                
        return count
                
        