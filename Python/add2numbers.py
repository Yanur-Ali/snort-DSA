class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        return_list = ListNode()
        head = return_list
        carry = 0
        
        while l1 or l2 or carry:
            curr_sum = 0
            if l1:
                curr_sum += l1.val
                l1 = l1.next
            if l2:
                curr_sum += l2.val
                l2 = l2.next
            curr_sum += carry
            carry = curr_sum // 10
            return_list.next = ListNode(curr_sum % 10)
            return_list = return_list.next
        
        return head.next
