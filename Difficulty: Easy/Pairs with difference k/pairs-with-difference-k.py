#User function Template for python3
from collections import Counter

class Solution:
    def countPairsWithDiffK(self, arr, k):
        count = 0
        freq = Counter(arr)
        
        for num in freq:
            if k > 0:
                # Count pairs (num, num + k)
                count += freq[num] * freq.get(num + k, 0)
            elif k == 0:
                # Count pairs where the same number appears more than once
                count += (freq[num] * (freq[num] - 1)) // 2
                
        return count




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends