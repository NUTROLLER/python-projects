import wikipedia
from wikipedia.exceptions import DisambiguationError
import webbrowser

#To get the random article, a function:
def get_random_article():
    print("Getting article...")
    while True:
        try:
            print("Article Found!")
            title = wikipedia.random()
            page = wikipedia.page(title)
            return page
        except DisambiguationError as e:
            print("")
            continue

def open_in_browser(title):
    url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
    webbrowser.open(url)  # Opens in the default browser

# Example usage
while True:
    article = get_random_article()
    title = (article.title)
    summary = article.summary
    print(f"Title: {title}\nSummary: {summary[:500]}")
    to_read = input("\nWould you like to read this article(y/n)?:").lower().strip()
    if (to_read == 'y'):
        open_in_browser(article.title)
    else:
        exit_key = input("\nLoad another article(y) or exit(n)? :").lower().strip()
        if exit_key == 'n':
            break
        else: 
            pass
