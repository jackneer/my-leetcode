def trap(nums):

    start = -1
    end = -1
    toward = 0
    prev_toward = 0
    total = 0

    for index in range(1, len(nums)):
        prev_toward = toward

        if nums[index] > nums[index - 1]:
            toward = 1
        elif nums[index] < nums[index - 1]:
            toward = -1
        else:
            toward = 0
        
        if start != -1 and toward > 0:
            end = index

        if toward < 0 and start == -1:
            start = index - 1

        if start != -1 and end != -1 and prev_toward > 0 and toward <= 0:
            total += area_between(nums, start, end)

            # reset
            if toward == 0:
                start = -1
            elif toward < 0:
                start = index -1
            end = -1
        
    return total


def area_between(nums, start, end):
    height = 0
    total = 0

    if nums[start] <= nums[end]:
        height = nums[start]
    else:
        height = nums[end]

    for i in range(start + 1, end):
        total += height - nums[i]

    return total


def main():
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))


if __name__ == '__main__':
    main()