#User function Template for python3

def max_sum(a,n):
    #code here
    
    current_value = sum(i * a[i] for i in range(n))
    
    
    array_sum = sum(a)
    
    max_value = current_value
    
   
    for i in range(1, n):
        current_value = current_value + array_sum - n * a[n - i]
        if current_value > max_value:
            max_value = current_value
    
    return max_value


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends