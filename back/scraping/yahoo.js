
const puppeteer = require('puppeteer');


module.exports.yahooScraping = async () => {
 
  const browser = await puppeteer.launch({
    headless: true,
    args: [
      '--disable-dev-shm-usage',
      '--no-sandbox'
    ]
  })

  let datas;
  try {
    const page = await browser.newPage()
    await page.goto('https://news.yahoo.co.jp/ranking/access/news')
    let list_selector = "div > div.sc-gipzik.hgiWWi > main#contents > div#yjnMain > div#contentsWrap > div.newsFeed > ol > li > a > div.newsFeed_item_body > div.newsFeed_item_text > div.newsFeed_item_title  "
    await page.waitForSelector('#contentsWrap')
    datas = await page.$$eval(list_selector, list => {
      return list.map(data => data.textContent);
  });

  console.log(datas)
   
  } catch (e) {
    console.error(e)
  } finally {
    browser.close()
    return datas;
  }
}