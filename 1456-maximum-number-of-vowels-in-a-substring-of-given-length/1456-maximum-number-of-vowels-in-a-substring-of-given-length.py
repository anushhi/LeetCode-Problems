class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        currCount = 0
        vowels = "aeiou"
        maxCount = 0
        
        for i , v in enumerate(s):
            if i >= k:
                if s[i-k] in vowels:
                    currCount -= 1
            if s[i] in vowels:
                currCount += 1
            
            maxCount = max(maxCount,currCount)
            
        return maxCount
                    
                
                
            
            
            