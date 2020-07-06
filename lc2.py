class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = ListNode(0)
        flag = 0
        curr = r
        while 1:
            if l1 == None and l2 == None and flag == 0:
                return r.next

            if l1 == None:
                val1 = 0
            else:
                val1 = l1.val
            
            if l2 == None:
                val2 = 0
            else:
                val2 = l2.val

            val = val1 + val2 + flag
            flag = 0
            if val >= 10:
                val = val - 10
                flag = 1
            
            curr.next = ListNode(val)
            curr = curr.next

            if l1 != None:
                l1 = l1.next
            if  l2 != None:
                l2 = l2.next
a = Solution()

l1 = ListNode(9)

l2 = ListNode(9)

print(a.addTwoNumbers(l1, l2))