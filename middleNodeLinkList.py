class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        
#Hare and Tortoise Algo
def findMiddle(list):
    if(not list or not list.next or not list.next.next):
        print("Size is less than 3, can't have middle element")
    else:  
        slow = list
        fast = list  
        while(fast != None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next  
        if(fast == None):
            print("String is even, ccan't have a middle node")
        else:
            print(f"Middle node is {slow.value}")

linkList = Node(1)
linkList.next = Node(2)
linkList.next.next = Node(3)
linkList.next.next.next = Node(12)
findMiddle(linkList)





    