# Take an array denoting daily stock price
# Return the maximum profit that could be made from buying and selling stock once

def buyAndSellStock(prices):
    minPrice, profit = float('inf'), 0

    for price in prices:
        minPrice = min(minPrice, price)
        profit = max(profit, (price - minPrice))
        
    return profit

if __name__ == "__main__":
    array = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    print(buyAndSellStock(array))
    