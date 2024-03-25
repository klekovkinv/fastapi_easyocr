import cv2
import easyocr
import numpy as np

class Model:
    def __init__(self, lang_list: list = ['en', 'ru'], gpu: bool = True) -> None:
        self.lang_list = lang_list
        self.gpu = gpu
        self.reader = easyocr.Reader(self.lang_list, gpu=self.gpu)

    def normalize_text(text):
        text = text.lower()
        text = ' '.join(text.split())  # remove extra spaces, tabs, line breaks
        return text

    def predict(self, image):
        image_array = np.array(bytearray(image), dtype=np.uint8)
        img = cv2.imdecode(image_array, -1)
        if img is None or img.size == 0:
            return ""
        img_resized = cv2.resize(img, (450, 600))
        print(f"Image shape: {img_resized.shape}")
        print(f"Image type: {type(img_resized)}")
        prediction = self.reader.readtext('https://basket-11.wb.ru/vol1640/part164012/164012457/images/big/1.jpg')
        return self.normalize_text(' '.join([p[1] for p in prediction]))
