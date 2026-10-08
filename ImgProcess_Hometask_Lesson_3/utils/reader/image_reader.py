import cv2

def read_data(file_path):
    image = cv2.imread(file_path, cv2.COLOR_BGR2GRAY)
    return image