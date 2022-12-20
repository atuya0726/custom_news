import json
import urllib.request
import os
import json
class CotohaApi:
    def __init__(self):
        self.client_id  = os.getenv("COTOHA_CLIENT_ID")
        self.client_secret = os.getenv("COTOHA_CLIENT_SECRET")
        self.base_url = os.getenv("COTOHA_BASE_URL")
        self.access_token_publish_url = os.getenv("COTOHA_ACCESS_TOKEN_PUBLISH_URL")
        self.fetch_access_token()

    

    def fetch_access_token(self):
        url = self.access_token_publish_url
        header = {
            "Content-Type": "application/json;charset=UTF-8"
        }

        request_body = {
            "grantType": "client_credentials",
            "clientId": self.client_id,
            "clientSecret": self.client_secret
        }

        request_body = json.dumps(request_body).encode()

        request = urllib.request.Request(url, request_body, header)

        result = urllib.request.urlopen(request)

        result_body = json.loads(result.read())

        self.access_token = result_body["access_token"]


    def extract_keywords_and_attach (self, article_dicts):
        url = self.base_url + "nlp/v1/keyword"

        headers={
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Bearer " + self.access_token
        }

        for article_dict in article_dicts:
            request_body = {
                "document": article_dict["content"]
            }
            request_body = json.dumps(request_body).encode()
            request = urllib.request.Request(url, request_body, headers)

            try:
                result = urllib.request.urlopen(request)
            except urllib.request.HTTPError as e:
                print("<Error>" + e.reason)
            
            result_body = json.loads(result.read())
            article_dict["keywords"] = json.dumps(result_body)

        return article_dicts
    