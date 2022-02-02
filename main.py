from typing import List, Optional


def listToString(l1: List[int]) -> str:
    pstring = "["
    for i, value in enumerate(l1):
        pstring += "{:d}".format(value)
        if i < len(l1) - 1:
            pstring += ", "
    pstring += "]"
    return pstring


def twoSum(vers: int, nums: List[int], target: int) -> List[int]:
    # Trivial Solution
    if vers == 1:
        for x in range(0, len(nums) - 1):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x, y]
        return [0, 0]
    # Fast Solution
    else:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in seen:
                return [i, seen[remaining]]
            seen[value] = i


def runTwoSum():
    inList = [3, 2, 4]
    target = 6
    print("twoSum Trivial Solution:")
    print("List: " + listToString(inList))
    print("Target: {:d}".format(target))
    out = twoSum(1, inList, target)
    print("Output: " + listToString(out))
    print("twoSum Fast Solution:")
    print("List: " + listToString(inList))
    print("Target: {:d}".format(target))
    out = twoSum(0, inList, target)
    print("Output: " + listToString(out))


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linkedListToList(ll: ListNode) -> List[int]:
    listOut =[]
    c = ll
    while c is not None:
        listOut.append(c.val)
        c = c.next
    return listOut


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


def makeLinkedList(ll: List[int]) -> ListNode:
    listOut = None
    c = listOut
    for x in ll:
        if c is None:
            c = ListNode()
            listOut = c
        else:
            c.next = ListNode()
            c = c.next
        c.val = x
    return listOut


def runAddTwoNumbers():
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    print("addTwoNumbers Solution:")
    print("List1: " + listToString(l1))
    print("List2: " + listToString(l2))
    out = addTwoNumbers(makeLinkedList(l1), makeLinkedList(l2))
    print("Output: " + listToString(linkedListToList(out)))

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    print("addTwoNumbers Solution:")
    print("List1: " + listToString(l1))
    print("List2: " + listToString(l2))
    out = addTwoNumbers(makeLinkedList(l1), makeLinkedList(l2))
    print("Output: " + listToString(linkedListToList(out)))


def main():
    # Two Sum
    runTwoSum()
    runAddTwoNumbers()


if __name__ == "__main__":
    main()
