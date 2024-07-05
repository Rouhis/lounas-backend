from flask import Flask, jsonify
from scrapers import ninanKeittio, dylan, factoryPasila, isopaja, delhirasoi, arden  # Import other restaurant scrapers as needed

app = Flask(__name__)

def clean_menu(menu):
    return [item for item in menu if item.strip()]

@app.route('/menus', methods=['GET'])
def get_menus():
    menus = []
    arden.get_menu()
    # Get menus from all restaurant scrapers and clean them
    #menus.append({'restaurant': 'Ninan Keittiö', 'menu': clean_menu(ninanKeittio.get_menu()['menu'])})
    #menus.append({'restaurant': 'Dylan Böle', 'menu': clean_menu(dylan.get_menu()['menu'])})
    #menus.append({'restaurant': 'Factory Pasila', 'menu': clean_menu(factoryPasila.get_menu()['menu'])})
    #menus.append({'restaurant': 'Iso Paja', 'menu': clean_menu(isopaja.get_menu()['menu'])})
    #menus.append({'restaurant': 'Delhi Rasoi', 'menu': clean_menu(delhirasoi.get_menu()['menu'])})
    # Add calls to other restaurant scraper functions as needed
    
    return jsonify({'menus': menus})

if __name__ == '__main__':
    app.run(debug=True)
