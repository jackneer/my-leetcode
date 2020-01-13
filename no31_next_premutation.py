def next_premutation(nums):
    print(nums)
    done = False
    
    for i in reversed(range(len(nums) - 1)):
        if nums[i] < nums[i + 1]:
            temp = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = temp
            done = True
            break

    if not done:
        for i in range(int(len(nums) / 2)):
            temp = nums[i]
            nums[i] = nums[len(nums) - 1 - i]
            nums[len(nums) - 1 - i] = temp

    return nums


def main():
    print(next_premutation([1, 2, 3]))
    print(next_premutation([3, 2, 1]))
    print(next_premutation([1, 1, 5]))


if __name__ == '__main__':
    main()