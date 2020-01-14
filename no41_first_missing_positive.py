def first_missing_positive(nums):
    nums.sort()

    current = 1
    found = False
    index = 0

    while not found:
        if index >= len(nums) or nums[index] > current:
            found = True

        elif nums[index] < current:
            index += 1

        elif nums[index] == current:
            current += 1

    return current


def main():
    print(first_missing_positive([1,2,0]))
    print(first_missing_positive([3,4,-1,1]))
    print(first_missing_positive([7,8,9,11,12]))


if __name__ == '__main__':
    main()