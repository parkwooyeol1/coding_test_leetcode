class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        node = result
        k = 0
         #2, 4, 3   #5, 6, 4
        while l1 or l2 or k:
            if l1:
                a = l1.val
            if l2:
                b = l2.val

            i = (a+b+k) % 10
            k = (a+b+k) // 10
            node.next = ListNode(i)
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        retult = retult.next
        return result

            

