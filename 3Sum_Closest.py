class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Sort the array to simplify the two-pointer approach
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n):
            # Two-pointer approach
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If the current sum is exactly the target, return it
                if current_sum == target:
                    return current_sum
                
                # Update the closest_sum if the current_sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move the pointers based on comparison with target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum