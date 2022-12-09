from dotenv import load_dotenv, find_dotenv
import os
from data_processing.data_processing import CotohaApi
load_dotenv(find_dotenv())

def fetch_news_data():
    client_id = os.getenv("COTOHA_CLIENT_ID")
    client_secret = os.getenv("COTOHA_CLIENT_SECRET")
    base_url = os.getenv("COTOHA_BASE_URL")
    access_token_publish_url = os.getenv("COTOHA_ACCESS_TOKEN_PUBLISH_URL")

    print(base_url)
    # cotoha_api = CotohaApi(client_id, client_secret, base_url, access_token_publish_url)

    # document = "私は人間だとは思いませんが、ある意味では人間であると思ってもよいと思います。"

    # result = cotoha_api.extract_keywords_from_texts(document)

    # print(result)
