class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left_idx = findLeft(nums, target)
        right_idx = findRight(nums, target)
        
        if left_idx <= right_idx and right_idx < len(nums) and nums[left_idx] == target and nums[right_idx] == target:
            return [left_idx, right_idx]
        else:
            return [-1, -1]