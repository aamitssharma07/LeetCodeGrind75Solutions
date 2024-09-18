input_array = [-1, 4 ,6 ,-4, 12, 5 , 6]
max_sum = -float("inf")
current_sum = 0
for value in input_array:
    current_sum = current_sum + value
    max_sum = max (max_sum,current_sum)
    if(current_sum > 0):
        pass
    else:
        current_sum = 0
print(max_sum)
        
    
        
            
            
        
        
        

    
    
