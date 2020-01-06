def three_sum(nums):
    check_sums = []
    result = []

    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range( j + 1, len(nums)):                
                sum = nums[i] + nums[j] + nums[k]
                check_sum = abs(nums[i]) + abs(nums[j]) + abs(nums[k])
                temp = [nums[i], nums[j], nums[k]]
                
                if sum == 0 and check_sum not in check_sums:
                    result.append(temp)
                    check_sums.append(check_sum)

    return result


def main():
    print(three_sum([-1, 0, 1, 2, -1, -4]))


if __name__ == '__main__':
    main()