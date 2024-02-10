class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        if len(s) == 0:
            return True
        
        for i in range(len(t)):
            if s[ptr] == t[i]:
                ptr += 1
            if ptr == len(s):
                return True
            
        return False
            
                
            