# # Solution 1
# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def majorityElement(self, A):
#         max_count = 0
#         for first in A:
#             for compare in A:
#                 if first == compare:
#                     max_count += 1
#             if max_count > len(A) / 2:
#                 return first
#             else:
#                 max_count = 0

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        # Sort all elements
        A.sort()
        # Counter to keep track of occurance
        count = 1
        # Return number if list length is 1
        if len(A) == 1:
            return A[0]
        # if list has more than 1 numbers, Loop on each element to n-1
        for i in range(len(A) - 1):
            # if element is equal to next in list, increment the counter
            if A[i] == A[i + 1]:
                count += 1
                # if the element is found more than n/2 then return the element
                if count > len(A) // 2:
                    return A[i]
            else:
                count = 1


if __name__ == '__main__':
    sol = Solution()
    ans = sol.majorityElement([8, 8, 7, 7, 7])
    print(ans)
