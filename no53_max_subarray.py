def max_subarray(nums):
    n = len(nums)
    max = None

    for i in range(n):
        for length in range(2, n + 1):
            temp = nums[i:length]

            if len(temp) >= 2:
                total = sum(temp)

                if max is None:
                    max = total
                else:
                    if total > max:
                        max = total

    return max
    

def main():
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))


if __name__ == '__main__':
    main()