import urllib.request
article = urllib.request.urlopen('https://en.wikipedia.org/wiki/Special:Random')
print(article.read())