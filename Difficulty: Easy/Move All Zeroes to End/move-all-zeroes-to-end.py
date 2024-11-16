#User function Template for python3

class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        left = 0
        right = 1
        
        while left < n and right < n:
            if arr[left] == 0:
                while right < n and arr[right] == 0:
                    right += 1
                    
                if right == n:
                    break
                
                if arr[right] != 0:
                    arr[left], arr[right] = arr[right], arr[left]
                    right += 1
                    left += 1
            else:
                left += 1
                right += 1
        
        return arr

    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends