import cv2 as cv


def processing(image):
    if len(image.shape) == 2:
        return cv.equalizeHist(image)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    ycrcb[:, :, 0] = cv.equalizeHist(ycrcb[:, :, 0])
    return cv.cvtColor(ycrcb, cv.COLOR_YCrCb2BGR)
