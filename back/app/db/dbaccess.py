from sqlalchemy import create_engine
import os


class DBAccess():
    def __init__(self):
        self.POSTGRES_USER = os.getenv('POSTGRES_USER')
        self.POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
        self.POSTGRES_SERVER = os.getenv('POSTGRES_SERVER')
        self.POSTGRES_PORT = os.getenv('POSTGRES_PORT')
        self.POSTGRES_DB = os.getenv('POSTGRES_DB')
    # DB接続処理
    def connect_database(self):
        try:
            # DB接続文字列の作成
            # 接続文字列は、postgresql://接続ユーザ名:接続PW@サーバ名:port番号
            SQLALCHEMY_DATABASE_URL = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
                self.POSTGRES_USER, self.POSTGRES_PASSWORD, self.POSTGRES_SERVER, self.POSTGRES_PORT, self.POSTGRES_DB
            )
            print(SQLALCHEMY_DATABASE_URL)
            engine = create_engine(SQLALCHEMY_DATABASE_URL)

            # DBへの接続
            conn = engine.connect()
            print("Successful Database Access!!")
        except Exception as err:
            # 接続時にエラーとなった場合、エラーを返す。
            print(err)
            exit()
        
        return conn

    # DB切断処理
    def disconnect_database(self,conn):
        conn.close()