class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        k = len(s1)
        for i in range(k):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        if self.matches(s1_count, s2_count):
            return True
        for i in range(k, len(s2)):
            s2_count[ord(s2[i]) - ord('a')] += 1
            s2_count[ord(s2[i-k]) - ord('a')] -= 1
            if self.matches(s1_count, s2_count):
                return True
        return self.matches(s1_count, s2_count)
    
    def matches(self, s1_count, s2_count):
        for i in range(26):
            if s1_count[i] != s2_count[i]:
                return False
        return True
