class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(("A","E","I","O","U","a","e","i","o","u"))
        p1 = 0
        p2 = len(s)-1
        s = list(s)
        while p1 < p2:
            if s[p1] in vowels and s[p2] in vowels:
                s[p1],s[p2] = s[p2],s[p1]
                p1 += 1
                p2 -= 1
            elif s[p2] not in vowels:
                p2 -= 1
            elif s[p1] not in vowels:
                p1 += 1
                
        return "".join(s)