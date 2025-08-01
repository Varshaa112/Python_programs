#Given a linked list, if there is a cycle, return the node where the cycle begins.If there is no cycle, return None.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return slow
