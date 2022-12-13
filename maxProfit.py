class Solution:
    def maxProfit(self, prices: list[int]) -> int:   
        
        if min(prices) == prices[-1]:
            prices.pop()
        else:
            pass
        
        day = prices.index(min(prices))
        alt_prices = prices[day:]
        prices = prices[:day]
        print(prices, alt_prices, day)
        
        print("I am here now", prices, alt_prices, day)
        if len(alt_prices) < 1:
            print(f"I made it here! {alt_prices}")
            prices = alt_prices
        elif prices and ((max(prices) - min(prices)) > (max(alt_prices) - min(alt_prices))) and (prices.index(max(prices)) !=0 or (min(prices)!=prices[-1])):
            print("Need to re-shuffle")
            if len(prices) > 2 and (prices[0]!=min(prices) or prices[-1]!=max(prices)):
                print("Optimizing")
                self.maxProfit(prices)
            else:
                prices = prices
                print(f"Re-router {prices} {alt_prices}")
                return (max(prices) - min(prices))
        else:
            print("NO SHUFFLE")
            print(alt_prices)
            return(max(alt_prices) - min(alt_prices))
        
        print("I am here now at the end",prices, alt_prices)
        return (max(prices) - min(prices))