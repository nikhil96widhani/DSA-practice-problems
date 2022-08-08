# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hashset = set()
        temp = head
        while temp and temp.next:
            if temp in hashset:
                return True
            else:
                hashset.add(temp)
            temp = temp.next

        return False
