from dotenv import load_dotenv
import os
from data_processing.data_processing import CotohaApi
load_dotenv()
from db.db import ComputeDB
from scraping.scraping import scraping

def fetch_news_data():
    article_dict = scraping()
    


    # ComputeDB.insert_articles(article_dict)
    # a = ComputeDB.select_all_articles()
    # print(a)
    print(ComputeDB.select_today_articles())
    
