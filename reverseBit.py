# class Solution:
#     def reverseBits(self, n: int) -> int:
       
#         #Convert into use two pointer for reversing but string is immutable. Or push every element into stack,keep poping and convert them into decimal
 
#         #Convert into string
n = 10
x = bin(10) #bin will give the string
n = bin(n)[2:].zfill(32) #zfill function will do the padding
print(n)
n = [int(bit) for bit in n]
count = 0
reverse_decimal = 0
#This will take the elements from the start and convert into binnary which is same likreversing the number and converting into binnary
while(len(n)):
   reverse_decimal = reverse_decimal +  n.pop(0)* 2** count
   count+=1
# return reverse_decimal
print(reverse_decimal)