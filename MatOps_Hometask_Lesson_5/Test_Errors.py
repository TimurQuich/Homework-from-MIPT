import Matrix_Operations as op

vector = op.create_vector("string")

matrix = op.create_matrix(10, "string")

matrix_1 = op.create_matrix(4, 1)
matrix_2 = op.create_matrix(2, 6)

matrix_res = op.multiply_m_m(matrix_1, matrix_2)

op.print_matrix(matrix_1)
op.print_matrix(matrix_2)
op.print_matrix(matrix_res)

op.write_to_file('result.txt', matrix_res)

result = op.read_from_file('not_existed.txt')

bin_counts, bin_probs = op.get_histogram("string")

filter = op.get_filter("string", "string")
