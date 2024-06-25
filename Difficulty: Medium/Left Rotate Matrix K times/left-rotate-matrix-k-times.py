class Solution:
    def rotateMatrix(self, k, mat):
        # code here
        res=[]
        m,n=len(mat),len(mat[0])
        for i in range(n):
            temp=[]
            for j in range(m):
                temp.append(mat[j][i])
            res.append(temp)
        k=k%len(res)
        while k:
            temp=res[0]
            res.pop(0)
            res.append(temp)
            k-=1
        for i in range(n):
            temp=[]
            for j in range(m):
                mat[j][i]=res[i][j]
        return mat


#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()

# } Driver Code Ends