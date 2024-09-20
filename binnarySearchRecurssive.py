class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchBinnary(start,end):
            mid = int((start+end)/2)
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target and start<=end):
                return searchBinnary(mid+1, end)
            elif(nums[mid]>target and start<=end):
                return searchBinnary(start, mid-1 )
            else:
                return -1
        start = 0
        end = len(nums)-1
        return searchBinnary(start, end)

            
        