from PIL import Image
import numpy as np
import re

img = Image.open("img_examples/example2.png") # RGBA format
arr = np.array(img)
n, p = arr.shape[:2]

# Binarization

bin_arr = np.array([[0] * p for _ in range(n)])

for i in range(n):
    for j in range(p):
        if np.sum(arr[i][j][:3]) / 3 > 127: # Ignore the last number in a pixel (A)
            bin_arr[i, j] = 1
        else:
            bin_arr[i, j] = 0

n_bin, p_bin = bin_arr.shape

# Dividing into separate blocks

block_size = 51

num_blocks_h = n_bin // block_size
num_blocks_w = p_bin // block_size

# Coding blocks

coded_arr = np.array([[0] * num_blocks_w for _ in range(num_blocks_h)])

for i in range(num_blocks_h):
    for j in range(num_blocks_w):
        block = bin_arr[i * block_size : (i + 1) * block_size, j * block_size : (j + 1) * block_size]
        if block.mean() >= 0.5:
            coded_arr[i][j] = 1

# Converting blocks into a string

coded_img = ""

for i in range(num_blocks_h):
    coded_img += "".join(coded_arr[i, :].astype(str))

# Finding the pattern "cross"

cross_size = 3
gap = "." * (num_blocks_w - cross_size)
pattern = f"(?=(101{gap}000{gap}101))"
match_list = []

for match in re.finditer(pattern, coded_img):
    col = match.start() % num_blocks_w
    if col <= num_blocks_w - cross_size:
        match_list.append(match)

print(len(match_list))
