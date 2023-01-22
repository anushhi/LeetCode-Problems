class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Optimal  Approach
        if not nums:
            return 0
        
        nums.sort()
        l = len(nums)
        res = set()
        for i in range(l):
            target3 = target - nums[i]
            for j in range(i+1,l):
                target2 = target3 - nums[j]
                left = j+1
                right = l-1
                
                while(left<right):
                    two_sum = nums[left] + nums[right]
                    if two_sum  < target2:
                        left += 1
                    elif two_sum > target2:
                        right -= 1
                    else:
                        quad = [nums[i],nums[j],nums[left],nums[right]]
                        res.add(tuple(quad))
                        
                        while left < right and nums[left] == quad[2]:
                            left += 1
                        
                        while left < right and nums[right] == quad[3]:
                            right -= 1
                while j + 1 < l and nums[j] == nums[j+1]:
                    j+= 1
            while i + 1 < l and nums[i] == nums[i+1]:
                i+= 1
        return res

