def twoSum(self, nums: List[int], target: int) -> List[int]:
    half = len(nums) // 2
    for x in range(0, half):
        for y in range(x + 1, len(nums) - 1):
            if nums[x] + nums[y] == target:
                return [x, y]

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()