class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #Use dictionary and keep the count there if it's 2 then return yes
        dict = {

        }
        for index,value  in enumerate(nums):
            if(dict.get(value)!=None):
                return True
            else:                
                dict[value] = 1 
        return False

    #Other way is sort the array and then check for the consecutive two elements, if they are same then return True else return False after iterating the whole array

    # #Time Complexity is O(nlogn) and Space Complexity is O(nlogn)
    #     if(len(nums)==1):
    #         return False
    #     else:
    #         nums.sort()#return a new sorted array 
    #         index1 = 0
    #         index2 = 1
    #         while(index2!=len(nums)):
    #             if(nums[index1]==nums[index2]):
    #                 return True
    #             else:
    #                 index1 +=1
    #                 index2 +=1
    #         return False