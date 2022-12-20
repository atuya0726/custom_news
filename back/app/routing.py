from typing import Union
from fastapi import FastAPI
from .store_news_data.store_news_data import store_news_data
from .store_news_data.db.db import ComputeDB

app = FastAPI()


@app.get("/health")
def read_root():
    return {"Hello": "World"}

@app.get("/store")
def store():
    try:
        store_news_data()
    except Exception as e:
        return e
    finally:
        print("SUCCESS")

@app.get("/fetch")
def fetch():
    try:
        data = ComputeDB.select_today_articles()
        return data
    except Exception as e:
        return e
    finally:
        print("SUCCESS")








