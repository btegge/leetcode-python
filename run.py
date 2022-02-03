from twoSum import twoSum
from lengthOfLongestSubstring import lengthOfLongestSubstring
from addTwoNumbers import addTwoNumbers
from findMedianSortedArrays import findMedianSortedArrays
from longestPalindrome import longestPalindrome
from zigzagConversion import convert
from reverseInteger import reverse
from stringToInteger import myAtoi
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
    print()


def runAddTwoNumbers():
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    print("List1: " + listToString(l1))
    print("List2: " + listToString(l2))
    out = addTwoNumbers(makeLinkedList(l1), makeLinkedList(l2))
    print("Output: " + listToString(linkedListToList(out)))

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    print("List1: " + listToString(l1))
    print("List2: " + listToString(l2))
    out = addTwoNumbers(makeLinkedList(l1), makeLinkedList(l2))
    print("Output: " + listToString(linkedListToList(out)))
    print()


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
    print()


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
    print()


def runLongestPalindrome():
    s = "babad"
    print("Input: " + s)
    print("Output: " + longestPalindrome(0, s))
    s = "cbbd"
    print("Input: " + s)
    print("Output: " + longestPalindrome(0, s))
    s = "a"
    print("Input: " + s)
    print("Output: " + longestPalindrome(0, s))
    s = "bb"
    print("Input: " + s)
    print("Output: " + longestPalindrome(0, s))
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print("Input: " + s)
    print("Output: " + longestPalindrome(1, s))
    print()


def runZigzagConversion():
    s = "PAYPALISHIRING"
    numRows = 3
    print("Input String: " + s)
    print("Input numRows: {:d}".format(numRows))
    print("Output: " + convert(s, numRows))
    s = "PAYPALISHIRING"
    numRows = 4
    print("Input String: " + s)
    print("Input numRows: {:d}".format(numRows))
    print("Output: " + convert(s, numRows))


def runReverseInteger():
    x = 123
    print("Input: {:d}".format(x))
    print("Output: {:d}".format(reverse(0, x)))
    x = -123
    print("Input: {:d}".format(x))
    print("Output: {:d}".format(reverse(0, x)))
    x = -123
    print("Input: {:d}".format(x))
    print("Output: {:d}".format(reverse(1, x)))
    x = 120
    print("Input: {:d}".format(x))
    print("Output: {:d}".format(reverse(0, x)))
    x = 901000
    print("Input: {:d}".format(x))
    print("Output: {:d}".format(reverse(1, x)))
    x = 0
    print("Input: {:d}".format(x))
    print("Output: {:d}".format(reverse(1, x)))
    x = 1534236469
    print("Input: {:d}".format(x))
    print("Output: {:d}".format(reverse(1, x)))


def runStringToInteger():
    s = "42"
    print("Input: " + s)
    print("Output: {:d}".format(myAtoi(s)))
    s = "   -42"
    print("Input: " + s)
    print("Output: {:d}".format(myAtoi(s)))
    s = "4193 with words"
    print("Input: " + s)
    print("Output: {:d}".format(myAtoi(s)))
