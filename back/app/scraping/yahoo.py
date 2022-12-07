import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp/ranking/access/news"

res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

elems = soup.select(".newsFeed_item_link")

for i,elem in enumerate(elems):
    link = elem.attrs["href"]
    title = elem.select("div.newsFeed_item_text > div.newsFeed_item_title")[0].contents[0]
    print({"rank":i+1,"title":title,"link":link})