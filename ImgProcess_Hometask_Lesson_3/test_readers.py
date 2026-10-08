import os
import sys
import argparse

from utils.reader import image_reader as imread
from utils.reader import csv_reader, bin_reader, txt_reader, json_reader
from utils.processor import histogram
from utils.writer import csv_writer, bin_writer, txt_writer, image_writer, json_writer
from utils.image_toner import stat_correction, equalization, gamma_correction


# The main function
def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-img', '--img_path', required=True, help='Path to image')
    parser.add_argument('-p', '--path', default=None, help='Input file path ')
    parser.add_argument('-o', '--output', required=True, help='Save file path')
    parser.add_argument('-m', '--method', required=True,
                        choices=['stat_corr', 'equalize', 'gamma'],
                        help='Method for image processing')
    parser.add_argument('-g', '--gamma', type=float, default=1.0, help='Gamma value')
    return parser


def get_histogram(path):
    img = imread.read_data(path)
    return histogram.image_processing(img)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    formats = {
        '.png': get_histogram,
        '.jpg': get_histogram,
        '.jpeg': get_histogram,
        '.bmp': get_histogram,
        '.csv': csv_reader.read_data,
        '.json': json_reader.read_data,
        '.txt': txt_reader.read_data,
        '.bin': bin_reader.read_data
    }

    parser = init_parser()
    args = parser.parse_args(sys.argv[1:])
    image = imread.read_data(args.img_path)
    ext = os.path.splitext(args.img_path)[1].lower()

    if ext not in formats:
        print("Unsupported file format")
        sys.exit(1)

    reader = formats[ext]
    hist_template = reader(args.img_path)

    if args.method == 'stat_corr':
        res_image = stat_correction.processing(hist_template, image)
    elif args.method == 'equalize':
        res_image = equalization.processing(image)
    elif args.method == 'gamma':
        res_image = gamma_correction.processing(image, args.gamma)
    image_writer.write_data(args.output, res_image)
