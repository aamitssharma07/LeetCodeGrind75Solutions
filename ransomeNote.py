class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(len(ransomNote)>len(magazine)):
            return False
        else:
            ransomDict = {}
            magazineDict = {}

            #Defining dictionary to count number of particular character in ransomNote
            for char in ransomNote:
                if(ransomDict.get(char)!=None):
                    ransomDict[char] = ransomDict.get(char)+1
                else:
                    ransomDict[char] = 1
            #Defining dictionary to count number of particular character in magazine
            for char in magazine:
                if(magazineDict.get(char)!=None):
                    magazineDict[char] = magazineDict.get(char)+1
                else:
                    magazineDict[char] = 1            

            #If ransomDict is a subset of magazineDict, then staring  ransomNote can be coinstructed by magazine

            for key in ransomDict:
                #This condition is important and magazineDict.get(key)!=None will take care if it's none, otherwise will get error if we comapre none with int 
                if(magazineDict.get(key)!=None and  (ransomDict.get(key)==magazineDict.get(key) or ransomDict.get(key)<=magazineDict.get(key))):
                    pass
                else:
                    return False
            return True
