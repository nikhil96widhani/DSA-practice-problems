class Solution(object):
    # Sample Code
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for bracket in s:
            if bracket in bracket_dict:
                if not stack or bracket_dict[bracket] != stack[-1]:
                    return False
                else:
                    del stack[-1]
            else:
                stack.append(bracket)

        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()
    ans = sol.isValid('()[]{}')
    print(ans)
