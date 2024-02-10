class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def IsPalindrome(s):
            ptr1 = 0
            ptr2 = len(s)-1
            while(ptr1<ptr2):
                
                if s[ptr1] == s[ptr2]:
                    ptr1+=1
                    ptr2-=1
                else:
                    return False
            return True
        
        cnt = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
            
                ans = IsPalindrome(s[i:j])
                if ans:
                    cnt+=1
                
        return cnt
            
                
                
                