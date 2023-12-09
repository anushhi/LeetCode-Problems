class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind,ele in enumerate(nums):
            if target - ele in hashmap:
                return [hashmap[target-ele],ind]
            hashmap[ele] = ind
                
                
                
                
        
                
            