#https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1

class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def getMiddle(self, head):
        # Code here
        # return the value stored in the middle node
        fast=head
        slow=head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        if fast.next and fast.next.next==None:
            slow=slow.next
        return slow.data
