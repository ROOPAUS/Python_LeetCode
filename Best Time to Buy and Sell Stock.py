class Solution:
    def maxProfit(self, prices: [int]) -> int:
        max_profit_total, max_profit_current = 0, 0
        for i in range(1, len(prices)):
            max_profit_current = max(0, max_profit_current + prices[i] - prices[i-1])
            max_profit_total = max(max_profit_current, max_profit_total)
        return max_profit_total
nums=[]
n=int(input("Enter number of elementa in a string:"))
for i in range(n):
    nums.append(int(input("Enter element:")))
result= Solution().maxProfit(nums)
print(result)