class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        d1,d2 = {},{}
        s1,s2 = set(word1),set(word2)
        for word in word1:
            d1[word] = d1.get(word,0) + 1
            
        for word in word2:
            d2[word] = d2.get(word,0) + 1
            
        freq_d1 = sorted(d1.values())
        freq_d2 = sorted(d2.values())
        
        if freq_d1 == freq_d2 and s1 == s2:
            return True
        else:
            return False
        
            
        
        