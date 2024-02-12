class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        left = 0
        right = len(nums)-1
        
        while(left<right):
            curr = nums[left] + nums[right]
            
            if curr == k:
                ans += 1
                left += 1
                right -= 1
                
            elif curr < k:
                left += 1
            else:
                right -= 1
                
        return ans
        
        