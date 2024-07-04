# scrapers/restaurant1.py

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import locale

# Set locale for Finnish date parsing
locale.setlocale(locale.LC_TIME, 'fi_FI.UTF-8')

def get_menu():
    url = 'https://www.ninankeittio.fi/helsinki-pasila-fennia/'
    div_class = 'fusion-text fusion-text-9'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return {'error': str(e)}

    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find_all('div', class_=div_class)
    print(divs)
    today = datetime.now()
    day = today.strftime('%A').capitalize()
    date_str = f"{day} {today.day}.{today.month}."
    
    items = []

    # Iterate over each found div
    for div in divs:
        # Iterate over each <p> tag within the div
        for p in div.find_all('p'):
            # Find the <strong> tag within the <p> tag
            strong_tag = p.find('strong')
            if strong_tag:
                # Get the text content of the <strong> tag
                day_str = strong_tag.get_text().strip()
                print(f"Found date string in HTML: {day_str}")
                if day_str == date_str:
                    print(f"Match found for today: {day_str}")
                    # Find the next sibling <ul> element
                    ul = p.find_next_sibling('ul')
                    if ul:
                        # Find all <li> elements within the <ul> element
                        list_items = ul.find_all('li')
                        for li in list_items:
                            # Append the text content of each <li> to the items list
                            items.append(li.get_text())
                    else:
                        print("No <ul> sibling found after the <p> tag with the date.")
                else:
                    print(f"No match for today's date. Found: {day_str}")
    
    
    return {'menu': items}
