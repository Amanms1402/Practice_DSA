class Solution:
    #Function to reverse a linked list.
    vowels={"a","e","i","o","u"}

    def arrangeCV(self, head):
        curr=head
        vHead,p=None,None
        cHead,q=None,None
        while curr:
            if curr.data in self.vowels:
                if vHead:
                    vHead.next=curr
                    vHead=vHead.next
                else:
                    vHead=curr
                    p=curr
                
            else:
                if cHead:
                    cHead.next=curr
                    cHead=cHead.next
                else:
                    cHead=curr
                    q=curr
            curr=curr.next
        if cHead:
            cHead.next=None
        if vHead:
            vHead.next=q
        return p if p else q

#{ 
 # Driver Code Starts
# Node Class
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)

# } Driver Code Ends