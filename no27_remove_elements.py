def remove_elements(nums, val):    
    encounter = False

    for i in reversed(range(0, len(nums))):
        if not encounter and nums[i] != val:
            nums.pop(i)
        elif nums[i] == val:
            encounter = True
            nums.pop(i)

    return len(nums)


def main():
    print(remove_elements([3,2,2,3], 3))
    print(remove_elements([0,1,2,2,3,0,4,2], 2))
    pass


if __name__ == '__main__':
    main()