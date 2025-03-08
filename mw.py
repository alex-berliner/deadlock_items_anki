def mediawiki_template_to_html_full(item_type, item_name="Heroic Aura", item_tier="", souls="", item_icon="", item_description="", item_stat1="", item_stat2="", item_stat3="", item_stat4="", item_stat5="", item_stat6="", item_stat7="", has_components=False, component1_name="Basic Magazine", has_passive1=False, passive1_cooldown="", passive1_description="", passive1_stat1="", passive1_stat2="", passive1_stat3="", passive1_stat4="", passive1_stat5="", passive1_stat6="", has_passive2=False, passive2_cooldown="", passive2_description="", passive2_stat1="", passive2_stat2="", passive2_stat3="", passive2_stat4="", passive2_stat5="", has_active1=False, active1_cooldown="", active1_description="", active1_stat1="", active1_stat2="", active1_stat3="", active1_stat4="", active1_stat5="", active1_stat6="", has_iscomponentof=False, iscomponentof1_name="Basic Magazine", sound1="", sound2=""):
    """
    Converts the full, complex MediaWiki template to equivalent HTML.

    Args:
        ... (All parameters from the MediaWiki template)

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
            <td colspan="4" style="{header_style}"><span style="font-weight:bold; text-shadow: 2px 2px rgba(0, 0, 0, 0.2); ">{item_name}</span></td>
            <td rowspan="2" style="text-align:right; border-radius:0px 8px 0px 0px; {header_style}"><span>[[File:{item_icon if item_icon else item_name}.png|64px]]</span>
            </td>
        </tr>
        <tr>
            <td colspan="4" style="{header_style}"><div style="{shop_bonus_style}">{shop_bonus_content}</div></td>
        </tr>
        <tr>
            <td colspan=4 class="infobox-image" style="padding:5px; text-align:center;">[[File:{item_icon if item_icon else item_name}.png|144px]]</td>
        </tr>
        <tr>
            <td colspan=2 style="text-align:right; width:50%; border-right:1px solid {header_style.split('background-color: ')[1].split(';')[0]}; padding-right:0.5em;">Cost</td>
            <td colspan=2 style="padding-left:0.5em;">{souls}</td>
        </tr>
        <tr>
            <td colspan=2 style="text-align:right; width:50%; border-right:1px solid {header_style.split('background-color: ')[1].split(';')[0]}; padding-right:0.5em;">Tier</td>
            <td colspan=2 style="padding-left:0.5em;">{item_tier}</td>
        </tr>
        <tr>
            <td colspan=2 style="text-align:right; width:50%; border-right:1px solid {header_style.split('background-color: ')[1].split(';')[0]}; padding-right:0.5em;">Shop Bonus</td>
            <td colspan=2 style="padding-left:0.5em;">{shop_bonus_text}</td>
        </tr>
    '''

    if has_components:
        html += f'''
        <tr>
            <td colspan="4" style="text-align:left; padding:0 12px; font-weight:bold; font-size:16px; font-family:'Retail Demo Bold',serif; background-color: {passive_header_style.split('background-color: ')[1].split(';')[0]}; color: {passive_header_style.split('color: ')[1].split(';')[0]};">COMPONENTS:<br/>{{ItemIcon|{component1_name}}}</td>
        </tr>
        '''

    if item_description:
        html += f'''
        <tr>
            <td colspan="4" style="text-align:left; padding:0 12px; color:#FFEFD7; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_description}</td>
        </tr>
        '''

    if item_stat1:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat1}</td>
        </tr>
        '''
    if item_stat2:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat2}</td>
        </tr>
        '''
    if item_stat3:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat3}</td>
        </tr>
        '''
    if item_stat4:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat4}</td>
        </tr>
        '''
    if item_stat5:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat5}</td>
        </tr>
        '''
    if item_stat6:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat6}</td>
        </tr>
        '''
    if item_stat7:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:left; padding:2px 12px; background-color: {table_style.split('background-color: ')[1].split(';')[0]};">{item_stat7}</td>
        </tr>
        '''

    if has_passive1:
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
        if passive1_stat1 or passive1_stat2 or passive1_stat3 or passive1_stat4 or passive1_stat5 or passive1_stat6:
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

    if has_passive2:
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
        if passive2_stat1 or passive2_stat2 or passive2_stat3 or passive2_stat4 or passive2_stat5:
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

    if has_active1:
        cooldown_html = f'<td colspan=1 style="text-align;center; width:25%; max-width:80px; background-color:#0C1414; color:#FFEFD7;">[[File:Cooldown Icon.png|20px]] {active1_cooldown}</td>' if active1_cooldown else ''
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
        if active1_stat1 or active1_stat2 or active1_stat3 or active1_stat4 or active1_stat5 or active1_stat6:
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

    if has_iscomponentof:
        html += f'''
        <tr>
            <td colspan="4" style="text-align:left; padding:0 12px; font-weight:bold; font-size:16px; font-family:'Retail Demo Bold',serif; background-color: #704A0C; color: #D1CBC6;">IS COMPONENT OF:<br/>{{ItemIcon|{iscomponentof1_name}}}</td>
        </tr>
        '''

    if sound1:
        html += f'''
        <tr>
            <td colspan=4 style="text-align:center; padding:2px 12px; background-color: {header_style.split('background-color: ')[1].split(';')[0]};">Sounds</td>
        </tr>
        <tr>
            <td colspan="4">[[File:{sound1}]]</td>
        </tr>
        '''

    if sound2:
        html += f'''
        <tr>
            <td colspan="4">[[File:{sound2}]]</td>
        </tr>
        '''

    html += "</table>"
    return html
print(mediawiki_template_to_html_full(
    item_name="Basic Magazine",
    item_type="Weapon",
    item_tier="1",
    has_components=False,
    has_passive1=False,
    has_passive2=False,
    has_active1=False,
    has_iscomponentof=True,
    item_stat1="+26% [[Ammo]]",
    item_stat2="+12% [[Weapon Damage]]",
    souls="500",
    iscomponentof1_name="Titanic Magazine"
))