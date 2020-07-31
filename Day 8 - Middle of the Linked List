'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Ex:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
'''

# Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        val = head
        if val is None:
            return []
        place = 0
        while val is not None:
            if val is not None:
                value = val.val
            val = val.next
            place += 1
            
        # place is the length of the list
        # middle node is place//2 + 1
        
        app_val = head
        counter = 1
        goal = place//2 + 1
        
        while app_val is not None:
            if counter == goal:
                return app_val
            app_val = app_val.next
            counter += 1
