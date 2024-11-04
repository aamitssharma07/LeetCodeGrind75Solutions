#Top Down        
def giveFabonaciTopDown(index):
    def fab(n):
        if(n==1):
            return 1
        elif(n==0):
            return 0
        else:
            if(dp[n]==-1):#This condition will chekc if the that function call is already computed or not
                dp[n] = fab(n-1) + fab(n-2) #This will store the result into the arrau so that we don't have to compute again
                return dp[n]
            else:
                return dp[n]
    dp = [-1]*(index+1)
    return fab(index)


#Buttom Up with Space Complexity O(n) and TC = O(n)
def giveFabonacciButtomUp(index):
    dp = [-1]*(index+1)
#Initialize the value with the base case
    dp[0]=0  
    dp[1]=1
    for index  in range(2,index+1):
        dp[index]  = dp[index-1]  + dp[index-2]
    return dp[index]    

#Reducing spcae complexity to O(1)
def giveOptimizedFabonacciButtomUp(index):
    nextPrev = 0
    prev = 1
    for index  in range(2,index+1):
        curr  = nextPrev + prev
        nextPrev = prev
        prev = curr 
    return curr 

print(giveFabonaciTopDown(5))

print(giveFabonacciButtomUp(5))

print(giveOptimizedFabonacciButtomUp(5))

