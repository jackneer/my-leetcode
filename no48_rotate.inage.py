def rotate(image):
    new_img = [[0 for x in range(len(image))] for y in range(len(image))]

    for row in range(len(image)):
        for col in range(len(image[row])):
            new_img[col][len(image) - 1 - row] = image[row][col]

    return new_img


def main():
    print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
    print(rotate([[ 5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))


if __name__ == '__main__':
    main()