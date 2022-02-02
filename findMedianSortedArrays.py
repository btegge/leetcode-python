from typing import List


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
