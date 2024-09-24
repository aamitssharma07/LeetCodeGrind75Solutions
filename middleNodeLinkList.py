# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # BrutForce
        # head2 = head
        # count1 = 0
        # count2 = 1
        # while(head2):
        #     count1+=1
        #     head2 = head2.next
            

        # head2 = head
        # if(count1%2==0): #Length is even then there are two middle nodes 
            
        #     while(count2!=count1//2):
        #         count2+=1
        #         head2 = head2.next
        #     return head2.next
        # else:#Length is odd then ythere is single middle node
        #     while(count2!=  (count1/2)+0.5):
        #         head2 = head2.next
        #         count2+=1
        #     return head2


    #Another approach is Kaydan's Algo
        slow = head
        fast = head.next
        while(fast!=None and fast.next!=None):
            slow= slow.next
            fast = fast.next.next
        if(fast==None):
            return slow
        else:
            return slow.next
            