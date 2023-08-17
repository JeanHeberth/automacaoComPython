import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(15)
# maximize_window()
driver.maximize_window()


# get()
driver.get("https://chercher.tech/practice/implicit-wait-example")

checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
assert checkbox.is_displayed()
time.sleep(3)





# quit() Mata o processo completo.
driver.quit()