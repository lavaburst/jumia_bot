from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cridentials


import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.jumia.co.ke/")

offers = ["Pembe", "XIAOMI"]
bei = ["319", "10,699"]






def email_popup():

    emails = driver.find_element(By .XPATH, '//*[@id="pop"]/div/section/button')
    emails.click()
    time.sleep(1)

def see_category():
    

    see_all = driver.find_element(By .XPATH, "//*[@id='jm']/main/div[1]/div[2]/section/div/div/div[1]/a")

    see_all.send_keys(Keys.ENTER)
    time.sleep(2)

def article_items():
    
    all_articles = driver.find_element(By .XPATH, '/html/body/div/main/div[2]/div[3]/section/div[1]')

    articles = all_articles.find_elements(By .XPATH, "//*[@id='jm']/main/div[2]/div[3]/section/div[1]/article")
    return articles



def find_artices():
    articles = article_items()

    for article in articles:


        products = article.find_element(By .CLASS_NAME, "core")
        # print(products)
        information = products.find_element(By .CLASS_NAME, "info")

        item_name = information.find_element(By .CLASS_NAME, "name")
        correct_name = item_name.text

        
        item_price = information.find_element(By .CLASS_NAME, "prc")
        ksh = item_price.text

        item = {'name': correct_name, 'price': ksh}
        return item
        
        

def find_offers():
    item = find_artices()
    global next_page

    next_page = False
    
    y = item["name"]
    x = item["price"]
    for offer in offers:
        
        if offer in y:
            
            for p in bei:
                # print(p)
                if p in x: 
                    next_page = True
                    print(next_page)
                    
                    
                    print(item)
                    
                    
                    clickable = driver.find_element(By .CLASS_NAME, "core")
        
                    clickable.send_keys(Keys.ENTER)
                    time.sleep(2)
                else:
                    pass



                   
def nexting():
    print(next_page)
                    
    
        
def get_homepage():
    driver.get("https://www.jumia.co.ke/")


def add_to_cart():
    add_cart = driver.find_element(By .XPATH, '//*[@id="add-to-cart"]/button')
    add_cart.send_keys(Keys.ENTER)
    time.sleep(4)

def open_the_cart():
    open_cart = driver.find_element(By .XPATH, '//*[@id="jm"]/header/section/div[2]/a')
    open_cart.send_keys(Keys.ENTER)
    time.sleep(2)

def cart_checkout():
    checkout = driver.find_element(By .XPATH, '//*[@id="jm"]/main/div/div[2]/div/article/div[3]/a')
    checkout.click()
    time.sleep(2)


def get_email():
    email = driver.find_element(By .XPATH, '/html/body/div/div[4]/form/div[2]/div[2]/label/input')
    email.send_keys(cridentials.EMAIL)
    time.sleep(1)
    go_on = driver.find_element(By .XPATH, '/html/body/div/div[4]/form/div[2]/div[3]/div/button')
    go_on.send_keys(Keys.ENTER)
    time.sleep(2)


def get_password():
    password = driver.find_element(By .NAME, "password")
    password.send_keys(cridentials.PASSWORD)
    time.sleep(2)
    log_in = driver.find_element(By .XPATH, '//*[@id="loginButton"]/span[1]')
    password.send_keys(Keys.ENTER)
    time.sleep(20)

def confirm_code():
    submit  = driver.find_element(By .XPATH, "//*[@id='btn-remind-me-later']")
    submit.send_keys(Keys.ENTER)
    time.sleep(5)

def puckup_station():
    pick_station = driver.find_element(By .XPATH, '//*[@id="select-pickupstation-btn"]')
    pick_station.click()

def select_station():
    window_handle = driver.window_handles[0]
    driver.switch_to.window(window_handle)
    time.sleep(3)
    choice = driver.find_element(By .XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/form/div[5]/div[2]')
    clicking = choice.find_element(By .XPATH, '//*[@id="pus-popup-form"]/div[5]/div[2]/label')
    time.sleep(1)
    clicking.click()
    time.sleep(1)
    select_this = driver.find_element(By .XPATH, '//*[@id="pus-popup-form"]/div[6]/button')
    select_this.send_keys(Keys.ENTER)
    time.sleep(1)

def cofirm_station():
    next_step = driver.find_element(By .XPATH, '//*[@id="osh-opc-btn-save"]')
    next_step.send_keys(Keys.ENTER)
    time.sleep(1)

def order_confirmation():
    confirm_order = driver.find_element(By .XPATH, '//*[@id="osh-opc-paymentForm"]/button')
    confirm_order.send_keys(Keys.ENTER)
    time.sleep(3)
def payment():
    pay_now = driver.find_element(By .XPATH, '/html/body/main/div/div/div[3]/div/div/div[5]/div/div/form/div/div/div/div/div/button')
    pay_now.send_keys(Keys.ENTER)
    time.sleep(15)

