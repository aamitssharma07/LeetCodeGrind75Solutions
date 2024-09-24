class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_value = len(nums)/2
        dict = {}

        #In a dictionry store the count of each different values. After storing keep checking  the corresponding value count in dictionary at that time, if it's greater than majority_value return that value 
        for values in nums:
            if(not dict.get(values)):
                dict[values] = 1
            else:
                dict[values]=dict.get(values)+1
            if(dict.get(values)> majority_value):
                return values