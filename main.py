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


def lengthOfLongestSubstring(s: str) -> int:
    length = 0
    candidate = ""
    candLen = 0
    for i, char in enumerate(s):
        if char not in candidate:
            candidate += char
            candLen += 1
        else:
            if candLen > length:
                length = candLen
            while char in candidate:
                candLen -= 1
                candidate = candidate[1:]
            candidate += char
            candLen += 1
    return candLen if candLen > length else length


def runLengthOfLongestSubstring():
    s = "abcabcbb"
    print("String: " + s)
    print("Length of longest substring: {:d}".format(lengthOfLongestSubstring(s)))
    s = "bbbbb"
    print("String: " + s)
    print("Length of longest substring: {:d}".format(lengthOfLongestSubstring(s)))
    s = "pwwkew"
    print("String: " + s)
    print("Length of longest substring: {:d}".format(lengthOfLongestSubstring(s)))


def recursiveFMSA(nums1: List[int], nums2: List[int]) -> float:
    if len(nums2) < len(nums1):
        return recursiveFMSA(nums2, nums1)
    n1 = len(nums1)
    n2 = len(nums2)
    lo = 0
    hi = n1
    while lo <= hi:
        cut1 = (lo + hi) // 2
        cut2 = (n1 + n2 + 1) // 2 - cut1
        left1 = -1e6 if cut1 == 0 else nums1[cut1 - 1]
        left2 = -1e6 if cut2 == 0 else nums2[cut2 - 1]
        right1 = 1e6 if cut1 == n1 else nums1[cut1]
        right2 = 1e6 if cut2 == n2 else nums2[cut2]
        if left1 <= right2 and left2 <= right1:
            if (n1 + n2) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2
            else:
                return max(left1, left2)
        elif left1 > right2:
            hi = cut1 - 1
        else:
            lo = cut1 + 1
    return 0


def findMedianSortedArrays(vers: int, nums1: List[int], nums2: List[int]) -> float:
    # Trivial Solution
    if vers == 0:
        merged = []
        l1p = 0
        l2p = 0
        while l1p != len(nums1) and l2p != len(nums2):
            if nums1[l1p] < nums2[l2p]:
                min = nums1[l1p]
                l1p += 1
            else:
                min = nums2[l2p]
                l2p += 1
            merged.append(min)
        if l1p < len(nums1):
            merged.extend(nums1[l1p:])
        else:
            merged.extend(nums2[l2p:])
        medpos = len(merged) // 2
        return (merged[medpos - 1] + merged[medpos]) / 2 if len(merged) % 2 == 0 else merged[medpos]
    # Recursive Solution
    else:
        return recursiveFMSA(nums1, nums2)


def runFindMedianSortedArrays():
    nums1 = [1, 3]
    nums2 = [2]
    print("Array1: " + listToString(nums1))
    print("Array2: " + listToString(nums2))
    print("Median: {:f}".format(findMedianSortedArrays(0, nums1, nums2)))

    nums1 = [1, 2]
    nums2 = [3, 4]
    print("Array1: " + listToString(nums1))
    print("Array2: " + listToString(nums2))
    print("Median: {:f}".format(findMedianSortedArrays(1, nums1, nums2)))


def main():
    runTwoSum()
    runAddTwoNumbers()
    runLengthOfLongestSubstring()
    runFindMedianSortedArrays()


if __name__ == "__main__":
    main()
