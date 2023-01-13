from db import ComputeDB

def select_today_articles():
    data = ComputeDB.select_all_articles()
    return data

def select_all_articles():
    data = ComputeDB.select_all_articles()
    return data

def select_keywords_from_ten_days_ago():
    data = ComupteDB.select_keywords_from_ten_days_ago()
    return data
    