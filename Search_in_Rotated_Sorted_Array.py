class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # Correct the way to get the length of the list

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Determine which part is sorted
            if nums[left] <= nums[mid]:  # Left part is sorted
                if nums[left] <= target < nums[mid]:  # Target is in the left part
                    right = mid - 1
                else:  # Target is in the right part
                    left = mid + 1
            else:  # Right part is sorted
                if nums[mid] < target <= nums[right]:  # Target is in the right part
                    left = mid + 1
                else:  # Target is in the left part
                    right = mid - 1
        
        return -1  # Target not found