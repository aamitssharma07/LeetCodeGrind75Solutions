new_head = None
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse(root):            
    new_head = None
    def reverse(root):            
        if(root.next==None):
            return root
        else:
            if(root.next.next==None):
                nonlocal new_head
                new_head = root.next
                root.next.next = root
                root.head = None
            else:
                reverse(root.next)
                root.next.next = root
                root.head = None
        return new_head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
x = reverse(head)
while(x!=None):
    print(x.val)
    x = x.next
    

