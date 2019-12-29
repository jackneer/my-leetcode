def two_sum(nums, target):
    for i in range(0, len(nums) - 1):
        for j in range(i, len(nums)):
            sum = nums[i] + nums[j]
            if target == sum:
                return [nums[i], nums[j]]
    return None

def main():
    nums = [2, 7, 12, 8]
    target = 9
    result = two_sum(nums, target)
    print(result)
    pass

if __name__ == '__main__':
    main()