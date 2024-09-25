class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if(char == '[' or char =='(' or char == '{' ):
                stack.append(char)
            else:
                if(len(stack)!=0):
                    corresponding_open_brcaket = stack.pop()
                    if((char == ']' and corresponding_open_brcaket=='[') or (char == '}' and corresponding_open_brcaket=='{') or (char == ')' and corresponding_open_brcaket=='(' )):
                        pass
                    else:
                        return False
                else:
                    return False

        if(len(stack)==0):
            return True
        else:
            return False
        
     