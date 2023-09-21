from typing import List


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    buy_day = 0
    sale_day = buy_day + 1

    while sale_day < len(prices):

        if prices[buy_day] < prices[sale_day]:
            profit = prices[sale_day] - prices[buy_day]
            max_profit = max(max_profit, profit)
            sale_day += 1
        else:
            buy_day = sale_day
            sale_day = buy_day + 1

    return max_profit

# print(profit)
# print(f"index {buy_day} {sale_day}")

# prices = [5,8,9,2,4,3,2,6,4]

# prices = [7, 8, 9, 5, 3, 6, 4]

# maximum_profit ?
# buyDay = 0
# saleDay = 1
# profit = salePrice - buyPrice
