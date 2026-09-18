import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#from utils.server_check import check_server

#check_server("https://rahulshettyacademy.com/angularpractice/shop")
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/shop/")

list_products = driver.find_elements(By.XPATH,"//div[@class='row']")

for product in list_products:
    product_name = product.find_element(By.XPATH,"//h4[@class='card-title']/a").text
    if product_name == "iphone X":
        product.find_element(By.XPATH,"//button[@class='btn btn-info']").click()
        break

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()

list_buttons = driver.find_elements(By.XPATH,"//table[@class='table table-hover']")

for button in list_buttons:
    button_name = button.find_element(By.XPATH,"//button[@class='btn btn-success']").text
    if button_name == "Checkout":
        button.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        break

driver.find_element(By.ID,"country").send_keys("Cameroun")
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()
wait = WebDriverWait(driver, 10)
