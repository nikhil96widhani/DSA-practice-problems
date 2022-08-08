# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Dont delete the node just replace value and the next to the next element value and next
        node.val = node.next.val
        node.next = node.next.next
        # # or
        # node.val, node.next = node.next.val, node.next.next


if __name__ == '__main__':
    sol = Solution()
    # ans = sol.deleteNode()
    # print(ans)
