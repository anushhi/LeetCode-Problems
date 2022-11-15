class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = 0
        ans = -float('inf')
        
        if len(nums) == 1:
            return nums[0]*1.0
        for i in range(len(nums)):
            if i < k-1:
                cur += nums[i]
            elif i == k-1:
                cur += nums[i]
                ans = max(ans,cur)
            else:
                cur -= nums[i-k]
                cur += nums[i]
                ans = max(cur,ans)
                
        return ans*1.0/k
        