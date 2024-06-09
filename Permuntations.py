class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])  # Append a copy of the current permutation
            for i in range(start, end):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Recursively build the permutation from the next element
                backtrack(start + 1, end)
                # Swap back to restore the original array state for backtracking
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0, len(nums))
        return result