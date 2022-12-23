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
        sql_text = "SELECT * FROM articles WHERE created_date='{0}-{1}-{2}'".format(dt_now.year, dt_now.month, dt_now.day)
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
        
