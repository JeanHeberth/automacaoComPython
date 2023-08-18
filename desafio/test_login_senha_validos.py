import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# maximize_window()

# get()
driver.get("https://www.saucedemo.com")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
btnLogin = driver.find_element(By.ID, "login-button")
username.send_keys("standard_user")
password.send_keys("secret_sauce")
btnLogin.click()


paginaProducts = driver.find_element(By.XPATH, "//span[@class='title']")
assert paginaProducts

time.sleep(3)
# quit() Mata o processo completo.
driver.quit()