from typing import Union
from fastapi import FastAPI
from store_news_data.store_news_data import store_news_data

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
        return {"SUCCESS"}

# @app.get("/fetch")
# def fetch():






