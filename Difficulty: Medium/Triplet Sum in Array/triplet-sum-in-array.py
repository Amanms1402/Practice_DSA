#User function Template for python3
class Solution:
     
    # Should return true if there exists a triplet in the
    # array arr[] which sums to x. Otherwise false
    def find3Numbers(self, arr, n, x):
        # Your Code Here
        arr.sort()
        for i in range(n-1):
            left = i + 1
            right = n - 1 
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                if current_sum == x:
                    return 1
                if current_sum > x:
                    right -= 1
                else:
                    left += 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, X = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        if (ob.find3Numbers(A, n, X)):
            print(1)
        else:
            print(0)
        print("~")

# } Driver Code Ends