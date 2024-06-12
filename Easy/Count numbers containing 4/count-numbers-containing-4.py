
class Solution:
    def countNumberswith4(self, n : int) -> int:
        count = 0
        for i in range(n+1):
            j = str(i)
            if '4' in j:
                count+=1
        return count
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.countNumberswith4(n)

        print(res)

# } Driver Code Ends