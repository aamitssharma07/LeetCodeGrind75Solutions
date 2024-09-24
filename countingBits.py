class Solution:
    def countBits(self, n: int) -> List[int]:
        #Using predefined method bin()
        # ans =[]
        # for value in range(n+1):
        #     binnary = bin(value)   #this bin function returns string
        #     ans.append(binnary.count('1'))
        # return ans 



        #Using my own method of converting into binnary
        def binn(value):
            binnary_list =[]
            while(value!=0):
                rem = value%2
                binnary_list.insert(0,rem)
                value = value//2
            return binnary_list

        ans =[]
        for value in range(n+1):
            binnary = binn(value)   #customized function binn
            ans.append(binnary.count(1))
        return ans 