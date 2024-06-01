
class Solution:
    def oddEven(self, s : str) -> str:
        even="bdfhjlnprtvxz"
        ans=0
        ss=set(s)
        for i in ss:
            if i in even:
                if s.count(i)%2==0:
                    ans+=1
            else:
                if s.count(i)%2!=0:
                    ans+=1
        if ans%2==0:
            return "EVEN"
        return "ODD"
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends