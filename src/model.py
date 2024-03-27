import cv2
import easyocr
import numpy as np

from .config import MODEL_LANG_LIST, MODEL_GPU

class Model:
    def __init__(self, lang_list: list = MODEL_LANG_LIST, gpu: bool = MODEL_GPU) -> None:
        self.lang_list = lang_list
        self.gpu = gpu
        self.reader = None

    def load_model(self) -> None:
        self.reader = easyocr.Reader(self.lang_list, gpu=self.gpu)

    @staticmethod
    def normalize_text(text: str) -> str:
        text = text.lower()
        text = ' '.join(text.split())  # remove extra spaces, tabs, line breaks
        return text

    def predict(self, image: bytes) -> dict[str, str]:
        if self.reader is None:
            raise ValueError("Model not loaded")

        image_array = np.array(bytearray(image), dtype=np.uint8)
        img = cv2.imdecode(image_array, -1)
        if img is None or img.size == 0:
            return {'text': ''}

        prediction = self.reader.readtext(img)
        return {'text': self.normalize_text(' '.join([p[1] for p in prediction]))}
