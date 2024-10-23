class Solution:
    def isPalindrome(self, x: int) -> bool:

        # #time Complexity is the time taken to splice the string and extra space i.e.O(n) is required to convert int into string 
        # x = str(x)
        # #Slicing string in python strung[start:stop:step]
        # reverse_x = x[: : -1]
        # if(x==reverse_x):
        #     return True
        # else:
        #     return False



        #Without converting integer into string
        if(x<0): #Is a number is negative, we can't get the same number from right
            return False
        else:
            #reersing the inreger if it's positive
            num = x
            new_num = 0
            while(num!=0):
                rem = num % 10
                new_num = new_num * 10 + rem
                num = num//10

            if(new_num == x):
                return True
            else:
                return False

    
        