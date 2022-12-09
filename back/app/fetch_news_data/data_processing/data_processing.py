import json
import urllib.request
class CotohaApi:
    def __init__(self, client_id, client_secret, base_url, access_token_publish_url):
        self.client_id  = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.access_token_publish_url = access_token_publish_url
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


    def extract_keywords_from_texts (self, document):
        url = self.base_url + "nlp/v1/keyword"

        headers={
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "Bearer " + self.access_token
        }

        request_body = {
            "document": document
        }
        request_body = json.dumps(request_body).encode()

        request = urllib.request.Request(url, request_body, headers)

        try:
            result = urllib.request.urlopen(request)
        except urllib.request.HTTPError as e:
            print("<Error>" + e.reason)
        
        result_body = json.loads(result.read())

        return result_body
    