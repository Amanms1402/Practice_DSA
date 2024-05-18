#User function Template for python3
from typing import List

class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        if a[-2]<a[-1]: return a[-1]
        if a[0]>a[1]: return a[0]
        l,r = 1,len(a)-2
        while l<r:
            m = (l+r)//2
            if a[m]<a[m+1]: l = m+1
            else: r = m
        return a[l]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findPeakElement(a)
        print(ans)

# } Driver Code Ends