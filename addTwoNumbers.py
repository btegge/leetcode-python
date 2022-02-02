from typing import Optional
from ListNode import ListNode


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    output = ListNode()
    c = output
    c1 = l1
    c2 = l2
    remainder = 0
    while c1 or c2:
        c1v = 0 if not c1 else c1.val
        c2v = 0 if not c2 else c2.val
        cv = c1v + c2v + remainder
        remainder = 0 if cv < 10 else cv // 10
        c.val = cv if remainder == 0 else cv - (remainder * 10)
        c1 = None if not c1 else c1.next
        c2 = None if not c2 else c2.next
        if c1 or c2:
            c.next = ListNode()
            c = c.next

    if remainder > 0:
        c.next = ListNode()
        c = c.next
        c.val = remainder

    return output