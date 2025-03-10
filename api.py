import requests

"""
curl -X 'GET' \
  'https://assets.deadlock-api.com/v2/items?language=english&client_version=5509' \
  -H 'accept: application/json'
"""

def get_deadlock_items(client_version, language="english"):
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

def main():
    in_shop = get_shopable_items(get_deadlock_items("5509"))

if __name__ == "__main__":
    main()
