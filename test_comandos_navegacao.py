import time

from selenium import webdriver

driver = webdriver.Chrome()
# maximize_window()
driver.maximize_window()


# get()
driver.get("https://google.com")
time.sleep(3)

# refresh()
driver.refresh()

#get()
driver.get("https://www.saucedemo.com/")
time.sleep(3)

# back()
driver.back()
time.sleep(3)

# forward()
driver.forward()
time.sleep(3)

driver.switch_to.new_window("tab")
time.sleep(5)


# close() Fecha uma janela ou uma aba, a que estiver ativa no momento.
#driver.close()

# quit() Mata o processo completo.
driver.quit()