#User function Template for python3

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''


class Solution():
#Function to sort the given doubly linked list using Merge Sort.
    def sortDoubly(self, head: 'Node') -> 'Node':
        
        def merge(l1: Node, l2: Node) -> Node:
            dummy = Node(-1)
            node = dummy
            while l1 and l2:
                if l1.data <= l2.data:
                    node.next, node, l1 = l1, l1, l1.next
                else:
                    node.next, node, l2 = l2, l2, l2.next
            # Attaching any remaining nodes
            node.next = l1 or l2
            return dummy.next
        
        def mergesort(l1: Node, n: int) -> Node:
            if n == 1:
                return l1
            n_half = n // 2
            l1_tail = l1
            for _ in range(n_half - 1):
                l1_tail = l1_tail.next
            l2, l1_tail.next = l1_tail.next, None
            l1 = mergesort(l1, n_half)
            l2 = mergesort(l2, n - n_half)
            return merge(l1, l2)
        
        n, node = 0, head
        while node:
            n += 1
            node = node.next
        
        l = mergesort(head, n)
        # Fixing prevs
        prev, node = None, l
        while node:
            node.prev, prev, node = prev, node, node.next
        return l
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while (node is not None):
        print(node.data, end=" ")
        temp = node
        node = node.next
    print()
    while (temp):
        print(temp.data, end=" ")
        temp = temp.prev


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        ob = Solution()
        llist.head = ob.sortDoubly(llist.head)
        printList(llist.head)
        print()

# } Driver Code Ends