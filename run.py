from twoSum import twoSum
from lengthOfLongestSubstring import lengthOfLongestSubstring
from addTwoNumbers import addTwoNumbers
from findMedianSortedArrays import findMedianSortedArrays
from typing import List
from ListNode import ListNode


def listToString(l1: List[int]) -> str:
    pstring = "["
    for i, value in enumerate(l1):
        pstring += "{:d}".format(value)
        if i < len(l1) - 1:
            pstring += ", "
    pstring += "]"
    return pstring


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


def linkedListToList(ll: ListNode) -> List[int]:
    listOut =[]
    c = ll
    while c is not None:
        listOut.append(c.val)
        c = c.next
    return listOut


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