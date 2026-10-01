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


def get_histogram(lst, bin_range=10):
    N = len(lst)
    if N == 0:
        return [], []

    bin_counts = [0 for _ in range(bin_range)]
    for x in lst:
        idx = int(x // 10)
        if 0 <= idx < bin_range:
            bin_counts[idx] += 1
        else:
            if idx >= bin_range:
                bin_counts[-1] += 1

    bin_prob = [bin_counts[i] / N for i in range(len(bin_counts))]
    return bin_counts, bin_prob


def get_flter(lst, kernel):
    N = len(lst)
    K = len(kernel)
    pad = K // 2

    padded_lst = [0] * pad + lst + [0] * pad
    result = []

    for i in range(N):
        current_sum = 0
        for j in range(K):
            current_sum += padded_lst[i + j] * kernel[j]
        result.append(current_sum)

    return result


def write_to_file(filepath, matrix):
    with open(filepath, 'w', encoding='utf-8') as f:
        for row in matrix:
            if isinstance(row, list):
                f.write(" ".join(map(str, row)) + "\n")
            else:
                f.write(str(row) + "\n")


def read_from_file(filepath):
    matrix = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                row = list(map(float, line.split()))
                matrix.append(row)
    return matrix