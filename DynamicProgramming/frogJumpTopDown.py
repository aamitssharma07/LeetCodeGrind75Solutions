#Top Down
def frogJump(index,HEIGHT,dp):    
    if(dp[index]!=-1):
        return dp[index]
    else:
        if(index == 0):
            return dp[index]
        elif(index==1):
            dp[index]=HEIGHT[0]
            
        else:
            oneStep = frogJump(index-1,HEIGHT,dp) + abs(HEIGHT[index-1]-HEIGHT[index-2])
            twoStep = frogJump(index-2,HEIGHT,dp) + abs(HEIGHT[index-1]-HEIGHT[index-3])
            
            dp[index] = min(oneStep,twoStep)
            
    print(dp)
    return dp[index]
def minEnergy(index,HEIGHT):
    dp = [-1]*(index+1) 
    return frogJump(index,HEIGHT,dp)  
    
HEIGHT = [10,12,20,15]  
dest_stair = 3 
print(minEnergy(dest_stair,HEIGHT))




