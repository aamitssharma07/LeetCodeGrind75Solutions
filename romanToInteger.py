class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        if(len(s)==1):
            return dict.get(s[0])
        else:
            index = 0
            sum = 0
            while(index<len(s)-1):
                if(dict.get(s[index+1])<=dict.get(s[index])):
                    sum = sum+dict.get(s[index])
                    index+=1
                else:
                    sum = sum-dict.get(s[index])
                    index+=1
            sum = sum + dict.get(s[index])
            return sum