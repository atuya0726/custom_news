from fastapi import FastAPI
import os
import sys
sys.path.append(os.path.abspath(os.getenv('DB_MODULE')))
from .store_news_data.store_news_data import store_news_data
from .fetch_news_data import *

app = FastAPI()


@app.get("/health")
def read_root():
    return {"Hello": "World"}

@app.get("/store")
def store():
    try:
        store_news_data()
        print("SUCCESS")
    except Exception as e:
        return e
    

@app.get("/fetch")
def fetch():
    try:
        data = select_today_articles()
        print("SUCCESS")
        return data
    except Exception as e:
        return e
    
       

@app.get("/all")
def all():
    try:
        data = select_all_articles()
        print("SUCCESS")
        return data
    except Exception as e:
        return e
    

@app.get("/hot_keywords")
def hot_keyword():
    try:
        data = select_keywords_from_ten_days_ago()
        print("SUCCESS")
        return data
    except Exception as e:
        return err
    








