A especificação acima menciona a criação de uma API em NodeJS, mas como você solicitou um código Python com FastAPI, estou fornecendo um código Python. Porém, se você precisar de um código NodeJS, avise-me.

Aqui está o código Python usando FastAPI:


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str = None

storage = []

@app.get("/")
def read_root():
    """Returns a welcome message"""
    return {"Message": "Welcome to FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Returns a specific item by its ID"""
    for item in storage:
        if item['id'] == item_id:
            return item

    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/")
def create_item(item: Item):
    """Creates a new item and store it"""
    new_item = item.dict()
    new_item['id'] = len(storage) + 1
    storage.append(new_item)
    return new_item


Este é um exemplo simples com dois endpoints. O endpoint POST `/items/` recebe um item com os campos `name`, `price` e `description` e armazena o item. O endpoint GET `/items/{item_id}` retorna o item com o `item_id` especificado.