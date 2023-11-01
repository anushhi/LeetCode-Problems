from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Approach1
        # if (str1 + str2) != (str2 + str1):
        #     return ""
        # if str1 == str2:
        #     return str1
        # else:
        #     hcf = gcd(len(str1),len(str2))
        #     ans = str1[:hcf]
        #     return ans
        # Approach2
#         Algorithm
#         Find the shorter string among str1 and str2, without loss of generality, let it be          str1.

#         Start with base = str1, and check if both str1 and str2 are made of multiples of            base.
#         If so, return base.
#         Otherwise, we shall try a shorter string by removing the last character from base.

#         If we have checked all prefix strings without finding the GCD string, return "".

        l1, l2 = len(str1),len(str2)
        
        def valid(k):
            if l1 % k or l2 % k:
                return False
            n1,n2 = l1//k, l2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base
        
        for i in range(min(l1,l2),0,-1):
            if valid(i):
                return str1[:i]
        return ""
            
        
        