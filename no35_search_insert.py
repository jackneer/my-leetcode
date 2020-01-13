def search(nums, target):
    position = -1
    
    for i in range(len(nums)):        
        if nums[i] >= target:
            position = i
            break
    
    if position == -1:
        position = len(nums)

    return position


def main():    
    print(search([1,3,5,6], 5))
    print(search([1,3,5,6], 2))
    print(search([1,3,5,6], 7))
    print(search([1,3,5,6], 0))


if __name__ == '__main__':
    main()