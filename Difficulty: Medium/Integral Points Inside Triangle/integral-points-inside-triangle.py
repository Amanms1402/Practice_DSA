#User function Template for python3

from math import gcd
class Solution:
    def InternalCount(self, p, q, r):
        x1,y1=p[0],p[1]
        x2,y2=q[0],q[1]
        x3,y3=r[0],r[1]
        m1,m2,m3=abs(x1-x2),abs(x1-x3),abs(x2-x3)
        n1,n2,n3=abs(y1-y2),abs(y1-y3),abs(y2-y3)
        a,b,c=gcd(m1,n1),gcd(m2,n2),gcd(m3,n3)
        x=a+b+c
        area=abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
        res=(area-x+2)//2
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        p=[0]*2
        q=[0]*2
        r=[0]*2
        p[0],p[1],q[0],q[1],r[0],r[1]=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.InternalCount(p,q,r);
        print(ans)
# } Driver Code Ends