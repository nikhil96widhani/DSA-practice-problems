class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Notes: Using floyds tortoise and Hare algorithm
        Assuming fast will loop back to a position which will be equal to slow sometime in the loop,
        when cycle is found means both are at same point, then check every next to find the match node
        """
        fast, slow = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while (slow is not fast):
                    fast = fast.next
                    slow = slow.next
                return slow
        return None