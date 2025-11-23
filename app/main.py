from fastapi import FastAPI, HTTPException


app = FastAPI()

# Simpel database in-memory
items = {"1": "Laptop", "2": "Keyboard"}


@app.get("/")
def read_root():
    return {"message": "Hello, DevOps!"}


@app.get("/items/{item_id}")
def read_item(item_id: str):
    if item_id in items:
        return {"item_id": item_id, "name": items[item_id]}
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items/{item_id}")
def create_item(item_id: str, name: str):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = name
    return {"item_id": item_id, "name": name}
