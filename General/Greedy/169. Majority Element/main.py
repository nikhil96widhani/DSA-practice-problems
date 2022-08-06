class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        # We take first number of the array
        number = A[0]
        # give it count = 1 because we have it one time now
        count = 1
        # Loop from the second value of array
        for i in range(1, len(A)):
            # if next number == the selected number, increament the counter
            if A[i] == number:
                count += 1
            # else if the count = 0 ( means other number has substracted it enough times
            # so it can be replaced with other number)
            elif count == 0:
                number = A[i]
                count = 1
            # else counter decrement if another number is found
            else:
                count -= 1
        # The number will be returned with count >= 1
        # because it will occur more than 50 times so if n = 5
        # then other numbers can cancel out 2 times the final count will be 1 because 3-2 =1
        return number

# # AWESOME METHOOD
# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def majorityElement(self, A):
#         A.sort()
#         return A[len(A)//2]
#

if __name__ == '__main__':
    sol = Solution()
    ans = sol.majorityElement(
                                [6,5,5]
                              )
    print(ans)
