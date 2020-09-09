
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            # i = 2 --> dp[2]c = dp[1]b + dp[0]a
            # i = 3 --> dp[3]c = dp[2]b + dp[1]a
            dp[i] = dp[i - 1] + dp[i-2]
        return dp[n]


    def climbStairs2(self, n: int) -> int:
        c, b, a = 1, 1, 1
        for i in range(2, n + 1):
            c = b + a
            a = b
            b = c
        return c

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs2(1))
