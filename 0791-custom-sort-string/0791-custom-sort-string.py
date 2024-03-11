class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = defaultdict(int)

        for i, c in enumerate(s):
            freq[c] += 1

        ans = []
        for c in order:
            tmp = []

            while freq[c]:
                tmp.append(c)
                freq[c] -= 1
            
            ans += tmp

        # adding chars which are absent not in order
        for k,v in freq.items():
            if v > 0:
                ans += k * v
        
        return ''.join(ans)