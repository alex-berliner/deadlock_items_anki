import concurrent.futures
import requests
import os
from api import *

# Remember to delete cache/ when the game is updated
# This creates an index of all the items' urls in the deadlock wiki. Some items
# have "_(item)" appended if the item's name is also something else,
# ie "Bullet Lifesteal" is an item and a stat. So we have to figure out which
# to use.
def get_urls(client_version):
    def process_url(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            if "infobox_item" not in response.text:
                url += "_(item)"
            return url
        except requests.exceptions.RequestException as e:
            print(f"Error processing {url}: {e}")
            return None  # Indicate failure
    wiki_url_prefix = "https://deadlock.wiki/"
    if os.path.exists("build/cache/urls.txt"):
        print("build/cache/urls.txt already exists. Skipping URL generation.")
        return open("build/cache/urls.txt", "r").readlines()

    in_shop = get_shopable_items(get_deadlock_items(client_version))
    urls = [wiki_url_prefix + x["name"].replace(" ", "_") for x in in_shop]
    r_urls = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_url, urls))

    for result in results:
        if result is not None:
            r_urls.append(result)

    if not os.path.exists("build/cache"):
        os.makedirs("build/cache")

    with open("build/cache/urls.txt", "w") as f:
        for url in r_urls:
            f.write(url + "\n")

    return r_urls

anki_deck_header="""\
#separator:tab
#html:true
"""
anki_card_format="""\
"<img src=""$$ITEM_NAME$$_front.png"">"	"<img src=""$$ITEM_NAME$$_back.png"">"\
"""
def make_deck(urls):
    o = anki_deck_header
    for e in urls:
        img_name=e.split("/")[-1].strip()
        o += anki_card_format.replace("$$ITEM_NAME$$", img_name) + "\n"
    open("build/deadlock_anki_import.txt", "w").write(o)