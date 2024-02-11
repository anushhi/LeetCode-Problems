class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        ans = [[],[]]
        for ele in s1:
            if ele not in s2:
                ans[0].append(ele)
        for ele in s2:
            if ele not in s1:
                ans[1].append(ele)
        return ans