import copy
from random import random

def create_vector(N):
    vector = [round(random(), 3) for _ in range(N)]
    return vector


def create_matrix(M, N):
    matrix = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            matrix[i][j] = round(random(), 3)
    return matrix


def multiply_m_m(matrix_1, matrix_2):
    if not matrix_1 or not matrix_2:
        return
    M = len(matrix_1)
    K = len(matrix_2[0])
    N = len(matrix_2)
    result = [[0] * K for _ in range(M)]
    for i in range(M):
        for j in range(K):
            a = 0
            for indx in range(N):
                a += matrix_1[i][indx] * matrix_2[indx][j]
            result[i][j] = a
    return result


def multiply_m_v(matrix, vector):
    if not matrix or not vector:
        return
    M = len(matrix)
    N = len(vector)
    result = [[0] for _ in range(M)]
    for i in range(M):
        c = 0
        for j in range(N):
            c += matrix[i][j] * vector[j][0]
        result[i][0] = c
    return result


def print_matrix(matrix):
    for row in matrix:
        print(*row)
    return


def print_vector(vector):
    for x in vector:
        print(*x)
    return


def get_sum_diag(matrix):
    N = len(matrix)
    redund = matrix[N // 2][N // 2] if N % 2 else 0
    main_diag = sum([matrix[i][i] for i in range(N)])
    second_diag = sum([matrix[i][N-i-1] for i in range(N)])
    return main_diag + second_diag - redund


def convolution_2D(matrix, kernel):
    M = len(matrix)
    N = len(matrix[0])
    matrix_upd = copy.deepcopy(matrix)
    result = copy.deepcopy(matrix)
    for row in matrix_upd:
        row.insert(0, 0)
        row.append(0)
    matrix_upd.insert(0, [0 for _ in range(M + 2)])
    matrix_upd.append([0 for _ in range(M + 2)])
    K = len(kernel)
    for i in range(M):
        for j in range(N):
            s = 0
            for i_1 in range(K):
                for j_1 in range(K):
                    s += matrix_upd[i+i_1][j+j_1] * kernel[i_1][j_1]
            result[i][j] = s
    for row in result:
        print(*row)


print(create_vector(10))

print()

for row in create_matrix(4, 5):
    print(*row)

matrix_1 = [
    [0, 1, 2, 3],
    [4, 2, 1, 7],
    [9, 10, 11, 23]
]

matrix_2 = [
    [0, 1],
    [4, 2],
    [9, 10],
    [6, 4]
]

print()

for row in multiply_m_m(matrix_1, matrix_2):
    print(*row)

print()

matrix = [
    [0, 1, 2, 3],
    [4, 2, 1, 7],
    [9, 10, 11, 23]
]

vector = [[34], [3], [14], [56]]

for row in multiply_m_v(matrix, vector):
    print(*row)

print()

print_matrix(matrix)

print()

print_vector(vector)

print()

matrix = [
    [0, 1, 2],
    [4, 2, 1],
    [9, 10, 11]
]

print(get_sum_diag(matrix))

print()

matrix = [
    [10, 1, 2, 4, 2],
    [4, 2, 1, 5, 4],
    [4, 2, 1, 10, 10],
    [9, 10, 11, 12, 21],
    [23, 11, 2, 0, -1]
]

kernel = [
    [0, 1, 2],
    [4, 2, 1],
    [9, 10, 11]
]

print()

convolution_2D(matrix, kernel)