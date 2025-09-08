# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # main issue: think about how to handle the carry value when we get to the end of one of the      lists without repeating parts of the code

        res = ListNode()
        dummy = res
        carry = 0
        while l1 or l2:
            if l1 and l2:
                added = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif not l1:
                added = l2.val + carry
                l2 = l2.next
            else:
                added = l1.val + carry
                l1 = l1.next

            val = added % 10
            carry = added // 10

            node = ListNode(val)
            res.next = node
            res = res.next

        if carry != 0:
            res.next = ListNode(carry)
        
        return dummy.next