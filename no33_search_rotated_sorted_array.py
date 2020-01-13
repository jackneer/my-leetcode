def search(nums, target):
    direction = 1
    
    if target < nums[0]:
        direction = -1
    
    index = 0
    match = -1
    
    for i in range(len(nums)):
        if direction == 1:
            index = i
        else:
            index = len(nums) - 1 - i
    
        if nums[index] == target:
            match = index
            break

    return match

def main():    
    print(search([4,5,6,7,0,1,2], 0))
    print(search([4,5,6,7,0,1,2], 3))


if __name__ == '__main__':
    main()