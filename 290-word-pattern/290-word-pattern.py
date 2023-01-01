class Solution:
    def helper(self,lst):
        d = defaultdict(lambda : 0)
        seen = set()
        dp = [0]*len(lst)
        for i,val in enumerate(lst):
            if val not in seen:
                seen.add(val)
                d[val] = i
            else:
                dp[i] = d[val]
        return dp
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        if len(set(pattern)) != len(set(words)):return False
        print(pattern,words)
        dp1 = self.helper(pattern)
        dp2 = self.helper(words)
        print('dp1',dp1)
        print('dp2',dp2)
        if dp1==dp2:
            return True
        else:
            return False
        
                