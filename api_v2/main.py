import os
from typing import List

import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

import models
import schema


DATABASE_URL = f'postgresql://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}' \
               f'/{os.environ["DB_NAME"]}'

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)


@app.get('/')
async def root():
    return {'message': 'hello world'}


@app.get('/event-bought/', response_model=List[schema.EventBought])
async def event_bought():
    events = db.session.query(models.EventBought).all()
    return events


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
