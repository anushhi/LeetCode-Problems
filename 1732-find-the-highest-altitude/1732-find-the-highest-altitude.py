class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = 0
        max_alt = -float('inf')
        
        for i in range(len(gain)):
            curr_alt += gain[i]
            max_alt = max(curr_alt,max_alt)
            
        max_alt = max(max_alt,0)
        
        return max_alt
                