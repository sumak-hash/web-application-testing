import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#from utils.server_check import check_server

#check_server("https://rahulshettyacademy.com/angularpractice/")
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH, "//input[@name='name']").send_keys("testname")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("test@example.com")
driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("testpassword")
driver.find_element(By.XPATH, "//input[@id='exampleCheck1']").click()




selectbuttons= driver.find_elements(By.XPATH, "select[@id='exampleFormControlSelect1']")
for selectbtn in selectbuttons:
    if selectbtn.get_attribute("value")== "Male":
        selectbtn.click()
        assert selectbtn.is_selected()
        break

radiobuttons= driver.find_elements(By.XPATH, "input[@type=radio]")

for radiobtn in radiobuttons:
    if radiobtn.get_attribute("value")== "option1":
        radiobtn.click()
        assert radiobtn.is_selected()
        break
driver.find_element(By.XPATH, "//input[@name='bday']").send_keys("01/01/1990")

driver.find_element(By.CLASS_NAME, "btn").click()


wait = WebDriverWait(driver, 10)


