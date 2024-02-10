class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = -float('inf')
        cnt = 0
        curr_sum = 0
        if len(nums) == 0:
            return nums[0]
        
        for i in range(len(nums)):
            if cnt < k-1:
                cnt += 1
                curr_sum += nums[i]
            elif cnt == k-1:
                curr_sum += nums[i]
                if sum_ < curr_sum:
                    sum_ = curr_sum
                    cnt += 1
            else:
                curr_sum -= nums[i-k]
                curr_sum += nums[i]
                if sum_ < curr_sum:
                    sum_ = curr_sum
                    
        return sum_/k
            
                   
                
            
        
                