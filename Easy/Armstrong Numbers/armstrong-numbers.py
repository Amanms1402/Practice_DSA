#User function Template for python3

class Solution:

    def armstrongNumber (self, n):

        # code here 

        x=n//100

        z=n%10

        y=n%100

        y=y//10

        if x*x*x + y*y*y + z*z*z==n:

            return "true"

        else:

            return "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends