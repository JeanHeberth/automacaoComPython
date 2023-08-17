import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
# maximize_window()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

#get()
driver.get("https://chercher.tech/practice/frames")

iframe1 = driver.find_element(By.ID, "frame1")
driver.switch_to.frame(iframe1)

# label_topic = driver.find_element(By.XPATH, "//*[@id='topic']/following-sibling::input")
label_topic = driver.find_element(By.XPATH, "//input[@type='text']")
label_topic.send_keys("Iframe_ 1")
time.sleep(3)


iframe3 = driver.find_element(By.ID, "frame3")
driver.switch_to.frame(iframe3)
check_box = driver.find_element(By.XPATH, "//input[@id='a']")
check_box.click()
time.sleep(3)

driver.switch_to.default_content()

iframe2 = driver.find_element(By.ID, "frame2")
driver.switch_to.frame(iframe2)
dropDown = Select(driver.find_element(By.XPATH,"//select[@id='animals']"))
dropDown.select_by_visible_text("Big Baby Cat")



# # quit() Mata o processo completo.
time.sleep(3)
driver.quit()

