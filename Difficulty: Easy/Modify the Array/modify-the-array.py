#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        length = len(arr)
        for i in range(length-1):
            if arr[i] == arr[i+1]:
                arr[i] = arr[i+1]*2
                arr[i+1] = 0
        
        ans = []
        zero = 0
        
        for i in arr:
            if i == 0:
                zero += 1
            
            else:
                ans.append(i)
        
        for i in range(zero):
            ans.append(0)
        
        return ans




#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends