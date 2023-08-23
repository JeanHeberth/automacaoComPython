import time

import pytest
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


btnAddToCart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
btnAddToCart.click()

btnCart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
btnCart.click()

productValid = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
productValid.is_displayed()
time.sleep(2)


btnContinueShopping = driver.find_element(By.ID, "continue-shopping")
btnContinueShopping.click()

btnAddToCartTo = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
btnAddToCartTo.click()

btnCart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
btnCart.click()








time.sleep(5)
# quit() Mata o processo completo.
# driver.quit()