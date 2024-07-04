from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

def get_menu():
    url = 'https://delhirasoi.fi/lounas-lunch-helsinki-tripla'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return {'error': str(e)}

    soup = BeautifulSoup(response.content, 'html.parser')
    h3_tags = soup.find_all('h3')  # Fetch all <h3> tags from the site

    today = datetime.now()
    day_abbr = today.strftime('%a')[:2]  # Get abbreviated weekday name (first two letters)
    day_number = today.day  # Day of the month without leading zero
    month_number = today.month  # Month number without leading zero
    tomorrow = today + timedelta(days=1)
    tomorrow_abbr = tomorrow.strftime('%a')[:2]
    tomorrow_day_number = tomorrow.day
    tomorrow_month_number = tomorrow.month
    date_str = f"{day_abbr.capitalize()} {day_number}.{month_number}."
    tomorrow_str = f"{tomorrow_abbr.capitalize()} {tomorrow_day_number}.{tomorrow_month_number}."

    menu_items = []

    for h3 in h3_tags:
        text = h3.get_text().strip().replace('\t', '')  # Clean up the text
        if date_str in text:
            next_h3 = h3.find_next('h3')
            while next_h3 and tomorrow_str not in next_h3.get_text():
                text = next_h3.get_text().strip().replace('\t', '')  # Clean up the text
                if tomorrow_str in text:  # Check if we've reached tomorrow's date
                    break
                menu_items.append(text)
                next_h3 = next_h3.find_next('h3')

    return {'restaurant': 'Delhi Rasoi', 'menu': menu_items}

if __name__ == "__main__":
    menu = get_menu()
