from dotenv import load_dotenv
import os
from data_processing.data_processing import CotohaApi
load_dotenv()
from db.db import ComputeDB
from scraping.scraping import scraping

def fetch_news_data():
    data = scraping()
    data = data[0]
    print(data)


    # ComputeDB.insert_articles(2,data["title"],data["rank"],"test_keyword","yahoo","test_content")
    # a = ComputeDB.select_all_articles()
    # print(a)
    print(ComputeDB.select_today_articles())
    
