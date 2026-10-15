from Log_Manager import LogMaster
from random import random, randint

Log = LogMaster("Matrix_Operations")
source = "Matrix_Operations.py"
user = "Stephen"


def create_vector(N):
    code = randint(100000, 999999)
    try:
        vector = [round(random(), 3) for _ in range(N)]
    except TypeError as e:
        level = "ERROR"
        message = "Введите число!"
        vector = None
        print(message)
    except Exception as e:
        level = "ERROR"
        message = "Что-то не так..."
        vector = None
        print(message)
    else:
        level = "INFO"
        message = "Штатно"
    finally:
        Log.log(
            level,
            source,
            message,
            code,
            user,
            create_vector.__name__,
        )
    return vector


def create_matrix(M, N):
    code = randint(100000, 999999)
    try:
        matrix = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                matrix[i][j] = round(random(), 3)
    except TypeError as e:
        level = "ERROR"
        message = "Введите число!"
        matrix = None
        print(message)
    except Exception as e:
        level = "ERROR"
        message = "Что-то не так..."
        matrix = None
        print(message)
    else:
        level = "INFO"
        message = "Штатно"
    finally:
        Log.log(
            level,
            source,
            message,
            code,
            user,
            create_matrix.__name__,
        )
    return matrix


def multiply_m_m(matrix_1, matrix_2):
    code = randint(100000, 999999)
    try:
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
    except TypeError as e:
        level = "ERROR"
        message = "Задайте матрицы!"
        result = None
        print(message)
    except IndexError as e:
        level = "ERROR"
        message = "Матрицы несовместимы!"
        result = None
        print(message)
    except Exception as e:
        level = "ERROR"
        add_data = e
        message = "Что-то не так..."
        result = None
        print(message)
    else:
        level = "INFO"
        message = "Штатно"
    finally:
        Log.log(
            level,
            source,
            message,
            code,
            user,
            multiply_m_m.__name__,
        )
    return result


def multiply_m_v(matrix, vector):
    code = randint(100000, 999999)
    try:
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
    except TypeError as e:
        level = "ERROR"
        message = "Задайте матрицу и вектор!"
        result = None
        print(message)
    except IndexError as e:
        level = "ERROR"
        message = "Матрица и вектор несовместимы!"
        result = None
        print(message)
    except Exception as e:
        level = "ERROR"
        message = "Что-то не так..."
        result = None
        print(message)
    else:
        level = "INFO"
        message = "Штатно"
    finally:
        Log.log(
            level,
            source,
            message,
            code,
            user,
            multiply_m_v.__name__,
        )
    return result


def print_matrix(matrix):
    code = randint(100000, 999999)
    try:
        for row in matrix:
            print(*row)
        print()
    except TypeError as e:
        level = "ERROR"
        message = "Задайте матрицу!"
        print(message)
    except Exception as e:
        level = "ERROR"
        message = "Что-то не так..."
        print(message)
    else:
        level = "INFO"
        message = "Штатно"
    finally:
        Log.log(
            level,
            source,
            message,
            code,
            user,
            print_matrix.__name__,
        )
    return


def print_vector(vector):
    code = randint(100000, 999999)
    try:
        for x in vector:
            print(*x)
        print()
    except TypeError as e:
        level = "ERROR"
        message = "Задайте вектор!"
        print(message)
    except Exception as e:
        level = "ERROR"
        message = "Что-то не так..."
        print(message)
    else:
        level = "INFO"
        message = "Штатно"
    finally:
        Log.log(
            level,
            source,
            message,
            code,
            user,
            print_vector.__name__,
        )
    return


