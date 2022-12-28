from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"))
print(soup.name)