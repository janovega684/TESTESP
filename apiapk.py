from fastapi import FastAPI

app = FastAPI()

from untitled import find_students



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/PRUEBA")
async def estudiante(name1: str = None, name2: str = None):

    students = find_students(name1=None, name2=None)

    return students


