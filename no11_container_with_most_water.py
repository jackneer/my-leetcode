def max_area(nums):
    max_area_val = 0

    for left_index in range(0, len(nums) - 1):
        for right_index in range (left_index + 1, len(nums)):
            area = min(nums[left_index], nums[right_index]) * (right_index - left_index)
            if area > max_area_val:                
                max_area_val = area

    return max_area_val


def min(a, b):
    if a < b:
        return a
    else:
        return b


def main():    
    print(max_area([1,8,6,2,5,4,8,3,7]))


if __name__ == '__main__':
    main()