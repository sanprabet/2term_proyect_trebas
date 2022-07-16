import json, requests
from pprint import pprint
import repository


def get_all_product_for_display():
    """
    This function return: Price and name from products
    """
    try:
        products = []
        products_raw = repository.get_all_products()

        for product in products_raw:
            new_product = {
                'id': product.get('id', None),
                'name': product.get('name', None),
                'price': product.get('price', None),
            }
            products.append(new_product)
        
        return products

    except Exception as err:
        print('[print_products] Something went wrong: ' + str(err))

def process_order(order_ids):

    customer_order = {
        'products':[],
        'final_price': 0,
        'count_doesnt_exist': 0
    }

    for order_id in order_ids:
        product = repository.get_product_by_id(order_id)

        if not product: 
            customer_order['count_doesnt_exist'] += 1
            continue

        product_name = product['name']
        product_price = product['price']

        customer_order['products'].append(product_name)
        customer_order['final_price'] += product_price
    
    return customer_order
        
        








