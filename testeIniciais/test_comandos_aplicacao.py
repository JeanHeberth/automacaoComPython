import time

from selenium import webdriver

driver = webdriver.Chrome()
# maximize_window()
driver.maximize_window()

#get()
driver.get("https://www.saucedemo.com/")
print("O titulo da página é: ", driver.title)
print("A URL da página é: ", driver.current_url)
# print("O source da página é: ", driver.page_source)

# quit() Mata o processo completo.
driver.quit()