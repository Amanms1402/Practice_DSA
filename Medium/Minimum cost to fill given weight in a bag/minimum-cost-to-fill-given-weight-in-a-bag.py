
from typing import List


class Solution:
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        from sys import setrecursionlimit
        setrecursionlimit(2*10**3)
        from functools import lru_cache
        @lru_cache(None)
        def dfs(ix=n-1,wth=w):
            nonlocal cost
            if wth==0:
                return 0
            if ix<0:
                return float('inf')
            if cost[ix]==-1:
                return dfs(ix-1,wth)
            mn=dfs(ix-1,wth)
            if wth-ix-1>=0:
                mn=min(
                    mn,
                    dfs(ix,wth-ix-1)+cost[ix],
                    dfs(ix-1,wth-ix-1)+cost[ix]
                    )
            return mn
        mn=dfs()
        return mn if mn!=float('inf') else -1
        



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

        w = int(input())

        cost = IntArray().Input(n)

        obj = Solution()
        res = obj.minimumCost(n, w, cost)

        print(res)

# } Driver Code Ends