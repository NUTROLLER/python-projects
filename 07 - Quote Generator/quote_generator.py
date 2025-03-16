# This bad boy fetches quotes from https://zenquotes.io and then displays them so long as
# the user wants it. Since ZenQuotes allow only 5 requests per 30 seconds without an API
# key, we have to wait for 30 seconds before fetching more quotes.

import requests
import json
import time
def get_quote():
    r = requests.get("https://zenquotes.io/api/random")
    try:
        to_json = r.json()
        item = to_json[0]  # Get first (and only) quote
        print(f"\n❝ {item['q']} ❞\n- {item['a']}\n")
    except json.JSONDecodeError:
        print("Failed to parse JSON.")
count = 0
while True:
    to_load = input("Load quote(y/n)?").lower().strip()
    if (count<5 and to_load == 'y'):
        get_quote()
        count+=1
    elif(count == 5):
        count = 0
        print("Please wait 30 seconds before trying again.")
        time.sleep(30)
    elif(to_load == 'n'):
        print("Exiting...")
        break
    else:
        print("Please enter only 'y' or 'n'.")




