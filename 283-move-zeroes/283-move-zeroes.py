class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[l] = nums[i]
                l+=1
        
        for j in range(l,len(nums)):
            nums[j]=0
