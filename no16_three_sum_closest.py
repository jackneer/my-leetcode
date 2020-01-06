def three_sum_closest(nums, target):
    result = 0
    min_d = -1

    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range( j + 1, len(nums)):                
                sum = nums[i] + nums[j] + nums[k]

                d = abs(sum - target)

                if min_d < 0 or d < min_d:
                    min_d = d
                    result = sum

    return result


def main():
    print(three_sum_closest([-1, 2, 1, -4], 1))


if __name__ == '__main__':
    main()