def get_histogram(lst, bin_range=10):
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
    return bin_counts, bin_prob


lst = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2]
bin_range = 4

result = get_histogram(lst, bin_range)
for i in range(len(result[0])):
    print(f"Bin {i + 1}: counts = {result[0][i]}, probability = {result[1][i]}")