def get_sum_diag(matrix):
    code = randint(100000, 999999)
    try:
        N = len(matrix)
        redund = matrix[N // 2][N // 2] if N % 2 else 0
        main_diag = sum([matrix[i][i] for i in range(N)])
        second_diag = sum([matrix[i][N - i - 1] for i in range(N)])
        result = main_diag + second_diag - redund
    except TypeError as e:
        level = "ERROR"
        message = "Задайте матрицу!"
        result = None
        print(message)
    except Exception as e:
        level = "ERROR"
        message = "Что-то не так..."
        result = None
        print(message)
    else:
        level = "INFO"
        message = "Штатно"
    finally:
        Log.log(
            level,
            source,
            message,
            code,
            user,
            get_sum_diag.__name__,
        )
    return result


def get_histogram(lst, bin_range=10):
    code = randint(100000, 999999)
    try:
        N = len(lst)
        if N == 0:
            return [], []

        min_num = min(lst)
        bin_width = (max(lst) - min_num) / bin_range
        bin_counts = [0 for _ in range(bin_range)]

        # if the list consists of equal values
        if bin_width == 0:
            bin_counts[0] = N
            bin_prob = [0 for _ in range(bin_range)]
            bin_prob[0] = 1
            return bin_counts, bin_prob

        for x in lst:
            indx = min(int((x - min_num) / bin_width), bin_range - 1)
            bin_counts[indx] += 1

        bin_prob = [bin_counts[i] / N for i in range(len(bin_counts))]
    except TypeError as e:
        level = "ERROR"
        message = "Задайте список!"
        bin_counts, bin_prob = None, None
        print(message)
    except Exception as e:
        level = "ERROR"
        message = "Что-то не так..."
        bin_counts, bin_prob = None, None
        print(message)
    else:
        level = "INFO"
        message = "Штатно"
    finally:
        Log.log(
            level,
            source,
            message,
            code,
            user,
            get_histogram.__name__,
        )
    return bin_counts, bin_prob


def get_filter(lst, kernel):
    code = randint(100000, 999999)
    try:
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
    except TypeError as e:
        level = "ERROR"
        message = "Задайте список!"
        result = None
        print(message)
    except Exception as e:
        level = "ERROR"
        message = "Что-то не так..."
        result = None
        print(message)
    else:
        level = "INFO"
        message = "Штатно"
    finally:
        Log.log(
            level,
            source,
            message,
            code,
            user,
            get_filter.__name__,
        )
    return result


def write_to_file(filepath, matrix):
    code = randint(100000, 999999)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            for row in matrix:
                if isinstance(row, list):
                    f.write(" ".join(map(str, row)) + "\n")
                else:
                    f.write(str(row) + "\n")
    except TypeError as e:
        level = "ERROR"
        message = "Задайте матрицу или список!"
        print(message)
    except PermissionError as e:
        level = "ERROR"
        message = "Отсутствует доступ к файлу!"
        print(message)
    except IsADirectoryError as e:
        level = "ERROR"
        message = "Укажите файл!"
        print(message)
    except OSError as e:
        level = "FATAL"
        message = "Не хватает места на диске!"
        print(message)
    except Exception as e:
        level = "ERROR"
        message = "Что-то не так..."
        print(message)
    else:
        level = "INFO"
        message = "Штатно"
    finally:
        Log.log(
            level,
            source,
            message,
            code,
            user,
            write_to_file.__name__,
        )


def read_from_file(filepath):
    code = randint(100000, 999999)
    try:
        matrix = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    row = list(map(float, line.split()))
                    matrix.append(row)
    except FileNotFoundError as e:
        level = "ERROR"
        message = "Файл не найден!"
        matrix = None
        print(message)
    except PermissionError as e:
        level = "ERROR"
        message = "Отсутствует доступ к файлу!"
        matrix = None
        print(message)
    except IsADirectoryError as e:
        level = "ERROR"
        message = "Укажите файл!"
        matrix = None
        print(message)
    except OSError as e:
        level = "FATAL"
        message = "Не хватает места на диске!"
        matrix = None
        print(message)
    except Exception as e:
        level = "ERROR"
        message = "Что-то не так..."
        matrix = None
        print(message)
    else:
        level = "INFO"
        message = "Штатно"
    finally:
        Log.log(
            level,
            source,
            message,
            code,
            user,
            read_from_file.__name__,
        )
    return matrix