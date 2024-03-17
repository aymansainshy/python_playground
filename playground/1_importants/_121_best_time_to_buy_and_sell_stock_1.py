from typing import List

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


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


# prices = [5,8,9,2,4,3,2,6,4]

# prices = [7, 8, 9, 5, 3, 6, 4]

# maximum_profit ?
# buyDay = 0
# saleDay = 1
# profit = salePrice - buyPrice


if __name__ == '__main__':
    given_prices = [7, 1, 5, 3, 6, 4]
    maxP = maxProfit(given_prices)

    print(maxP)
