def jump(nums):
    if len(nums) == 1:
        return True
    else:
        temp = []

        for i in range(1, nums[0] + 1):           
            temp.append(jump(nums[i:]))

        if len(temp) <= 0:
            return False
        else:
            if True in temp:
                return True
            else:
                return False


def main():
    print(jump([2,3,1,1,4]))
    print(jump([3,2,1,0,4]))


if __name__ == '__main__':
    main()