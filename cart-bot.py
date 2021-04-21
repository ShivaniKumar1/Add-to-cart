
# allows you to access website information without popping up a browser
import requests
import json
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

def availability() :
    # website you want to monitor
    r = requests.get('https://featuresneakerboutique.com/products.json')
    products = json.loads((r.text))['products']

    for product in products:
        #print(product['title'])
        pname = product['title']

        if pname == 'Paper Planes All Points Hoodie - OD Green':
            print("Product Name: " + pname)
            producturl = 'https://featuresneakerboutique.com/products/' + product['handle']
            print(producturl)
        return producturl
    return False

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

#where our chromedriver is located
driver = webdriver.Chrome(options=options, executable_path = r'C:\Users\User\Documents\chromedriver.exe')

#the website url of the product
url = "https://feature.com/collections/footwear/products/adidas-originals-zx-8000-sg-golf-white"
driver.get(url)

#the specific size of the product (have elements at first so you can see the diff ones then change to element)
driver.find_element_by_xpath('//div[@data-value="10"]').click()
driver.find_element_by_xpath('//button[@class="primary-btn add-to-cart"]').click()
driver.find_element_by_css_selector('span.cart-items-count')

if driver.find_element_by_text_link('1'):
    driver.get("https://feature.com/cart")

if cart == False:
    print("Product not in Cart.")

driver.get("https://feature.com/checkout")


#comment = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.ID, 'contenteditable-textarea'))
#comment.click()
#comment.send.keys("HELO")
#driver.find_element_by_id("submit-button").click()