import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# maximize_window()
driver.maximize_window()

#get()
driver.get("https://demo.applitools.com")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
btnSignin = driver.find_element(By.ID, "log-in")



username.send_keys("Testando o username")
password.send_keys("123456789")
checkbox.click()
btnSignin.click()



time.sleep(5)


# quit() Mata o processo completo.
driver.quit()