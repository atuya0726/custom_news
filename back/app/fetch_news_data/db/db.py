from typing import List
from sqlalchemy.sql import text
import datetime
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir))
from dbaccess import DBAccess


# MA_CODEの内容を全件取得する。
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
                detum = {"article_id":row[0], "title":row[1], "ranking":row[2], "keywords":row[3], "referenced_site":row[4], "content":row[5], "created_date":row[6] }
                article_data.append(detum)
                
        except Exception as err:
            print(err)
            exit()
        
        finally:
            db.disconnect_database(con)

        return article_data
    
    def bulk_insert_articles(article_dict):
        db = DBAccess()
        con = db.connect_database()
        sql_text = "INSERT INTO articles (title, ranking, referenced_site, content, created_date, url, keywords) VALUES 

        for row in article_data:



        print(sql_text)
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
                detum = {"article_id":row[0], "title":row[1], "ranking":row[2], "keywords":row[3], "referenced_site":row[4], "content":row[5], "created_date":row[6] }
                article_data.append(detum)
        except Exception as err:
            print(err)
            exit()
        finally:
            db.disconnect_database(con)

        return article_data
        
