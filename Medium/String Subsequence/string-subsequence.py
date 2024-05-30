
class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        # code here
        import sys
        sys.setrecursionlimit(10**6)
        from functools import lru_cache
        
        @lru_cache(None)
        def match(i, j):
            if i < 0:
                return 1
            if j < 0:
                return 0
            r = match(i, j-1)

            if s2[i] == s1[j]:
                r += match(i-1, j-1)
            return r%(10**9+7)
        return match(len(s2)-1, len(s1)-1)
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s1 = (input())

        s2 = (input())

        obj = Solution()
        res = obj.countWays(s1, s2)

        print(res)

# } Driver Code Ends