# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if( head == None or head.next==None):#Handles if there is no node, single node that is pointing to none
            return False
        else:
            slow =  head
            fast = head.next
            while(fast != slow and fast!=None and fast.next!=None):#This handles that if there is no loop or loop
                fast = fast.next.next
                slow = slow.next
            if(fast == slow):
                return True
            else:
                return False
            
linkList = ListNode(4)
linkList.next = ListNode(5)
linkList.next.next = linkList
isCyclic = Solution()
print(isCyclic.hasCycle(linkList))