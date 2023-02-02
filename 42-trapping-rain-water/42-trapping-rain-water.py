class Solution:
    def trap(self, height: List[int]) -> int:
#         #BruteForce TC = O(N*2) sc-> O(1)
#         n = len(height)
#         ans = 0
#         #iterate over complete array
#         for i in range(n):
#             j = i
#             leftmax = 0
#             rightmax = 0
            
#             #find the left max
#             while (j>=0):
#                 leftmax = max(leftmax,height[j])
#                 j-=1
            
#             #find the rightmax
#             j = i
            
#             while(j<n):
#                 rightmax = max(rightmax,height[j])
#                 j+=1
                
#             ans += min(leftmax,rightmax) - height[i]
            
#         return ans
    
        #Better Approach
        n = len(height)
        ans = 0
        suffix = [0]*n
        prefix = [0]*n
        
        prefix[0] = height[0]
        for i in range(1,n):
            prefix[i] = max(prefix[i-1],height[i])
            
        suffix[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            suffix[i] = max(suffix[i+1],height[i])
        
        for i in range(n):
            ans += min(suffix[i],prefix[i]) - height[i]
            
        return ans
        
        
                
            
            
            