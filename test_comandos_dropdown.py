import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# maximize_window()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

#get()
driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")

dropdown_products = Select(driver.find_element(By.XPATH, "//select[@id='first']"))
dropdown_animals = Select(driver.find_element(By.XPATH, "//select[@id='animals']"))
dropdown_multiple = Select(driver.find_element(By.XPATH, "//select[@id='second']"))
# dropdown_custom = Select(driver.find_element(By.XPATH, "///button[@id='custom']"))


dropdown_products.select_by_visible_text("Google")
dropdown_products.select_by_index(3)
dropdown_products.select_by_value("Apple")
dropdown_animals.select_by_value("avatar")
dropdown_multiple.select_by_visible_text("Pizza")
time.sleep(2)
dropdown_multiple.select_by_visible_text("Burger")
time.sleep(2)


# quit() Mata o processo completo.
driver.quit()