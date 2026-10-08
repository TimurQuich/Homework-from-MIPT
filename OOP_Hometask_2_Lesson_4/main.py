import Pictures
from Methods import Operations

print("\n-------------------------")
print("\nMonochrome to monochrome")
print("\n-------------------------")

print("\nInitial Monochrome Picture")

init_values = [
    [212, 12, 31, 1, 3],
    [59, 113, 90, 50, 73],
    [22, 182, 41, 51, 13],
]

for row in init_values:
    print(*row)

print("\nInitial parameters")

t_exp, t_stand_dev = 145, 125

print(f"t_exp = {t_exp}; t_stand_dev = {t_stand_dev}")

print("\nProcessed Monochrome Picture")

image = Pictures.MonochromePicture(5, 3, init_values)

result = Operations.mono_to_mono(image, t_exp, t_stand_dev)

Operations.show_picture(result)

print("\n-------------------------")
print("\nColor to color")
print("\n-------------------------")

print("\nInitial Color Picture")

init_values = [
    [[1, 134, 213], [31, 255, 123], [232, 21, 83]],
    [[60, 13, 23], [36, 2, 143], [32, 41, 41]],
    [[123, 4, 3], [41, 21, 23], [98, 65, 42]],
    [[60, 13, 23], [36, 2, 143], [32, 41, 41]]
]

for row in init_values:
    print(*row)

# R, G, B
t_props = [[43, 12], [190, 23], [21, 78]]

print("\nInitial parameters")

print(f"R - t_exp = {t_props[0][0]}; t_stand_dev = {t_props[0][1]}")
print(f"G - t_exp = {t_props[1][0]}; t_stand_dev = {t_props[1][1]}")
print(f"B - t_exp = {t_props[2][0]}; t_stand_dev = {t_props[2][1]}")

print("\nProcessed Color Picture")

image = Pictures.ColorPicture(3, 4, init_values)



result = Operations.color_to_color(image, t_props)

Operations.show_picture(result)

print("\n-------------------------")
print("\nBinary to binary")
print("\n-------------------------")

print("\nInitial Binary Picture")

init_values = [
    [0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1]
]

for row in init_values:
    print(*row)

image = Pictures.BinaryPicture(5, 3, init_values)

print("\nProcessed Binary Picture")

result = Operations.binary_to_binary(image)

Operations.show_picture(result)

print("\n-------------------------")
print("\nColor to mono")
print("\n-------------------------")

print("\nInitial Color Picture")

init_values = [
    [[1, 134, 213], [31, 255, 123], [232, 21, 83]],
    [[60, 13, 23], [36, 2, 143], [32, 41, 41]],
    [[123, 4, 3], [41, 21, 23], [98, 65, 42]],
    [[60, 13, 23], [36, 2, 143], [32, 41, 41]]
]

for row in init_values:
    print(*row)

image = Pictures.ColorPicture(3, 4, init_values)

result = Operations.color_to_mono(image)

print("\nProcessed Monochrome Picture")

Operations.show_picture(result)

print("\n-------------------------")
print("\nMonochrome to color")
print("\n-------------------------")

print("\nInitial Monochrome Picture")

init_values = [
    [212, 12, 31, 1, 3],
    [59, 113, 90, 50, 73],
    [22, 182, 41, 51, 13],
]

for row in init_values:
    print(*row)

print("\nPalette")

palette = {
    0:   (0, 0, 0),
    50:  (128, 0, 0),
    100: (255, 0, 0),
    150: (0, 128, 0),
    200: (0, 0, 128),
    255: (255, 255, 255)
}

for key in sorted(palette.keys()):
    print(f"{key} - {palette[key]}")

print("\nProcessed Color Picture")

image = Pictures.MonochromePicture(5, 3, init_values)

result = Operations.mono_to_color(image, palette)

Operations.show_picture(result)

print("\n-------------------------")
print("\nMonochrome to binary")
print("\n-------------------------")

print("\nInitial Monochrome Picture")

init_values = [
    [212, 12, 31, 1, 3],
    [59, 113, 90, 50, 73],
    [22, 182, 41, 51, 13],
]

for row in init_values:
    print(*row)

benchmark = 122

print(f"\nBenchmark = {benchmark}")

print("\nProcessed Binary Picture")

image = Pictures.MonochromePicture(5, 3, init_values)

result = Operations.mono_to_binary(image, benchmark)

Operations.show_picture(result)

print("\n-------------------------")
print("\nBinary to monochrome")
print("\n-------------------------")

print("\nInitial Binary Picture")

init_values = [
    [0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1]
]

for row in init_values:
    print(*row)

print("\nProcessed Monochrome Picture")

image = Pictures.BinaryPicture(5, 3, init_values)

result = Operations.binary_to_mono(image)

Operations.show_picture(result)

print("\n-------------------------")
print("\nColor to binary")
print("\n-------------------------")

print("\nInitial Color Picture")

init_values = [
    [[1, 134, 213], [31, 255, 123], [232, 21, 83]],
    [[60, 13, 23], [36, 2, 143], [32, 41, 41]],
    [[123, 4, 3], [41, 21, 23], [98, 65, 42]],
    [[60, 13, 23], [36, 2, 143], [32, 41, 41]]
]

for row in init_values:
    print(*row)

benchmark = 122

print(f"\nBenchmark = {benchmark}")

print("\nProcessed Binary Picture")

image = Pictures.ColorPicture(3, 4, init_values)

result = Operations.color_to_binary(image, benchmark)

Operations.show_picture(result)

print("\n-------------------------")
print("\nBinary to color")
print("\n-------------------------")

print("\nInitial Binary Picture")

init_values = [
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
]

for row in init_values:
    print(*row)

print("\nPalette")

palette = {
    0:   (0, 0, 0),
    255: (255, 255, 255)
}

for key in sorted(palette.keys()):
    print(f"{key} - {palette[key]}")

print("\nProcessed Color Picture")

image = Pictures.BinaryPicture(5, 3, init_values)

result = Operations.binary_to_color(image, palette)

Operations.show_picture(result)
