class Solution:
    def twoSum(self, nums, target):
        num_map = {}  #store value, index mapping
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store number, its index
            num_map[num] = i

# Example 
nums = [2, 7, 11, 15]
target = 9
result = Solution().twoSum(nums, target)
print(result)  
