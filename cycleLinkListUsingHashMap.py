# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(not head or not head.next ):
            return False
        elif(head.next==head):
            return True
        else:
            head1 = head
            hashMap = {}
            #Fill the values in hash map, where address is the key and value of node is the value. Before putting the value if the key exists means that the adress is already there so there is the circle in link list
            while(hashMap.get(id(head1)) == None and head1 != None):
                hashMap[id(head1)]= head1.val
                head1 = head1.next
            if(head1 == None):
                return False
            else:
                return True

            

