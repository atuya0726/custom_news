from .data_processing.data_processing import CotohaApi
from db import ComputeDB
from .scraping.scraping import scraping

def store_news_data():
    article_dicts = scraping()
    print("SUCCESS scraping!!")
    cotoha = CotohaApi()

    formatted_article_dicts = cotoha.extract_keywords_and_attach(article_dicts)
    # print(formatted_article_dicts)
    print("SUCCESS cotoha data_processing")
    
    ComputeDB.bulk_insert_articles(formatted_article_dicts)
   

