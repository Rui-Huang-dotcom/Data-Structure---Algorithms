from typing import List

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


l1=ListNode(1,2)
l2=ListNode(1,3)
a=Solution()
a.mergeTwoLists(l1,l2)
# print(l1.next)
# print(l2.next)
# l1=ListNode(2)
# l2=ListNode(3)
# a.mergeTwoLists(l1,l2)
# l1=ListNode(4)
# l2=ListNode(4)
# a.mergeTwoLists(l1,l2)


print(l1.val)