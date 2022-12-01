class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = ('a','e','i','o','u','A','E','I','O','U')
        c1 = 0
        c2 = 0
        b = len(s)//2
        for i in range(len(s)//2):
            b = len(s)//2
            if s[i] in l:
                c1 +=1
            if s[i+b] in l:
                c2+=1
        if c1 == c2:
            return True
        else:
            return False
                
            