class Solution:
    def myPow(self, x: float, n: int) -> float:
#       Optimised approach{TC=> O(logN)}
        if n == 0:
            return 1
        num = abs(n)
        # if num < 0:
        #     num = abs(num)
        ans = 1.0
        while num:
            if num % 2 == 0:
                x = x*x
                num = num//2
            else:
                ans *= x
                num -= 1
        if n < 0:
            ans = 1.0/ans
        return ans
#          if n == 0:
#             return 1
        
#         total, val, left = 1, x, abs(n)

#         while left > 1:
#             if left % 2 == 0:
#                 left = left // 2
#                 val = val * val
#             else:
#                 total *= val
#                 left -= 1

#         return total * val if n > 0 else 1 / (total * val)
        
    
        # Brute Force{TC => O(N) }
#         ans = 1.0
        
#         for i in range(abs(n)):
#             if n < 0:
#                 ans/=x
#             else:
#                 ans*=x
#         return ans



        
        


        
            
        