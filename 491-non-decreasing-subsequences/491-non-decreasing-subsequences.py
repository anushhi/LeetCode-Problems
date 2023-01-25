class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        current_seq = []
        def backtrack(ind):
            
            if ind == len(nums):
                if len(current_seq) >= 2:
                    ans.add(tuple(current_seq))
                return
            
            if not current_seq or current_seq[-1] <= nums[ind]:
                current_seq.append(nums[ind])
                backtrack(ind + 1)
                current_seq.pop()
            backtrack(ind+1)
            
        backtrack(0)
        return ans 
            
            
            
                    
        