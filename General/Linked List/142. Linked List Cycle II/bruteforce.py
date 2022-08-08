class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hashset = set()
        temp = head
        while temp and temp.next:
            if temp in hashset:
                return temp
            else:
                hashset.add(temp)
            temp = temp.next

        return None