#Top Down
def frogJump(index,HEIGHT,dp):    
    if(dp[index]!=-1):
        return dp[index]
    else:
        #Base Cases
        dp[0]=0
        dp[1]=abs(HEIGHT[1]-HEIGHT[0])
        stair = 3
        while(stair<=index):
            dp[stair-1]=abs(HEIGHT[stair-1]- HEIGHT[stair-2])
            stair +=1
        return dp[index-1]
#The space complexity of above function is O(n)    
def op

def minEnergy(index,HEIGHT):
    dp = [-1]*index  
    return frogJump(index,HEIGHT,dp)  
    
HEIGHT = [10,20,15,10]   
print(minEnergy(len(HEIGHT),HEIGHT))




