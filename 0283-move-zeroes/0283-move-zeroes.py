class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        """
        Do not return anything, modify nums in-place instead.
        """
            
        cnt = 0
        ptr = 0
        for i in range(len(nums)):
            if nums[ptr] == 0 and nums[i] != 0:
                nums[ptr],nums[i] = nums[i],nums[ptr]
                ptr += 1
            if nums[ptr] != 0:
                ptr += 1
                
        
                
                
        
                
            
                
                
            
            
                
        