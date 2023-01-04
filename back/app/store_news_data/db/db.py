from typing import List
from sqlalchemy.sql import text
import datetime
from .dbaccess import DBAccess

class ComputeDB:
    def select_all_articles():
        db = DBAccess()
        # Databaseへのアクセス
        con = db.connect_database()

        article_data = []
        query = text("SELECT * FROM articles;")

        try:
            rows = con.execute(query)
            for row in rows:
                detum = {"article_id":row[0], "title":row[1], "ranking":row[2], "referenced_site":row[3], "content":row[4], "created_date":row[5], "url":row[6], "keywords":row[7] }
                article_data.append(detum)
                
        except Exception as err:
            print(err)
            exit()
        
        finally:
            db.disconnect_database(con)

        return article_data
    
    def bulk_insert_articles(formatted_article_dicts):
        db = DBAccess()
        con = db.connect_database()
        sql_text = "INSERT INTO articles (title, ranking, referenced_site, content, created_date, url, keywords) VALUES "

        for article_dict in formatted_article_dicts:
            temp = "('{}',{},'{}','{}',CURRENT_DATE,'{}','{}'),".format(article_dict["title"],article_dict["ranking"],article_dict["referenced_site"],article_dict["content"],article_dict["url"],article_dict["keywords"])
            sql_text = sql_text + temp
        sql_text = sql_text[:-1]
        sql_text = sql_text + ";"



        # print(sql_text)
        query = text(sql_text)

        try:
            print(con.execute(query))
            print("SUCESS INSERT!!")
        except Exception as err:
            print(err)
            exit()
        finally:
            db.disconnect_database(con)

    def select_today_articles():
        db = DBAccess()
        con = db.connect_database()
        dt_now = datetime.datetime.now()
        sql_text = "SELECT * FROM articles WHERE created_date='{0}-{1}-{2}';".format(dt_now.year, dt_now.month, dt_now.day)
        print(sql_text)
        query = text(sql_text)

        article_data = []

        try:
            rows = con.execute(query)
            for row in rows:
                detum = {"article_id":row[0], "title":row[1], "ranking":row[2], "referenced_site":row[3], "content":row[4], "created_date":row[5], "url":row[6], "keywords":row[7] }
                article_data.append(detum)
        except Exception as err:
            print(err)
            exit()
        finally:
            db.disconnect_database(con)

        return article_data

    def select_keywords_from_ten_days_ago():
        db = DBAccess()
        con = db.connect_database()
        dt_now = datetime.datetime.now()
        dt_ten_days_ago = dt_now - datetime.timedelta(days=10)
        sql_text = "SELECT keywords, content FROM articles WHERE created_date BETWEEN '{0}-{1}-{2}' AND '{3}-{4}-{5}';".format( dt_ten_days_ago.year, dt_ten_days_ago.month, dt_ten_days_ago.day, dt_now.year, dt_now.month, dt_now.day)
        print(sql_text)
        query = text(sql_text)

        all_keywords_data = {}

        try:
            rows = con.execute(query)
            for row in rows:
                article_keywords = row[0]['result']
                content = row[1]
                for keyword_data in article_keywords:
                    keyword = keyword_data["form"]
                    if keyword in all_keywords_data:
                        all_keywords_data[keyword]["score"] += float(keyword_data["score"])
                        all_keywords_data[keyword]["content"].append(content)
                    else:
                        all_keywords_data[keyword] = {"score":float(keyword_data["score"]), "content":[content]}
                    
        except Exception as err:
            print(err)
            exit()
        finally:
            db.disconnect_database(con)

        all_keywords_data = sorted(all_keywords_data.items(), key=lambda x:x[1]["score"], reverse=True)
        top_ten_keywords_data = all_keywords_data[:10]
        print(top_ten_keywords_data)
        return top_ten_keywords_data
        
