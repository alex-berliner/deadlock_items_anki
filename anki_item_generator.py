import os
from deck_generator import *
from img_gen import *

def main():
    if not os.path.exists("build"):
        os.makedirs("build")
    if not os.path.exists("build/collection.media"):
        os.makedirs("build/collection.media")
    if not os.path.exists("build/cache"):
        os.makedirs("build/cache")
    urls=get_urls()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(make_item_image, urls))
    for u in urls:
        make_item_image(u)
    make_deck(urls)

if __name__ == "__main__":
    main()