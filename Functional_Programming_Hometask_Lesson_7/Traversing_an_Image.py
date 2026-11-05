import math

def linearly_traverse(arr):
    for rows in arr:
        for element in rows:
            yield element


def spirally_traverse(arr):
    m = len(arr)
    n = len(arr[0])

    r = (m - 1) // 2
    c = (n - 1) // 2

    yield arr[r][c]

    dr = [0, -1, 0, 1]
    dc = [-1, 0, 1, 0]

    step_len = 1
    idx = 0
    step_count = 1
    total = m * n

    while step_count < total:
        for _ in range(2):
            for _ in range(step_len):
                r += dr[idx]
                c += dc[idx]
                if 0 <= r < m and 0 <= c < n:
                    yield arr[r][c]
                    step_count += 1
                    if step_count == total:
                        return
            idx = (idx + 1) % 4
        step_len += 1


def zig_zag_traverse(arr):
    m = len(arr)
    n = len(arr[0])

    i, j = 0, 0
    is_up = True
    k = 0 # Count

    while k < m * n:
        if is_up:
            while i >= 0 and j < n:
                yield arr[i][j]
                i -= 1
                j += 1
                k += 1
            if i < 0 and j < n:
                i = 0
            if j == n:
                i += 2
                j -= 1
        else:
            while j >= 0 and i < n:
                yield arr[i][j]
                i += 1
                j -= 1
                k += 1
            if j < 0 and i < n:
                j = 0
            if i == n:
                i -= 1
                j += 2

        is_up = not is_up


def _peano_generator(n, idx):
    x, y = 0, 0
    s = 1
    cur_idx = idx
    matrix_size = 2 ** n

    while s < matrix_size:
        quadrant = cur_idx % 4

        if quadrant == 0:
            rx, ry = 0, 0
        elif quadrant == 1:
            rx, ry = 0, 1
        elif quadrant == 2:
            rx, ry = 1, 1
        else:
            rx, ry = 1, 0

        if ry == 0:
            if rx == 1:
                x = s - 1 - x
                y = s - 1 - y
            x, y = y, x

        x += s * rx
        y += s * ry

        cur_idx = cur_idx // 4
        s *= 2

    return x, y


def peano_traverse(arr):
    m = len(arr)
    n = len(arr[0])
    power = int(round(math.log2(m)))

    for i in range(m * n):
        x, y = _peano_generator(power, i)
        row = (m - 1) - y
        col = x
        yield arr[row][col]

# Test

if __name__ == '__main__':
    mon_image = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Linear Traversal")
    for x in linearly_traverse(mon_image):
        print(x)

    print()

    print("Spiral Traversal")
    for x in spirally_traverse(mon_image):
        print(x)

    print()

    print("Zig-Zag Traversal")
    for x in zig_zag_traverse(mon_image):
        print(x)

    print()

    mon_image_upd = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    print("Peano Traversal")
    for x in peano_traverse(mon_image_upd):
        print(x)
