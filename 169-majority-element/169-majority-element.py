class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Using Hashmap {TC => O(NLogN),SC=>O(N)}
        # d = {}
        # for num in nums:
        #     d[num] = d.get(num,0)+1
        #     if d[num] > len(nums)//2:
        #         return num
        # Using Moore's Voting Algorithm
        count = 0
        ele = 0
        for num in nums:
            if count == 0:
                ele = num
            if ele == num:
                count += 1
            if ele != num:
                count -= 1
        return ele
        
            