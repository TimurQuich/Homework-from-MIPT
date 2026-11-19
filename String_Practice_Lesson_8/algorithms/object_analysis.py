"""
Шаблонный метод (Template method)
"""
import cv2
import numpy as np
# ИСПРАВЛЕНО: Правильный импорт класса HistEncoder из файла encoder.py
from encoders.encoder import HistEncoder

class ObjectAnalysis(object):
    def template_method(self, image):

        image = self.noise_filtering(image)
        data = self.segmentation(image)
        data = self.object_parameters(data)

        return data

    def noise_filtering(self, image):
        raise NotImplementedError()

    def segmentation(self, data):
        raise NotImplementedError()

    def object_parameters(self, data):
        (image, data) = data
        (numLabels, labels, stats, centroids) = data
        x = []
        y = []
        w = []
        h = []
        area = []
        for i in range(1, numLabels):
            # extract the connected component statistics for the current
            # label
            x.append(stats[i, cv2.CC_STAT_LEFT])
            y.append(stats[i, cv2.CC_STAT_TOP])
            w.append(stats[i, cv2.CC_STAT_WIDTH])
            h.append(stats[i, cv2.CC_STAT_HEIGHT])
            area.append(stats[i, cv2.CC_STAT_AREA])

        return (x, y, w, h, area)


class BinaryImage(ObjectAnalysis):
    def __init__(self):
        pass

    def noise_filtering(self, image):
        median = cv2.medianBlur(image, 5)
        return median

    def segmentation(self, image):
        output = cv2.connectedComponentsWithStats(
            image,
            4, # connectivity
            cv2.CV_32S)
        return (image, output)

class MonochromeImage(BinaryImage):
    def __init__(self):
        pass

    def noise_filtering(self, image):
        median = cv2.GaussianBlur(image, (5,5), 0)
        return median

    def segmentation(self, image):
        edges = cv2.Canny(image, 100, 255)
        output = cv2.connectedComponentsWithStats(
            edges,
            4, # connectivity
            cv2.CV_32S)
        return (edges, output)

class ColorImage(MonochromeImage):
    def __init__(self):
        pass

    def segmentation(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        kernel = np.ones((3, 3), np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

        dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
        _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
        sure_fg = np.uint8(sure_fg)

        unknown = cv2.subtract(opening, sure_fg)

        _, markers = cv2.connectedComponents(sure_fg)
        markers = markers + 1
        markers[unknown == 255] = 0

        markers = cv2.watershed(image, markers)

        mask = np.zeros(gray.shape, dtype=np.uint8)
        mask[markers > 1] = 255

        output = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
        return (mask, output)

"""
Декоратор - структурный паттерн
"""

class FilteredAnalysis(ObjectAnalysis):
    def __init__(self, obj):
        self._proc = obj

    def template_method(self, image):
        (_x, _y, _w, _h, _area) = self._proc.template_method(image)
        x = []
        y = []
        w = []
        h = []
        area = []

        for i in range(len(_area)):
            if _area[i] > 10 and _area[i] < 2500:
                x.append(_x[i])
                y.append(_y[i])
                w.append(_w[i])
                h.append(_h[i])
                area.append(_area[i])

        return (x,y,w,h,area)


class HuMomentsDecorator(ObjectAnalysis):

    def __init__(self, obj):
        self._proc = obj

    def template_method(self, image):
        res = self._proc.template_method(image)

        if len(res) == 5:
            _x, _y, _w, _h, _area = res
            hu_list = []
        else:
            _x, _y, _w, _h, _area, hu_list = res

        new_hu_moments = []

        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        for i in range(len(_area)):
            roi = gray[_y[i]:_y[i] + _h[i], _x[i]:_x[i] + _w[i]]

            moments = cv2.moments(roi)
            hu = cv2.HuMoments(moments).flatten().tolist()
            new_hu_moments.append(hu)

        return (_x, _y, _w, _h, _area, new_hu_moments)


if __name__== '__main__':
    print("Binary Image Processing")
    bin_segm = BinaryImage()
    (x, y, w, h, area) = bin_segm.template_method(cv2.imread('../data/1.jpg', cv2.IMREAD_GRAYSCALE))
    for i in range(len(area)):
        print([x[i], y[i], w[i], h[i], area[i]])

    print("Decorated Binary Image Processing")
    filt_bin = FilteredAnalysis(BinaryImage())
    (x, y, w, h, area) = filt_bin.template_method(cv2.imread('../data/1.jpg', cv2.IMREAD_GRAYSCALE))
    for i in range(len(area)):
        print([x[i], y[i], w[i], h[i], area[i]])

    result = cv2.imread('../data/1.jpg')

    for i in range(len(area)):
        print([x[i], y[i], w[i], h[i], area[i]])
        cv2.rectangle(result, (x[i], y[i]), (x[i] + w[i], y[i] + h[i]), (0, 0, 255), 2)

    cv2.imwrite('../data/result_binary.jpg', result)

    print("Monochrome Image Processing")
    bin_segm = MonochromeImage()
    (x, y, w, h, area) = bin_segm.template_method(cv2.imread('../data/2.jpg', cv2.IMREAD_GRAYSCALE))
    for i in range(len(area)):
        print([x[i], y[i], w[i], h[i], area[i]])

    print("Decorated Monochrome Image Processing")
    filt_bin = FilteredAnalysis(MonochromeImage())
    (x, y, w, h, area) = filt_bin.template_method(cv2.imread('../data/2.jpg', cv2.IMREAD_GRAYSCALE))

    result = cv2.imread('../data/2.jpg')

    for i in range(len(area)):
        print([x[i], y[i], w[i], h[i], area[i]])
        cv2.rectangle(result, (x[i], y[i]), (x[i] + w[i], y[i] + h[i]), (0, 0, 255), 2)

    cv2.imwrite('../data/result_monochrome.jpg', result)

    print("Color Image Processing - Watershed")
    color_segm = ColorImage()
    (x, y, w, h, area) = color_segm.template_method(cv2.imread('../data/3.jpg'))
    for i in range(len(area)):
        print([x[i], y[i], w[i], h[i], area[i]])

    print("Color Image Processing with Hu Moments - Without Area Filter")
    hu_color = HuMomentsDecorator(ColorImage())
    (x, y, w, h, area, hu_moments) = hu_color.template_method(cv2.imread('../data/3.jpg'))
    for i in range(len(area)):
        formatted_hu = [float(f"{m:.4e}") for m in hu_moments[i]]
        print([x[i], y[i], w[i], h[i], area[i], formatted_hu])

    print("Decorated Color Image Processing - Filtered and Hu Moments")
    hu_filt_color = HuMomentsDecorator(FilteredAnalysis(ColorImage()))
    (x, y, w, h, area, hu_moments) = hu_filt_color.template_method(cv2.imread('../data/3.jpg'))

    result = cv2.imread('../data/3.jpg')

    if len(area) == 0:
        print("Objects don't fit the area condition")
    else:
        for i in range(len(area)):
            formatted_hu = [float(f"{m:.4e}") for m in hu_moments[i]]
            print([x[i], y[i], w[i], h[i], area[i], formatted_hu])
            cv2.rectangle(result, (x[i], y[i]), (x[i] + w[i], y[i] + h[i]), (0, 255, 0), 2)

    cv2.imwrite('../data/result_color.jpg', result)

    print("Strategy Pattern - HistEncoder")

    hu_filt_color = HuMomentsDecorator(FilteredAnalysis(ColorImage()))
    color_data = hu_filt_color.template_method(cv2.imread('../data/3.jpg'))

    HistEncoder.encode('../data/result_objects.json', color_data)

    HistEncoder.encode('../data/result_objects.csv', color_data)
