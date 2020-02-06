def jump(nums):
    if len(nums) == 1:
        return 0
    else:
        temp = []

        for i in range(1, nums[0] + 1):           
            temp.append(jump(nums[i:]))

        return min(temp) + 1


def main():
    print(jump([2,3,1,1,4]))


if __name__ == '__main__':
    main()