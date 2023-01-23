class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
        
#         nums.sort()
#         count = 1
#         temp = 1
#         prev = nums[0]
#         for i in range(1,len(nums)):
            
#             if nums[i] == prev + 1:
#                 temp += 1
#             elif nums[i] != prev :
#                 temp = 1
#             prev = nums[i]
#             count = max(count,temp)
                
            
                
#         return count

#optimal Solution
        num_set = set(nums)
        longest_streak = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_streak = 1
                current_num = num
                while current_num + 1 in num_set:
                    current_streak += 1
                    current_num += 1
                longest_streak = max(longest_streak,current_streak)
        return longest_streak
                
        