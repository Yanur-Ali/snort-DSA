
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, mi = 0, inf
        for v in prices:
            mi = min(mi, v)
            ans = max(ans, v - mi)
        return ans


class Solution(object):
  def maxProfit(self, prices):

    if not prices:
      return 0
    ans = 0
    pre = prices[0]
    for i in range(1, len(prices)):
      pre = min(pre, prices[i])
      ans = max(prices[i] - pre, ans)
    return ans
