#User function Template for python3
class Solution:

	def matchPairs(self, n, nuts, bolts):
	    order = {'!':1,'#':2,'$':3,'%':4,'&':5,'*':6,'?':7,'@':8,'^':9}
	    nuts_mapping = [order[i] for i in nuts]
	    bolts_mapping = [order[j] for j in bolts]
	    nuts_mapping.sort()
	    bolts_mapping.sort()
	    reverse_order = {v:k for k,v in order.items()}
	    nuts[:] = [reverse_order[i] for i in nuts_mapping]
	    bolts[:] = [reverse_order[j] for j in bolts_mapping]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(n, nuts, bolts)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends