class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        # #Store array into hash table, where value of list should be the key of hash table and index should be the value

        # dict = {}
        # for index,value in enumerate(nums):
        #     dict[value]=index
        
        # #Check all the value in range are in hashmap
        # for value in range(length+1):
        #     if(dict.get(value) is None):
        #         return value 


    # Optmized Solution
        n_sums = 0
        for x in range(length+1):
            n_sums += x

        array_sum = 0
        for value in nums:
            array_sum += value

        return n_sums - array_sum
        

