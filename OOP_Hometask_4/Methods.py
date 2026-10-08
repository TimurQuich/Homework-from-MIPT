from Pictures import BinaryPicture, MonochromePicture, ColorPicture


class Operations:
    @staticmethod
    def get_picture_values(picture):
        values = []
        for y in range(picture.height):
            for x in range(picture.width):
                values.append(picture.show_values(x, y))
        return values

    @staticmethod
    def show_picture(picture):
        M = picture.height
        N = picture.width
        for y in range(M):
            row = []
            for x in range(N):
                row.append(picture.show_values(x, y))
            print(*row)


    @staticmethod
    def expected_value(values):
        N = len(values)
        return sum(values) / N

    @staticmethod
    def stand_dev(values):
        N = len(values)
        exp = Operations.expected_value(values)
        sum_sq = sum([(values[i] - exp) ** 2 for i in range(N)])
        return (sum_sq / N) ** 0.5


    @staticmethod
    def mono_to_mono(picture, t_exp, t_stand_dev):
        M = picture.height
        N = picture.width
        values = Operations.get_picture_values(picture)
        exp_init = Operations.expected_value(values)
        stand_dev_init = Operations.stand_dev(values)
        result = MonochromePicture(N, M)
        for y in range(M):
            for x in range(N):
                pixel = picture.show_values(x, y)
                new_pixel = t_stand_dev * (pixel - exp_init) / stand_dev_init + t_exp
                new_pixel = min(max(0, new_pixel), 255)
                result.set_values(x, y, round(new_pixel, 3))
        return result


    @staticmethod
    def color_to_color(picture, t_props):
        M = picture.height
        N = picture.width
        result = ColorPicture(N, M)
        for k in range(3):
            channel = []
            for y in range(M):
                for x in range(N):
                    channel.append(picture.show_values(x, y)[k])
            stand_dev_init = Operations.stand_dev(channel)
            exp_init = Operations.expected_value(channel)
            t_exp = t_props[k][0]
            t_stand_dev = t_props[k][1]
            for y in range(M):
                for x in range(N):
                    pixel = list(picture.show_values(x, y))
                    new_val = t_stand_dev * (pixel[k] - exp_init) / stand_dev_init + t_exp
                    pixel[k] = round(min(max(0, new_val), 255), 3)
                    current = list(result.show_values(x, y))
                    current[k] = pixel[k]
                    result.set_values(x, y, current)
        return result


    @staticmethod
    def binary_to_binary(picture):
        return picture


    @staticmethod
    def color_to_mono(picture):
        M = picture.height
        N = picture.width
        result = MonochromePicture(N, M)
        for y in range(M):
            for x in range(N):
                r, g, b = picture.show_values(x, y)
                result.set_values(x, y, round((r + g + b) / 3, 3))
        return result


    @staticmethod
    def mono_to_color(picture, palette):
        M = picture.height
        N = picture.width
        result = ColorPicture(N, M)
        keys = sorted(palette.keys())
        for y in range(M):
            for x in range(N):
                gray = picture.show_values(x, y)
                closest = min(keys, key=lambda k: abs(k - gray))
                result.set_values(x, y, list(palette[closest]))
        return result


    @staticmethod
    def mono_to_binary(picture, benchmark=128):
        M = picture.height
        N = picture.width
        result = BinaryPicture(N, M)
        for y in range(M):
            for x in range(N):
                pixel = picture.show_values(x, y)
                if pixel > benchmark:
                    result.set_values(x, y, 1)
                else:
                    result.set_values(x, y, 0)
        return result


    @staticmethod
    def binary_to_mono(picture):
        import math
        M = picture.height
        N = picture.width
        result = MonochromePicture(N, M)

        whites = []
        for y in range(M):
            for x in range(N):
                if picture.show_values(x, y) == 1:
                    whites.append((x, y))

        if not whites:
            return result

        max_dist = 0
        distances = [[0] * N for _ in range(M)]

        for y in range(M):
            for x in range(N):
                if picture.show_values(x, y) == 1:
                    distances[y][x] = 0
                else:
                    min_d = min(
                        math.hypot(x - wx, y - wy) for wx, wy in whites
                    )
                    distances[y][x] = min_d
                    if min_d > max_dist:
                        max_dist = min_d

        if max_dist == 0:
            max_dist = 1

        for y in range(M):
            for x in range(N):
                norm = distances[y][x] / max_dist * 255
                result.set_values(x, y, round(norm, 3))

        return result


    @staticmethod
    def color_to_binary(picture, benchmark=100):
        mono = Operations.color_to_mono(picture)
        return Operations.mono_to_binary(mono, benchmark)


    @staticmethod
    def binary_to_color(picture, palette):
        M = picture.height
        N = picture.width
        mono = MonochromePicture(N, M)
        for y in range(M):
            for x in range(N):
                pixel = picture.show_values(x, y)
                mono.set_values(x, y, 255 if pixel else 0)
        return Operations.mono_to_color(mono, palette)
