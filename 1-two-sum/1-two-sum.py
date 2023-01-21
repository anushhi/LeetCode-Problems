class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        
        for ind,ele in enumerate(nums):
            
            if target-ele in d:
                return [d[target-ele],ind]
            else:
                d[ele] = ind
                
        
                
            