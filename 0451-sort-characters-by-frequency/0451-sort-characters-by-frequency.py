class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for string in s:
            d[string] = d.get(string,0) + 1
            
        ans = sorted(d.items(),key = lambda x:[-x[1],x[0]])
        res = [key*value for key,value in ans]
        return ''.join(res)