def search(nums, target):
    direction = 1
    
    if target < nums[0]:
        direction = -1
    
    index = 0
    match = []
    
    for i in range(len(nums)):
        if direction == 1:
            index = i
        else:
            index = len(nums) - 1 - i

        if nums[index] == target:
            if len(match) == 2:
                match.pop(1)

            match.append(index)
    
    if len(match) == 0:
        match = [-1, -1]
    elif len(match) == 1:
        match.append(match[0])            

    return match


def main():    
    print(search([5,7,7,8,8,10], 8))
    print(search([5,7,7,8,8,10], 6))


if __name__ == '__main__':
    main()