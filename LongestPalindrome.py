class Solution:
    def longestPalindrome(self, s: str) -> int:
        if(len(s)==1):
            return 1
        else:
            dict = {}
            longest_palindrome = 0
            first_odd = True    # this will owrk as a flag to check if there is single odd count, then along with pair 1 can also be added
            for value in s:     # stores the count of each element in dict
                if(not dict.get(value)):
                    dict[value]=1
                else:
                    dict[value]=dict.get(value) + 1


            for value in dict:
                if(dict[value]%2==0):#Will check if there are pairs of any charcter than all of them will contribute to the palindrome
                    longest_palindrome = longest_palindrome +  dict[value]
                else:  # Will add only the pare in the palindrome
                    if(first_odd):
                        longest_palindrome = longest_palindrome + (dict[value]//2 * 2)  +1
                        first_odd = False
                    else:
                        longest_palindrome = longest_palindrome + (dict[value]//2 * 2)                    
        return  longest_palindrome