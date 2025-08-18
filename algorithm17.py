class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def oddEvenList(self, head):
        node = head
        odd = ListNode(0)
        odd1 = odd
        even = ListNode(0)
        even1 = even
        while node and node.next:
            odd1.next= node
            even1.next = node.next
            odd1 = odd1.next
            even1 = even1.next
            node = node.next.next
        if node:
            odd1.next = node
            odd1 = odd1.next
        even1.next = None

        odd = odd.next
        even = even.next
        odd1.next = even
        return odd
s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s.oddEvenList(head)

