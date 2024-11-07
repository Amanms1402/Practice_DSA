#User function Template for python3
class Solution:
    # Function to determine if array arr can be split into three equal sum sets.
    def findSplit(self, arr):
        s=sum(arr)
        if s%3!=0:
            return [-1,-1]
        val=s//3
        cnt,tot=0,0
        indices=[]
        i=0
        for j in range(len(arr)):
            cnt+=arr[j]
            
            if (cnt==val):
                tot+=1
                cnt=0
                indices.append([i,j])
                i=j+1
                if tot==3:
                    break
        if tot==3:
            return indices[:2]
        else:
            return [-1,-1]


        # Return an array of possible answer, driver code will judge and return true or false based on



#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if result == [-1, -1]:
            print("false")
        else:
            print("true")
        print("~")

# } Driver Code Ends