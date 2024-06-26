# main.py

from flask import Flask, jsonify
from scrapers import ninanKeittio, dylan, factoryPasila # Import other restaurant scrapers as needed

app = Flask(__name__)

@app.route('/menus', methods=['GET'])
def get_menus():
    menus = []
    
    # Get menus from all restaurant scrapers
    menus.append(ninanKeittio.get_menu())
    menus.append(dylan.get_menu())
    menus.append(factoryPasila.get_menu())
    # Add calls to other restaurant scraper functions as needed
    
    return jsonify({'menus': menus})

if __name__ == '__main__':
    app.run(debug=True)
