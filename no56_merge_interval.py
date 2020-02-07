def merge(nums):
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
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
    print(merge([[1,4],[4,5]]))


if __name__ == '__main__':
    main()