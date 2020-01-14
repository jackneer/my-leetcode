def combination_sum(nums, target):    
    combinations = divide(nums, target)

    for item in combinations:
        item.sort()
    
    for item in reversed(combinations):
        if combinations.count(item) > 1:
            combinations.remove(item)

    for item in nums:
        count = nums.count(item)
        for combination in reversed(combinations):
            count_combination = combination.count(item)

            if count_combination > count:
                combinations.remove(combination)

    return combinations


def divide(nums, target):
    all = []

    if target in nums:
        all.append([target])
    
    for i in range(1, int(target / 2) + 1):
        if i in nums:            
            temp = divide(nums, target - i)            
            for item in temp:
                item.append(i)
                all.append(item)

    return all


def main():
    print(combination_sum([10,1,2,7,6,1,5], 8))
    print(combination_sum([2,5,2,1,2], 5))


if __name__ == '__main__':
    main()