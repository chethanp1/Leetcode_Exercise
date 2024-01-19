# 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head  # Initialize the slow pointer to the head of the linked list
        fast_pointer = head  # Initialize the fast pointer to the head of the linked list
        while fast_pointer and fast_pointer.next:  # Traverse the linked list until the fast pointer reaches the end or a cycle is detected
            slow_pointer = slow_pointer.next  # Move the slow pointer one step forward
            fast_pointer = fast_pointer.next.next  # Move the fast pointer two steps forward
            if slow_pointer == fast_pointer:  # If the slow pointer and the fast pointer meet, there is a cycle
                return True
        return False  # If the fast pointer reaches the end of the linked list, there is no cycle