def combination_sum(nums, target):    
    combinations = divide(nums, target)

    for item in combinations:
        item.sort()
    
    for item in reversed(combinations):
        if combinations.count(item) > 1:
            combinations.remove(item)        

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
    print(combination_sum([2,3,6,7], 7))
    print(combination_sum([2,3,5], 8))


if __name__ == '__main__':
    main()