

#Using loop
def fabonacciUsingLoop(n):
    if(n==1):
        list = [1]
    elif(n==2):
        list = [1,2]
    elif(n==3):
        list = [1,2,3]
        
    else:
        list = [1,2,3]
        while(len(list)<n):
            list.append(list[len(list)-1]+list[len(list)-2])
    
    return list

#Using Recurssion
def fabonacciUsingRecurssion(n):
    if(n <=1):
        return 1
    else:
        return fabonacciUsingRecurssion(n-1) + fabonacciUsingRecurssion(n-2)
        
    
    

n = 5   
print(fabonacciUsingLoop(n))

for value in range(1,n+1):
    print(fabonacciUsingRecurssion(value))
    