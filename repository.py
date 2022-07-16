# product / feedstock / sale / purchase

import json, requests
from pprint import pprint

def get_all_products():
    try:
        api_url = "https://asm-manager.herokuapp.com/product/"
        response = requests.get(api_url)

        if response.status_code != 200: raise Exception('Server error')
        
        if not response.json(): return None
        else:
            return response.json()

    except Exception as err:
        print('[get_all_products] Something went wrong: ' + str(err))

def get_product_by_id(id):
    try:
        api_url = "https://asm-manager.herokuapp.com/product/" + str(id)
        response = requests.get(api_url)

        if (response.status_code != 200) or (not response.json()): return None
        else:
            return response.json()

    except Exception as err:
        print('[get_product_by_id] Something went wrong: ' + str(err))

get_product_by_id('33')

