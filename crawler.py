 # -*- coding: utf-8 -*
#爬蟲基礎
import urllib.request as req
url = "https://www.ptt.cc/bbs/LoL/index.html"

#建立一個request物件 -> 附加Request Headers的資訊
request = req.Request(
    url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
)

#讀取已得到的資料
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

#解析原始碼，取得每篇文章的標題
import bs4
soup = bs4.BeautifulSoup(data, "html.parser")
print(soup.title.text) #標題

titles = soup.find_all("div", class_ = "title") #尋找所有class = "title" 的 div標籤
for title in titles:
    if title.a != None: #若逼條有包含a(沒有被刪除)，則印出來 #a是一個tag
        print(title.a.string)