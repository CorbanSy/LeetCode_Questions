class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            # Swap nums[i] with nums[nums[i] - 1] until nums[i] is out of range or nums[i] is in the correct position
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Find the first position where the number is not correct
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positions are correct, the missing number is n + 1
        return n + 1