const puppeteer = require('puppeteer');


module.exports.yahooScraping = async () => {
 
  const browser = await puppeteer.launch({
    headless: true,
    args: [
      '--disable-dev-shm-usage',
      '--no-sandbox'
    ]
  })

  let all_data = [];
  try {
    let datas;
    let datas_href;
    const page = await browser.newPage()
    await page.goto('https://news.yahoo.co.jp/ranking/access/news')
    let list_selector_href = "div > div.sc-gipzik.hgiWWi > main#contents > div#yjnMain > div#contentsWrap > div.newsFeed > ol > li > a"
    await page.waitForSelector('#contentsWrap')
    datas_href = await page.$$eval(list_selector_href, list => {
      return list.map(data => data.href);
    });
    let list_selector = "div > div.sc-gipzik.hgiWWi > main#contents > div#yjnMain > div#contentsWrap > div.newsFeed > ol > li > a > div.newsFeed_item_body > div.newsFeed_item_text > div.newsFeed_item_title  "
    datas = await page.$$eval(list_selector, list => {
      return list.map(data => data.textContent);
    });

    for(rank=0;rank<datas.length;rank++){
      let tmp = {rank:rank,data:datas[rank],href:datas_href[rank]};
      all_data.push(tmp);
    }
    

    console.log(datas)
   
  } catch (e) {
    console.error(e)
  } finally {
    browser.close()
    return all_data;
  }
}