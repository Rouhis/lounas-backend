from bs4 import BeautifulSoup
import requests
from datetime import datetime
import locale

def get_menu():
    url = 'https://ravintolafactory.com/lounasravintolat/ravintolat/factory-pasila'
    div_class = 'list'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return {'error': str(e)}

    soup = BeautifulSoup(response.content, 'html.parser')
    today = datetime.now()
    day_name = today.strftime('%A').capitalize()  # Get weekday name and capitalize it
    day_number = today.day  # Day of the month without leading zero
    month_number = today.month  # Month number without leading zero
    year_number = today.year  # Year number
    date_str = f"{day_name.capitalize()} {day_number}.{month_number}.{year_number}"

    items = []

    # Find the <h3> tag with today's date
    date_heading = soup.find('h3', text=date_str)
    if date_heading:
        # Find the next <p> tag after the date heading
        menu_paragraph = date_heading.find_next('p')
        if menu_paragraph:
            # Extract the text content of the menu items
            menu_items = menu_paragraph.get_text(separator='\n').split('\n')
            items.extend(menu_items)
        else:
            print(f"No menu found for date: {date_str}")
    else:
        print(f"No heading found for date: {date_str}")

    return {'menu': items}