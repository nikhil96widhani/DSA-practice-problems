class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        sell_price = prices[-1]
        profit = 0
        i = len(prices)
        while i >=0:
            if prices[i]>prices[i-1] and prices[i]-prices[i-1]>profit:
                profit = prices[i]-prices[i-1]
                sell_price = prices[i]
            else:
                i -=1

if __name__ == '__main__':
    sol = Solution()
    ans = sol.maxProfit([7,1,5,3,6,4])
    print(ans)
