class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #BruteForce
        # for i in range(len(nums) - 2):
        #     for j in range(i+1, len(nums) - 1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] < nums[j] and nums[j] < nums[k]:
        #                 return True
        # return False
        
        #OptimisedApproach
        
        # if len(nums) == 1 or len(nums) == 2:
        #     return False
        
        first = second = math.inf
        for num in nums:
            if num < first:
                first = num
            elif num > first and num < second:
                second = num
            elif num > second:
                return True
        return False
            
            
            
                
        