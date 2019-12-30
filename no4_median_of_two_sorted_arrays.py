def find_median(nums1, nums2):

    merged = []

    while len(nums1) > 0 or len(nums2) > 0:
        if len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] < nums2[0]:
                merged.append(nums1.pop(0))
            elif nums1[0] > nums2[0]:
                merged.append(nums2.pop(0))
            else:                
                merged.append(nums1.pop(0))
                merged.append(nums2.pop(0))
        elif len(nums1) > 0:
            merged.append(nums1.pop(0))
        elif len(nums2) > 0:
            merged.append(nums2.pop(0))

    if len(merged) % 2 == 0:
        mid_index = int(len(merged) / 2)
        return (merged[mid_index - 1] + merged[mid_index]) / 2
    else:
        mid_index = int((len(merged) + 1) / 2) - 1
        return merged[mid_index]


def main():
    nums1 = [1, 3]
    nums2 = [2]
    median = find_median(nums1, nums2)
    print(median)

    nums1 = [1, 2]
    nums2 = [3, 4]
    median = find_median(nums1, nums2)
    print(median)
    pass


if __name__ == '__main__':
    main()