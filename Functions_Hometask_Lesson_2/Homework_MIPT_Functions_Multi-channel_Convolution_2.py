def dec_multi_channel_convolution(func):
    def wrapper(image, kernel):
        M = len(image)
        N = len(image[0])
        channels = len(image[0][0])
        result = [[[0] * channels for _ in range(N)] for _ in range(M)]
        for k in range(channels):
            image_upd = [[0] * N for _ in range(M)]
            for i in range(M):
                for j in range(N):
                    image_upd[i][j] = image[i][j][k]
            inter_result = func(image_upd, kernel)
            for i in range(M):
                for j in range(N):
                    result[i][j][k] = inter_result[i][j]
        return result
    return wrapper


@dec_multi_channel_convolution
def convolution_2D(matrix, kernel):
    M = len(matrix)
    N = len(matrix[0])

    result = [[0] * N for _ in range(M)]

    # Expanding an initial matrix
    K = len(kernel)
    pad = K // 2

    matrix_upd = [[0] * (N + 2 * pad) for _ in range(M + 2 * pad)]
    for i in range(pad, M + pad):
        for j in range(pad, N + pad):
            matrix_upd[i][j] = matrix[i-pad][j-pad]


    for i in range(M):
        for j in range(N):
            s = 0
            for i_1 in range(K):
                for j_1 in range(K):
                    s += matrix_upd[i+i_1][j+j_1] * kernel[i_1][j_1]
            result[i][j] = s
    return result


image = [
    [[255, 0, 0], [0, 5, 0], [0, 255, 0]],
    [[255, 0, 0], [40, 155, 0], [0, 255, 0]],
    [[255, 0, 0], [32, 255, 0], [23, 255, 0]],
    [[255, 0, 0], [0, 255, 0], [0, 255, 0]],
    [[255, 0, 0], [23, 215, 43], [12, 255, 0]]
]

kernel = [
    [0, 1, 2],
    [4, 2, 1],
    [9, 10, 11]
]

# This kernel for checking

# kernel = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

for row in convolution_2D(image, kernel):
    print(*row)
