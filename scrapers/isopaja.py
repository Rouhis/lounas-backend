from bs4 import BeautifulSoup
import requests
from datetime import datetime

def get_menu():
    url = 'https://www.hhravintolat.fi/iso-paja'  # Update this URL to the actual URL containing the HTML structure

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return {'error': str(e)}

    soup = BeautifulSoup(response.content, 'html.parser')

    today = datetime.now()
    day_abbr = today.strftime('%a')[:2]  # Get abbreviated weekday name (first two letters)
    day_number = today.day  # Day of the month without leading zero
    month_number = today.month  # Month number without leading zero
    date_str = f"{day_abbr.capitalize()} {day_number}.{month_number}."
    print(f"Today's date string: {date_str}")  # Debug print for today's date

    items = []

    date_heading = soup.find('h1', text=date_str)
    if date_heading:
        menu_paragraph = date_heading.find_next('p')
        if menu_paragraph:
            parent_div = menu_paragraph.find_parent('div')
            patent_parent_div = parent_div.find_parent('div')  # Find the parent <div> of the <p> tag
            if patent_parent_div:
                menu_paragraphs = patent_parent_div.find_all('p')  # Find all <p> tags within the parent <div>
                for paragraph in menu_paragraphs:
                    items.append(paragraph.get_text(strip=True))
            else:
                print(f"No parent div found for the menu paragraph.")
        else:
            print(f"No menu found for date: {date_str}")
    else:
        print(f"No heading found for date: {date_str}")

    return {'restaurant': 'Restaurant 2', 'menu': items}

if __name__ == "__main__":
    menu = get_menu()
    print(menu)
