class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = defaultdict(str)
        for word1,word2 in zip(s,t):
            if word1 in hashmap:
                if hashmap[word1] != word2:
                    return False
            elif word2 in hashmap.values():
                return False
            else:
                hashmap[word1] = word2
        return True
                
            
        
        