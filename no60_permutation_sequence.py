def permutation_sequence(n, k):
    temp = permutations(list(range(1, n + 1)))

    if k <= len(temp):
        return ''.join(str(x) for x in temp[k - 1])
    else:
        return None


def permutations(nums):
    if len(nums) > 2:
        all = []

        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            temp = permutations(temp)

            for item in temp:
                item.insert(0, nums[i])
                all.append(item)

        return all
    else:
        return [[nums[0], nums[1]],[nums[1], nums[0]]]


def main():
    print(permutation_sequence(3, 3))
    print(permutation_sequence(4, 9))


if __name__ == '__main__':
    main()