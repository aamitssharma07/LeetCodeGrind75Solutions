def isPalindrome(s) -> bool:    
    s = s.lower()
    start = 0
    end = len(s)-1
    while(start <= end):
        while(start <= end and (s[start].isalpha() or s[start].isdigit()) and (s[end].isalpha() or s[end].isdigit()) ):
            # print(start, end)
            # print(s[start], s[end])
            if(s[start]== s[end] ):
                start += 1
                end -= 1
            else:
                print()
                return False

        # print(start, end)
        # print(s[start], s[end])
        if((start<= end) and not (s[start].isalpha() or [start].isdigit())) :
            start += 1
            
        if((end >= start) and not (s[end].isalpha() or s[end].isdigit())):
            end += -1
            
    return True


print(isPalindrome("0P"))

