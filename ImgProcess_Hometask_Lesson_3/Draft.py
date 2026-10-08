try:
    with open('file.txt', 'w') as f:
        f.write("Ambiguous phrase")
except FileExistsError:
    print("File already exists")
