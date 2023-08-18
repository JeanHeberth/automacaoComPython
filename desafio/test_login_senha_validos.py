import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# get()
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.implicitly_wait(5)
driver.maximize_window()



username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
btnLogin = driver.find_element(By.ID, "login-button")
username.send_keys("standard_user")
password.send_keys("secret_sauce")
btnLogin.click()


paginaProducts = driver.find_element(By.XPATH, "//span[@class='title']")
assert paginaProducts.is_displayed()

time.sleep(3)
# quit() Mata o processo completo.
driver.quit()