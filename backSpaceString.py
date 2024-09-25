class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Use stack to store and pop the values
        def backspaceString(str):
            backspacedString = []
            for char in str:
                if(char == '#' and len(backspacedString)!=0):
                  backspacedString.pop()
                else:
                    if(char!='#'):
                        backspacedString.append(char)
            return backspacedString
 
        if(backspaceString(s)==backspaceString(t)):
            return True
        else:
            return False