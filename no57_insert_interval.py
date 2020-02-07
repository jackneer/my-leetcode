def insert(nums, new_nums):
    inserted = False

    for i in range(len(nums)):
        if nums[i][0] >= new_nums[0]:
            nums.insert(i, new_nums)
            inserted = True
            break
        
    if not inserted:
        nums.append(new_nums)

    remove_index = []

    for i in range(len(nums)):    
        if i not in remove_index:
            for j in range(i + 1, len(nums)):
                if nums[j][0] >= nums[i][0] and nums[j][0] <= nums[i][1]:
                    if nums[j][1] > nums[i][1]:
                        nums[i][1] = nums[j][1]
                    
                    remove_index.append(j)

    sorted(remove_index)

    for item in reversed(remove_index):
        nums.remove(nums[item])

    return nums


def main():
    print(insert([[1,3],[6,9]], [2,5]))
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))


if __name__ == '__main__':
    main()