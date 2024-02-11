class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in range(len(arr)):
            d[arr[i]] = d.get(arr[i],0) + 1
            
        s1 = set(d.values())
        s2 = set(arr)
        if len(s1) == len(s2):
            return True
        else:
            return False