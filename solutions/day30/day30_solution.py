# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        Add two numbers represented as reversed linked lists.
        Return the sum as a linked list.
        """
        dummy = ListNode(0)   # Dummy node to simplify logic
        curr = dummy
        carry = 0

        # Traverse both lists until both are None and no carry left
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            # Advance pointers
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next   # Head of the result list
