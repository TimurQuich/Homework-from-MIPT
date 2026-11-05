class ArrayIterator:
    def __init__(self, array):
        self.i = 0
        self.array = array

    def __next__(self):
        try:
            result = self.array[self.i]
        except IndexError:
            raise StopIteration
        else:
            self.i += 1
            return result

    def __iter__(self):
        return self


def spirally_traverse(arr):
    m = len(arr)
    n = len(arr[0])

    result = []
    vis = [[False] * n for _ in range(m)]

    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    r, c = m - 1, 0

    idx = 0

    for _ in range(m * n):
        result.append(arr[r][c])
        vis[r][c] = True

        new_r, new_c = r + dr[idx], c + dc[idx]

        if 0 <= new_r < m and 0 <= new_c < n and not vis[new_r][new_c]:
            r, c = new_r, new_c
        else:
            idx = (idx + 1) % 4
            r += dr[idx]
            c += dc[idx]

    return result