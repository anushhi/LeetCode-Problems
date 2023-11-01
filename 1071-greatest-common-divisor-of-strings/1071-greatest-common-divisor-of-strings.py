from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2) != (str2 + str1):
            return ""
        if str1 == str2:
            return str1
        else:
            hcf = gcd(len(str1),len(str2))
            ans = str1[:hcf]
            return ans
            
        
        