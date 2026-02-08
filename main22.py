print("main22")
from fastapi import FastAPI
from fastapi import Depends

app=FastAPI()
#the dependency function that handles reusable logic
def get_message():
  return "Hello World from the dependency"
@app.get("/")
def read_root(message: str=Depends(get_message)):
  return {"message":message}
# def read_root():
    # return {"HelloWorld1":"from main22.py"}
@app.post("/items/")
def create_item(item: dict):
  return {"item":item}