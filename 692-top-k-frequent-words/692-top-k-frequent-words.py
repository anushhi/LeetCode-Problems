class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(lambda:0)
        for word in words:
            d[word] += 1
            
        res = sorted(d.items(),key = lambda x:(-x[1],x[0]))[:k]
        return [ele for ele,val in res]