
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, b - a) for a, b in pairwise(prices))


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum( max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)) )


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum( prices[i] - prices[i - 1] for i in range(1, len(prices)) if prices[i] > prices[i - 1] )

############

class Solution(object):
  def maxProfit(self, prices):
   
    ans = 0
    for i in range(1, len(prices)):
      if prices[i] > prices[i - 1]:
        ans += prices[i] - prices[i - 1]
    return ans

