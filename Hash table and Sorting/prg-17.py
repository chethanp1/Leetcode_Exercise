# 21. Merge Two Sorted Lists
# # You are given the heads of two sorted linked lists list1 and list2.
# # Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# # Return the head of the merged linked list.

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()  # Create a dummy head node for the merged list
        current = head  # Initialize a pointer to the current node
        while list1 and list2:
            if list1.val < list2.val:  # Compare the values of the first nodes of the input lists
                current.next = list1  # Add the smaller node to the merged list
                list1 = list1.next  # Move the pointer of the input list that contributed the smaller node
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move the pointer of the merged list to the last added node

        current.next = list1 or list2  # Add the remaining nodes of the non-empty input list to the merged list
        return head.next  # Return the merged list, skipping the dummy head node