def permutations(nums):
    if len(nums) > 2:
        all = []

        for i in range(len(nums)):
            temp = nums.copy()
            print(temp)
            temp.pop(i)
            temp = permutations(temp)

            for item in temp:
                item.insert(0, nums[i])
                all.append(item)

        return all
    else:
        return [[nums[0], nums[1]],[nums[1], nums[0]]]


def main():
    print(permutations([1, 2, 3]))


if __name__ == '__main__':
    main()