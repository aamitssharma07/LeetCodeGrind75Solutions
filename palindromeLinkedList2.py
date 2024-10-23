# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Function to reverse the linked list from a given node
        def reverse(root):            
            if(root.next == None):  # If the list has only one element, return the root
                return root
            else:
                prev = None
                current = root
                nex = current.next  # Keep track of the next node
                
                # Iterate through the list and reverse the links
                while(current != None):
                    current.next = prev  # Reverse the current node's pointer
                    prev = current       # Move 'prev' to the current node
                    current = nex        # Move to the next node
                    if(nex):             # If there is a next node, move nex forward
                        nex = nex.next
            return prev  # Return the new head of the reversed list

        # Function to check if the length of the linked list is even or odd
        def checkEven(root):
            count = 0
            while(root != None):  # Count the total number of nodes
                count += 1
                root = root.next
            # Return True if the count is even, otherwise False
            return count % 2 == 0

        # If the linked list has only one node, it's a palindrome by default
        if(head.next == None):
            return True
        else:
            # If the list has an even number of nodes, start 'fast' at the second node
            if(checkEven(head)):
                slow = head
                fast = head.next
            else:  # If the list has an odd number of nodes, start both 'slow' and 'fast' at head
                slow = head
                fast = head                            
            
            first_half_start = head  # Pointer to the start of the list
            
            # Move 'slow' to the middle and 'fast' to the end of the list
            while(fast.next != None):
                slow = slow.next
                fast = fast.next.next
            
            # Reverse the second half of the list
            nexthalf_start = reverse(slow.next)
            first_half_start = head
            slow.next = nexthalf_start  # Point the end of the first half to the reversed second half
            
            # Compare the values from the first half and the reversed second half
            while(nexthalf_start != None):
                if(first_half_start.val != nexthalf_start.val):  # If values don't match, not a palindrome
                    return False
                else:
                    first_half_start = first_half_start.next
                    nexthalf_start = nexthalf_start.next

            # Restore the original list structure by reversing the second half back
            slow.next = reverse(slow.next)
        
        return True  # If all values matched, it's a palindrome
