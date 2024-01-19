# 2. Add Two Numbers
# # You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# #
# # You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Create a new linked list to store the sum
        head = ListNode()
        current = head
        carry = 0
        # Iterate through the lists and the carry
        while (l1 != None or l2 != None or carry != 0):
            # Get the value of each node, or 0 if the node is None
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            # Calculate the total sum and the new carry
            total = l1_value + l2_value + carry
            current.next = ListNode(total % 10)  # Add a new node with the units digit of the sum
            carry = total // 10  # Update the carry for the next iteration
            # Move to the next nodes in the input lists and the result list
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
        # Return the new linked list, skipping the dummy head node
        return head.next