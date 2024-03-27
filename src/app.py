import contextlib

from fastapi import FastAPI, File

from .model import Model
from .schemas import ModelOutput
from .config import MODEL_LANG_LIST, MODEL_GPU



model = Model(lang_list=MODEL_LANG_LIST, gpu=MODEL_GPU)

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    model.load_model()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the OCR API"}


@app.post("/predict")
async def predict(image: bytes = File(...)) -> ModelOutput:
    return model.predict(image)
