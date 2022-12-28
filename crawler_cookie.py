 # -*- coding: utf-8 -*
#爬蟲基礎
import time
import urllib.request as req
page = 20

#抓取單一頁面的函式
def getData(url):
    #建立一個request物件 -> 附加Request Headers的資訊
    request = req.Request(
        url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
    )

    #讀取已得到的資料
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    #解析原始碼，取得每篇文章的標題
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_ = "title") #尋找所有class = "title" 的 div標籤
    for title in titles:
        if title.a != None: #若標題有包含a(沒有被刪除)，則印出來
            print(title.a.string)
            time.sleep(0.05)

    #抓取下一頁的連結
    next_link = root.find("a", string = "‹ 上頁") #尋找內文是‹ 上頁的a標籤
    return next_link["href"]


# main
url = "https://www.ptt.cc/bbs/LoL/index.html" #第一頁的網址

count = 0
while count <= page: #count為要抓取的頁數(使「抓上一頁」重複執行)
    url = "https://www.ptt.cc" + getData(url)
    count += 1