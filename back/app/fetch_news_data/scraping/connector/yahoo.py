import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp/ranking/access/news"

def result():
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")

    elems = soup.select(".newsFeed_item_link")

    scraping_data = []

    for i,elem in enumerate(elems):
        link = elem.attrs["href"]
        title = elem.select("div.newsFeed_item_text > div.newsFeed_item_title")[0].contents[0]
        scraping_data.append({"rank":i+1,"title":title,"link":link})
    print(scraping_data)
    return scraping_data