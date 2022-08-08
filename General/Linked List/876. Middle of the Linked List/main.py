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

        :Notes:
        USING FLOYDS TORTOISE and HARE ALGORITHM
        oneX = pointer which runs one next per loop
        twoX = pointer which runs 2x faster per loop
        Assumption: end of the loop, twoX will be twice ahead of oneX hence oneX will be the middle
        """
        oneX, twoX = head, head

        while twoX:

            twoX = twoX.next
            if twoX:
                twoX = twoX.next
            else:
                break
            oneX = oneX.next

        return oneX

# odd = //2
# even
if __name__ == '__main__':
    sol = Solution()
    ans = sol.middleNode()
    # print(ans)
