from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    results = {"Hello": "World"}
    return results

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
