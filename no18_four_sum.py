def four_sum(nums, target):
    result = []
    check_sums = []

    for i in range(0, len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            for k in range( j + 1, len(nums) - 1):
                for l in range( k + 1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    check_sum = abs(nums[i]) + abs(nums[j]) + abs(nums[k]) + abs(nums[l])

                    if sum == target and check_sum not in check_sums:
                        result.append([nums[i],  nums[j],  nums[k],  nums[l]])
                        check_sums.append(check_sum)

    return result


def main():
    print(four_sum([1, 0, -1, 0, -2, 2], 0))


if __name__ == '__main__':
    main()