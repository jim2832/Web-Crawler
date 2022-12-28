import requests
from bs4 import BeautifulSoup

url = "https://github.com/jim2832?tab=repositories"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("a", itemprop="name codeRepository")

print("Current Repository:\n")
count = 1
for title in titles:
    print(f"Project{count}:",title["href"].replace("/jim2832/", ""))
    count+=1