class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for ele in nums:
            hashmap[ele] = hashmap.get(ele,0) + 1
            if hashmap[ele] > 1:
                return True
        
        return False
        
        
        
        
    