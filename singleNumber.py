class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if(len(nums)==1):
            return nums[0]
        else:
            first = 0
            second = 1
            while(second<len(nums) and nums[first]==nums[second]):
                first +=2
                second += 2
            return nums[first]

            