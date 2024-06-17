import requests
import xml.etree.ElementTree as ET

def get_menu():
    url = 'https://europe-west1-luncher-7cf76.cloudfunctions.net/api/v1/rss/week/3aba0b64-0d43-41ea-b665-1d2d6c0f2d5e/current?days=current&language=fi'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return {'error': str(e)}

    try:
        root = ET.fromstring(response.content)
    except ET.ParseError as e:
        return {'error': 'Failed to parse XML'}

    items = []

    # Parse the XML to extract menu items from the description tag
    for item in root.findall('.//item'):
        description = item.find('description').text
        if description:
            # Clean up the description and split into individual menu items
            menu_items = description.replace('<![CDATA[', '').replace(']]>', '').split('<br>')
            for menu_item in menu_items:
                items.append(menu_item.strip())

    return {'restaurant': 'Dylan Böle', 'menu': items}
