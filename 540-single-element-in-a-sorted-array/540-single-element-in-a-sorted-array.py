class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0,len(nums)-1
        
        while(start<end):
            mid = 2*((start+end)//4)
            if nums[mid] == nums[mid+1]:
                start = mid+2
            else:
                end = mid
        return nums[start]
        
        