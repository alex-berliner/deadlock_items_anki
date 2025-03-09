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
            # pprint.pp(sections["section_attributes"])
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
    # pprint.pp(item)
    card += [item["name"]]
    # pprint.pp(item)
    properties, elevated_properties, important_properties = properties_of_item(item)

    return "\n".join(card)

def mw_vars(item_json):
    """
    Converts a JSON item description to a dictionary of variables for mediawiki_template_to_html_full.
    Excludes stats with a value of 0.
    """

    item_name = item_json.get("name")
    item_type = item_json.get("item_slot_type").capitalize() if item_json.get("item_slot_type") else None
    item_tier = item_json.get("item_tier")
    souls = item_json.get("cost")
    component_items = item_json.get("component_items")
    activation = item_json.get("activation")
    properties = item_json.get("properties", {})
    tooltip_sections = item_json.get("tooltip_sections", [])

    # Extract relevant properties
    item_stats = []
    passive1_stats = []
    passive2_stats = []
    active1_stats = []

    passive1_cooldown = None
    passive2_cooldown = None
    active1_cooldown = None

    for prop_name, prop_data in properties.items():
        label = prop_data.get("label")
        value = prop_data.get("value")
        postfix = prop_data.get("postfix", "")

        try:
            # First, ensure value is a string before attempting replacements
            value_str = str(value)
            numeric_value = float(value_str.replace('m', '').replace('%', '').replace('s',''))
            if numeric_value == 0:
                continue # Skip stats with a value of 0
        except ValueError:
            pass # Keep strings, such as "1m" or "10%"

        if label and value is not None:
            formatted_stat = f"{prop_data.get('prefix', '')}{value}{postfix} {label}"
            if "AbilityCooldown" in prop_name:
                if activation == "passive" and passive1_cooldown is None:
                    passive1_cooldown = f"{value}{postfix}"
                elif activation == "passive" and passive1_cooldown is not None and passive2_cooldown is None:
                    passive2_cooldown = f"{value}{postfix}"
                elif activation == "active":
                    active1_cooldown = f"{value}{postfix}"

            if "Ability" not in prop_name:
                item_stats.append(formatted_stat)
            elif activation == "passive" and passive1_cooldown is None:
                passive1_stats.append(formatted_stat)
            elif activation == "passive" and passive2_cooldown is None and passive1_cooldown is not None:
                passive2_stats.append(formatted_stat)
            elif activation == "active":
                active1_stats.append(formatted_stat)

    #Extract description
    description = ""
    if tooltip_sections:
        for section in tooltip_sections:
            if section.get("section_type") == "innate":
                attributes = section.get("section_attributes", [])
                for attr in attributes:
                    properties_list = attr.get("properties", [])
                    elevated_properties = attr.get("elevated_properties", [])
                    important_properties = attr.get("important_properties", [])

                    for prop_name in properties_list + elevated_properties + important_properties:
                        prop_data = properties.get(prop_name)
                        if prop_data:
                            description += f"{prop_data.get('prefix', '')}{prop_data.get('value', '')}{prop_data.get('postfix', '')} {prop_data.get('label', '')}. "

    # Construct the function call
    call_params = {
        "item_name": item_name,
        "item_type": item_type,
        "item_tier": item_tier,
        "souls": souls,
        "item_description": description.strip() if description else None,
        "item_stat1": item_stats[0] if len(item_stats) > 0 else None,
        "item_stat2": item_stats[1] if len(item_stats) > 1 else None,
        "item_stat3": item_stats[2] if len(item_stats) > 2 else None,
        "item_stat4": item_stats[3] if len(item_stats) > 3 else None,
        "item_stat5": item_stats[4] if len(item_stats) > 4 else None,
        "item_stat6": item_stats[5] if len(item_stats) > 5 else None,
        "item_stat7": item_stats[6] if len(item_stats) > 6 else None,
    }

    if component_items:
        call_params["component1_name"] = component_items[0].replace("upgrade_", "").replace("_", " ").title()

    if activation == "passive":
        if passive1_cooldown is not None:
            call_params["passive1_cooldown"] = passive1_cooldown
            call_params["passive1_stat1"] = passive1_stats[0] if len(passive1_stats) > 0 else None
            call_params["passive1_stat2"] = passive1_stats[1] if len(passive1_stats) > 1 else None
            call_params["passive1_stat3"] = passive1_stats[2] if len(passive1_stats) > 2 else None
            call_params["passive1_stat4"] = passive1_stats[3] if len(passive1_stats) > 3 else None
            call_params["passive1_stat5"] = passive1_stats[4] if len(passive1_stats) > 4 else None
            call_params["passive1_stat6"] = passive1_stats[5] if len(passive1_stats) > 5 else None
        if passive2_cooldown is not None:
            call_params["passive2_cooldown"] = passive2_cooldown
            call_params["passive2_stat1"] = passive2_stats[0] if len(passive2_stats) > 0 else None
            call_params["passive2_stat2"] = passive2_stats[1] if len(passive2_stats) > 1 else None
            call_params["passive2_stat3"] = passive2_stats[2] if len(passive2_stats) > 2 else None
            call_params["passive2_stat4"] = passive2_stats[3] if len(passive2_stats) > 3 else None
            call_params["passive2_stat5"] = passive2_stats[4] if len(passive2_stats) > 4 else None

    elif activation == "active":
        if active1_cooldown is not None:
            call_params["active1_cooldown"] = active1_cooldown
            call_params["active1_stat1"] = active1_stats[0] if len(active1_stats) > 0 else None
            call_params["active1_stat2"] = active1_stats[1] if len(active1_stats) > 1 else None
            call_params["active1_stat3"] = active1_stats[2] if len(active1_stats) > 2 else None
            call_params["active1_stat4"] = active1_stats[3] if len(active1_stats) > 3 else None
            call_params["active1_stat5"] = active1_stats[4] if len(active1_stats) > 4 else None
            call_params["active1_stat6"] = active1_stats[5] if len(active1_stats) > 5 else None

    # Filter out None values
    call_params = {k: v for k, v in call_params.items() if v is not None}

    return call_params

def main():
    items = get_deadlock_items()
    # print(len(items))
    in_shop = get_shopable_items(items)
    # print(in_shop)
    item = item_to_card(in_shop[0])
    # print(json.loads(json.dumps(in_shop[0])))
    # print(item)
    # pprint.pp(items[1])
    print(mw_vars(in_shop[41]))
    # for (i,e) in enumerate(in_shop):
    #     if "surge" in e["name"].lower():
    #         print(i, e["name"])
        # print(e["name"])

if __name__ == "__main__":
    main()