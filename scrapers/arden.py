from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

def get_menu():
    url = 'https://www.ardenrestaurants.fi/menut/towertabletmenu.html'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return {'error': str(e)}

    print(response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    h3_tags = soup.find_all('h3')  # Fetch all <h3> tags from the site

    today = datetime.now()
    day_abbr = today.strftime('%a')
    print(day_abbr)

    menu_items = []

    print(h3_tags)

    return {'menu': menu_items}

if __name__ == "__main__":
    menu = get_menu()
