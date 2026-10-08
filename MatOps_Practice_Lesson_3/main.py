import time
import Matrix_Operations as op


def main():
    mat_A = op.create_matrix(2, 3)
    mat_B = op.create_matrix(3, 2)
    mat_square = op.create_matrix(3, 3)

    vec_u = [[0.5], [1.2], [3.0]]

    print("Initial matrix A:")
    op.print_matrix(mat_A)

    print()

    print("Initial matrix B:")
    op.print_matrix(mat_B)

    print()

    print("Matrix-matrix multiplication:")
    res_mm = op.multiply_m_m(mat_A, mat_B)
    op.print_matrix(res_mm)

    print()

    print("Matrix-vector multiplication:")
    res_mv = op.multiply_m_v(mat_A, vec_u)
    op.print_vector(res_mv)

    print()

    print("Square matrix for diagonal sum calculation:")
    op.print_matrix(mat_square)
    sum_diags = op.get_sum_diag(mat_square)
    print(f"Sum of diagonals: {sum_diags}")

    print()

    print("Vector histogram calculation:")
    raw_vector = op.create_vector(20)
    int_vector = [int(x * 100) for x in raw_vector]
    print(f"Initial list: {int_vector}")
    counts, probs = op.get_histogram(int_vector, bin_range=10)
    for i in range(len(counts)):
        print(f"Bin {i + 1} contains {counts[i]} element(s). Probability: {round(probs[i], 3)}")

    print()

    print("Vector kernel filtering:")
    filter_target = [10, 10, 10, 50, 50, 50, 10, 10]
    kernel = [-1, 0, 1]
    filtered_res = op.get_flter(filter_target, kernel)
    print(f"Filtered result: {filtered_res}")

    print()

    print("Operations with files:")
    filename = "result.txt"
    op.write_to_file(filename, mat_square)
    print(f"Result saved to '{filename}'")

    print()

    loaded_matrix = op.read_from_file(filename)
    print("Data is read from file:")
    op.print_matrix(loaded_matrix)

    print()

    big_mat1 = op.create_matrix(80, 80)
    big_mat2 = op.create_matrix(80, 80)
    big_vec = [[0.5] for _ in range(80)]
    big_list = [int(x * 100) for x in op.create_vector(5000)]

    t1 = time.time()
    op.multiply_m_m(big_mat1, big_mat2)
    t2 = time.time()
    print(f"Matrix-matrix multiplication (80x80): {round(t2 - t1, 6)} seconds")

    t3 = time.time()
    op.multiply_m_v(big_mat1, big_vec)
    t4 = time.time()
    print(f"Matrix-vector multiplication (80x80): {round(t4 - t3, 6)} seconds")

    t5 = time.time()
    op.get_sum_diag(big_mat1)
    t6 = time.time()
    print(f"Diagonal sum calculation (80x80): {round(t6 - t5, 6)} seconds")

    t7 = time.time()
    op.get_histogram(big_list, bin_range=10)
    t8 = time.time()
    print(f"Histogram (5000 elements): {round(t8 - t7, 6)} seconds")

    t9 = time.time()
    op.get_flter(big_list, kernel)
    t10 = time.time()
    print(f"Vector filter (5000 elements): {round(t10 - t9, 6)} seconds")


if __name__ == "__main__":
    main()