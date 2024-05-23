#User function Template for python3

class Solution:
    def kPalindrome(self, str, n, k):
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            dp[i][i] = 0

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if str[i] == str[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        return 1 if dp[0][n - 1] <= k else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        n = int(arr[0])
        k = int(arr[1])
        str = input()

        ob = Solution()
        print(ob.kPalindrome(str, n, k))

# } Driver Code Ends