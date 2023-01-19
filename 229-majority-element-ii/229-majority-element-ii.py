class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        ans = set()
        
        for num in nums:
            d[num] = d.get(num,0) + 1
            if d[num] > len(nums)//3:
                ans.add(num)
        return ans