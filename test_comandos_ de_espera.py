import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(15)
# maximize_window()
driver.maximize_window()


# get()
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
wait = WebDriverWait(driver, 20)
checkbox = driver.find_element(By.ID, "alert")
checkbox.click()
wait.until(EC.alert_is_present())



time.sleep(3)





# quit() Mata o processo completo.
driver.quit()