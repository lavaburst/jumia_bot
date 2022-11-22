import jumia_functions
import time

jumia_functions.email_popup()

i = 1

while i < 10:

    jumia_functions.see_category()
    jumia_functions.article_items()

    jumia_functions.find_artices()



    jumia_functions.find_offers()

    if jumia_functions.next_page == True:
        jumia_functions.add_to_cart()

        jumia_functions.open_the_cart()

        jumia_functions.cart_checkout()
        try:
            jumia_functions.get_email()
            jumia_functions.get_password()
            jumia_functions.confirm_code()
            jumia_functions.puckup_station()
            jumia_functions.select_station()
            jumia_functions.cofirm_station()
            jumia_functions.order_confirmation()
            jumia_functions.payment()
            jumia_functions.get_homepage()
        except:
            
            jumia_functions.puckup_station()
            jumia_functions.select_station()
            jumia_functions.cofirm_station()
            jumia_functions.order_confirmation()
            jumia_functions.payment()
            jumia_functions.get_homepage()


    else:
        print('nonsense')
        jumia_functions.get_homepage()









