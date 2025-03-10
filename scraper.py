from converter import *
import concurrent.futures
from replace import *
import pprint
import requests
import json
import os
from deadlock_anki import *
from lxml import html

wiki_url_prefix = "https://deadlock.wiki/"
def process_url(url):
    """Processes a single URL and returns the modified URL if needed."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        if "infobox_item" not in response.text:
            url += "_(item)"
        print(url)
        return url
    except requests.exceptions.RequestException as e:
        print(f"Error processing {url}: {e}")
        return None  # Indicate failure

def get_urls():
    """
    Checks if urls.txt exists. If not, generates URLs, writes them to urls.txt, and returns them.
    """
    if os.path.exists("urls.txt"):
        print("urls.txt already exists. Skipping URL generation.")
        return open("urls.txt", "r").readlines()

    in_shop = get_shopable_items(get_deadlock_items())
    urls = [wiki_url_prefix + x["name"].replace(" ", "_") for x in in_shop]
    r_urls = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_url, urls)) #results is a list of the return values of process_url

    for result in results:
        if result is not None:
            r_urls.append(result)

    with open("urls.txt", "w") as f:
        for url in r_urls:
            f.write(url + "\n")

    return r_urls

def download_html():
    wiki_url_prefix = "https://deadlock.wiki/"
    in_shop = get_shopable_items(get_deadlock_items())
    urls = [wiki_url_prefix + x["name"].replace(" ", "_") for x in in_shop]

    # Create the items_html folder if it doesn't exist
    if not os.path.exists("items_html"):
        os.makedirs("items_html")

    for url in [x for x in urls ]:# if "Spirit_Lifesteal" in x
        filename = url.split("/")[-1] + ".html"
        filepath = os.path.join("items_html", filename)

        # Check if the file already exists
        if os.path.exists(filepath) or os.path.exists(filepath.replace(".html", "_(item).html")):
            # print(f"File already exists: {filename}")
            continue  # Skip to the next URL

        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        if "infobox_item" not in response.text:
            url += "_(item)"
            filename = url.split("/")[-1] + ".html"
            filepath = os.path.join("items_html", filename)
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        # Write the HTML content to the file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Downloaded: {filename}")

def extract_xpath_content():
    html_contents = []
    items_html_dir = "items_html"

    if not os.path.exists(items_html_dir):
        print("items_html directory does not exist. Please run download_html() first.")
        return []

    for filename in os.listdir(items_html_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(items_html_dir, filename)
            # print(filepath)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    html_content = f.read()
                    tree = html.fromstring(html_content)
                    elements = tree.xpath("/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div")
                    if elements:
                        html_contents.append(html.tostring(elements[0], encoding='unicode'))
                    else:
                        html_contents.append(None) #append None if the xpath wasn't found.
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                html_contents.append(None) #append None if there was an error processing the file.

    return html_contents
import re

def extract_png_strings(html_content):
    """
    Extracts all quoted strings from HTML that end with ".png".

    Args:
        html_content (str): The HTML content.

    Returns:
        list: A list of strings that match the pattern.
    """
    png_strings = []
    # Regular expression to find quoted strings ending with ".png"
    # It handles both single and double quotes.
    pattern = r'["\']([^"\']*\.png)["\']'
    matches = re.findall(pattern, html_content)
    png_strings.extend(matches)
    return png_strings

def get_images_to_download(a):
    o = set()
    for e in a:
        # print(e)
        if e.startswith("/images/"):
            o.add("https://deadlock.wiki" + e)
            # print("https://deadlock.wiki" + e)
        # else:
        #     print(e)
        #     o += [e]
    return o

anki_deck_header="""
#separator:tab
#html:true
"""
anki_card_format=""" "<img src=""$$ITEM_NAME$$_front.png"">"	"<img src=""$$ITEM_NAME$$_back.png"">" """
def make_deck(urls):
    o = anki_deck_header
    for e in urls:
        img_name=e.split("/")[-1].strip()
        o += anki_card_format.replace("$$ITEM_NAME$$", img_name) + "\n"
    print(o)

def main():
    # download_html()
    # extracted_contents = extract_xpath_content()
    # rhf = replace_html.replace("$$REPLACE$$", "\n".join(extracted_contents))
    # rhf = rhf.replace("img src=\"/images", "img src=\"https://deadlock.wiki/images")
    # to_replace = get_images_to_download(extract_png_strings(rhf))
    # # for e in to_replace:
    # #     print(e)
    #     # rhf = rhf.replace(original, replace)
    # print(rhf)
    # # print("\n".join())
    # # ive have the html displaying properly. the images are being referenced to the server which is ok for testing but it wont work for anki
    # # i think i need to download all the images. i can do that quickly by downloading the page ive generated but its not an automated process like i would like
    # # i could also reference the images from the api but im not sure how to link the references from the html to the json.
    urls=get_urls()
    # for u in urls:
    #     make_item_image(u)
    make_deck(urls)

if __name__ == "__main__":
    main()