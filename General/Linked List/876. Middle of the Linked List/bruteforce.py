# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        :Notes: Store all heads in a list
        curr =  head , curr = None if last node
        loop while curr is not none and append to list
        return the middle element at the end
        """
        if head.next == None:
            return head
        else:
            all_nodes = []
            curr = head
            while curr:
                all_nodes.append(curr)
                if curr.next is None:
                    curr = None
                else:
                    curr = curr.next
            return all_nodes[len(all_nodes) // 2]


# odd = //2
# even
if __name__ == '__main__':
    sol = Solution()
    ans = sol.middleNode()
    # print(ans)
