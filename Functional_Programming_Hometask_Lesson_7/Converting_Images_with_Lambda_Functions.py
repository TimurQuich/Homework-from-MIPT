import Traversing_an_Image as tr

from functools import partial

# Lambda Functions

pixel_rgb_to_gray = lambda p: int(0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2])

image_rgb_to_gray = lambda img: [list(map(pixel_rgb_to_gray, row)) for row in img]


def get_local_area(img, a, b, kernel_size):
    half = kernel_size // 2
    for i in range(-half, half + 1):
        for j in range(-half, half + 1):
            yield img[a + i][b + j]


def convolution(kernel, img, a, b):
    kernel_size = int(len(kernel) ** 0.5)
    local_area_stream = get_local_area(img, a, b, kernel_size)
    return sum(w * v for w, v in zip(kernel, local_area_stream))

# Partial Application

box_kernel = [1 / 9] * 9 # kernel: 3x3
box_blur = partial(convolution, box_kernel)

gaussian_kernel = [
    1/16, 2/16, 1/16,
    2/16, 4/16, 2/16,
    1/16, 2/16, 1/16
]

box_gaussian = partial(convolution, gaussian_kernel)

# MSE

calculate_mse = lambda img1, img2: sum(
    (p1 - p2) ** 2 for row1, row2 in zip(img1, img2) for p1, p2 in zip(row1, row2)
) / (len(img1) * len(img1[0]))


# Auxiliary Function

def filter_by_traj(img, filter_func, kernel_size, traverse_func):
    m = len(img)
    n = len(img[0])
    half = kernel_size // 2

    coord_arr = [[(i, j) for j in range(n)] for i in range(m)]

    filtered_img = [[img[i][j] for j in range(n)] for i in range(m)]

    for i, j in traverse_func(coord_arr):

        if half <= i < m - half and half <= j < n - half:
            filtered_img[i][j] = int(filter_func(img, i, j))

    return filtered_img

# Test

if __name__ == '__main__':

    color_img = [
        [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0]],
        [[100, 100, 100], [50, 150, 250], [80, 80, 80], [0, 0, 0]],
        [[200, 50, 10,], [30, 90, 120], [255, 255, 255], [120, 120, 120]],
        [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]]
    ]

    print("Converting RGB to Gray")
    gray_img = image_rgb_to_gray(color_img)
    for row in gray_img:
        print(row)

    print()

    test_img = [
        [10, 80, 30, 40],
        [50, 10, 100, 80],
        [90, 3, 11, 120],
        [130, 140, 150, 160]
    ]

    print("Linear Filtration")
    res_linear = filter_by_traj(
        test_img, box_gaussian, 3, tr.linearly_traverse
    )
    for row in res_linear:
        print(row)

    print()

    print("Zig-Zag Filtration")
    res_zig_zag = filter_by_traj(
        test_img, box_gaussian, 3, tr.zig_zag_traverse
    )

    for row in res_zig_zag:
        print(row)

    print()

    mse = calculate_mse(res_linear, res_zig_zag)
    print("MSE:", mse)
