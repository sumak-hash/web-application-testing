import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_login_valid_credentials():


    # Arrange
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    # Act
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Learning@830$3mK2")
    radiobuttons= driver.find_elements(By.XPATH, "input[@type=radio]")

    for radiobtn in radiobuttons:
      if radiobtn.get_attribute("value")== "user":
        radiobtn.click()
        assert radiobtn.is_selected()
        break

    selectbuttons= driver.find_elements(By.XPATH, "select[@data-type=btn-info]")
    for selectbtn in selectbuttons:
         if selectbtn.get_attribute("value")== "stud":
          selectbtn.click()
          assert selectbtn.is_selected()
          break


    driver.find_element(By.CSS_SELECTOR, "#terms").is_selected()

    driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

    wait = WebDriverWait(driver, 10)



    # Assert


def test_login_invalid_password():


    # Arrange
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    # Act
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("testpassword123")
    radiobuttons= driver.find_elements(By.XPATH, "input[@type=radio]")

    for radiobtn in radiobuttons:
      if radiobtn.get_attribute("value")== "user":
        radiobtn.click()
        assert radiobtn.is_selected()
        break

    selectbuttons= driver.find_elements(By.XPATH, "select[@data-type=btn-info]")
    for selectbtn in selectbuttons:
         if selectbtn.get_attribute("value")== "stud":
          selectbtn.click()
          assert selectbtn.is_selected()
          break


    driver.find_element(By.CSS_SELECTOR, "#terms").is_selected()

    driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
    wait = WebDriverWait(driver, 10)


    # Assert




def test_login_invalid_username():


    # Arrange
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    # Act
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("invalidusername")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("testpassword123")
    radiobuttons= driver.find_elements(By.XPATH, "input[@type=radio]")

    for radiobtn in radiobuttons:
      if radiobtn.get_attribute("value")== "user":
        radiobtn.click()
        assert radiobtn.is_selected()
        break

    selectbuttons= driver.find_elements(By.XPATH, "select[@data-type=btn-info]")
    for selectbtn in selectbuttons:
         if selectbtn.get_attribute("value")== "stud":
          selectbtn.click()
          assert selectbtn.is_selected()
          break


    driver.find_element(By.CSS_SELECTOR, "#terms").is_selected()

    driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
    wait = WebDriverWait(driver, 10)

    # Assert


def test_login_empty_ppassword():


    # Arrange
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    # Act
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("testpassword123")
    radiobuttons= driver.find_elements(By.XPATH, "input[@type=radio]")

    for radiobtn in radiobuttons:
      if radiobtn.get_attribute("value")== "user":
        radiobtn.click()
        assert radiobtn.is_selected()
        break

    selectbuttons= driver.find_elements(By.XPATH, "select[@data-type=btn-info]")
    for selectbtn in selectbuttons:
         if selectbtn.get_attribute("value")== "stud":
          selectbtn.click()
          assert selectbtn.is_selected()
          break


    driver.find_element(By.CSS_SELECTOR, "#terms").is_selected()

    driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
    wait = WebDriverWait(driver, 10)

    # Assert















#class LoginPage:

#    def __init__(self, driver):
 #       self.driver = driver

  #  def enter_email(self, email):
 #       self.driver.find_element(By.ID, "email").send_keys(email)

 #   def enter_password(self, password):
 #       self.driver.find_element(By.ID, "password").send_keys(password)

  #  def click_login(self):
  #      self.driver.find_element(By.ID, "login-button").click()