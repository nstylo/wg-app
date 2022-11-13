from fastapi import FastAPI
from . import db

# TEMP: Got to import this, so all tables will be loaded on startup
from . import model

app = FastAPI()


@app.on_event("startup")
def startup():
    print(db.Base.metadata.tables)
    db.Base.metadata.create_all(db.engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
