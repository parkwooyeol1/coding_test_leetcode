class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head):
        node = head
        a = None
        # 1, 2, 3, 4, None -> 5, 4, 3, 2, 1, None
        while node:
            b = node.next # 2, 3, 4  / 3, 4, /  4  /None
            node.next = a  # 1, None / 2, 1, None / 4, 3, 2, 1, None
            a = node 
            node = b  # 2, 3, 4 / 3, 4/ 4 / None
            
        return a
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
s = Solution()
print(s.reverseList(head1))