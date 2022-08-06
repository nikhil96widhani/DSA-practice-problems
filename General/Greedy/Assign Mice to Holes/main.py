class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):

        A.sort()
        B.sort()
        z = []
        for i in range(len(A)):
            sub = A[i]-B[i]
            if sub<0:
                z.append(-sub)
            else:
                z.append(sub)

        return max(z)


if __name__ == '__main__':
    sol = Solution()
    ans = sol.mice([-4, 2, 3], [0, -2, 4])
    print(ans)
