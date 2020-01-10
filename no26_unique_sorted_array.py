def unique_sorted(nums):
    for i in reversed(range(1, len(nums))):
        if nums[i] == nums[i -1]:
            nums.pop(i)

    return len(nums)


def main():
    print(unique_sorted([1,1,2]))
    print(unique_sorted([0,0,1,1,1,2,2,3,3,4]))
    pass


if __name__ == '__main__':
    main()