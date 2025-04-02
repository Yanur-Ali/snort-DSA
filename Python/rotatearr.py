class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        k %= n
        if n < 2 or k == 0:
            return
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

############

class Solution(object):
  def rotate(self, nums, k):
   
    if len(nums) == 0 or k == 0:
      return

    def reverse(start, end, s):
      while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    n = len(nums) - 1
    k = k % len(nums)
    reverse(0, n - k, nums)
    reverse(n - k + 1, n, nums)
    reverse(0, n, nums)
