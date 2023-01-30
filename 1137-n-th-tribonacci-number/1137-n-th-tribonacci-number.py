class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1]*n
        def trib(n,dp):
            ans1 = sys.maxsize
            ans2 = sys.maxsize
            ans3 = sys.maxsize
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if dp[n-1] == -1:
                ans1 = trib(n-1,dp)
                dp[n-1] = ans1
            else:
                ans1 = dp[n-1]
            if dp[n-2] == -1:
                ans2 = trib(n-2,dp)
                dp[n-2] = ans2
            else:
                ans2 = dp[n-2]
            if dp[n-3] == -1:
                ans3 = trib(n-3,dp)
                dp[n-3] = ans3
            else:
                ans3 = dp[n-3]
            return (ans1+ans2+ans3)
        return trib(n,dp)
                
        
        