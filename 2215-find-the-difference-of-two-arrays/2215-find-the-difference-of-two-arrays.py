class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        ans1 = []
        ans2 = []
        for ele in s1:
            if ele not in s2:
                ans1.append(ele)
        for ele in s2:
            if ele not in s1:
                ans2.append(ele)
        return[ans1,ans2]