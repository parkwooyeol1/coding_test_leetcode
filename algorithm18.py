class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution():
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m==n:
            return head
        root = start = ListNode(None)
        root.next = head

        for _ in range(m-1):
            start = start.next  # start : 1, 2, 3, 4, 5, None
        end = start.next    # end : 2, 3, 4, 5, None

        for _ in range(n-m):
            tmp, start.next, end.next  = start.next, end.next, end.next.next
            start.next.next = tmp
            

            
        self.print_list_node(root.next)
    def print_list_node(self, node: ListNode) :
        while node :
            print(node.val, end='')
            if node.next != None :
                print('->',end='')
            node = node.next
    


s = Solution()
left = 2
right = 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s.reverseBetween(head, left, right)

