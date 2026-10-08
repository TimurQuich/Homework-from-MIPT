import cv2 as cv
import numpy as np


def processing(image, gamma=1.0):
    lookUpTable = np.empty((1, 256), np.uint8)
    for i in range(256):
        lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    result = cv.LUT(image, lookUpTable)
    return result