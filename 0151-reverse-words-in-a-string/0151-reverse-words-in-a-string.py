class Solution:
    def reverseWords(self, s: str) -> str:
#         ans = ""
#         for word in s.split():
#             ans = word+" "+ans
            
#         return ans.strip()

        return " ".join(s.split()[::-1])
        