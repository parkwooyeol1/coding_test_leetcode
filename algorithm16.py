class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def swapPairs(self, head): 
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a를 가르키도록 해당
            b = head.next
            head.next = b.next
            b.next = head
            # prev가 b를 가르키도록 할당
            prev.next = b
            # 다음번 비교를 위해서 이동
            head = head.next
            prev = prev.next.next
        return root.next
        

            
s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(s.swapPairs(head))
