from fastapi import FastAPI, File

from .model import Model
from .schemas import ModelOutput


model = Model()
# print(model.reader.readtext('https://basket-11.wb.ru/vol1640/part164012/164012457/images/big/1.jpg'))
app = FastAPI()

@app.post("/predict")
async def predict(image: bytes = File(...)) -> ModelOutput:
    return model.predict(image)
