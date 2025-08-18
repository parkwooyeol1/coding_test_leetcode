class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:            
    def mergeTwoLists(self, list1, list2):
        node = ListNode(1)
        a = node

        while list1 and list2:
            if list1.val <= list2.val:
                a.next = list1
                list1 = list1.next

            else:
                a.next = list2
                list2 = list2.next
            a = a.next


        if list1:
            a.next = list1
        if list2:
            a.next = list2
        node = node.next
        return node
    
    """
    def solution(l1, l2):
    if not l1 :
        return l2
    if l1.val > l2.val:
        l1, l2 = l2, l1
    l1.next = solution(l1.next, l2)
    return l1
    """
    
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
head2 = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
#head1 = None
#head2 = None
s= Solution()
print(s.mergeTwoLists(head1, head2))