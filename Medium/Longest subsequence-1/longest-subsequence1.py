
from typing import List

class Solution:
    def longestSubseq(self, N, A):
        dp, max1 = [1]*N, float("-inf")
        
        for i in range(1, N):
            for j in range(i):
                if abs(A[i]-A[j])==1:
                    dp[i]=max(dp[i], dp[j]+1)
                    max1=max(max1, dp[i])
        return max1
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        a = IntArray().Input(n)

        obj = Solution()
        res = obj.longestSubseq(n, a)

        print(res)

# } Driver Code Ends