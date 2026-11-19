import copy
import re

import decoders.decoder
import encoders.encoder

"""
Стратегия (Strategy)
"""

class Hist:
    @classmethod
    def read(cls, file_path):
        if re.search(r'\.bin$', file_path):
            decoder = decoders.decoder.BinHistDecoder
        elif re.search(r'\.txt$', file_path):
            decoder = decoders.decoder.TxtHistDecoder
        elif re.search(r'\.json$', file_path):
            decoder = decoders.decoder.JsonHistDecoder
        elif re.search(r'\.csv$', file_path):
            decoder = decoders.decoder.CsvHistDecoder
        elif re.search(r'\.(png|jpg|jpeg|bmp)$', file_path):
            decoder = decoders.decoder.ImageHistDecoder
        else:
            raise RuntimeError('Невозможно получить данные %s' % file_path)
        data = decoder.decode(file_path)
        return cls(data)

    @classmethod
    def write(cls, filename):
        pass

    def __init__(self, data):
        self._data = data

    def get_data(self):
        return copy.deepcopy(self._data)

if __name__ == "__main__":
    hist = Hist.read('../data/csv_test.csv')
    print(hist.get_data())
