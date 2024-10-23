class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    #Using two pinter approach
      start = 0
      end = len(nums)-1
      newSquaredSortedArray = []
      while(end>=start):
        if(abs(nums[start])>abs(nums[end])):
            newSquaredSortedArray.insert(0,nums[start]**2)
            start +=1
        else:
            newSquaredSortedArray.insert(0,nums[end]**2)
            end -=1

      return newSquaredSortedArray


        