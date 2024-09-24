# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#Recursiev Approach and it be done in O(n) time        
        new_head = None
        def reverse(head):
            nonlocal new_head
            if(head.next==None):
                new_head = head
                return 
            else:
                reverse(head.next)
                head.next.next = head

        if(head!=None):
            reverse(head)
            head.next = None    
        return new_head
#******************Iterative***************************

            # if(head == None or head.next== None):
            #     return head
            # else:
            #     head1 = head
            #     temp1 = head1.next
            #     temp2 = head1.next.next
            #     while(temp2!=None):
            #         temp1.next=head1
            #         head1 = temp1
            #         temp1 = temp2
            #         temp2 = temp2.next
            #     temp1.next = head1
            #     head.next = None
            #     return temp1