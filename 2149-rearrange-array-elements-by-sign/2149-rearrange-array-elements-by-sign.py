class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ptr1 = 0
        ptr2 = 1
        res = [0]*len(nums)
        for i in nums:
            if i > 0:
                res[ptr1] = i
                ptr1 += 2
            else:
                res[ptr2] = i
                ptr2 +=2
                
        return res
                
        
                
        
        