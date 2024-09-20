# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

# In owrst case the complexity is O(n)   
#     def firstBadVersion(self, n: int) -> int:
#         for value in range(n,0,-1):
#             if(isBadVersion(value)):
#                 if(value==1):
#                     return value
#             else:
#                 return value+1

#Above function can be optimized by using the logic of binnary search so the complexity will be O(logn) and as per the question there must be a vlue
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end =   n
        mid = int((start+end)/2)
        while(start!=end):
            if(isBadVersion(mid)!=True):
                start = mid+1
            else:
                end = mid
            mid = int((start+end)/2)
        return start