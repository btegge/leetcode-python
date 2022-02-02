from typing import List


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
    outstr = "["
    out = twoSum(1, [3, 2, 4], 6)
    outstr += "{:d}".format(out[0])
    outstr += ","
    outstr += "{:d}".format(out[1])
    outstr += "]"
    print(outstr)
    outstr = "["
    out = twoSum(0, [3, 2, 4], 6)
    outstr += "{:d}".format(out[0])
    outstr += ","
    outstr += "{:d}".format(out[1])
    outstr += "]"
    print(outstr)


def main():
    # Two Sum
    runTwoSum()


if __name__ == "__main__":
    main()
