import pprint
import requests
import json
"""
curl -X 'GET' \
  'https://assets.deadlock-api.com/v2/items?language=english&client_version=5509' \
  -H 'accept: application/json'
"""

def get_deadlock_items(language="english", client_version="5509"):
    url = "https://assets.deadlock-api.com/v2/items"
    headers = {
        "accept": "application/json"
    }
    params = {
        "language": language,
        "client_version": client_version
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    except ValueError:
        print("Invalid JSON response")
        return None
    except Exception as generic_error:
        print(f"A generic error occured : {generic_error}")
        return None

def get_shopable_items(items):
    shopable_items = []
    if not isinstance(items, list):
        return [] #handle the case where items is not a list.

    for item in items:
        if isinstance(item, dict) and item.get("shopable") == True:
            shopable_items.append(item)
    return shopable_items

def class_name_to_item_name(class_name):
    return class_name

def properties_of_item(item):
    properties = []
    elevated_properties = []
    important_properties = []
    for sections in item["tooltip_sections"]:
        if "section_attributes" in sections:
            pprint.pp(sections["section_attributes"])
            for attr in sections["section_attributes"]:
                if "properties" in attr:
                    properties += attr["properties"]
                if "elevated_properties" in attr:
                    elevated_properties += attr["elevated_properties"]
                if "important_properties" in attr:
                    important_properties += attr["important_properties"]
    return properties, elevated_properties, important_properties

def item_to_card(item):
    card = []
    pprint.pp(item)
    card += [item["name"]]
    pprint.pp(item)
    properties, elevated_properties, important_properties = properties_of_item(item)

    return "\n".join(card)

def main():
    items = get_deadlock_items()
    # print(len(items))
    in_shop = get_shopable_items(items)
    # print(in_shop)
    item = item_to_card(in_shop[0])
    # print(item)
    # pprint.pp(items[1])


if __name__ == "__main__":
    main()