from deadlock_anki import *
def mw_html(call_params):
    """
    Generates HTML output from mediawiki template parameters.
    """

    item_type = call_params.get("item_type")
    item_name = call_params.get("item_name", "Heroic Aura")
    item_tier = call_params.get("item_tier")
    souls = call_params.get("souls")
    item_icon = call_params.get("item_icon")
    item_description = call_params.get("item_description")
    item_stat1 = call_params.get("item_stat1")
    item_stat2 = call_params.get("item_stat2")
    item_stat3 = call_params.get("item_stat3")
    item_stat4 = call_params.get("item_stat4")
    item_stat5 = call_params.get("item_stat5")
    item_stat6 = call_params.get("item_stat6")
    item_stat7 = call_params.get("item_stat7")
    component1_name = call_params.get("component1_name")
    passive1_cooldown = call_params.get("passive1_cooldown")
    passive1_description = call_params.get("passive1_description")
    passive1_stat1 = call_params.get("passive1_stat1")
    passive1_stat2 = call_params.get("passive1_stat2")
    passive1_stat3 = call_params.get("passive1_stat3")
    passive1_stat4 = call_params.get("passive1_stat4")
    passive1_stat5 = call_params.get("passive1_stat5")
    passive1_stat6 = call_params.get("passive1_stat6")
    passive2_cooldown = call_params.get("passive2_cooldown")
    passive2_description = call_params.get("passive2_description")
    passive2_stat1 = call_params.get("passive2_stat1")
    passive2_stat2 = call_params.get("passive2_stat2")
    passive2_stat3 = call_params.get("passive2_stat3")
    passive2_stat4 = call_params.get("passive2_stat4")
    passive2_stat5 = call_params.get("passive2_stat5")
    active1_cooldown = call_params.get("active1_cooldown")
    active1_description = call_params.get("active1_description")
    active1_stat1 = call_params.get("active1_stat1")
    active1_stat2 = call_params.get("active1_stat2")
    active1_stat3 = call_params.get("active1_stat3")
    active1_stat4 = call_params.get("active1_stat4")
    active1_stat5 = call_params.get("active1_stat5")
    active1_stat6 = call_params.get("active1_stat6")
    iscomponentof1_name = call_params.get("iscomponentof1_name")
    sound1 = call_params.get("sound1")
    sound2 = call_params.get("sound2")
    """
    Converts the full, complex MediaWiki template to equivalent HTML.

    Args:
        ... (All parameters from the MediaWiki template, now None-able)

    Returns:
        An HTML string representing the generated table.
    """

    table_style = f"text-align:left; border-collapse:collapse; width:312px; max-width:100%; height:30px; color: #FFEFD7; padding:12px; font-family:'Retail Demo Regular',serif; "
    header_style = "width:280px; padding:5px 12px; text-align:center; font-size:24px; font-family:'Retail Demo Bold',serif; "
    shop_bonus_style = "font-size:80%; text-align: center; font-weight: bold; width: 100px; "
    passive_header_style = "text-align:left; padding:2px 12px; "
    passive_stat_box_style = "text-align:left; width:300px; max-width:280px; border-radius:8px; margin:6px auto; "
    active_header_style = "text-align:left; padding:2px 12px; "

    # Table background color
    if item_type == "Weapon":
        table_style += "background-color: #80550F;"
        header_style += "background-color: #C97A03;"
        shop_bonus_style += "background-color: #A36202;"
        passive_header_style += "background-color: #583B0E; color: #C4B49E;"
        passive_stat_box_style += "background-color: #67430A;"
        active_header_style += "background-color: #583B0E;"
    elif item_type == "Vitality":
        table_style += "background-color: #4D7214;"
        header_style += "background-color: #659818;"
        shop_bonus_style += "background-color: #507A11;"
        passive_header_style += "background-color: #354F11; color: #BDB59D;"
        passive_stat_box_style += "background-color: #3D5B0E;"
        active_header_style += "background-color: #354F11;"
    elif item_type == "Spirit":
        table_style += "background-color: #623585;"
        header_style += "background-color: #8B56B4;"
        shop_bonus_style += "background-color: #704491;"
        passive_header_style += "background-color: #43265B; color: #C1B2A8;"
        passive_stat_box_style += "background-color: #4D2869;"
        active_header_style += "background-color: #43265B;"
    else:
        table_style += "background-color: #80550F;"
        header_style += "background-color: #C97A03;"
        shop_bonus_style += "background-color: #A36202;"
        passive_header_style += "background-color: #583B0E; color: #C4B49E;"
        passive_stat_box_style += "background-color: #67430A;"
        active_header_style += "background-color: #583B0E;"

    shop_bonus_content = {
        f"{item_type}/1": {"Weapon": "+6% [[File:Weapon Icon.png|20px]]", "Vitality": "+11% [[File:Vitality Icon.png|20px]]", "Spirit": "+4 [[File:Spirit icon.png|20px]]"},
        f"{item_type}/2": {"Weapon": "+10% [[File:Weapon Icon.png|20px]]", "Vitality": "+14% [[File:Vitality Icon.png|20px]]", "Spirit": "+8 [[File:Spirit icon.png|20px]]"},
        f"{item_type}/3": {"Weapon": "+14% [[File:Weapon Icon.png|20px]]", "Vitality": "+17% [[File:Vitality Icon.png|20px]]", "Spirit": "+12 [[File:Spirit icon.png|20px]]"},
        f"{item_type}/4": {"Weapon": "+18% [[File:Weapon Icon.png|20px]]", "Vitality": "+20% [[File:Vitality Icon.png|20px]]", "Spirit": "+16 [[File:Spirit icon.png|20px]]"},
    }.get(f"{item_type}/{item_tier if item_tier else '1'}", "+0").get(item_type, "+0")

    shop_bonus_text = {
        f"{item_type}/1": {"Weapon": "+6% Weapon Damage", "Vitality": "+11% Base Health", "Spirit": "+4 Spirit Power"},
        f"{item_type}/2": {"Weapon": "+10% Weapon Damage", "Vitality": "+14% Base Health", "Spirit": "+8 Spirit Power"},
        f"{item_type}/3": {"Weapon": "+14% Weapon Damage", "Vitality": "+17% Base Health", "Spirit": "+12 Spirit Power"},
        f"{item_type}/4": {"Weapon": "+18% Weapon Damage", "Vitality": "+20% Base Health", "Spirit": "+16 Spirit Power"},
    }.get(f"{item_type}/{item_tier if item_tier else '1'}", "+0").get(item_type, "+0")

    html = f'''
        <table style="{table_style}">
            <tr>
                <td colspan="5" style="{header_style}"><span style="font-weight:bold; text-shadow: 2px 2px rgba(0, 0, 0, 0.2); ">{item_name}</span></td>
            </tr>
            <tr>
                <td colspan="5" style="{header_style}"><div style="{shop_bonus_style}">{shop_bonus_content}</div></td>
            </tr>
            <tr>
                <td colspan=5 class="infobox-image" style="padding:5px; text-align:center;">[[File:{item_icon if item_icon else item_name}.png|144px]]</td>
            </tr>
            <tr>
                <td colspan=3 style="text-align:right; width:50%; border-right:1px solid {header_style.split('background-color: ')[1].split(';')[0]}; padding-right:0.5em;">Cost</td>
                <td colspan=2 style="padding-left:0.5em;">{souls if souls else ''}</td>
            </tr>
            <tr>
                <td colspan=3 style="text-align:right; width:50%; border-right:1px solid {header_style.split('background-color: ')[1].split(';')[0]}; padding-right:0.5em;">Tier</td>
                <td colspan=2 style="padding-left:0.5em;">{item_tier if item_tier else ''}</td>
            </tr>
            <tr>
                <td colspan=3 style="text-align:right; width:50%; border-right:1px solid {header_style.split('background-color: ')[1].split(';')[0]}; padding-right:0.5em;">Shop Bonus</td>
                <td colspan=2 style="padding-left:0.5em;">{shop_bonus_text}</td>
            </tr>
        '''

    if component1_name is not None:
        html += f'''
        <tr>
            <td colspan="4" style="text-align:left; padding:0 12px; font-weight:bold; font-size:16px; font-family:'Retail Demo Bold',serif; background-color: {passive_header_style.split('background-color: ')[1].split(';')[0]}; color: {passive_header_style.split('color: ')[1].split(';')[0]};">COMPONENTS:<br/>{{ItemIcon|{component1_name}}}</td>
        </tr>
        '''

    if item_description is not None:
        html += f'''
        <tr>
            <td colspan="4" style="text-align:left; padding:0 12px; color:#FFEFD7; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_description}</td>
        </tr>
        '''

    if item_stat1 is not None:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat1}</td>
        </tr>
        '''
    if item_stat2 is not None:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat2}</td>
        </tr>
        '''
    if item_stat3 is not None:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat3}</td>
        </tr>
        '''
    if item_stat4 is not None:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat4}</td>
        </tr>
        '''
    if item_stat5 is not None:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat5}</td>
        </tr>
        '''
    if item_stat6 is not None:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat6}</td>
        </tr>
        '''
    if item_stat7 is not None:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat7}</td>
        </tr>
        '''

    if passive1_description is not None or passive1_stat1 is not None or passive1_stat2 is not None or passive1_stat3 is not None or passive1_stat4 is not None or passive1_stat5 is not None or passive1_stat6 is not None:
        cooldown_html = f'<td colspan=1 style="text-align:center; width:25%; max-width:80px; background-color:#0C1414; color:#FFEFD7;">[[File:Cooldown Icon.png|20px]] {passive1_cooldown}</td>' if passive1_cooldown else ''
        colspan = 4 - (1 if passive1_cooldown else 0)
        html += f'''
        <tr>
            <td colspan="{colspan}" style="{passive_header_style}">''Passive'' {cooldown_html}
        </tr>
        '''
        if passive1_description:
            html += f'''
            <tr>
                <td colspan=4 style="text-align:left; padding:2px 12px;">{passive1_description}</td>
            </tr>
            '''
        if passive1_stat1 is not None or passive1_stat2 is not None or passive1_stat3 is not None or passive1_stat4 is not None or passive1_stat5 is not None or passive1_stat6 is not None:
            html += f'''
            <tr>
                <td colspan=4 style="{passive_stat_box_style}">
            '''
            if passive1_stat1:
                html += f'<tr><td>{passive1_stat1}</td></tr>'
            if passive1_stat2:
                html += f'<tr><td>{passive1_stat2}</td></tr>'
            if passive1_stat3:
                html += f'<tr><td>{passive1_stat3}</td></tr>'
            if passive1_stat4:
                html += f'<tr><td>{passive1_stat4}</td></tr>'
            if passive1_stat5:
                html += f'<tr><td>{passive1_stat5}</td></tr>'
            if passive1_stat6:
                html += f'<tr><td>{passive1_stat6}</td></tr>'
            html += '</td></tr>'

    if passive2_description is not None or passive2_stat1 is not None or passive2_stat2 is not None or passive2_stat3 is not None or passive2_stat4 is not None or passive2_stat5 is not None:
        cooldown_html = f'<td colspan=1 style="text-align:center; width:25%; max-width:80px; background-color:#0C1414; color:#FFEFD7;">[[File:Cooldown Icon.png|20px]] {passive2_cooldown}</td>' if passive2_cooldown else ''
        colspan = 4 - (1 if passive2_cooldown else 0)
        html += f'''
        <tr>
            <td colspan="{colspan}" style="{passive_header_style}">''Passive'' {cooldown_html}
        </tr>
        '''
        if passive2_description:
            html += f'''
            <tr>
                <td colspan=4 style="text-align:left; padding:2px 12px;">{passive2_description}</td>
            </tr>
            '''
        if passive2_stat1 is not None or passive2_stat2 is not None or passive2_stat3 is not None or passive2_stat4 is not None or passive2_stat5 is not None:
            html += f'''
            <tr>
                <td colspan=4 style="{passive_stat_box_style}">
            '''
            if passive2_stat1:
                html += f'<tr><td>{passive2_stat1}</td></tr>'
            if passive2_stat2:
                html += f'<tr><td>{passive2_stat2}</td></tr>'
            if passive2_stat3:
                html += f'<tr><td>{passive2_stat3}</td></tr>'
            if passive2_stat4:
                html += f'<tr><td>{passive2_stat4}</td></tr>'
            if passive2_stat5:
                html += f'<tr><td>{passive2_stat5}</td></tr>'
            html += '</td></tr>'

    if active1_description is not None or active1_stat1 is not None or active1_stat2 is not None or active1_stat3 is not None or active1_stat4 is not None or active1_stat5 is not None or active1_stat6 is not None:
        cooldown_html= f'<td colspan=1 style="text-align:center; width:25%; max-width:80px; background-color:#0C1414; color:#FFEFD7;">[[File:Cooldown Icon.png|20px]] {active1_cooldown}</td>' if active1_cooldown else ''
        colspan = 4 - (1 if active1_cooldown else 0)
        html += f'''
        <tr>
            <td colspan="{colspan}" style="{active_header_style}"><b>Active</b> {cooldown_html}
        </tr>
        '''
        if active1_description:
            html += f'''
            <tr>
                <td colspan=4 style="text-align:left; padding:2px 12px;">{active1_description}</td>
            </tr>
            '''
        if active1_stat1 is not None or active1_stat2 is not None or active1_stat3 is not None or active1_stat4 is not None or active1_stat5 is not None or active1_stat6 is not None:
            html += f'''
            <tr>
                <td colspan=4 style="{passive_stat_box_style}">
            '''
            if active1_stat1:
                html += f'<tr><td>{active1_stat1}</td></tr>'
            if active1_stat2:
                html += f'<tr><td>{active1_stat2}</td></tr>'
            if active1_stat3:
                html += f'<tr><td>{active1_stat3}</td></tr>'
            if active1_stat4:
                html += f'<tr><td>{active1_stat4}</td></tr>'
            if active1_stat5:
                html += f'<tr><td>{active1_stat5}</td></tr>'
            if active1_stat6:
                html += f'<tr><td>{active1_stat6}</td></tr>'
            html += '</td></tr>'

    if iscomponentof1_name is not None:
            iscomponent_bg_color = "#704A0C"  # Default
            iscomponent_text_color = "#D1CBC6"  # Default

            if item_type == "Weapon":
                iscomponent_bg_color = "#704A0C"
                iscomponent_text_color = "#D1CBC6"
            elif item_type == "Vitality":
                iscomponent_bg_color = "#436310"
                iscomponent_text_color = "#CACFC7"
            elif item_type == "Spirit":
                iscomponent_bg_color = "#552D74"
                iscomponent_text_color = "#CCC8D2"

            html += f'''
            <tr>
                <td colspan="4" style="text-align:left; padding:0 12px; font-weight:bold; font-size:16px; font-family:'Retail Demo Bold',serif; background-color: {iscomponent_bg_color}; color: {iscomponent_text_color};">IS COMPONENT OF:<br/>{{ItemIcon|{iscomponentof1_name}}}</td>
            </tr>
            '''

    if sound1 is not None:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:center; padding:2px 12px; background-color: {header_style.split('background-color: ')[1].split(';')[0]};">Sounds</td>
        </tr>
        <tr>
            <td colspan="4">[[File:{sound1}]]</td>
        </tr>
        '''

    if sound2 is not None:
        html += f'''
        <tr>
            <td colspan="4">[[File:{sound2}]]</td>
        </tr>
        '''

    html += "</table>"
    return html

