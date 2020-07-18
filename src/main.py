from typing import Dict, Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> Dict:
    return {"Hello": "World"}


@app.get("/item/{item_id}")
def read_item(item_id: int, q: Optional[str] = None) -> Dict:
    return {"item_id": item_id, "q": q}
