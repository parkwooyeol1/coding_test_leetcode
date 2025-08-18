class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
"""
class Solution:
    def isPalindrome(self, head):
        node = head
        a = []
        while node:
            a.append(node.val)
            node = node.next
        k = list(reversed(a))
        
        return a==k
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None # reversed linked list
        slow = fast = head # 두 개의 runner (init은 처음 값으로)
        # runner를 이용하여 역순 연결 리스트 구성
        
        while fast and fast.next: # fast running (slow runner가 딱 연결 리스트 중간까지 도달하도록 함)
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        if fast: # 연결리스트가 홀수의 원소를 갖는 경우, 가운데 원소를 palindrome 체크에서 배제하도록 함.
            slow = slow.next
        
        # palindrome 여부 체크
        while rev and slow.val == rev.val:
            rev, slow = rev.next, slow.next
        
        return not rev 
    # palindrome이 아니어서 while loop을 탈출했다면 rev가 None이 아니므로 False일 것이고, 정상적으로 while이 종료되었다면 rev가 None이므로 True일 것이다. (slow로 해도 상관 X)

head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
s = Solution()
print(s.isPalindrome(head))