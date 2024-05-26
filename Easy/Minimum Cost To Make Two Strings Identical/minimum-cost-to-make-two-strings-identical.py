#User function Template for python3
class Solution:
    def findMinCost(self, x, y, costX, costY):
        X, Y = len(x), len(y)
        dp = [[0] * (Y+1) for _ in range(X+1)]
        for i in reversed(range(X)):
            for j in reversed(range(Y)):
                if x[i] == y[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        lcs = dp[0][0]
        return costX * (X - lcs) + costY * (Y-lcs)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        X, Y, costX, costY = input().split()
        costX = int(costX)
        costY = int(costY)
        ob = Solution()
        ans = ob.findMinCost(X, Y, costX, costY)
        print(ans)

# } Driver Code Ends