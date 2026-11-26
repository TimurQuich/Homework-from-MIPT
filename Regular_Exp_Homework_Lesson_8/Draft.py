for i in range(len(coded_img)):
    possible_cross = (
        coded_img[i : i + cross_size] +
        coded_img[i + cross_size + gap : i + 2 * cross_size + gap] +
        coded_img[i + 2 * (cross_size + gap) : i + 3 * cross_size + 2 * gap]
    )
    print(possible_cross)
    if possible_cross == cross_in_line:
        count += 1