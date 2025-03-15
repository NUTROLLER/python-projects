from bs4 import BeautifulSoup
fsoup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(fsoup.prettify())