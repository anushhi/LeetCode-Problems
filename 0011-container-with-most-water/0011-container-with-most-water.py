class Solution:
    def maxArea(self, height: List[int]) -> int:
        store = 0
        left = 0
        right = len(height) -1
        curr = 0
        
        while(left <= right):
            dis = right - left
            min_height = min(height[left],height[right])
            curr = min_height * dis
            if curr > store:
                store = curr
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return store
            