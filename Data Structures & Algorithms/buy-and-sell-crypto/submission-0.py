class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        stack = [prices[0]]
        for price in prices[1:]:
            if price > stack[-1]:
                ans = max(ans, price - stack[-1])
            else:
                stack.pop()
                stack.append(price)
        return ans
        