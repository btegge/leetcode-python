from typing import List


def maxArea(height: List[int]) -> int:
    areaMax = 0
    l = 0
    r = len(height) - 1
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        areaMax = max(areaMax, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return areaMax