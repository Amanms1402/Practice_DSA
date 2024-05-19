
from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # Just Chiil and Code
        ans = 10**9
        diff = float('inf')
        i , j = 0, n-1
        
        while i <= j:
            mid = (i+j)//2
            if k == arr[mid]:
                return arr[mid]
            
            currDiff = abs(k - arr[mid])
            if abs(ans - k) > currDiff or (abs(ans-k) == currDiff and ans < arr[mid]):
                ans = arr[mid]
            
            if k < arr[mid]:
                j = mid-1
            else:
                i= mid+1
            
        return ans



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends