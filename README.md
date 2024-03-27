```
docker build -t fastapi .
```
```
docker run -it --rm -v $(pwd)/src:/workspace/src -p 8000:8000 fastapi
```
```
uvicorn src.app:app --reload --proxy-headers --host 0.0.0.0
```
