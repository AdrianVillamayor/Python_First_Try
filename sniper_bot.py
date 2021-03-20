from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = "https://www.amazon.es/Microsoft-RRS-00009-Xbox-Series-S/dp/B087VM5XC6"
session = HTMLSession()

def init():
    product_page = session.get(url)
    found = product_page.html.find("#add-to-cart-button")
    return found

def amazonBuySystem():
    driver = webdriver.Firefox(executable_path=r'/Users/Adrian/Documents/geckodriver')
    driver.get(url)
    driver.find_element_by_id("sp-cc-accept").click()
    sleep(2)
    driver.find_element_by_id("add-to-cart-button").click()
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[4]/div[1]/div[8]/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/span/span/input").click()
    sleep(2)
    email = driver.find_element_by_id("ap_email")
    email.send_keys("adrian.villamayor@gmail.com")

def main():
    check = init()

    if check :
        amazonBuySystem()

if __name__ == "__main__":
    main()
