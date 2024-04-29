#Your task is to complete this function
#Your function should return the new head pointer
class Solution:
    def deleteK(self, head, k):
        #code here 
        if k==1:
            return None
        temp=head.next
        prev=head
        c=1
        while(temp):
            c+=1
            if c%k==0:
                prev.next=temp.next 
            prev=temp
            temp=temp.next 
        return head 


#{ 
 # Driver Code Starts
class node:

    def __init__(self, x):
        self.data = x
        self.next = None


def createLinkedList(arr):
    head = node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        new_node = node(arr[i])
        curr.next = new_node
        curr = curr.next

    return head


def printlist(ptr):
    while ptr != None:
        print(ptr.data, end=" ")
        ptr = ptr.next
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())

        obj = Solution()
        head = createLinkedList(arr)
        new_head = obj.deleteK(head, k)
        printlist(new_head)

# } Driver Code Ends