# This project fetches latest headlines from https://www.bbc.com and then displays
#5 of them.
import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
try:   
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    fetched = True
except:
    print("Unable to fetch BBC News.")

if fetched:
    print("Latest Headlines:\n")
    headlines = soup.find_all("h2")
    for idx,h in enumerate(headlines[:5],1):
        print(f"{idx}. {h.get_text(strip=True).removesuffix("<!-- -->")}")

else:
    print("Please try again later!")