# print(mw_html(
#     item_name="Basic Magazine",
#     item_type="Vitality",
#     item_tier="1",
#     item_stat1="+26% [[Ammo]]",
#     item_stat2="+12% [[Weapon Damage]]",
#     souls="500",
#     iscomponentof1_name="vitality item"
# ))
# print(mw_html(
#     item_name="Surge of Power",
#     item_type="Spirit",
#     item_tier="3",
#     souls="3,000",
#     item_stat1="+75 Bonus Health",
#     passive1_description="Imbue an ability with '''permanent Spirit Power'''. When that ability is used, gain bonus '''Move Speed''' and maintain full speed while attacking.",
#     passive1_cooldown="10.5s",
#     passive1_stat1="+34 Imbued Ability Spirit Power",
#     passive1_stat2="15% Fire Rate Bonus (Conditional)",
#     passive1_stat3="+2m/s Move Speed (Conditional)",
#     passive1_stat4="6s Move Speed Duration"
# ))
# print(mw_html(
#     item_name="Improved Spirit",
#     item_type="Spirit",
#     item_tier="3",
#     souls="3000",
#     item_description="{s:sign}3 Health Regen. {s:sign}1mm/s Sprint Speed. {s:sign}125 Bonus Health. {s:sign}30 Spirit Power.",
#     item_stat1="{s:sign}125 Bonus Health",
#     item_stat2="{s:sign}3 Health Regen",
#     item_stat3="{s:sign}1mm/s Sprint Speed",
#     item_stat4="{s:sign}30 Spirit Power",
#     component1_name="Improved Spirit",
# ))

def print_all(in_shop):
    all_html = [mw_html(mw_vars(x)) for x in in_shop]
    print("\n".join(all_html))

def main():
    items = get_deadlock_items()
    in_shop = get_shopable_items(items)
    # print_all(in_shop)
    # pprint.pp(in_shop[41]["description"])
    print_all(in_shop)

if __name__ == "__main__":
    main()
