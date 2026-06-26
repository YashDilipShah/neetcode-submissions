class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        cur = head
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev, cur = cur, next_node
        return prev