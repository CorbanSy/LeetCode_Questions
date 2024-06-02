class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Pointer for the position of the next unique element
        k = 1

        # Traverse the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it's unique
            if nums[i] != nums[i - 1]:
                # Place the unique element at the next position
                nums[k] = nums[i]
                # Move the pointer for the next unique element
                k += 1

        return k