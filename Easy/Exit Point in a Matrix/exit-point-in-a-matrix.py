#User function Template for python3

class Solution:
	def FindExitPoint(self, n, m, matrix):
		i, j = 0, 0
		directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
		d = 0
		while 0<=i<n and 0<=j<m:
		    if matrix[i][j]:
		        matrix[i][j] = 0
		        d = (d+1)%4
		    i += directions[d][0]
	        j += directions[d][1]
	    
	    return i-directions[d][0],j-directions[d][1] 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.FindExitPoint(n, m, matrix)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends