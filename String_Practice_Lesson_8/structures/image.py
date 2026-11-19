import cv2

class AbstractFactoryImageReader():
    def read_image(self, file_path):
        raise NotImplementedError()


class BinImageReader(AbstractFactoryImageReader):
    def read_image(self, file_path):
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        if image is not None:
            _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        return image


class MonochromeImageReader(AbstractFactoryImageReader):
    def read_image(self, file_path):
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        return image


class ColorImageReader(AbstractFactoryImageReader):
    def read_image(self, file_path):
        image = cv2.imread(file_path, cv2.IMREAD_COLOR)
        return image


def get_image_reader(ident):
    if ident == 0:
        return BinImageReader()
    elif ident == 1:
        return MonochromeImageReader()
    elif ident == 2:
        return ColorImageReader()


if __name__ == "__main__":
    try:
        for i in range(3):
            reader = get_image_reader(i)

    except Exception as e:
        print(e)

    print("The demonstration of the program working")
    try:
        bin_reader = get_image_reader(0)
        img0 = bin_reader.read_image('../data/1.jpg')
        print(f"BinImageReader: {img0.shape if img0 is not None else 'File is not found'}")

        mono_reader = get_image_reader(1)
        img1 = mono_reader.read_image('../data/2.jpg')
        print(
            f"MonochromeImageReader: {img1.shape if img1 is not None else 'File is not found'}")

        color_reader = get_image_reader(2)
        img2 = color_reader.read_image('../data/3.jpg')
        print(f"ColorImageReader: {img2.shape if img2 is not None else 'File is not found'}")

    except Exception as e:
        print(e)
