#User function Template for python3

class Solution:
    def jugglerSequence(self, n):
        ans = []
        
        while n>1:
            ans.append(n)
            if n % 2 == 0:
                n = int(n**(1/2))
            else:
                n = int(n**(3/2))
        ans.append(1)
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()

# } Driver Code Ends