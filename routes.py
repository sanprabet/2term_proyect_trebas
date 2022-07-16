## Heres where the routes that frontend calls should live
## This is a false API 

from pprint import pprint
import service

# @cafeteriaApi.route('/', methods=['GET'])
def order():
    try:

        print(
            """ 
            Hey, thanks for choosing our coffe shop!!!!
            Please choose the products that you want to purchase from the list below.
            """)

        all_products = service.get_all_product_for_display()

        for product in all_products:
            product_id = product.get('id', 'No id')
            product_name = product.get('name', 'No name')
            product_price = product.get('price', 'No price')
            print(f'Id: {product_id}  /  Product: {product_name}  /  Price: {product_price}')

        print(
            """ 
            When you finish choosing, please write the product ID follow by clicking the Return/Enter key
            Write F when you finish your order so we can calculate the total 
            """
        )
        
        res = ""
        user_products = []

        while True:
            try:
                res = str(int(input("Write the product Id: ")))
                user_products.append(res)
            except:
                break
        
        return user_products

    except Exception as err:
        print('[Exception: print_products]' + str(err))

def display_order(order):
    print(
    """
    


    Thanks for ordering with us

    This is your final order!!!!!



    """)

    products_names = order.get('products', [])
    final_price = str(order.get('final_price', 0))
    bad_products = order.get('count_doesnt_exist', 0)

    print(f"Products you choose:")

    num_lens = len(products_names)
    for name in products_names:
        print(f"{num_lens} -> {name}")
        num_lens -= 1

    print("")
    print(f"The total of your order is: {final_price}")
    print("")

    if bad_products: print(f"You wrote {bad_products} ids that dont exist, but we took care of them")

    print(
    """
    


    Now pay the programmer :D



    """)



if __name__ == "__main__":
    customer_order = order()
    final_order = service.process_order(customer_order)
    display_order(final_order)







    