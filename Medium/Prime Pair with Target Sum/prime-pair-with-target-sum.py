
from typing import List


class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # code here
        nums = [True for _ in range(n + 1)]
        nums[0] = nums[1] = False
        for i in range(2, len(nums)):
            if nums[i] == False:
                continue
            for j in range(i * i, len(nums), i):
                nums[j] = False
        
        for i in range(n + 1):
            if nums[i] and nums[n - i]:
                return [i, n - i]
        
        return [-1, -1]



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

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends