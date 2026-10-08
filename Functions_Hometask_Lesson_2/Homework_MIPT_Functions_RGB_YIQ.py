def convert_RGB_YIQ(vector):
    RGB_to_YIQ = [
        [0.299, 0.587, 0.114],
        [0.5959, -0.2746, -0.3213],
        [0.2115, -0.5227, 0.3112]
    ]
    YIQ_to_RGB = [
        [1, 0.956, 0.619],
        [1, -0.272, -0.647],
        [1, -1.106, 1.703]
    ]

    n = 3
    m = 3

    result = [0 for _ in range(n + 1)]

    if vector[-1]:
        c = YIQ_to_RGB
        result[-1] = 0
    else:
        c = RGB_to_YIQ
        result[-1] = 1

    for i in range(n):
        s = 0
        for j in range(m):
            s += c[i][j] * vector[j]
        result[i] = s
    return result


vector = [255, 255, 1, 0]
print(convert_RGB_YIQ(vector))
