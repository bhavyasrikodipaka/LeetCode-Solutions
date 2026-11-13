class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in nums:
            if i != 0:
                nums[idx] = i
                idx += 1
        for i in range(idx, len(nums)):
            nums[i] = 0