class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = int((start + end)/2)
        while (nums[mid]!=target and start<end):#Importnat coditioon to make sure that ether target value is there or there is no such value in the array
            if(nums[mid]>target):
                end = mid-1
            else:
                start = mid+1
            mid = int((start + end)/2)
        if(nums[mid]==target):
            return mid
        else:
            return -1