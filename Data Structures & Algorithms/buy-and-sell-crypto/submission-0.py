class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = prices[0]
        lst = []

        for sell in prices:
            
            if mini > sell:
                mini = sell
            else:
                profit = sell - mini
                lst.append(profit)
        return max(lst)