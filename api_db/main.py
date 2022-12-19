from fastapi import FastAPI
import uvicorn

from database.db_saver import DBSaver
from database.db_session import db_connection

app = FastAPI()


@app.get("/")
async def index():
    return "Приморський районний суд м. Одеси"


@app.get("/{user_id}")
async def status_check(user_id):
    with DBSaver() as saver:
        saver.save(user_id=user_id)


if __name__ == "__main__":
    db_connection()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
