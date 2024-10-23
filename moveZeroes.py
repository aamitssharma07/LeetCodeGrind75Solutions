class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums)>1):
            for x in range(len(nums)):
              if(nums[x]!=0):
                non_zero_index = x
                for y in range(non_zero_index):
                    if(nums[y]==0):
                        nums[y]=nums[non_zero_index]
                        nums[non_zero_index]=0

                